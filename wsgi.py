# from app import app

# if __name__ == "__main__":
#     # app.run()
#     host = '0.0.0.0'
#     port = 5000
#     httpd = simple_server.make_server(host, port, app)
#     httpd.serve_forever()

from wsgiref import simple_server
from app import app

httpd = simple_server.make_server('0.0.0.0', 5000, app)
httpd.serve_forever()
