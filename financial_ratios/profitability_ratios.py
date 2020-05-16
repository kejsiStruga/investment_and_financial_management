"""
Profitability ratios:

Derived from ----------> INCOME STATEMENT
To Measure -----------> Firm's ability to generate profits as a percentage of sales generated
"""


class ProfitabilityRatio:
    def __init__(self, sales, gross_profit, operating_income, ebit, net_income):
        self.sales = sales
        self.gross_profit = gross_profit
        self.operating_income = operating_income
        self.ebit = ebit
        self.net_income = net_income

    def get_gross_margin(self):
        return self.gross_profit / self.sales

    def get_operating_margin(self):
        return self.operating_income / self.sales

    def get_ebit_margin(self):
        return self.ebit / self.sales

    def get_net_profit_margin(self):
        return self.net_income / self.sales


if __name__ == '__main__':
    sales = 100000
    gross_profit = 7832
    operating_income = 2748
    ebit = 3278
    net_income = 323

    profitabilityRatio = ProfitabilityRatio(sales, gross_profit, operating_income, ebit, net_income)

    print(profitabilityRatio.get_ebit_margin())
