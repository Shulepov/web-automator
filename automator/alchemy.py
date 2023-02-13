import requests
from time import sleep

#url = "https://polygon-mainnet.g.alchemy.com/v2/aGqIQl6tOWm2Cd4Yib13I86NsXv_8Ro2"

class Alchemy:
	class Networks:
		ARBITRUM = "arb-mainnet"
		OPTIMISM = "opt-mainnet"
		POLYGON = "polygon-mainnet"
		ETHEREUM = "eth-mainnet"

	GWEI_IN_WEI = 1000000000
	ETH_IN_WEI = 1000000000000000000

	def __init__(self):
		self.api_key = "aGqIQl6tOWm2Cd4Yib13I86NsXv_8Ro2"

	def get_api_url(self, network):
		return f'https://{network}.g.alchemy.com/v2/{self.api_key}'

	def get_gas_price_wei(self, network):
		payload = {
	    	"id": 1,
	    	"jsonrpc": "2.0",
	    	"method": "eth_gasPrice"
		}

		headers = {
	    	"accept": "application/json",
	    	"content-type": "application/json"
		}
		url = self.get_api_url(network)
		response = requests.post(url, json=payload, headers=headers)
		hex_price = response.json()["result"]
		return int(hex_price, 16)

	def get_gas_price_gwei(network):
		gas_wei = self.get_gas_price_wei(network)
		return gas_wei * 1.0 / Alchemy.GWEI_IN_WEI

	def wait_for_gas_price(self, network, max_target_gwei):
		max_target_gas_wei = max_target_gwei * Alchemy.GWEI_IN_WEI
		while True:
			current_gas = self.get_gas_price_wei()
			if current_gas > max_target_gas_wei:
				sleep(60) #wait 1 minute
			else:
				break

	def get_tokens_balances(self, network, address, tokens):
		payload = {
	    	"id": 0,
	    	"jsonrpc": "2.0",
	    	"method": "alchemy_getTokenBalances",
	    	"params": [
	    		address,
	    		tokens
	    	]
		}
		headers = {
	    	"accept": "application/json",
	    	"content-type": "application/json"
		}
		url = self.get_api_url(network)
		print(url)
		response = requests.post(url, json=payload, headers=headers)
		balances = response.json()["result"]["tokenBalances"]
		ret = {}
		for entry in balances:
			hex_balance_wei = entry["tokenBalance"]
			balance = int(hex_balance_wei, 16) / Alchemy.ETH_IN_WEI
			ret[entry["contractAddress"]] = balance
		return ret

	def get_token_balance(self, network, address, token):
		balances = self.get_tokens_balances(network, address, [token])
		return balances[token]

if __name__ == '__main__':
	#price = get_gas_price(Networks.ARBITRUM)
	#print(price)
	alchemy = Alchemy()
	balances = alchemy.get_tokens_balances(Alchemy.Networks.ARBITRUM, '0x31ecB0819346Edd4Ac31E2C3aDACD6629e411A78', ['0x82aF49447D8a07e3bd95BD0d56f35241523fBab1'])
	print(balances)
	balance = alchemy.get_token_balance(Alchemy.Networks.ARBITRUM, '0x31ecB0819346Edd4Ac31E2C3aDACD6629e411A78', '0x82aF49447D8a07e3bd95BD0d56f35241523fBab1')
	print(balance)
	