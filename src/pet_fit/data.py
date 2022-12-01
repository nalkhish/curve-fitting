from dataclasses import dataclass


@dataclass
class Tac:
    time_axis: str
    conc_axis: str
    times: list[float]
    concs: list[float]


@dataclass
class TwoTcm:
    K1: float
    k2: float
    k3: float
    k4: float
    vb: float
