# -*- coding: utf-8 -*-
from model.contact import Contact
import string
import random
import pytest

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " * 10 + string.punctuation
    return prefix + " ".join([random.choice(symbols) for i in range (random.randrange(maxlen))])


testdata = [Contact(firstname="", lastname="", address="", middlename="", homephone="", mobilephone="", workphone="", email="", email2="", email3="")] +[
            Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20),
            homephone=random_string("home", 10), mobilephone=random_string("mobile", 10), workphone=random_string("work", 10),
            email=random_string("email", 20), email2=random_string("email2", 20), email3=random_string("email3", 20))
            for i in range(3)]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.add_contact(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)








