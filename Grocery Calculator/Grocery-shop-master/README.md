# Simple Client-Server Grocery shop app with a GUI

A server that contains the prices and does all the calculations
A client that consume the server data and view the products

![app image](res/app.png?raw=true "App Image")

---

## How it works

in here we adapted a very simple API that is as follows

the server expect the request to one of the following:

* calculate the total cost
    ```python
    {
        'request' : 'cash',
        'data': requests_dict {dict}
    }
    ```
  * note the ```request_dict``` is expected to be
    ```python
    {
        'fruit' : amount {int},
        'fruit' : amount {int},
        .
        .
        .
    }
    ```
* get the prices AKA menu
    ```python
    {
        'request' : 'prices',
        'data': None
    }
    ```

the server responses is also so simple as follows:

* in case of cash request
    ```python
    {
    'request': 'cash',
    'data': total_cash {float}
    }
    ```
* in case of prices request
    ```python
    {
    'request' : 'prices',
    'data' : fruits_dict {dict}
    }
    ```
  * note that ```fruits_dict``` will be as follows
    ```python
    {
    'fruit' : price {float}
    .
    .

    }
    ```
