from model.contact import Contact


def test_modify_first(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.init_contact_creation()
        app.contact.fill_inputs(Contact(firstname="Test"))
        app.contact.click_submit_button()
    app.contact.modify_first_contact(Contact(firstname="1234", lastname="2345"))
    app.return_to_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

