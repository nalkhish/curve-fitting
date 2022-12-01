from pet_fit.data import Tac, TwoTcm


def two_tcm(input: Tac, params: TwoTcm) -> Tac:
    """Simulate a 2TCM model.

    Args:
        input (Tac): Input TAC.
        params (TwoTcm): 2TCM parameters.

    Returns:
        Tac: Simulated TAC.
    """
    cpet_tac = Tac(
        time_axis=input.time_axis,
        conc_axis=input.conc_axis,
        times=input.times,
        concs=[],
    )

    prev_time = 0
    prev_ci = 0
    prev_ci_integ = 0
    prev_cnd = 0
    prev_cnd_integ = 0
    prev_cs = 0
    prev_cs_integ = 0

    # simulate TAC for a 2TCM based on input and params
    for time, ci in zip(input.times, input.concs):
        dt = time - prev_time
        dt_half = dt / 2
        # go into input
        d_ci_integ = 0.5 * (ci + prev_ci) * dt
        ci_integ = prev_ci_integ + d_ci_integ
        # go into first compartment
        cnd = (
            params.K1 * ci_integ
            - (
                (params.k2 + params.k3 / (1 + params.k4 * dt_half))
                * (prev_cnd_integ + prev_cnd * dt_half)
            )
            + (
                (params.k4 / (1 + (params.k4 * dt_half)))
                * (prev_cs_integ + (prev_cs * dt_half))
            )
        ) / (1 + ((params.k2 + params.k3 / (1 + (params.k4 * dt_half))) * dt_half))
        cnd_integ = prev_cnd_integ + (0.5 * (cnd + prev_cnd) * dt)
        # go into second compartment
        cs = (
            (params.k3 * cnd_integ) - (params.k4 * (prev_cs_integ + prev_cs * dt_half))
        ) / (1 + (params.k4 * dt_half))
        cs_integ = prev_cs_integ + (0.5 * (cs + prev_cs) * dt)
        # calculate total tac
        ct = cs + cnd
        cb = params.vb * ci
        cpet = ((1 - params.vb) * ct) + cb
        cpet_tac.concs.append(cpet)

        # update dependencies
        prev_time = time
        prev_ci = ci
        prev_ci_integ = ci_integ
        prev_cnd = cnd
        prev_cnd_integ = cnd_integ
        prev_cs = cs
        prev_cs_integ = cs_integ
    return cpet_tac
