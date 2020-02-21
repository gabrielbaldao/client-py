# client-py

## Install

```console
pip install git+https://github.com/OmniTrade/client-py.git
```

## Usage

Require the client in your code by adding:


```python
from omnitradeClient import Client
from omnitradeClient import StreamingClient
```

You can use both the public or private API.

### Public
------

Instance your public client by using:

```python
public_client = Client()
```

#### .get_public

Use **`.get_public`** to make a GET request to an URL, as the following example:

```python
client_public.get_public('/api/v2/markets')
```

### Private
------

When using the private client, you also have to specify your access and private keys in the instantiation:

```python
private_client = Client({ access_key: 'your_access_key', secret_key: 'your_secret_key' })
```

You can also set a timeout and/or endpoit by adding the arguments:

```python
private_client = Client({ access_key: 'your_access_key', secret_key: 'your_secret_key', timeout: 60, endpoint: 'https://omnitrade.io/' })
```
#### .get

Use **`.get`** to make a GET request to an URL, you can also set the required arguments, as the following example:

```python
private_client.get('/api/v2/orders', { market: 'btcbrl' })
```

#### .post

Use **`.post`** to make a POST request to an URL, you can also set the required arguments, as the following example:

```python
private_client.post('/api/v2/order', { market: 'btcbrl', side: 'buy', volume: '0.42', price: '4200.0' })
```

### WebSocket
------ 

```python
streaming_client = StreamingClient(callbackFunction, {'access_key': '123456', 'secret_key': '123412'})
```

This `callbackFunction` must to receive one parameter.

## Licence

OmniTrade (C) All Rights Reserved.
