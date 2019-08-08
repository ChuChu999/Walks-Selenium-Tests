from enum import Enum
import woi_actions
import time
import unittest


class TestName(Enum):
    REGULAR_BOOKING = "test_regular_booking"
    PROMO_CODE = "test_promo_code"
    LOAD_ALL_TOURS = "test_load_all_tours"


class Environment(Enum):
    STAGING = "woi_staging"
    PRODUCTION = "woi_production"


class WOITests(unittest.TestCase):

    test_name = None
    environment = None

    def setUp(self):
        self.general = woi_actions.General()

        self.general.set_up_selenium()

        self.promo_code = woi_actions.PromoCode(self.general)
        self.cache = woi_actions.Cache(self.general)

    def tearDown(self):
        self.general.tear_down_selenium()

    def test_regular_booking(self):
        self.general.initialize_test(WOITests.test_name, WOITests.environment)
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
        self.general.initialize_test(WOITests.test_name, WOITests.environment)
        self.general.load_site()
        self.general.select_market()
        self.general.select_tour()
        self.general.increment_month()
        self.general.select_date()
        self.general.select_time()
        self.general.select_adults()
        self.general.book_tour()
        self.promo_code.fill_promo_code()  # fill promo code
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

    def test_load_all_tours(self):
        self.general.initialize_test(WOITests.test_name, WOITests.environment)
        self.general.load_site()
        self.cache.load_all_tours()
        time.sleep(3)


def run_test(test_name: TestName, environment: Environment):
    suite = unittest.TestSuite()
    runner = unittest.TextTestRunner()
    WOITests.test_name = test_name.value
    WOITests.environment = environment.value

    suite.addTest(WOITests(test_name.value))
    runner.run(suite)


if __name__ == "__main__":
    WOITests.environment = Environment.STAGING

    unittest.main()
