class Callback:
    '''
        Description: api callback function object
        params:
            - function - function to call as callback
            - return_type -  callback function return type
    '''
    def __init__(self, function=None, return_type=None):
        self.function = function
        self.return_type = return_type
