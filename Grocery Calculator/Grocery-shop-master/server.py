import socket
import json
import threading
import config
# handling the connection
def threaded_answer(address, conn):
    
    while True:
        str_data = conn.recv(1024).decode()
        if not str_data:
            break
        data = json.loads(str_data)
        
        print("got connection from address %s on port %s"%(address[0], address[1]))
        print("got request")
        print(data)
        # check the request
        request_type = data['request']
        resp = {}
        
        if request_type == 'cash':
            resp['request'] = 'cash'
            total = sum([config.PRICES[fruit]*data['data'][fruit] for fruit in data['data'].keys() ])
            resp['data'] = total
        elif request_type == 'prices':
            resp['request'] = 'prices'
            resp['data'] = config.PRICES
        
        print("respones is :")
        print(resp)

        str_resp = json.dumps(resp).encode()
        conn.send(str_resp)
    conn.close()




with socket.socket() as my_socket:
    # AF_INET refers to the address family ipv4. The SOCK_STREAM means connection oriented TCP protocol.
    my_socket.bind((config.IP_ADDRESS, config.PORT_NUMBER))

    my_socket.listen(5)
    counter = 0

    while True:
        conn, add = my_socket.accept()
        thread = threading.Thread(target=threaded_answer, args=(add, conn,))
        thread.start()
