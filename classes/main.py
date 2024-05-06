from Bill import Bill
from Flatmate import Flatmate
from PDFReport import PDFReport

"""
This is the main function.
Start running this file and you'll find a bill generated in your root directory.
"""


def setup_flatmates():
    flatmates = []
    n = int(input("Enter total number of Flatmates: "))
    for i in range(0, n):
        if i == 0:
            name = str(input(f'Enter your name: '))
            duration = int(input(f'Enter Number of days you stayed: '))
            flatmates.append(Flatmate(name=name, stay_duration=duration))
        else:
            name = str(input(f'Enter name of the {i + 1}th person: '))
            duration = int(input(f'Enter Number of days {name} stayed: '))
            flatmates.append(Flatmate(name=name, stay_duration=duration))

    return flatmates


def setup_bill():
    amount = int(input("Enter Bill amount: "))
    category = str(input("Enter Bill category: "))
    period = str(input("Enter Billing cycle(without spaces): "))
    return Bill(amount=amount, category=category, period=period)


def generate_bill(flatmates, bill):
    for person in flatmates:
        person.pays(bill=bill, flatmates=flatmates)

    filename = f'{bill.period}_{bill.category}_Bill.pdf'
    pdf_report = PDFReport(filename=filename)
    upload_to_cloud = str(input("Do you want to upload the bill to Cloud?(Y/N)"))
    pdf_report.generate(flatmates, bill=bill, upload_to_cloud=upload_to_cloud)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flatmates = setup_flatmates()
    bill = setup_bill()
    generate_bill(flatmates=flatmates, bill=bill)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
