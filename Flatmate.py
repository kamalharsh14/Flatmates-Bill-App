class Flatmate:
    """
    Creates a Flatmate object to store data about the person
    Name: Name of the person.
    Stay Duration: Time period this person stayed in the flat(will be used for calculating share in the bill).
    Amount To be Paid: Stores the bill share amount,
    Pays(): Will return the calculated amount for that person.
    """

    def __init__(self, name, stay_duration):
        self.name = name
        self.stay_duration = stay_duration
        self.amount_to_be_paid = 0

    def pays(self, bill, flatmates):
        total_weight = 0
        for person in flatmates:
            total_weight += person.stay_duration
        percentage_share = self.stay_duration / total_weight
        amount_to_be_paid = round((bill.amount * percentage_share), 2)
        self.amount_to_be_paid = amount_to_be_paid
