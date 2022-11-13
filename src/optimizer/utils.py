"""Utilitaries functions for the optimizer"""

import numpy as np

def compute_score(
    dates:np.array,
    time_limit:int,
    daily_users:np.array):
    """Compute the score of a solution

    Parameters
    ----------
    dates : array
        Dates at which the features were implemented, array of size (number of features,)\n
        Example: [10, 15, 25] -> feature 1 was effective on time step 10, feature 2 on time step 15 and feature 3 on time step 25
    time_limit : int
        Maximum time limit
    daily_users : array
        Numbers of daily users that benefit from each features, array of size (number of features,)\n

    Returns
    -------
    int
        Number of points of the solution
    """
    assert dates.shape == daily_users.shape
    return np.dot(
        (time_limit - dates).clip(min=0),
        daily_users.T
    )