#-*- coding: utf-8 -*-

import argparse
from http.server import HTTPServer
import cc_checker.luhn_handler as luhn_handler


def start_server(addr, port):
    luhn_server = HTTPServer(
        (addr, port), luhn_handler.LuhnHTTPReequestHandler
    )

    try:
        luhn_server.serve_forever()
    except KeyboardInterrupt:
        pass

    luhn_server.server_close()


def main():
    parser = argparse.ArgumentParser(
        description="Run an HTTP server that validates credit card numbers"
    )

    parser.add_argument(
        '-l',
        '--listen',
        default='0.0.0.0',
        help='Specifies the address the server should listen on'
    )

    parser.add_argument(
        '-p',
        '--port',
        default=8080,
        help='Specifies the port the server should listen on'
    )

    args = parser.parse_args()
    start_server(addr=args.listen, port=args.port)


if __name__ == "__main__":
    main()
