import requests

# Replace with your BlockCypher API token
API_TOKEN = '0e6399a065d14c6da0210a5edabfd999'

class WalletAddressError(Exception):
    """Custom exception for wallet address errors."""
    pass

def get_address_info(wallet_address):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{wallet_address}?token={API_TOKEN}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        raise WalletAddressError(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        raise WalletAddressError(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        raise WalletAddressError(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        raise WalletAddressError(f"An error occurred: {req_err}")

    try:
        address_info = response.json()
    except ValueError:
        raise WalletAddressError("Invalid JSON response")

    return address_info

def convert_wallet_to_point(wallet_address):
    address_info = get_address_info(wallet_address)
    public_key = address_info.get('public')
    if not public_key:
        raise WalletAddressError('Public key not found for this address.')

    # Additional details you might want to extract
    balance = address_info.get('balance')
    total_received = address_info.get('total_received')
    total_sent = address_info.get('total_sent')
    n_tx = address_info.get('n_tx')

    print(f"Public Key for address {wallet_address}: {public_key}")
    print(f"Balance: {balance} satoshis")
    print(f"Total Received: {total_received} satoshis")
    print(f"Total Sent: {total_sent} satoshis")
    print(f"Number of Transactions: {n_tx}")

    # Add your logic for converting the public key to a point on the elliptic curve here
    # For demonstration purposes, we will just return the public key
    return public_key

# Example usage
if __name__ == "__main__":
    wallet_address = 'bc1qnuz0xer03tgrkw7gy5xnacrtuzpv3g8lrr56te'
    try:
        public_key = convert_wallet_to_point(wallet_address)
        print(f"Public Key: {public_key}")
    except WalletAddressError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")