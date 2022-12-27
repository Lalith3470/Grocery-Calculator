import json
import socket
import config
class Client:   
    def __init__(self):
        try:
            self.socket = socket.socket()
            self.socket.connect((config.IP_ADDRESS, config.PORT_NUMBER))
        except:
            raise Exception("make sure the server is up")

    def get_prices(self):
        # create a prices request
        prices = {
            'request': 'prices',
            'data': None
        }
        prices_str = json.dumps(prices).encode()
        self.socket.send(prices_str)

        response_str = self.socket.recv(1024).decode()
        response = json.loads(response_str)
        return response['data']

    def get_cash(self, orders):
        request = {'request': 'cash'}
        request['data'] = orders
        orders_str = json.dumps(request).encode()
        self.socket.send(orders_str)

        response = self.socket.recv(1024).decode()
        response = json.loads(response)
        return response['data']


if __name__ == '__main__':
    # for testing    
    prices = {
    'request': 'prices',
    'data': None
    }

    cash = {
        'request': 'cash',
        'data': {
            'banana': 1,
            'apple': 5,
            'orange': 3
        }
    }

    my_socket = socket.socket()

    my_socket.connect((config.IP_ADDRESS, config.PORT_NUMBER))

    print("testing the prices request")
    prices_str = json.dumps(prices).encode()
    my_socket.send(prices_str)

    response_str = my_socket.recv(1024).decode()
    response = json.loads(response_str)
    print("got response:")
    print(response)

    print("testing the cash request")
    cash_str = json.dumps(cash).encode()
    my_socket.send(cash_str)

    response = my_socket.recv(1024).decode()
    print("got response:")
    print(response)
    my_socket.close()
