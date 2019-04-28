
import socket
import sys
import json

MESSAGE_BOXES = {}

def _handle_data(data: dict):
    action = data.get('action')
    if not action:
        return { 'ok': False, 'error': 'No action' }
    
    if action == 'get':
        # {msgbox} -> {messages}
        msgbox = data.get('msgbox')
        if not msgbox:
            return { 'ok': False, 'error': 'No message box' }

        if msgbox in MESSAGE_BOXES:
            rsp = MESSAGE_BOXES[msgbox]
            del MESSAGE_BOXES[msgbox]
            return { 'ok': True, 'messages': rsp }
        else:
            return { 'ok': True, 'messages': [] }
    elif action == 'put':
        # {msgbox, message} -> {}
        msgbox = data.get('msgbox')
        msg = data.get('message')
        if not msgbox:
            return { 'ok': False, 'error': 'No message box' }
        if not msg:
            return { 'ok': False, 'error': 'No message'}

        if msgbox in MESSAGE_BOXES:
            MESSAGE_BOXES[msgbox].append(msg)
        else:
            MESSAGE_BOXES[msgbox] = [msg]

        return { 'ok': True }
    else:
        return { 'ok': False, 'error': 'Invalid action' }


def serve(host='0.0.0.0', port='8085'):

    port = int(port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print(' === SMOR SERVER STARTING ===')
    print(' *** listening on {}:{} ***'.format(host, port))
    sock.bind(server_address)
    sock.listen()

    while True:
        conn, addr = sock.accept()
        data = conn.recv(5000)
        try:
            resp = _handle_data(json.loads(data.decode('utf8')))
            conn.sendall(json.dumps(resp).encode('utf8'))
        except Exception as e:
            conn.sendall(json.dumps({
                'ok': False,
                'error': 'Exception thrown',
                'message': str(e)
            }).encode('utf8'))

        conn.close()        