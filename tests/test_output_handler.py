"""Check the validity of the solutions in solutions folder"""

import os
from src.input_handler.Parser import Parser

def check_solution(sol_name:str, inp_name:str):

    inp = Parser(inp_name)
    inp.parse()
    services = inp.services.keys()
    features = inp.services.keys()
    
    with open(os.path.join("data", sol_name), "r") as f:
        sol = f.read().strip()

    lines = sol.split("\n")

    n_eng = int(lines[0])

    ix = 1
    while ix<len(lines):
        n_task = int(lines[ix])
        for i, line in enumerate(lines[ix:ix + n_task]):
            words = line.split(" ")
            action = words[0]
            assert action in ["impl", "move", "new", "wait"], f"Wrong value at line {ix+i}: {line}"
            if action=="impl":
                assert words[1] in services, f"Wrong service for action 'impl' at line {ix+i}: {line}"
                # TODO: Add a check for the number of the binary
            elif action=="move":
                pass