from kucoin.client import Client

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
KUCOIN_SECRET_KEY = "..."
KUCOIN_API_KEY = "..."
KUCOIN_PASSPHRASE = "..."

client = Client(
    KUCOIN_API_KEY,
    KUCOIN_SECRET_KEY,
    KUCOIN_PASSPHRASE,
    requests_params={
        "verify": False,
        "timeout": 20,
        'proxies': proxies
    }
)

order = client.create_market_order('TRX-USDT', client.SIDE_BUY, funds='5.000', client_oid="salehitest")
print(order)
