import os
import unittest
from io import StringIO
import sys

from src.main import setup_flatmates, setup_bill, generate_bill


class TestBillGeneration(unittest.TestCase):

    def test_bill_generation(self):
        # Mock user input
        sys.stdin = StringIO("2\nAlice\n5\nBob\n7\n100\nElectricity\nJanuary\nY")

        # Run the code
        flatmates = setup_flatmates()
        bill = setup_bill()
        generate_bill(flatmates=flatmates, bill=bill)

        # Reset stdin
        sys.stdin = sys.__stdin__

        # Check if the file is generated
        filename = 'Test_Bill.pdf'


if __name__ == '__main__':
    unittest.main()
