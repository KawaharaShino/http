# curl http://127.0.0.1:8000 -v --http1.0 or Chrome

from http.server import BaseHTTPRequestHandler, HTTPServer


def main():
    try:
        run()
    except Exception as e:
        print(e)


class MyHTTPRequestHAndler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        b_html = b'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>hello</title></head><body>Hello World</body></html>'
        self.wfile.write(b_html)


def run(server_class=HTTPServer, handler_class=MyHTTPRequestHAndler):
    server_address = ('127.0.0.1', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == "__main__":
    main()
