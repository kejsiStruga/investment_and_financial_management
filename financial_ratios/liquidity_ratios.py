"""
Liquidity Ratios:

Derived from --------> BALANCE SHEET
To measure --------> Firm's ability to meet short term debt obligations
Helps in assessing --------> Firm's liquidity/solvency
"""


class LiquidityRatios:
    def __init__(self, current_assets, current_liabilities, cash,
                 short_term_investments, accounts_receivable):
        self.current_assets = current_assets
        self.current_liabilities = current_liabilities
        self.cash = cash
        self.short_term_investments = short_term_investments
        self.accounts_receivable = accounts_receivable

    def get_current_ratio(self):
        return self.current_assets / self.current_liabilities

    def get_quick_ratio(self):
        return (self.cash + self.short_term_investments + self.accounts_receivable) / self.current_liabilities

    def get_cash_ratio(self):
        return self.cash/self.current_liabilities


if __name__ == '__main__':
    current_assets = 100000
    current_liabilities = 7832
    cash = 2748
    short_term_investments = 3278
    accounts_receivable = 323

    liquidityRatios = LiquidityRatios(current_assets, current_liabilities, cash, short_term_investments, accounts_receivable)

    print(liquidityRatios.get_current_ratio())
