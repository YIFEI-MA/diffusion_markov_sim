from VoterModel import VoterModel
from data import *

vm = VoterModel([stocks[key] for key in stocks], [[key, opinions[key]] for key in opinions])
vm.draw_opinion_graph()
vm.iterate(3)
vm.draw_opinion_graph()
