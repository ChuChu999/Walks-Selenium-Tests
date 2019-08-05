import woi_actions
import time
import unittest


class WOITests(unittest.TestCase):

    def setUp(self):
        self.general = woi_actions.General()
        self.env = woi_actions.Environment

        self.general.set_up_selenium()

    def tearDown(self):
        self.general.tear_down_selenium()

    def test_booking(self):
        self.general.initialize_test("TestBooking", self.env.STAGING.value)
        self.general.load_site()
        self.general.select_market()
        self.general.select_tour()
        self.general.increment_month()
        self.general.select_date()
        self.general.select_time()
        self.general.select_adults()
        self.general.book_tour()
        self.general.fill_first_name()
        self.general.fill_last_name()
        self.general.fill_email()
        self.general.fill_phone()
        self.general.fill_credit_card()
        self.general.select_expiry_month()
        self.general.select_expiry_year()
        self.general.fill_cvv()
        self.general.fill_address()
        self.general.select_country()
        self.general.fill_zip_code()
        self.general.select_state()
        self.general.fill_city()
        self.general.tick_terms_and_conditions()
        self.general.submit_payment_form()
        time.sleep(3)

    def test_promo_code(self):
        self.promo = woi_actions.PromoCode(self.general)

        self.general.initialize_test("TestPromoCode", self.env.STAGING.value)
        self.general.load_site()
        self.general.select_market()
        self.general.select_tour()
        self.general.increment_month()
        self.general.select_date()
        self.general.select_time()
        self.general.select_adults()
        self.general.book_tour()
        self.promo.fill_promo_code()  # fill promo code
        self.general.fill_first_name()
        self.general.fill_last_name()
        self.general.fill_email()
        self.general.fill_phone()
        self.general.fill_credit_card()
        self.general.select_expiry_month()
        self.general.select_expiry_year()
        self.general.fill_cvv()
        self.general.fill_address()
        self.general.select_country()
        self.general.fill_zip_code()
        self.general.select_state()
        self.general.fill_city()
        self.general.tick_terms_and_conditions()
        self.general.submit_payment_form()
        time.sleep(3)


def run_test(test_name: str):
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()

    suite.addTest(WOITests(test_name))
    runner.run(suite)


def run_tests():
    unittest.main()


if __name__ == "__main__":
    # run_test("test_promo_code")
    run_tests()
