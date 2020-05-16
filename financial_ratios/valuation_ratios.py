"""

Helps investors assess te market value of a firm

Intended to make intra-industry comparisons of firms valuations

"""


class ValuationRatios:
    def __init__(self, market_cap, net_income, share_price, earnings_per_share, market_value_of_equity, debt, cash, ebit, sales):
        self.market_cap = market_cap
        self.net_income = net_income
        self.share_price = share_price
        self.earnings_per_share = earnings_per_share
        self.market_value_of_equity = market_value_of_equity
        self.debt = debt
        self.cash = cash
        self.ebit = ebit
        self.sales = sales

    def get_price_to_earning_ratio(self):
        return self.market_cap/self.net_income

    def get_price_to_earning_ratio_alternative_2(self):
        return self.share_price/self.earnings_per_share

    def get_ev_to_ebit_ratio(self):
        return (self.market_value_of_equity + self.debt - self.cash) / self.ebit

    def get_ev_to_sales(self):
        return (self.market_value_of_equity + self.debt - self.cash)/self.sales


