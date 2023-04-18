def update(self, *args, **kwargs):
        '''
        Makes args variadic
        '''
        argc = len(args)
        if argc > 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
