import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie
list = {}
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Methods', 'GET-POST,OPTIONS')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Headers)
    def do_POST(self):
        
        path = self.path
        if path == '/register':
            data_string = self.rfile.read(int(self.headers['Content-Length']))

            data = json.loads(data_string)
            id = data['id']
            password = data['password']
            list[id] = password

            list_a = {'id' : id,
                      'success' : True}
            
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps(list_a).encode('UTF-8'))


server_address = ('0.0.0.0', 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()




