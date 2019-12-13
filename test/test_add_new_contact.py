# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_new_contact(app):

    app.contact.fill_inputs(Contact(firstname="Test", middlename="Testovich", lastname="Testov", nickname="test1",
                            adress="Testovia, Test City, Test street",
                            mobilephone="+79999999999", email="test@test.ts"))
    app.contact.click_submit_button()
    app.return_to_home_page()






