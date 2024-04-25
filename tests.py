import unittest
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


class EpakaSearchFunctionalityTest(unittest.TestCase):

    def setUp(self):

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        # chrome_options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.epaka.pl")
        print('setup/driver get')
        self.accept_cookies()

    def driverQuit(self):
        self.driver.quit()

    def accept_cookies(self):

        try:
            cookies_button = WebDriverWait(self.driver, 0.1).until(EC.element_to_be_clickable((By.ID, "accept")))
            cookies_button.click()

        except:
            pass

    def test_search_by_city_name(self):

        punkty_nadan_link = self.driver.find_element(By.LINK_TEXT, "Punkty nadań")
        punkty_nadan_link.click()

        searchbar = self.driver.find_element(By.ID, "pointSearch")
        searchbar.send_keys("Siedlce")
        print('znaleziono siedlce w searchbarze')

        dropdown_menu = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, "tt-menu")))
        dropdown_option = dropdown_menu.find_element(By.CLASS_NAME, "tt-suggestion")
        dropdown_option.click()
        print('dropdown siedlce click')

        print('znaleziono diva z siedlcami')
        card_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.font-weight-800.text-black.font-size-22px")))
        html_content = card_element.get_attribute('outerHTML')

        if "Siedlce" in html_content:
            print("'Siedlce' znajdują się w html_content")

        self.assertTrue("Siedlce" in html_content)

        # time.sleep(4)

    def test_search_by_post_code(self):

        punkty_nadan_link = WebDriverWait(self.driver, 1).until(EC.visibility_of_element_located((By.LINK_TEXT, "Punkty nadań")))
        punkty_nadan_link.click()

        searchbar = self.driver.find_element(By.ID, "pointSearch")
        searchbar.send_keys("08-110")
        searchbar.send_keys(Keys.RETURN)

        time.sleep(2)

        searchbar2 = WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located((By.ID, "pointSearch")))
        searchbar2.click()
        searchbar2.send_keys(Keys.RETURN)

        print('znaleziono diva z siedlcami')

        card_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.font-weight-800.text-black.font-size-22px")))
        html_content = card_element.get_attribute('outerHTML')

        if "Siedlce" in html_content:
            print("'Siedlce' znajdują się w html_content")

        self.assertTrue("Siedlce" in html_content)

    def test_search_by_abbreviated_city_name(self):

        punkty_nadan_link = self.driver.find_element(By.LINK_TEXT, "Punkty nadań")
        punkty_nadan_link.click()

        searchbar = self.driver.find_element(By.ID, "pointSearch")
        searchbar.send_keys("sie")
        print('znaleziono wyniki w searchbarze')


        dropdown_elements = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "tt-menu")))

        for element in dropdown_elements:
            print('szuka elementu')
            dropdown_options = WebDriverWait(self.driver, 5).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "tt-selectable")))
            print('znalazlo element')

            for option in dropdown_options:


                option = element.find_element(By.CLASS_NAME, "tt-selectable")
                option_text = option.text
                if "dlce" in option_text:
                    print('Siedlce found')
                    option.click()
                    print('kliknieto')

                card_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.font-weight-800.text-black.font-size-22px")))
                html_content = card_element.get_attribute('outerHTML')
                if "Siedlce" in html_content:
                    print("'Siedlce' znajdują się w html_content")

                self.assertTrue("Siedlce" in html_content)


     # def test_search_by_abbreviated_city_name(self):
     #     pass





