'''The steps taken to move the system forward one day

'''
from fjarrsyn import Mover

def engine(agent_ms):
    '''Mover Engine to model one day in the market

    Parameters
    ----------
    agent_ms : AgentManagementSystem
        Mandatory input of the agent management system to be moved forward

    '''
    for producer_supplier_edge in agent_ms.shuffle_edges(False,
                                                         agent_ms.agents_graph.size(),
                                                         False):
        producer_node = producer_supplier_edge[0]
        supplier_node = producer_supplier_edge[1]

        supplier_node.agent_content.enact('Publish Unit Offer')
        producer_node.agent_content.enact('Evaluate Unit Offer')
        supplier_node.agent_content.enact('Accept Transaction Or Update Offer')
        producer_node.agent_content.enact('Transact Resources')

    for agent_node in agent_ms:
        agent_ms.engage_all_verbs(agent_node.agent_content)

market_day = Mover('One Market Day', engine)
