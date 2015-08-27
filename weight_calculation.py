"""
This file contains the base class to calculate weights for each
state
"""

class StateWeight(object):
    """
    Provides facilities for calculating the weight of a given state
    (such as a molecule, or mutant).
    
    Arguments
    ---------
    proposal : namedtuple of type TopologyProposal
        Contains the newly-proposed topology and
        associated metadata.

    Properties
    ----------
   log_ weight : float, read only
        The calculated log weight of this state
    """
    
    def __init__(self, proposal):
        pass

    @property
    def log_weight(self):
        return 0
