from pet_fit.data import Tac


def _diffs_sqd(tac1: Tac, tac2: Tac):
    """Squared differences between TAC concs.

    Parameters
    ----------
    tac1 : Tac
        First TAC.
    tac2 : Tac
        Second TAC.

    Returns
    -------
    list[float]
        Squared differences between TAC concs.
    """
    return [(c1 - c2) ** 2 for c1, c2 in zip(tac1.concs, tac2.concs)]


def lsq_unweighted(tac1: Tac, tac2: Tac):
    """Least squares cost function, unweighted.

    Parameters
    ----------
    tac1 : Tac
        First TAC.
    tac2 : Tac
        Second TAC.

    Returns
    -------
    float
        Sum of squared differences between TAC concs.
    """
    diffs_sqd = _diffs_sqd(tac1=tac1, tac2=tac2)
    return sum(diffs_sqd)


def lsq_weighted(tac1: Tac, tac2: Tac, weights: list[float]):
    """Least squares cost function, weighted.

    Parameters
    ----------
    tac1 : Tac
        First TAC.
    tac2 : Tac
        Second TAC.
    weights : list[float]
        Weights.

    Returns
    -------
    float
        Sum of squared differences between TAC concs, weighted.
    """
    diffs_sqd = _diffs_sqd(tac1=tac1, tac2=tac2)
    return sum(w * d for w, d in zip(weights, diffs_sqd))
