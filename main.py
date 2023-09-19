from http.server import HTTPServer, BaseHTTPRequestHandler,SimpleHTTPRequestHandler
from jinja2 import Environment, PackageLoader,select_autoescape
# from models.photo import PhotoMas

photo_mas=[
    {
        'data_aos':0,
        'img':"img_4.jpg"
    },
    {
        'data_aos':100,
        'img':"img_5.jpg"
    },
    {
        'data_aos':200,
        'img':"img_1.jpg"
    },

    {
        'data_aos':0,
        'img':"img_2.jpg"
    },
    {
        'data_aos':100,
        'img':"img_3.jpg"
    },
    {
        'data_aos':200,
        'img':"img_6.jpg"
    },
    {
        'data_aos':0,
        'img':"img_7.jpg"
    },
    {
        'data_aos':100,
        'img':"img_8.jpg"
    },
    {
        'data_aos':200,
        'img':"img_9.jpg"
    },
    {
        'data_aos':0,
        'img':"img_10.jpg"
    },
    {
        'data_aos':100,
        'img':"img_1.jpg"
    },
    {
        'data_aos':200,
        'img':"img_2.jpg"
    },
    {
        'data_aos':0,
        'img':"img_3.jpg"
    },
    {
        'data_aos':100,
        'img':"img_4.jpg"
    },
    {
        'data_aos':200,
        'img':"img_5.jpg"
    },
    {
        'data_aos':0,
        'img':"img_6.jpg"
    },
    {
        'data_aos':100,
        'img':"img_7.jpg"
    },
    {
        'data_aos':200,
        'img':"img_8.jpg"
    },
    {
        'data_aos':100,
        'img':"img_9.jpg"
    },
    {
        'data_aos':100,
        'img':"img_4.jpg"
    },
    {
        'data_aos':200,
        'img':"img_5.jpg"
    },
]

class CustomHandler(SimpleHTTPRequestHandler):
    env = Environment(
        loader=PackageLoader("main"),
        autoescape=select_autoescape()
    )

    def do_GET(self):
        if self.path.startswith('/media/'):
            super().do_GET()
        elif self.path == '/':
            self.render_index()




    def render_index(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        body=self.env.get_template('index.html').render(photo_mas=photo_mas)
        self.wfile.write(body.encode('utf-8'))

def run(server_class=HTTPServer,handler_class=BaseHTTPRequestHandler):
    
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("[+] Server starting")
    httpd.serve_forever()

if __name__=="__main__":
    run(handler_class=CustomHandler)