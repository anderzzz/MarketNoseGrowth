'''Market AgentManagementSystem

'''
import networkx as nx

from fjarrsyn import AgentManagementSystem
from fjarrsyn import node_maker

from producer import unit_to_cash

'''Structure and default content of agent environments'''
ENV_MESSAGE = {'cash' : 0.0, 'unit_features' : None, 'accept' : False}

class Market(AgentManagementSystem):

    def __init__(self, name, agents_producer, agents_supplier):

        #
        # Create agent graph and initialize parent class
        #
        agents_all = agents_producer + agents_supplier
        nodes_producer = node_maker(agents_producer, envs=[ENV_MESSAGE] * len(agents_producer))
        nodes_supplier = node_maker(agents_supplier, envs=[ENV_MESSAGE] * len(agents_supplier))
        agent_graph = nx.generators.complete_multipartite_graph(nodes_producer, nodes_supplier)

        super().__init__(name, agents_all, agent_graph)

        #
        # Define system laws to compel and mutate the Agents
        #
        self.set_law(unit_to_cash)
