import requests
import json
import time

def get_total_value(api_url, wallet_address):
    try:
        url = api_url.replace("WALLET_ADDRESS", wallet_address)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        result_data = data.get("result", {}).get("data", {})
        total_value = sum(result_data.values())
        return total_value

    except requests.RequestException as e:
        print(f"Error querying address {wallet_address}: {e}")
        return 0.0

with open('public.txt', 'r') as file:
    wallet_addresses = [line.strip() for line in file if line.strip()]

api_url_template = "https://api.getgrass.io/zvTlZ8PRouKKGTGNzg4k?input=%7B%22walletAddress%22:%22WALLET_ADDRESS%22%7D"

all_addresses_total = 0.0

for wallet_address in wallet_addresses:
    address_total = get_total_value(api_url_template, wallet_address)
    print(f"Address: {wallet_address}, Value Sum: {address_total}")
    all_addresses_total += address_total

    time.sleep(0.5)

print(f"All Addresses Total Value Sum: {all_addresses_total}")
