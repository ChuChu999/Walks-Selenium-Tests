from datetime import datetime
from enum import Enum
import os
import random
import re
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time


class Site(Enum):
    STAGING = "https://cf-staging.walksofitaly.com"
    PRODUCTION = "https://www.walksofitaly.com"


class General:

    def set_up_selenium(self):
        self.browser = webdriver.Chrome()
        self.wait = WebDriverWait(self.browser, 30)

    def tear_down_selenium(self):
        self.browser.quit()

    def initialize_test(self, test_name: str, url: str):
        self.test_name = test_name
        self.url = url
        self.screenshot_dir = "Screenshots/" + self.test_name

        os.makedirs(self.screenshot_dir, exist_ok=True)

    def initialize_action_chains(self):
        self.actions = ActionChains(self.browser)

    def save_screenshot(self, file_name: str):
        self.browser.save_screenshot(
            self.screenshot_dir + "/" + str(datetime.now()) + " - " + file_name)

    def focus(self, element: webdriver.remote.webelement.WebElement):
        self.browser.execute_script("arguments[0].focus();", element)

    def load_site(self):
        self.browser.get(self.url)
        # assert "Walks of Italy" in self.browser.title

    def select_market(self):
        view_tours = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "main-menu")))
        market = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'a[href="/rome-tours/"]')))

        self.initialize_action_chains()
        self.save_screenshot("Pre-Market.png")
        self.actions.move_to_element(view_tours).click(market).perform()
        self.save_screenshot("Post-Market.png")

    def select_tour(self):
        tour_overview = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "tour-list-container")))
        tours = tour_overview.find_elements_by_css_selector(
            "div.large a.image-link")
        tour = random.choice(tuple(tours))

        # print("\n" + tour.get_attribute("href"))
        self.save_screenshot("Pre-Tour.png")
        self.focus(tour)
        time.sleep(0.5)
        self.initialize_action_chains()
        self.actions.move_to_element(tour).perform()
        tour.send_keys(Keys.ENTER)
        self.save_screenshot("Post-Tour.png")

    def increment_month(self):
        for i in range(2):
            next_month = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.right-book-desktop a.datepick-cmd-next")))

            self.focus(next_month)
            time.sleep(0.1)
            next_month.click()
            time.sleep(0.25)

    def select_date(self):
        calendar = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.right-book-desktop div.datepick-month")))
        weeks = calendar.find_elements_by_tag_name("tr")
        availableDays = []

        for week in weeks:
            availableDays.extend(week.find_elements_by_tag_name("a"))

            if len(availableDays) > 0:
                break

        if not availableDays:
            raise Exception("no available days two months in advance")

        self.wait.until(EC.visibility_of(availableDays[0]))
        time.sleep(0.1)
        self.save_screenshot("Pre-Date.png")
        availableDays[0].send_keys(Keys.ENTER)

    def select_time(self):
        time_select = Select(self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.right-book-desktop select[name="time"]'))))

        time_select.select_by_index(1)

    def select_adults(self):
        adults = Select(self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.right-book-desktop select[name="adults"]'))))

        adults.select_by_index(1)

    def book_tour(self):
        book = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.right-book-desktop button.btn-book-now")))

        self.save_screenshot("Pre-Book.png")
        book.send_keys(Keys.ENTER)
        self.save_screenshot("Post-Book.png")

    def fill_first_name(self):
        first_name = self.wait.until(
            EC.visibility_of_element_located((By.ID, "first-name")))

        first_name.send_keys("Test")

    def fill_last_name(self):
        last_name = self.browser.find_element_by_name("last_name")

        last_name.send_keys("Booking")

    def fill_email(self):
        email = self.browser.find_element_by_name("email")

        email.send_keys("nicholas+staging@takewalks.com")

    def fill_phone(self):
        phone = self.browser.find_element_by_id("thePhone")

        phone.send_keys("1234567")
        self.save_screenshot("Post-Phone.png")

    def fill_credit_card(self):
        cc = self.browser.find_element_by_id("ccno")

        cc.send_keys("5555555555554444")

    def select_expiry_month(self):
        cc_month = Select(self.browser.find_element_by_name("ccMonth"))

        cc_month.select_by_value("12")

    def select_expiry_year(self):
        cc_year = Select(self.browser.find_element_by_name("ccYear"))

        cc_year.select_by_value("2022")

    def fill_cvv(self):
        cvv = self.browser.find_element_by_id("theCcv")

        cvv.send_keys("123")
        self.save_screenshot("Post-CVV.png")

    def fill_address(self):
        address = self.browser.find_element_by_name("street_address")

        address.send_keys("5323 Levander Loop")

    def select_country(self):
        country = Select(self.browser.find_element_by_name("country"))

        country.select_by_value("United States of America")

    def fill_zip_code(self):
        zip = self.browser.find_element_by_name("zip")

        zip.send_keys("78702")

    def select_state(self):
        state = Select(self.browser.find_element_by_id("state_select"))

        state.select_by_value("TX")

    def fill_city(self):
        city = self.browser.find_element_by_name("city")

        city.send_keys("Austin")

    def tick_terms_and_conditions(self):
        terms = self.browser.find_element_by_css_selector(
            'label[for="ccb_01"]')

        terms.click()

    def submit_payment_form(self):
        pay = self.browser.find_element_by_class_name("complete_booking")

        self.save_screenshot("Pre-Pay.png")
        pay.click()
        self.save_screenshot("Post-Pay.png")

        booking_confirmation = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.page-header h4")))
        booking_id = "".join(re.findall(r"\d", booking_confirmation.text))

        self.save_screenshot("BookingConfirmation - " + booking_id + ".png")


class PromoCode:

    def __init__(self, general: General):
        self.browser = general.browser
        self.wait = general.wait
        self.save_screenshot = general.save_screenshot

    def fill_promo_code(self):
        promo_code_box = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.promo-code-field button")))

        self.save_screenshot("Pre-PromoBox.png")
        promo_code_box.send_keys(Keys.ENTER)
        self.save_screenshot("Post-PromoBox.png")

        promo_code = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "promo")))

        promo_code.send_keys("rc10")
        self.save_screenshot("Post-PromoCode.png")

        apply_promo = self.browser.find_element_by_css_selector(
            "div.promo-code-field button")
        # self.save_screenshot("Post-ApplyPromo.png")
        apply_promo.send_keys(Keys.ENTER)
