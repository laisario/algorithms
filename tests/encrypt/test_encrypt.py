from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    'Test function encrypt_message'
    assert encrypt_message('test', 2) == 'ts_et'
    assert encrypt_message('test', 3) == 'set_t'
    assert encrypt_message('test', 6) == 'tset'
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(4, 2)
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('aaa', 'bbb')
