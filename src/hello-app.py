from pywebio.input import *
from pywebio.output import *

input("What's your name?")
select("Select food", ['Orange', 'Apple', 'Banana'])
checkbox("Are your okay?", options=["I'm okay."])
radio("What do you like to do?", options=['Eat', 'Sleep', 'Study'])
put_image(open('vestigo-logo.png', 'rb').read())

put_table([
    ['Hello-app version', '1.0.0'],
    ['Owner', "Joško T."]
    ])

if __name__ == '__main__':
    import argparse
    from pywebio.platform.tornado_http import start_server as start_http_server
    from pywebio import start_server as start_ws_server

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    parser.add_argument("--http", action="store_true", default=False, help='Whether to enable http protocol for communicates')
    args = parser.parse_args()

    if args.http:
        start_http_server(main, port=args.port)
    else:
        start_ws_server(main, port=args.port, websocket_ping_interval=30)