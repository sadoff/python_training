# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from group import Group


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("content").click()
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def init_group_creation(self):
        wd = self.wd
        self.init_group_creation()
        wd.find_element_by_name("new").click()

    def fill_group_form(self, group):
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def submit_group_creation(self):
        wd = self.wd
        self.submit_group_creation()
        wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
        wd = self.wd
        self.return_to_groups_page()
        wd.find_element_by_link_text("group page").click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        wd = self.wd
        self.login(username="admin", password="secret")
        self.fill_group_form(Group(name="test", header="test1", footer="test2"))
        self.return_to_groups_page()
        self.logout()

    def test_add_empty_group(self):
        wd = self.wd
        self.login( username="admin", password="secret")
        self.fill_group_form(Group(name="", header="", footer=""))
        self.logout()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
