from flask import render_template, request
from flask.views import MethodView
from classes.Bill import Bill
from classes.Flatmate import Flatmate
from classes.PDFReport import PDFReport

from BillForm import BillForm


class ResultsPage(MethodView):

    def post(self):
        bill_form = BillForm(request.form)

        amount = bill_form.amount.data
        category = bill_form.category.data
        period = bill_form.period.data
        bill = Bill(amount=amount, category=category, period=period)

        name_1 = bill_form.name_1.data
        stay_1 = bill_form.stay_duration_1.data
        flatmate_1 = Flatmate(name=name_1, stay_duration=stay_1)

        name_2 = bill_form.name_2.data
        stay_2 = bill_form.stay_duration_2.data
        flatmate_2 = Flatmate(name=name_2, stay_duration=stay_2)

        flatmates = [flatmate_1, flatmate_2]
        flatmate_1.pays(bill=bill, flatmates=flatmates)
        flatmate_2.pays(bill=bill, flatmates=flatmates)

        return render_template('results.html', bill=bill, flatmate1=flatmate_1, flatmate2=flatmate_2)
        # return (f"{flatmate_1.name} pays {flatmate_1.amount_to_be_paid} \n {flatmate_2.name} pays "
        #                        f"{flatmate_2.amount_to_be_paid}")
