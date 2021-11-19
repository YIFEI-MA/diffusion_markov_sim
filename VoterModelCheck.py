import warnings

import ndlib.models.opinions as op
import networkx as nx
from ndlib.models import ModelConfig
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend

from Visualizer import *

graph = nx.erdos_renyi_graph(100, 0.9)

model = op.VoterModel(graph)
config = ModelConfig.Configuration()
config.add_model_parameter('fraction_infected', 0.5)
model.set_initial_status(config)

iterations = model.iteration_bunch(10000)
trends = model.build_trends(iterations)
warnings.filterwarnings("ignore", category=DeprecationWarning)

setup_viz()
viz = DiffusionTrend(model, trends)
p = viz.plot("VoterModel.png")
