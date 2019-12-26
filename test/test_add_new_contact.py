# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", middlename="Testovich", lastname="Testov", nickname="test1",
                            adress="Testovia, Test City, Test street",
                            mobilephone="+79999999999", email="test@test.ts")
    app.contact.init_contact_creation()
    app.contact.fill_inputs(contact)
    app.contact.click_submit_button()
    app.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)







