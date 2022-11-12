import numpy as np
from src.optimizer.utils import compute_score

def test_compute_score():
    dates1 = np.array([25, 98, 76, 45])
    dates2 = np.array([15, 10, 76, 20])
    time_limit = 20
    daily_users = np.array([100, 50, 20, 10])
    
    assert compute_score(dates1, time_limit, daily_users) == 0
    assert compute_score(dates2, time_limit, daily_users) == 1000