import requests

# Function to get address information from Blockstream API
def get_address_info(wallet_address):
    url = f'https://blockstream.info/api/address/{wallet_address}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Error fetching address information: {response.status_code} - {response.text}')

# Function to convert wallet address to public key and extract additional details
def extract_wallet_details(wallet_address):
    address_info = get_address_info(wallet_address)
    details = {
        'address': wallet_address,
        'balance': address_info.get('chain_stats', {}).get('funded_txo_sum', 0) - address_info.get('chain_stats', {}).get('spent_txo_sum', 0),
        'transactions': address_info.get('chain_stats', {}).get('tx_count', 0),
        'unconfirmed_balance': address_info.get('mempool_stats', {}).get('funded_txo_sum', 0) - address_info.get('mempool_stats', {}).get('spent_txo_sum', 0)
    }
    return details

# Example usage
if __name__ == "__main__":
    wallet_address = 'bc1qnuz0xer03tgrkw7gy5xnacrtuzpv3g8lrr56te'
    try:
        wallet_details = extract_wallet_details(wallet_address)
        print(f"Wallet Details: {wallet_details}")
    except Exception as e:
        print(f"An error occurred: {e}")