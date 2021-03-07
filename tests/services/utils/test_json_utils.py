from apps.services.utils.JsonUtils import readJson


class TestJsonUtils:

    # ----- readJson ----- #
    def test_readJson_ok(self):
        assert readJson("tests/resources/jsonTest.json") == {"value": "test"}
