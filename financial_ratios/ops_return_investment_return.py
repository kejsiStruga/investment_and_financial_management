"""

Compare its income to its investment using financial info

Derived from BALANCE SHEET

"""

class OpsReturnInvestmentReturn:
    def __init__(self, net_income, book_value_of_equity, interest_expense, total_assets, ebit, tax_rate, net_debt, sales):
        self.net_income = net_income
        self.book_value_of_equity = book_value_of_equity
        self.interest_expense = interest_expense
        self.total_assets = total_assets
        self.ebit = ebit
        self.tax_rate = tax_rate
        self.net_debt = net_debt
        self.sales = sales

    def get_return_on_equity(self):
        return self.net_income/self.book_value_of_equity

    def get_return_on_assets(self):
        return (self.net_income + self.interest_expense)/self.total_assets

    def get_return_on_invested_capital(self):
        return (self.ebit*(1-self.tax_rate))/(self.book_value_of_equity + self.net_debt)

    def get_asset_turn(self):
        return self.sales/self.total_assets
