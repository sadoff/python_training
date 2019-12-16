from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.init_creation()
        app.group.fill_form(Group(name="test"))
        app.group.submit_creation()
        app.group.return_to_groups_page()
    app.group.delete_first()
