from number_guessing_game import (play_again, user_input)


def test_user_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 5)

    user_entry = user_input()
    assert user_entry == 5


def test_play_again(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda x: 'y')

    user_entry = play_again()
    assert user_entry == 'y'

    monkeypatch.setattr('builtins.input', lambda x: 'n')

    user_entry = play_again()
    assert user_entry == 'n'
