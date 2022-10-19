"""Tests about the correctness of the input"""

import os
from src.input_handler.utils import parse_features, parse_main_params, parse_services


def check_input(file_name:str):
    """Check the correctness of an input file

    Parameters
    ----------
    file_name : str
        name of the input file in the data folder
    """

    with open(os.path.join("data", file_name), "r") as f:
        inp = f.read().strip()
    
    lines = inp.split("\n")

    # Get the main parameters
    main_params = parse_main_params(lines[0])
    
    # Check that there are exactly 6 values
    assert len(main_params) == 6, "There should be 6 main parameters"
    l, g, s, b, f, n = main_params

    # Check that the input have the correct number of lines
    assert len(lines) == 1 + s + 2*f, f"File {file_name}: Wrong number of lines in the input"

    # Check that their values are valid
    assert 1 <= l <= int(1e3), f"Wrong value for L, {l}"
    assert 1 <= g <= int(1e5), f"Wrong value for G, {g}"
    assert 1 <= s <= int(1e4), f"Wrong value for S, {s}"
    assert 1 <= b <= int(1e4), f"Wrong value for B, {b}"
    assert 1 <= f <= int(1e4), f"Wrong value for F, {f}"
    assert 1 <= n <= 10, f"Wrong value for N, {n}"

    # Get the services
    services = parse_services(lines[1:s+1])

    # Check the correctness
    assert len(services) == s, f"File {file_name}: Missing services"
    for name, bin in services.items():
        assert 0 <= int(bin) <= b-1, f"File {file_name}: Wrong value for the bin associated to service {name}, {bin}"

    # Get the features
    features = parse_features(lines[s+1:])

    # Check the correctness
    assert len(features) == f, f"File {file_name}: Missing features"
    for name, feat in features.items():
        assert len(feat["impl_services"]) == feat["n_services"], f"File {file_name}: Number of services does not match the services associated to the feature {name}"
        assert 1 <= feat["difficulty"] <= int(1e2), f"File {file_name}: Wrong value for the difficulty of the feature {name}"
        assert 1 <= feat["n_users"] <= int(1e5), f"File {file_name}: Wrong value for the number of users of the feature {name}"


def test_inputs():
    """Test all the input file present in the folder data"""

    for filename in os.listdir("data"):
        check_input(filename)
