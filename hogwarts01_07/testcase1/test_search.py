from hogwarts01_07.app import App


def test_search():
    app = App()
    app.start()
    app.goto_main().goto_market().goto_search().search()