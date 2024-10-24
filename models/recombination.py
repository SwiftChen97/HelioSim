def recombination_rate(n, p, n0, p0, tau_n, tau_p, ni):
    """Calculate the Shockley-Read-Hall recombination rate."""
    R = (n * p - ni**2) / (tau_p * (n + n0) + tau_n * (p + p0))
    return R
