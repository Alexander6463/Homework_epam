import json
import os
from unittest.mock import AsyncMock

import pytest

from homework11.hw.task01 import CompanyRepository, MakeReport


@pytest.fixture()
async def input_data():
    with open("homework11/test/data_file.json", "r", encoding='utf-8') \
            as read_file:
        data = json.load(read_file)
    company = CompanyRepository()
    company.get_info_companies = AsyncMock(return_value=data)
    return await company.get_info_companies()


@pytest.fixture()
async def get_cost_of_dollar():
    company = CompanyRepository()
    company.get_value_dollar = AsyncMock(return_value=71.85)
    return await company.get_value_dollar()


@pytest.mark.asyncio()
async def test_pe_max_report(input_data, get_cost_of_dollar):
    MakeReport(await input_data, await get_cost_of_dollar).get_p_e_report()
    with open('p_e_report.json', 'r') as input_json:
        assert json.loads(input_json.read())[0] == \
               {'code': 'VNO',
                'name': 'Vornado Realty Trust',
                'P/E': -893.45}
    os.remove('p_e_report.json')


@pytest.mark.asyncio()
async def test_cost_max_report(input_data, get_cost_of_dollar):
    MakeReport(await input_data, await get_cost_of_dollar).get_cost_report()
    with open('cost_report.json', 'r') as input_json:
        assert json.loads(input_json.read())[0] == \
               {'code': 'AMZN',
                'name': 'Amazon',
                'price': 238932.86}
    os.remove('cost_report.json')


@pytest.mark.asyncio()
async def test_growth_max_report(input_data, get_cost_of_dollar):
    MakeReport(await input_data, await get_cost_of_dollar).get_growth_report()
    with open('growth_report.json', 'r') as input_json:
        assert json.loads(input_json.read())[0] == {'code': 'LB',
                                                    'name': 'L Brands Inc',
                                                    'growth': 347.65}
    os.remove('growth_report.json')


@pytest.mark.asyncio()
async def test_potential_profit_max_report(input_data, get_cost_of_dollar):
    MakeReport(await input_data, await get_cost_of_dollar).\
        get_potential_profit_report()
    with open('potential_profit_report.json', 'r') as input_json:
        assert json.loads(input_json.read())[0] == \
               {'code': 'GOOG',
                'name': 'Alphabet C (ex Google)',
                'potential profit': 84235.5}
    os.remove('potential_profit_report.json')
