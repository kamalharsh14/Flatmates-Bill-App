import configparser
import os
import webbrowser

from fpdf import FPDF

from classes.upload_pdf import upload_to_github


class PDFReport:
    """
    Creates a PDFReport object to generate reports
    Filename: Name of the file
    Generate(): Will generate the report
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmates, bill, upload_to_cloud):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Insert Title of the Bill
        self.insert_title(file=pdf)

        # Insert Billing Cycle/Period
        self.insert_value(file=pdf, key="Billing Cycle", value=bill.period)

        # Insert Contributors and Share
        for person in flatmates:
            self.insert_value(file=pdf, key=person.name, value=str(person.amount_to_be_paid))

        # Insert Total Bill
        self.insert_total_bill(file=pdf, bill=bill)

        upload = False

        if upload_to_cloud == 'Y':
            upload = True
        # Generate Output
        self.output(file=pdf, upload_to_cloud=upload)

    @staticmethod
    def insert_title(file):
        file.set_font(family='Times', size=24, style='B')
        file.cell(w=0, h=50, txt="Flatmates Bill", border=1, align="C", ln=2)

    @staticmethod
    def insert_value(file, key, value):
        file.set_font(family='Times', size=12, style='B')
        file.cell(w=269, h=20, txt=key, border=0, align="C")
        file.set_font(family='Times', size=14)
        file.cell(w=269, h=20, txt=value, border=0, align="C", ln=1)

    @staticmethod
    def insert_total_bill(file, bill):
        file.set_font(family='Times', size=14, style='B')
        file.cell(w=269, h=25, txt="Total", border=1, align="C")
        file.set_font(family='Times', size=14)
        file.cell(w=269, h=25, txt=str(bill.amount), border=1, align="C", ln=1)

    def output(self, file, upload_to_cloud):
        file.output(self.filename)
        webbrowser.open(self.filename)
        if upload_to_cloud:
            github_token = 'your_github_personal_access_token'
            repository_owner = 'your_username_or_organization'
            repository_name = 'your_repository_name'
            file_path = 'path/to/your/file.txt'
            upload_to_github(github_token, repository_owner, repository_name, file_path)
