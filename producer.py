'''Producer Agent Definitions

'''
from fjarrsyn import Agent
from fjarrsyn import Essence, Resource, Belief
from fjarrsyn import Buzz, Direction
from fjarrsyn import ResourceMap
from fjarrsyn import Compulsion
from fjarrsyn import MessageOperator

from funcs import _rnd_vector

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
        self.set_scaffold(resource_)

        #
        # Initialize the beliefs of the Buyer
        #
        belief_ = None

        #
        # Initialize messages used by Producer
        #
        buzz_unit_offer = Buzz('Unit Offer', ('unit_feature_vec', 'price'))
        direction_buy = Direction('Buy Unit on Offer', ('buy_decision',))
        direction_counter_offer = Direction('Issue Counter Offer', ('price_counter',))

        self.set_messages(buzz_unit_offer, direction_buy, direction_counter_offer)


'''Resource Map to add or subtract cash on hand for Producer'''
map_adjust_cash = ResourceMap('Adjust Producer Cash Level', 'delta', 'cash on hand', ('increment',))

'''Message Operator to extract unit resource data alone for Producer'''
op_resource_units = MessageOperator()

'''Principles for System: Compulsion to generate cash from a collection of units for a producer.'''
unit_to_cash = Compulsion('units to cash', law_unit_to_cash, map_adjust_cash,
                          op_resource_units, op_essence_disposition,
                          compel_func_kwargs={})

