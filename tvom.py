import numpy as np
"""
SIMPLE INTEREST FORMULAS

    c_0 ---> the principle
    r ---> the interest rate
    n ---> the number of time periods in the year
    c_n ---> the value at the last cash flow, which needs to be calculated
"""


def get_simple_interest_amount(c_0, r, n):
    c_n = c_0 * (1 + n*r)
    return c_n


def get_simple_interest_principal_amount(c_n, r, n):
    c_0 = c_n/(1 + n*r)
    return c_0


def get_simple_interest_with_varying_time_periods(c_0, r, n, type_of_time_period='German'):
    f = 0
    if type_of_time_period == 'German':
        f = 30/360
    c_f = c_0 * (1 + r*f)
    return c_f


"""
COMPOUND INTEREST FORMULAS
"""


def get_future_value(principle, rate, nr_of_time_periods_in_years):
    fv = principle*pow((1 + rate / 100), nr_of_time_periods_in_years)
    return fv


def get_present_value_by_discounting(future_value, rate, nr_of_time_periods_in_years):
    pv = future_value/pow( (1+rate/100), nr_of_time_periods_in_years)
    return pv


def get_time(c_n, c_0, q):
    """

    :param c_n: future value
    :param c_0: principal, aka. present value
    :param q: (1 + r)
    :return: time period - n - in years
    """
    n = (np.log(c_n) - np.log(c_0))/np.log(q)
    return n


def get_interest_rate(c_n, c_0, n):
    r = np.sqrt(n, (c_n / c_0)) - 1
    return r


if __name__ == "__main__":
    principle_amount = 100  # $100
    rate_of_interest = 10  # 5 percent
    years_to_go_by = 2

    print(get_future_value(principle_amount, rate_of_interest, years_to_go_by))

    print(get_present_value_by_discounting(get_future_value(principle_amount, rate_of_interest, years_to_go_by),
                                           rate_of_interest,
                                           years_to_go_by))
