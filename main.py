from flask import Flask

from HomePage import HomePage
from BillFormPage import BillFormPage
from ResultsPage import ResultsPage
from BillForm import BillForm

app = Flask(__name__)

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/home', view_func=HomePage.as_view('home'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('result_page'))

app.run()
