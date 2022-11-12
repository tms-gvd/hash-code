import numpy as np

def compute_score(dates, time_limit, daily_users):
    assert dates.shape == daily_users.shape
    return np.dot(
        (time_limit - dates).clip(min=0),
        daily_users.T
    )