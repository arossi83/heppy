
class POD(object):
    '''Base POD class for FCC EDM.
    '''

    def __init__(self, fccobj):
        '''make sure to set the fccobj attribute in your base class.'''
        self.fccobj = fccobj
        self.objid = (self.fccobj.getObjectID().index,
                      self.fccobj.getObjectID().collectionID)

    def __eq__(self, other):
        '''Returns true if the internal FCC pod is the same,
        It will be the case for two copies with the same internal pod, 
        e.g. two copies of the same particle.
        '''
        return self.objid == other.objid
        
    def __hash__(self):
        '''returns a hash built from the podio index and collection ID. 
        needed to use fcc objects as dictionary keys. 
        '''
        return hash( self.objid )

                
