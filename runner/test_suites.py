import datetime
import unittest
import HtmlTestRunner
from tests.login_tests import TestLogin
from tests.inventory_tests import TestInventory


class TestSuite(unittest.TestCase):

    DATE_TODAY = str(datetime.datetime.now().strftime("%d-%b-%Y"))

    def test_suite(self):
        test_suite = unittest.TestSuite()
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))
        test_suite.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestInventory))

        myrunner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title=f'Saucedemo Tests Report {self.DATE_TODAY}',
            report_name='Saucedemo_Tests_Report'
        )
        myrunner.run(test_suite)
