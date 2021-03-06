from service import Service

class Discovery(Service):
    """
    A Discovery service manages joining the mesh and other lifecycle operations
    """

    def __init__(self, path):

        Service.__init__(self,
                         path,
                         name='discovery', 
                         description = 'Discover all nodes in the mesh, and join as a node',
                         version=1)

