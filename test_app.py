import app


def test_greetDuane():
    response = app.greet('Duane')
    assert response == 'Hello Duane!'


def test_greetBob():
    response = app.greet('Bob')
    assert response == 'Hello Bob!'

