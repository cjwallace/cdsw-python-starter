from module.code import add

class TestAdd:
    def test_adding_zero_is_noop(self):
        assert add(1, 0) == 1