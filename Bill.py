class Bill:
    """
    Object that contains data about the BILL
    Amount: Total Bill Amount
    Period: Billing Period(for calculating payable amount)
    """

    def __init__(self, amount, category, period):
        self.amount = amount;
        self.category = category
        self.period = period;