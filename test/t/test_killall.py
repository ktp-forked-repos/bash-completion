import pytest


class TestKillall:

    # "p": Assume our process name completion runs ps and at least it is shown
    @pytest.mark.complete("killall p")
    def test_1(self, completion):
        assert completion

    @pytest.mark.complete("killall --signal ")
    def test_2(self, completion):
        assert all(x in completion for x in "INT KILL TERM".split())
