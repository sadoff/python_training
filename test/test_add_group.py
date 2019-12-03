# -*- coding: utf-8 -*-


import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.terminate)
    return fixture


def test_add_group(app):
        app.login(username="admin", password="secret")
        app.init_group_creation()
        app.fill_group_form(Group(name="test", header="test1", footer="test2"))
        app.submit_group_creation()
        app.return_to_groups_page()
        app.logout()


def test_add_empty_group(app):
        app.login(username="admin", password="secret")
        app.init_group_creation()
        app.fill_group_form(Group(name="", header="", footer=""))
        app.submit_group_creation()
        app.return_to_groups_page()
        app.logout()
