"""
Measures a firm's ability to meet its interest payments
Increase => the firm is earning much more than necessary to meet its obligations

HighQualityBorrowers > 5 * EBIT_INTEREST_COVERAGE

LowQualityBorrowers < 1.5 * EBIT_INTEREST_COVERAGE

"""


class InterestCoverageRatios:
    def __init__(self, ebit, interest_expense, ebitda):
        self.ebit = ebit
        self.interest_expense = interest_expense
        self.ebitda = ebitda

    def get_ebit_interest_coverage(self):
        return self.ebit/self.interest_expense

    def get_ebitda_interest_coverage(self):
        return self.ebitda/self.interest_expense


if __name__ == '__main__':
    ebit = 10000
    interest_expense = 7832
    ebitda = 2748

    interestCoverageRatios = InterestCoverageRatios(ebit, interest_expense, ebitda)

    print(interestCoverageRatios.get_ebit_interest_coverage())
