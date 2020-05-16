def get_future_value(principle, rate, years):
    fv = principle*pow((1 + rate / 100), years)
    return fv


if __name__ == "__main__":
    principle_amount = 100  # $100
    rate_of_interest = 10  # 5 percent
    years_to_go_by = 2

    print(get_future_value(principle_amount, rate_of_interest, years_to_go_by))
