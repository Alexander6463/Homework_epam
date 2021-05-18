"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
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


def find_occurrences(tree: dict, element: Any) -> int:
    def unpacking(dct):
        visited = []
        for key, value in dct.items():
            visited.append(key)
            if isinstance(value, dict):
                visited.extend(unpacking(value))
            elif isinstance(value, (list, tuple, set)):
                for el in value:
                    if not isinstance(el, dict):
                        visited.append(el)
                    else:
                        visited.extend(unpacking(el))
            else:
                visited.append(value)
        return visited

    return unpacking(tree).count(element)


if __name__ == '__main__':
    print(find_occurrences(example_tree, 'RED'))
