from wsgiref.simple_server import make_server


def app(environ, start_response):
    # environ.items()


    response_body = "<html><h1>Mi página</h1><p>Hello World</p></html>"

    status = '200 OK'

    response_headers = [
        ('Content-type', 'text/html'),
    ]

    start_response(status, response_headers)

    return [response_body.encode('utf-8')]

server = make_server('localhost', 8000, app=app)
server.serve_forever()