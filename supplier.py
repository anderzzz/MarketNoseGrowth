'''Supplier Agent Definitions

'''
import numpy as np

from fjarrsyn import Agent
from fjarrsyn import Essence, Resource

class Supplier(Agent):

    def __init__(self, name):

        super().__init__(name)

        #
        # Initialize the essence of the Supplier
        #
        essence_keys_lies = ['degree_of_lying']
        essence_init_lies = 0.0

        essence_ = Essence('Supplier Disposition', essence_keys_lies)
        essence_.set_values(essence_init_lies)
        self.set_scaffold(essence_)
