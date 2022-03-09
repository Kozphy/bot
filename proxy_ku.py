import ccxt


exchange = ccxt.poloniex({
    'proxies': {
        'http': 'http://192.168.100.156:8545',  # these proxies won't work for you, they are here for example
        'https': 'https://192.168.100.156:8546',
    },
})
