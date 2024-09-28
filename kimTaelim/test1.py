from http.server import BaseHTTPRequestHandler, HTTPServer
from http.cookies import SimpleCookie
count = {}
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        cookie = SimpleCookie()


        from_cookie = SimpleCookie(self.headers.get('Cookie'))
        sessionId = from_cookie.get('sessionId')

        if sessionId is None:
            sessionId = 'test1'
            cookie['sessionId'] = sessionId
            count[sessionId] = 0

        else:
            sessionId = sessionId.value
        
        count[sessionId] += 1

        self.send_response(200)
        self.send_header('Set-Cookie', cookie.output(header=''))
        self.end_headers()

    
        self.wfile.write(f'당신은 F5를 {count[sessionId]}번 눌렀습니다.'.encode('EUC-KR'))

server_address = ('0.0.0.0', 8080)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
httpd.serve_forever()