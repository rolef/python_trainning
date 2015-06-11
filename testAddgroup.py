# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class testAddgroup(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost:8000/addressbook/")

    def login(self, wd, username="admin", password="secret"):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("user").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def open_groups_page(self, wd):
        # open group page
        wd.find_element_by_link_text("groups").click()

    def create_group(self, wd):
        # init group creation
        wd.find_element_by_name("new").click()
        #fill grop fields
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("TestGroup1")
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("Myfirst Test group")
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("My first test group footer")
        # Submit group creation
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self, wd):
        # return to group page
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("groups").click()

    def logout(self, success, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").send_keys("\\undefined")
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").send_keys("\\undefined")
        self.assertTrue(success)

    def test_testAddgroup(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_groups_page(wd)
        self.create_group(wd)
        self.return_to_groups_page(wd)
        self.logout(success, wd)
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
