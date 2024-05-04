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

    def pays(self, bill, flatmate2, flatmate3):
        percentage_share = self.stay_duration / (self.stay_duration + flatmate2.stay_duration + flatmate3.stay_duration)
        amount_to_be_paid = round((bill.amount * percentage_share), 2)
        self.amount_to_be_paid = amount_to_be_paid
