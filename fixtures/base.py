import unittest
import os

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from menus.user_menu import UserMenu
from pages.login import LoginPage
from tests import CHROME_DRIVER, TEST_DIR


class BaseFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.wait = WebDriverWait(self.browser, 3)
        self.login_page = LoginPage(self.browser)
        self.login_page.go_to_page()
        self.user_menu = UserMenu(self.browser)

    def tearDown(self) -> None:

        if self._outcome.errors[1][1] is not None:

            test_name = self._testMethodName
            result_dir = os.path.join(TEST_DIR,'test_results')
            if not os.path.exists(result_dir):
                os.mkdir(result_dir)

            test_dir = os.path.join(result_dir,test_name)
            if not os.path.exists(test_dir):
                os.mkdir(test_dir)
            self.browser.save_screenshot(os.path.join(test_dir, f"{test_name}.png"))

            # file = open('page_source.html', 'w')
            # file.write(self.browser.page_source)
            # file.close()

            with open(os.path.join(test_dir, f"{test_name}.html"), 'w') as file:
                file.write(self.browser.page_source)

        self.browser.quit()  # some more changes