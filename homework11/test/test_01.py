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
    data = MakeReport(await input_data,
                      await get_cost_of_dollar).get_p_e_report()
    assert data[0] == {'code': 'VNO',
                       'name': 'Vornado Realty Trust',
                       'P/E': -893.45}


@pytest.mark.asyncio()
async def test_cost_max_report(input_data, get_cost_of_dollar):
    data = MakeReport(await input_data,
                      await get_cost_of_dollar).get_cost_report()
    assert data[0] == {'code': 'AMZN',
                       'name': 'Amazon',
                       'price': 238932.86}


@pytest.mark.asyncio()
async def test_growth_max_report(input_data, get_cost_of_dollar):
    data = MakeReport(await input_data,
                      await get_cost_of_dollar).get_growth_report()
    assert data[0] == {'code': 'LB',
                       'name': 'L Brands Inc',
                       'growth': 347.65}


@pytest.mark.asyncio()
async def test_potential_profit_max_report(input_data, get_cost_of_dollar):
    data = MakeReport(await input_data,
                      await get_cost_of_dollar).get_potential_profit_report()
    assert data[0] == {'code': 'GOOG',
                       'name': 'Alphabet C (ex Google)',
                       'potential profit': 84235.5}


@pytest.mark.asyncio()
async def test_save_method(input_data, get_cost_of_dollar):
    report = MakeReport(await input_data, await get_cost_of_dollar)
    data = report.get_potential_profit_report()
    report.save_report_into_json_file(data, 'potential_profit.json')
    with open('potential_profit.json', 'r') as input_file:
        assert json.loads(input_file.read())[0] == \
               {'code': 'GOOG',
                'name': 'Alphabet C (ex Google)',
                'potential profit': 84235.5}
    os.remove('potential_profit.json')
