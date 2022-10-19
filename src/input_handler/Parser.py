"""Parser to retrieve the informations"""

import os
from src.input_handler.utils import parse_main_params, parse_services, parse_features

class Parser:
    """Parse an input file into a more usable structure"""

    def __init__(self, name) -> None:
        
        self.name = name
        with open(os.path.join("data", name), "r") as f:
            self.input = f.read().strip()


    def parse(self):

        self.prob = {}
        lines = self.input.split("\n")

        # get the main parameters L, G, S, B, F, N
        l, g, s, b, f, n = parse_main_params(lines[0])
        self.prob["L"] = l
        self.prob["G"] = g
        self.prob["S"] = s
        self.prob["B"] = b
        self.prob["F"] = f
        self.prob["N"] = n

        # get the services infos on the lines N°1 to S
        self.prob["services"] = parse_services(lines[1:s+1])

        # get the features infos on the lines S+1 to the end, by group of 2
        self.prob["features"] = parse_features(lines[s+1:])
