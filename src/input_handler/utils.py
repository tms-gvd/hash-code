"""Utilitaries functions for Generator.py"""

from typing import List
from string import ascii_lowercase

def conv26(inp:int, len:int) -> List:
    """Convert a integer in base 26

    Parameters
    ----------
    inp : int
        input integer, must be <= 10000
    len : int
        len+1 is the length of the decomposition

    Returns
    -------
    List
        Decomposition of the input in base 26\n
        Examples:\n
            int2str(15,2) -> [0, 0, 15]\n
            int2str(27,2) -> [0, 1, 1]\n
            int2str(1e4,2) -> [14, 20, 16]
    """

    assert inp <= 10000, "Input must be <= 10000"
    if len==0:
        return [inp//1]
    else:
        ix = int(inp//(26**len))
        new_inp = int(inp - ix*(26**len))
        return [ix] + conv26(new_inp, len-1)


def int2str(inp:int) -> str:
    """Convert an int into a-z base

    Parameters
    ----------
    inp : int
        Integer to convert. Must be less than 1e4.

    Returns
    -------
    str
        Conversion of the input in the a-z base.\n
        Examples:\n
            1 -> aaa
            2 -> aab
            27 -> aba
    """

    assert 0 < inp < int(1e4), "Wrong values for input, must be less than 1e4"
    decomp = conv26(inp - 1, 2)
    return "".join([ascii_lowercase[val] for val in decomp])


def parse_main_params(inp:str) -> List:
    """Parse the first line of an input file

    Parameters
    ----------
    inp : str
        First line of the input file, ideally like this "L G S B F N"

    Returns
    -------
    List of int
        A list of integers containing the parameters, ideally like this: [L, G, S, B, F, N]
    """

    # parse L, G, S, B, F, N
    main_params = inp.split(" ")

    return [int(val) for val in main_params]


def parse_services(lines:List) -> dict:
    """Parse the lines describing the services

    Parameters
    ----------
    lines : List of str
        List of the lines giving the name and the associated bin of each service

    Returns
    -------
    dict
        For each service:\n
        Key -> name of the service\n
        Value -> bin associated (in str format!)
    """

    services = {}
    for serv_line in lines:
        name, bin = serv_line.split(" ")
        services[name] = bin
    
    return services


def parse_features(lines:List) -> dict:
    """Parse the lines describing the features

    Parameters
    ----------
    lines : List of str
        List of the lines giving the name of the featuren the number and list of associated services, the difficulty and the numbers of daily users

    Returns
    -------
    dict
        For each feature:\n
        Key -> name of the feature\n
        Value -> dict(
            "n_services": integer, number of associated services,
            "impl_services": List of str, list of the name of the associated services,
            "difficulty": integer, difficulty,
            "n_users": integer, number of daily users
        )
    """

    features = {}
    for ix in range(0, len(lines), 2):
        name, n_serv, diff, n_users = lines[ix].split(" ")
        services = lines[ix+1].split(" ")
        features[name] = {
            "n_services": int(n_serv),
            "difficulty": int(diff),
            "n_users": int(n_users),
            "impl_services": services
        }
    
    return features
