'''Producer Agent Definitions

'''
import numpy as np

from fjarrsyn import Agent
from fjarrsyn import Essence, Resource

def _rnd_vector(n_dim, magnitude=1.0):
    '''Generate random vector of specific dimension and magnitude'''

    vals = [np.random.ranf() - 0.5 for k in range(n_dim)]
    radial_adjust = np.sqrt(np.dot(vals, vals)) / magnitude

    return np.divide(vals, radial_adjust)

class Producer(Agent):

    def __init__(self, name, essence_ndim=5, cash_start=100.0, opex_per_resource=5.0):

        super().__init__(name)

        #
        # Initialize the essence of the Producer
        #

        # How Producer converts resource to cash
        essence_keys_cash_conv = ['cash_converter_{}'.format(k) for k in range(essence_ndim)]
        essence_init_cash_conv = list(_rnd_vector(essence_ndim))

        # Operating expenses
        essence_keys_opex = ['opex_per_resource']
        essence_init_opex = opex_per_resource

        # Join all parts of essence together
        essence_ = Essence('Producer Disposition', essence_keys_cash_conv + \
                                                   essence_keys_opex)
        essence_.set_values(essence_init_cash_conv + \
                            essence_init_opex)
        self.set_scaffold(essence_)

        #
        # Initialize the resources of the Producer
        #
        resource_ = Resource('Stock', ['cash on hand', 'productive_units'])
        resource_.set_values(cash_start, [])

        #
        # Initialize the beliefs of the Buyer
        #
        belief_ = None