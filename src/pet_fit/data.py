from dataclasses import dataclass


@dataclass
class Tac:
    time_axis: str
    conc_axis: str
    times: list[float]
    concs: list[float]
