from homework7.hw.task01 import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


def test_example_tree_value_red():
    assert find_occurrences(example_tree, 'RED') == 6


def test_example_tree_value_lot():
    assert find_occurrences(example_tree, 'value1') == 1


def test_example_tree_value_blue():
    assert find_occurrences(example_tree, 'BLUE') == 2


def test_example_tree_key_third():
    assert find_occurrences(example_tree, 'third') == 1


def test_example_tree_key_key3():
    assert find_occurrences(example_tree, 'key3') == 1
