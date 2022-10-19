"""Generate an input file from the basic parameters"""

import random
from src.input_handler.utils import int2str
import os

class RandomGenerator:

    def __init__(
        self,
        l:int,
        g:int,
        s:int,
        b:int,
        f:int,
        n:int
    ) -> None:

        """Initialize and check the validity of the parameters

        Parameters
        ----------
        l : int
            time limit in days
        g : int
            number of Google engineers
        s : int
            number of services
        b : int
            number of initial binaries
        f : int
            number of features
        n : int
            duration in days to create a new binary
        """

        self.l = l
        self.g = g
        self.s = s
        self.b = b
        self.f = f
        self.n = n

        self.input = f"{l} {g} {s} {b} {f} {n}\n"


    def create_services(self):

        for k in range(1, self.s+1):

            # create a name for each service
            name = "s-" + int2str(k)

            # add name and a random binary assigned to it to the input
            self.input += name + " " + str(random.randint(0, self.b-1)) + "\n"


    def create_features(self):

        # for each feature, do
        for k in range(1, self.f+1):

            # create a name
            name = "f-" + int2str(k)

            # add the characteristics
            modif_serv = random.randint(1, self.s)  # the number of services that need to be modified
            diff = random.randint(1, int(1e2))      # the difficulty
            users = random.randint(1, int(1e5))     # number of daily users
            self.input += f"{name} {modif_serv} {diff} {users}\n"

            # sample the services affected to the feature
            serv_ixs = random.sample(
                [_ for _ in range(1, self.s+1)],
                k=modif_serv
            )
            self.input += " ".join([int2str(val) for val in serv_ixs]) + "\n"


    def save(self, name):
        
        # append text extension to name if it does not end with it
        if not name.endswith(".txt"):
            name += ".txt"

        text_file = open(os.path.join("data", name), "w")
        text_file.write(self.input.strip())
        text_file.close()
