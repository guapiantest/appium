from hogwarts12_27.po.app import App


def test_addmember():
    app = App()
    app.start()
    app.goto_main().goto_addresslist().click_addmember().add_member_manual().add_contact()
