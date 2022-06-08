from sample import main


def test_main():
    try:
        main(':memory:')
        assert True
    except RuntimeError:
        assert False
