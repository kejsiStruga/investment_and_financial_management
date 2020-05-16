def get_future_value(principle, rate, years):
    future_value = pow(principle(1 + rate / 100), years)
    return future_value


if __name__ == "__main__":
    principle_amount = 100  # $100
    rate_of_interest = 5  # 5 percent
    years_to_go_by = 3

    print(get_future_value(principle_amount, rate_of_interest, years_to_go_by))
