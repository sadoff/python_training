# -*- coding: utf-8 -*-


import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.terminate)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.fill_group_form(Group(name="test", header="test1", footer="test2"))
        app.return_to_groups_page()
        app.logout()


def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.fill_group_form(Group(name="", header="", footer=""))
        app.return_to_groups_page()
        app.logout()
