from heppy.framework.analyzer import Analyzer
from heppy.papas.pfalgo.pfblockbuilder import PFBlockBuilder
from heppy.papas.data.papasevent import PapasEvent
from heppy.papas.pfalgo.distance  import Distance


class PapasPFBlockBuilder(Analyzer):
    ''' Module to construct blocks of connected clusters and tracks 
        particles will eventually be reconstructed from elements of a block
        
        
        Usage:
        from heppy.analyzers.PapasPFBlockBuilder import PapasPFBlockBuilder
        pfblocks = cfg.Analyzer(
            PapasPFBlockBuilder,
            tracks = 'tracks', 
            ecals = 'ecal_clusters', 
            hcals = 'hcal_clusters', 
            history = 'history_nodes', 
            output_blocks = 'reconstruction_blocks'
        )
        
        tracks: Name of dict in Event where tracks are stored
        ecals: Name of dict in Event where ecals are stored
        hcals: Name of dict in Event where hcals are stored
        history: Name of history_nodes, can be set to None.
        output_blocks: Name to be used for the blocks dict
        
    '''
    def __init__(self, *args, **kwargs):
        super(PapasPFBlockBuilder, self).__init__(*args, **kwargs)
        
                
    def process(self, event):
        
        papasevent = event.papasevent
        
        distance = Distance()
        
        
        uniqueids = []
        uniqueids = list(papasevent.get_collection('ts').keys()) + list(papasevent.get_collection('em').keys()) + list(papasevent.get_collection('hm').keys())   
        uniqueids = sorted(uniqueids)
        blockbuilder = PFBlockBuilder(uniqueids, papasevent, distance)
            
        papasevent.add_collection(blockbuilder.blocks)

        
