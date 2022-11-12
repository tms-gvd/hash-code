import numpy as np

class Engineer:

    def __init__(self, name, time_limit, create_bin) -> None:
        
        self.name = name
        self.wait = 0
        self.step = 0
        self.time_limit = time_limit
        self.create_bin = create_bin