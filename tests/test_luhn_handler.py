#-*- coding: utf-8 -*-

import io
import unittest

from .context import cc_checker
from cc_checker import luhn_handler


WINDOWS_LINE_ENDING = b'\r\n'
UNIX_LINE_ENDING = b'\n'


class TestableHandler(luhn_handler.LuhnHTTPReequestHandler):
    # This is to remove a warning from pytest. The class name starts with
    # 'Test', and because of that pytest will attempt to discover test cases in
    # this class, when it contains none.
    __test__ = False

    # Setting the buffer size is necessary for makefile() to be used to produce
    # the output stream, as opposed to socketserver._SocketWriter.
    wbufsize = 1

    def finish(self):
        # Do not close self.wfile, so we can read its value in the tests.
        self.wfile.flush()
        self.rfile.close()

    def date_time_string(self, timestamp=None):
        # Mocked date-time string for testing purposes.
        return 'DATETIME'

    def version_string(self):
        # Mocked server ID for testing purposes.
        return 'BaseHTTP/0.6 Python/3.10.2'


class MockSocket(object):
    def getsockname(self):
        return 'sockname'


class MockRequest(object):
    _sock = MockSocket()

    def __init__(self, path):
        self._path = path

    def makefile(self, *args, **kwargs):
        if args[0] == 'rb':
            return io.BytesIO('GET {} HTTP/1.1'.format(self._path).encode())
        elif args[0] == 'wb':
            return io.BytesIO(''.encode())
        else:
            raise ValueError("Unknown file type to make.", args, kwargs)


class TestLuhnHandler(unittest.TestCase):
    def _get_respoonse(self, request):
        handler = TestableHandler(request, ('0.0.0.0', 8000), None)
        response = handler.wfile.getvalue()
        handler.wfile.close()
        return response

    def test_valid_card_number(self):
        r = self._get_respoonse(MockRequest('/4263982640269299'))
        r = r.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
        self.assertEqual(
            r,
            b"""Content-Type: application/json\n\
Content-Length: 84\nHTTP/1.0 200 OK\n\
Server: BaseHTTP/0.6 Python/3.10.2\n\
Date: DATETIME\n\n\
{"Credit card number": "4263982640269299",\
 "Valid": true, "Issuing Network": "Visa"}""")

    def test_invalid_card_number(self):
        r = self._get_respoonse(MockRequest('/4263982640269297'))
        r = r.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
        self.assertEqual(
            r,
            b"""Content-Type: application/json\n\
Content-Length: 58\nHTTP/1.0 200 OK\n\
Server: BaseHTTP/0.6 Python/3.10.2\n\
Date: DATETIME\n\n\
{"Credit card number": "4263982640269297", "Valid": false}""")

    def test_error_card_number(self):
        r = self._get_respoonse(MockRequest('/byebye'))
        r = r.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
        self.assertEqual(
            r,
            b"""Content-Type: application/json\n\
Content-Length: 77\nHTTP/1.0 400 Bad Request\n\
Server: BaseHTTP/0.6 Python/3.10.2\n\
Date: DATETIME\n\n\
{"Credit card number": "byebye", \
"Error": "byebye is not a positive number."}""")

    def test_empty_card_number(self):
        r = self._get_respoonse(MockRequest('/'))
        r = r.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)
        self.assertNotEqual(str(r).find('400 Bad Request'), -1)
