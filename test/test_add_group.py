# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.init_creation()
        app.group.fill_form(Group(name="test", header="test1", footer="test2"))
        app.group.submit_creation()
        app.group.return_to_groups_page()
        app.session.logout()


def test_add_empty_group(app):
        app.session.login(username="admin", password="secret")
        app.group.init_creation()
        app.group.fill_form(Group(name="", header="", footer=""))
        app.group.submit_creation()
        app.group.return_to_groups_page()
        app.session.logout()
