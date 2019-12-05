from model.contact import Contact


def test_add_new_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact()
    app.contact.modify_fill_input(Contact(firstname="Test23", middlename="Testovich23", lastname="Testov23", nickname="test123",
                               adress="Testovia, Test City, Test street",
                               mobilephone="+79999999999", email="test@test.ts"))

    app.return_to_home_page()
    app.session.logout()
