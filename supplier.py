'''Supplier Agent Definitions

'''
import numpy as np

from fjarrsyn import Agent
from fjarrsyn import Essence, Resource

from funcs import _rnd_vector

class Supplier(Agent):

    def __init__(self, name, cash_start=0.0, feature_ndims=5, n_unit_init=10,
                 magnitude_generator=np.random.pareto, magnitude_generator_kwargs={'a':2.0}):

        super().__init__(name)

        #
        # Initialize the essence of the Supplier
        #
        essence_keys_lies = ['degree_of_lying']
        essence_init_lies = 0.0

        essence_ = Essence('Supplier Disposition', essence_keys_lies)
        essence_.set_values(essence_init_lies)
        self.set_scaffold(essence_)

        #
        # Initialize the resource of the Supplier
        #
        resource_ = Resource('Stock', ['cash on hand', 'sales_units'])
        spawned_units = []
        for k_unit in range(n_unit_init):
            mag = magnitude_generator(**magnitude_generator_kwargs)
            spawned_units.append(_rnd_vector(feature_ndims, mag))

        resource_.set_values(cash_start, spawned_units)
        self.set_scaffold(resource_)