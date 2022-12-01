import matplotlib.pyplot as plt

from pet_fit.data import Tac


def tac(tac: Tac, output_filename: str):
    """Plot a TAC and save it to a file."""
    fig, ax = plt.subplots()
    plt.plot(tac.times, tac.concs)
    plt.xlabel(tac.time_axis)
    plt.ylabel(tac.conc_axis)
    plt.title("Arterial Plasma")
    fig.savefig(output_filename)
    plt.close(fig)
