"""Convert a solution into txt format"""

import os

class ParseSolution:
    """Parse a solution into the correct submission"""

    def __init__(self, sol) -> None:
        """
        Parameters
        ----------
        sol : List of array
            Solution is List of array.\n
            Each array gives the actions of an engineer. It is of shape (number of actions, 3).\n
            Each action is caracterized by 3 numbers.\n
            The first number gives the type of action: 0 for implementing a feature, 1 for moving a services, 2 for creating a binary and 3 for waiting.\n
            The second number tells the feature to implement, the service to move or the time to wait. Ignored if first number is 2 (creating a binary).\n
            The third number tells the binary in which the feature is implemented or the service moved to. Ignored if first number is 2 or 3 (creating a binary or waiting).\n
        """
        
        self.sol = sol
        self.sub = str(len(self.sol)) + "\n"

    def convert(self, ix2features, ix2services):
        
        for ix, engineer in enumerate(self.sol):
            
            assert engineer.shape[1]==3, f"Wrong shape for engineer {ix}, should be 3"
            self.sub += f"{engineer.shape[0]}\n"

            for task in engineer:

                info1, info2, info3 = task

                if info1 == 0:
                    self.sub += "impl " + str(ix2features[info2]) + " " + str(info3) + "\n"
                elif info2 == 1:
                    self.sub += "move " + str(ix2services[info2]) + " " + str(info3) + "\n"
                elif info2 == 2:
                    self.sub += "new " + "\n"
                elif info2 == 3:
                    self.sub += "wait " + str(info2) + "\n"
                else:
                    raise ValueError("Wrong first vamue")
    
    def save(self, name):
        text_file = open(os.path.join("solutions", name), "w")
        text_file.write(self.sub.strip())
        text_file.close()
