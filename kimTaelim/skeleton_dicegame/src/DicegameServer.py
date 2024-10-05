from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from json_util.json_io import dict_to_json_data, json_data_to_dict
from auth.user_auth import register, login
from core.playgame import play
from core.ranking import ranking

class DicegameServer(BaseHTTPRequestHandler):
    """
    header를 만들어준다.
    """
    def make_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    """
    http://localhost:8080/service_name?query_params 형태의 
    /service_name?query_params만 필요함
    ?를 기준으로 구분함
    
    URL을 분리한다.
    """
    def divide_path(self) -> tuple:
        ###################작성필요########################
        # 힌트 : urlparse, parse_qs 함수를 사용
        ##################################################
        # http://localhost:8080 이후의, /service_name?query_params가 해당한다.
        service_with_query_params = urlparse(self.path)


        # /service_name?query_params 중 /service_name만 추출한다.
        servie_name = service_with_query_params.path
        # /service_name?query_params 중 query_params만 추출한다.
        query_params = parse_qs(service_with_query_params.query)

        return servie_name, query_params

    def do_GET(self):
        self.make_header()
        service_name, query_params = self.divide_path()
        result = {}

        # 서비스에 따라, 적절한 메소드를 호출한다.
        if service_name == '/playgame':
            player_id = query_params['id'][0]
            result = play(player_id)
        elif service_name == '/ranking':
            result = ranking()
        
        if result:
            result_data = dict_to_json_data(result)
            self.wfile.write(result_data.encode('utf-8'))

    def do_POST(self):
        self.make_header()
        service_name, _ = self.divide_path()

        # POST는 body에 데이터가 담겨있기 때문에, 읽어온다.
        json_data = self.rfile.read(int(self.headers['Content-Length'])).decode('utf-8')
        # 읽어온 json 데이터를 딕셔너리로 변환한다.
        dict_data = json_data_to_dict(json_data)
        result = {}

        # 서비스에 따라, 적절한 메소드를 호출한다.
        if service_name == '/register':
            result = register(dict_data)
        elif service_name == '/login':
            result = login(dict_data)
        
        if result:
            result_data = dict_to_json_data(result)
            self.wfile.write(result_data.encode('utf-8'))

server_address = ('localhost', 8080)
httpd = HTTPServer(server_address, DicegameServer)
httpd.serve_forever()