from pet_fit.data import Tac


def tac(filename: str):
    """Read a TAC from a file and return a Tac object."""
    # initiate empty Tac object
    tac = Tac(time_axis="", conc_axis="", times=[], concs=[])

    # read the file
    with open(filename) as f:
        lines = f.readlines()

    # fill Tac object
    tac.time_axis, tac.conc_axis = lines[0].split()
    for line in lines[1:]:
        time, conc = line.split()
        tac.times.append(float(time))
        tac.concs.append(float(conc))

    return tac
