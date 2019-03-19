from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import json


def Main():
    host = '127.0.0.1'
    port = 12345
    buffer_size = 2
    encoding = 'utf-8'
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind((host, port))  # On lie ce socket à l'adresse 127.0.0.1:12345
        sock.listen()  # On se met en attente de connexions
        print("Server listening at {}:{}".format(host, port))
        while True:
            # Les 2 premier bytes du message envoyé contiennent la longueur de celui-ci
            # Ainsi, le serveur connait la longueur du message à recevoir
            (c, addr) = sock.accept()  # Un nouveau client se connecte
            print("Connection received from {}:{}".format(*addr))
            msg = c.recv(buffer_size)  # On lit les données qu'il nous envoie
            length = int.from_bytes(msg, byteorder='little')
            if length > 0:
                response = c.recv(length).decode(encoding)
                print("Received message: {!r}".format(response))
                data = json.loads(response)
                print(data)
                if data["Msg type"] == "STATS":
                    message_send = {
                        "Msg type": "ACK",
                        "Msg ID": data["Msg ID"],
                    }
                    message_send = json.dumps(message_send)
                    message_length = len(message_send).to_bytes(buffer_size, byteorder='little')
                    encoded_message = bytes(message_send.encode(encoding))
                    message_final = message_length + encoded_message
                    c.send(message_final)

                elif data["Msg type"] == "CONFIG":
                    message_send = {
                        "Msg type": "CONFIG",
                        "Msg ID": data["Msg ID"],
                        "Max player delay": "<time in seconds>",
                        "Max coin blink delay": "<time in seconds>",
                        "Victory blink delay": "<time in seconds>",
                        "Level": "<integer>",
                        "Player1 color": "<color value>",
                        "Player2 color": "<color value>",
                    }
                    message_send = json.dumps(message_send)
                    message_length = len(message_send).to_bytes(buffer_size, byteorder='little')
                    encoded_message = bytes(message_send.encode(encoding))
                    message_final = message_length + encoded_message
                    c.send(message_final)
            else:
                print("Le serveur n'a renvoyé aucune réponse")
            c.close()


if __name__ == '__main__':
    Main()
