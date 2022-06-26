# curl http://127.0.0.1:8080 -v --http1.0
# curl -v http://localhost:8080/ -X POST -d "key=value"


import socket


def main():
    try:
        run()
    except Exception as e:
        print(e)


def run():
    server_ip = '127.0.0.1'
    server_port = 8080
    listen_num = 5
    buffer_size = 1024

    # 1.ソケットオブジェクトの作成
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_server:

        # 2.作成したソケットオブジェクトにIPアドレスとポートを紐づける
        tcp_server.bind((server_ip, server_port))

        # 3.作成したオブジェクトを接続可能状態にする
        tcp_server.listen(listen_num)

        # 4.ループして接続を待ち続ける
        while True:
            # 5.クライアントと接続する
            client, address = tcp_server.accept()
            with client:
                print('[*] Connected!! [ Source : {}]'.format(address))

                # 6.データを受信する
                data = client.recv(buffer_size)
                print('[*] Received Data : {}'.format(data))
                str_data = data.decode('utf-8')

                print('>>> start')
                list_data = str_data.split('\r\n')
                # リクエストを表示
                for data in list_data:
                    print(data)

                send_data = b'HTTP/1.1 200 OK\r\n'
                send_data += b'\r\n'
                print('>>> end')

                # GETの場合
                if str_data.startswith('GET'):
                    send_data += b'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width,initial-scale=1.0"><title>hello</title></head><body>Hello World</body></html>'

                # POSTの場合
                # elif str_data.startswith('POST'):
                    # TODO: リクエストを処理する
                    # list_data = str_data.split("\r\n\r\n")

                # 7.クライアントへデータを返す
                client.send(send_data)


if __name__ == '__main__':
    main()
