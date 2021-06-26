import varius


def test_storage():

    assert varius.VARIABLE_STORAGE == {}

    varius.VARIABLE_STORAGE["v0"] = {"a": 0.1, "b": 0.1}

    assert varius.VARIABLE_STORAGE["v0"] == {"a": 0.1, "b": 0.1}


def test_version():

    assert varius._CURRENT_VERSION is None

    varius._CURRENT_VERSION = "v0"

    assert varius._CURRENT_VERSION == "v0"


def test_global_scope():

    assert varius._CURRENT_VERSION == "v0"
    assert varius.VARIABLE_STORAGE["v0"] == {"a": 0.1, "b": 0.1}
