from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json

import pdb


class InventoryRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = json.dumps({
            'name': 'Pants',
            'price': 50.00,
            'quantity': 10
        })
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Content-length', str(len(data)))
        self.end_headers()
        self.wfile.write(data.encode())


def run():
    addr = ('', 44332)
    httpd = HTTPServer(addr, InventoryRequestHandler)
    httpd.serve_forever()


def run_bg():
    """
    Run Server in the Background

    Note: Run from tdd-workshop/
    """
    python_path = os.path.abspath('venv\\Scripts\\python.exe')
    args_data = os.path.abspath('.\\mocking\\solutions\\fake_server\\inv_server.py')
    os.spawnl(os.P_NOWAIT, python_path, '-m', args_data)


if __name__ == '__main__':
    run()
