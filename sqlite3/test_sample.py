from sample import main


def test_main():
    try:
        main()
        assert True
    except RuntimeError:
        assert False
