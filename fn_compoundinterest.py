#!/bin/python3

# spmather
# 2025-11-23


def compoundinterest(principal,rate,periods,years):
    """Compound interest is A = P(1+(r/n))^nt"""
    # Solve for A.  Vars P,r,n,t 
    rate_d_period  = rate / periods
    rate_d_period  = rate_d_period + 1
    years_t_period = periods * years
    growth         = rate_d_period ** years_t_period
    amount         = principal * growth
    return amount

# fin
