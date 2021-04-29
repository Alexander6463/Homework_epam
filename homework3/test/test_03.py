from homework3.hw.task03 import Filter, make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
]


def test_filter_function_even_numbers():
    positive_even = Filter(
        lambda a: a % 2 == 0, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_even.apply(range(100)) == list(
        filter(lambda a: (a % 2 == 0 and a > 0
                          and isinstance(a, int)), range(100))
    )


def test_filter_function_not_even_numbers():
    positive_non_even = Filter(
        lambda a: a % 2 == 1, lambda a: a > 0, lambda a: isinstance(a, int)
    )
    assert positive_non_even.apply(range(100)) == list(
        filter(lambda a: (a % 2 == 1 and a > 0
                          and isinstance(a, int)), range(100))
    )


def test_make_filter_func_name_type():
    assert make_filter(name="polly", type="bird").apply(sample_data) == [
        {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"}
    ]


def test_make_filter_func_last_name():
    assert make_filter(last_name="Gilbert").apply(sample_data) == [
        {
            "name": "Bill",
            "last_name": "Gilbert",
            "occupation": "was here",
            "type": "person",
        }
    ]
