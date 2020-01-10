from model.contact import Contact


def test_modify_first(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test", middlename="Testovich", lastname="Testov", nickname="test1",
                            adress="Testovia, Test City, Test street",
                            mobilephone="+79999999999", email="test@test.ts")
    if app.contact.count() == 0:
        app.contact.add_contact(contact)
    app.contact.modify_first_contact(Contact(firstname="Katya1"))
    app.return_to_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

