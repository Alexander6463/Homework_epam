import json

import pytest

from homework11.hw.task01 import MakeReport


@pytest.fixture()
def data_input():
    with open("homework11/test/data_file.json", "r", encoding='utf-8') \
            as read_file:
        data = json.load(read_file)
        return data


def test_pe_max_report(data_input):
    assert json.loads(MakeReport(data_input, 71.85).get_p_e_report())[0] \
           == {'code': 'VNO',
               'name': 'Vornado Realty Trust',
               'P/E': -893.45}


def test_cost_max_report(data_input):
    assert json.loads(MakeReport(data_input, 71.85).get_cost_report())[0] \
           == {'code': 'AMZN',
               'name': 'Amazon',
               'price': 238932.86}


def test_growth_max_report(data_input):
    assert json.loads(MakeReport(data_input, 71.85).get_growth_report())[0]\
           == {'code': 'LB',
               'name': 'L Brands Inc',
               'growth': 347.65}


def test_potential_profit_max_report(data_input):
    assert json.loads(MakeReport(data_input, 71.85).
                      get_potential_profit_report())[0] \
           == {'code': 'GOOG',
               'name': 'Alphabet C (ex Google)',
               'potential profit': 84235.5}
