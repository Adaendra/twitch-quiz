from apps.services.utils.JsonUtils import readJson


class TestJsonUtils:

    def test_read_json(self):
        assert readJson("tests/resources/jsonTest.json") == { "value": "test" }
