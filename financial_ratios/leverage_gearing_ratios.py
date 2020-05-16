"""
Measures a firm's reliance on debt as a source of financing

Derived from Balance Sheet and market value

"""


class LeverageGearingRatios:
    def __init__(self, total_debt, total_equity, net_debt, market_value, total_assets, book_value_of_equity):
        self.total_debt = total_debt
        self.total_equity = total_equity
        self.net_debt = net_debt
        self.market_value = market_value
        self.total_assets = total_assets
        self.book_value_of_equity = book_value_of_equity

    def get_debt_equity(self):
        return self.total_debt/self.total_equity

    def get_debt_to_capital(self):
        return self.total_debt/(self.total_debt + self.total_equity)

    def get_debt_to_ev(self):
        return self.net_debt/(self.market_value + self.net_debt)

    def get_equity_multiplier(self):
        return self.total_assets/self.book_value_of_equity


if __name__ == '__main__':
    total_debt = 100
    total_equity = 200
    net_debt = 20
    market_value = 24
    total_assets = 47
    book_value_of_equity = 34

    leverageGearingRatios = LeverageGearingRatios(total_debt, total_equity, net_debt, market_value, total_assets, book_value_of_equity)

    print(leverageGearingRatios.get_debt_equity())
