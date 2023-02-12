import requests
from time import sleep

#url = "https://polygon-mainnet.g.alchemy.com/v2/aGqIQl6tOWm2Cd4Yib13I86NsXv_8Ro2"

api_key = "aGqIQl6tOWm2Cd4Yib13I86NsXv_8Ro2"

ARBITRUM = "arbitrum"
OPTIMISM = "optimism"
POLYGON = "polygon"
ETHEREUM = "ethereum"

networks = {
	ARBITRUM: "arb-mainnet",
	OPTIMISM: "opt-mainnet",
	POLYGON: "polygon-mainnet",
	ETHEREUM: "eth-mainnet"
}

GWEI_IN_WEI = 1000000000

def get_gas_price_wei(network):
	payload = {
    	"id": 1,
    	"jsonrpc": "2.0",
    	"method": "eth_gasPrice"
	}

	headers = {
    	"accept": "application/json",
    	"content-type": "application/json"
	}
	url = f'https://{networks[network]}.g.alchemy.com/v2/{api_key}'
	response = requests.post(url, json=payload, headers=headers)
	hex_price = response.json()["result"]
	return int(hex_price, 16)

def get_gas_price_gwei(network):
	gas_wei = get_gas_price_wei(network)
	return gas_wei * 1.0 / GWEI_IN_WEI

def wait_for_gas_price(network, max_target_gwei):
	max_target_gas_wei = max_target_gwei * GWEI_IN_WEI
	while True:
		current_gas = get_gas_price_wei()
		if current_gas > max_target_gas_wei:
			sleep(60) #wait 1 minute
		else:
			break

if __name__ == '__main__':
	price = get_gas_price("arbitrum")
	print(price)