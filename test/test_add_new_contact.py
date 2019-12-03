# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.terminate)
    return fixture


def test_add_new_contact(app):

    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Test", middlename="Testovich", lastname="Testov", nickname="test1",
                            adress="Testovia, Test City, Test street",
                            mobilephone="+79999999999", email="test@test.ts"))
    app.return_to_home_page()
    app.session.logout()





