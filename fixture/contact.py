from model.contact import Contact


class ContactHelper:

    contact_cache = None

    def __init__(self, app):
        self.app = app

    def add_contact(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_inputs(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def fill_inputs(self, contact):
        wd = self.app.wd
        self.change_contact_field_value("firstname", contact.firstname)
        self.change_contact_field_value("lastname", contact.lastname)

    def change_contact_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def delete_first(self):
        wd = self.app.wd
        self.home_page()
        self.select_first_contact()
        wd.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/addressbook"):
            wd.get("http://localhost/addressbook")


    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.home_page()
        self.select_first_contact()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_inputs(new_contact_data)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_to_home_page()

    def click_submit_button(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                text = element.find_elements_by_css_selector("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = text
                firstname = text
                lastname = element.find_elements_by_tag_name("td")[1].text
                firstname = element.find_elements_by_tag_name("td")[2].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname))
            return list(self.contact_cache)