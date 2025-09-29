from . import *

class GlobalElements():        
    def topBar(self, **kwqrg):
        return MDTopAppBar(**kwqrg)
    
    def bottomBar(self, **kwqrg):
        return MDBottomAppBar()