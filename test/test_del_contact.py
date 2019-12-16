from model.contact import Contact


def test_delete_first(app):
    if app.contact.count() == 0:
        app.contact.fill_inputs(Contact(firstname="Test", middlename="Testovich", lastname="Testov", nickname="test1",
                                        adress="Testovia, Test City, Test street",
                                        mobilephone="+79999999999", email="test@test.ts"))
        app.contact.click_submit_button()
    app.contact.delete_first()
