#-*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
from json import dumps
from pathlib import PurePosixPath
from urllib.parse import unquote, urlparse
from . import luhn


class LuhnHTTPReequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        response = ''
        status_code = 0
        card_number = ''

        try:
            card_number = PurePosixPath(
                unquote(urlparse(self.path).path)
            ).parts[1]

            is_valid = luhn.is_valid_card_number(card_number)
            iin = luhn.issuing_network(card_number) if is_valid else 'Unknown'

            response = dumps({
                'Credit card number': f'{card_number}', 'Valid': is_valid,
                'Issuing Network': f'{iin}'
            }) if is_valid else dumps({
                'Credit card number': f'{card_number}', 'Valid': is_valid
            })
            status_code = 200
        except Exception as e:
            response = dumps(
                {'Credit card number': f'{card_number}', 'Error': f'{str(e)}'}
            )
            status_code = 400
        finally:
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(str(response))))
            self.send_response(status_code)
            self.end_headers()
            self.wfile.write(str(response).encode('utf8'))
