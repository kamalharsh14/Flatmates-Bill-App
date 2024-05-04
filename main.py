from Bill import Bill
from Flatmate import Flatmate
from PDFReport import PDFReport

"""
This is the main function.
Start running this file and you'll find a bill generated in your root directory.
"""


def generate_bill():
    bill = Bill(amount=1500, period="April 2024")
    Harsh = Flatmate(name="Harsh", stay_duration=20)
    Rounik = Flatmate(name="Rounik", stay_duration=30)
    Anupam = Flatmate(name="Anupam", stay_duration=7)

    Harsh.pays(bill=bill, flatmate2=Rounik, flatmate3=Anupam)
    Rounik.pays(bill=bill, flatmate2=Harsh, flatmate3=Anupam)
    Anupam.pays(bill=bill, flatmate2=Rounik, flatmate3=Harsh)

    filename = f'{bill.period}_Bill.pdf'
    pdf_report = PDFReport(filename=filename)
    flatmates = [Harsh, Anupam, Rounik]
    pdf_report.generate(flatmates, bill=bill)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_bill()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
