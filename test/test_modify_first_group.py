from model.group import Group

def test_add_group(app):
        app.session.login(username="admin", password="secret")
        app.group.modify_first_group()
        app.group.fill_form(Group(name="test2", header="test3", footer="test3"))
        app.group.submit_group_update()
        app.group.return_to_groups_page()
        app.session.logout()