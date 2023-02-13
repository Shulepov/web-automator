from .webbot import Browser
from .metamask import Metamask
from .alchemy import Alchemy

class Arbitrum:
	NetworkName = "Arbitrum One"
	class Token:
		WETH = "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1"
		USDC = "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8"

class Optimism:
	NetworkName = "Optimism"

class Polygon:
	NetworkName = "Polygon"

class EthMainnet:
	NetworkName = "Ethereum Custom"


def network_to_alchemy_network(network):
	networks = {}
	networks[Arbitrum.NetworkName] = Alchemy.Networks.ARBITRUM
	networks[Optimism.NetworkName] = Alchemy.Networks.OPTIMISM
	networks[Polygon.NetworkName] = Alchemy.Networks.POLYGON
	networks[EthMainnet.NetworkName] = Alchemy.Networks.ETHEREUM
	return networks[network]