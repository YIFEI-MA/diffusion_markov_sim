from VoterModel import VoterModel
from data import *

vm = VoterModel([stocks[key] for key in stocks], [[key, opinions[key]] for key in opinions])
vm.set_initial_price(price)
vm.draw_opinion_graph()
vm.iterate(3, individual_return, market_return, betas=beta, sigmas=sigma)
vm.draw_opinion_graph()
vm.show_price_history()
