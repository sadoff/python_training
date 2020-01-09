from model.contact import Contact


def test_modify_first(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", lastname="Test1")
    if app.contact.count() == 0:
        app.contact.add_contact(Contact(firstname="Test"))
    app.contact.modify_first_contact(Contact(firstname="1234", lastname="2345"))
    app.return_to_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

