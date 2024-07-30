import requests

# Replace with your BlockCypher API token
API_TOKEN = '0e6399a065d14c6da0210a5edabfd999'

def get_address_info(wallet_address):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}?token={API_TOKEN}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Error fetching address information:', response.status_code, response.text)

def convert_wallet_to_point(wallet_address):
    address_info = get_address_info(wallet_address)
    public_key = address_info.get('public')
    if public_key:
        print(f"Public Key for address {wallet_address}: {public_key}")
        # Add your logic for converting the public key to a point on the elliptic curve here
        # For demonstration purposes, we will just return the public key
        return public_key
    else:
        raise Exception('Public key not found for this address.')

# Example usage
if __name__ == "__main__":
    wallet_address = 'bc1qnuz0xer03tgrkw7gy5xnacrtuzpv3g8lrr56te'
    try:
        public_key = convert_wallet_to_point(wallet_address)
        print(f"Public Key: {public_key}")
    except Exception as e:
        print(e)
