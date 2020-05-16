"""

Decomposes ROE into 3 components:

1. Profitability - net profit margin

2. Asset efficiency - asset turnover

3. Leverage - equity multiplier

"""


class DuPoint:
    def __init__(self, net_income, sales, total_assets, book_value_of_equity):
        self.net_income = net_income
        self.book_value_of_equity = book_value_of_equity
        self.total_assets = total_assets
        self.sales = sales

    def get_roe(self):
        return (self.net_income / self.sales) * (self.sales / self.total_assets) * (
                    self.total_assets / self.book_value_of_equity)

