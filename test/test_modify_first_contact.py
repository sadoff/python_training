from model.contact import Contact


def test_add_new_contact(app):

    app.contact.edit_first()
    app.contact.fill_inputs(Contact(firstname="Test23", middlename="Testovich23", lastname="Testov23", nickname="test123",
                               adress="Testovia, Test City, Test street",
                               mobilephone="+79999999999", email="test@test.ts"))
    app.contact.update_button_click()
    app.return_to_home_page()

