from flask import render_template
from flask.views import MethodView

from BillForm import BillForm


class BillFormPage(MethodView):

    def get(self):
        bill_form = BillForm()
        return render_template('bill.html', billForm=bill_form)