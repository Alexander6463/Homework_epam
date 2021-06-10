import asyncio
import json
from concurrent.futures import ProcessPoolExecutor
from itertools import chain

import aiohttp
from bs4 import BeautifulSoup


class CompanyRepository:
    def __init__(self):
        self.companies = list()
        self.dollar = float()
        self.pages = list()
        self.firms = list()
        self.new_urls = list()
        self.firms2 = list()

    @staticmethod
    async def fetch_response(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()

    @staticmethod
    async def get_result_tasks(urls, request):
        pages = list()
        tasks = [asyncio.create_task(request(url)) for url in urls]
        await asyncio.gather(*tasks)
        for task in tasks:
            pages.append(task.result())
        return pages

    @staticmethod
    def get_url_for_first_part():
        base_url = 'https://markets.businessinsider.com/' \
                   'index/components/s&p_500?p='
        urls = [base_url + str(i) for i in range(1, 11)]
        return urls

    @staticmethod
    def get_url_for_second_part(lst):
        urls = list()
        for firm in chain(*lst):
            urls.append('https://markets.businessinsider.com' + firm['link'])
        return urls

    @staticmethod
    def get_first_part_info_from_html(html):
        result = list()
        soup = BeautifulSoup(html, 'html.parser')
        for tr in soup.find_all('tr'):
            current_dict = {"link": None, "cost": 0, 'growth': 0}
            info = tr.get_text().replace('\n\t', '').split()
            growth = info[-1]
            for td in tr:
                if 'title' in str(td):
                    link = td.find('a')['href']
                    current_dict.update({'link': link})
                elif "table__td" in str(td):
                    cost = float(td.get_text().split()[0].replace(',', ''))
                    current_dict.update({'cost': cost,
                                         'growth':
                                             float(growth.replace('%', ''))})
                    result.append(current_dict)
                    break
        return result

    @staticmethod
    def get_second_part_info_from_html(html):
        current_dict = {'name': None, 'P/E': 0, '52WL': 0, '52WH': 0}
        soup = BeautifulSoup(html, 'html.parser')
        for h1 in soup.find_all('h1'):
            for span in h1.find('span'):  # get name company
                current_dict.update({'name': span.strip()})
        for div_tag in soup.find_all('div',
                                     {'class': "snapshot__data-item"}):
            text = div_tag.get_text()
            if 'P/E' in text:
                current_dict.update({
                    "P/E": float(text.split()[0].replace(',', ''))})
            if '52 Week Low' in text:
                current_dict.update({
                    '52WL': float(text.split()[0].replace(',', ''))})
            if '52 Week High' in text:
                current_dict.update({
                    '52WH': float(text.split()[0].replace(',', ''))})
        return current_dict

    async def get_current_value_dollar(self):
        xml = await self.fetch_response(
            'http://www.cbr.ru/scripts/XML_daily.asp?date_req=07/06/2021')
        soup = BeautifulSoup(xml, 'html.parser')
        for valute in soup.find_all('valute'):
            if 'USD' in valute.get_text():
                return float(valute.find('value').get_text().
                             replace(',', '.'))

    @staticmethod
    def update_info_firm1_and_firm2(firms1, firms2):
        firm_result = list()
        for firm in zip(chain(*firms1), firms2):
            new_dict = dict()
            link = firm[0]['link']
            firm[0]['link'] = link.replace('/stocks/', '').\
                replace('-stock', '')
            new_dict.update(firm[1])
            new_dict.update(firm[0])
            firm_result.append(new_dict)
        return firm_result

    @staticmethod
    def parse_info_multiprocess(func, html):
        with ProcessPoolExecutor(max_workers=4) as pool:
            res = pool.map(func, html)
        return list(res)

    async def get_info_companies(self):
        self.pages = await self.get_result_tasks(
            self.get_url_for_first_part(),
            self.fetch_response)
        self.firms = self.parse_info_multiprocess(
            self.get_first_part_info_from_html,
            self.pages)
        self.new_urls = self.get_url_for_second_part(self.firms)
        self.pages = await self.get_result_tasks(
            self.get_url_for_second_part(self.firms),
            self.fetch_response)
        self.firms2 = self.parse_info_multiprocess(
            self.get_second_part_info_from_html,
            self.pages)
        return self.update_info_firm1_and_firm2(self.firms, self.firms2)


class Company:
    def __init__(self, firm):
        self.name = firm['name']
        self.cost = firm['cost']
        self.pe_index = firm['P/E']
        self.link = firm['link']
        self.week_low_52 = firm['52WL']
        self.week_high_52 = firm['52WH']
        self.growth = firm['growth']


class MakeReport:
    def __init__(self, firms, dollar):
        self.companies = firms
        self.cost_dollar = dollar

    def get_cost_report(self):
        res_json = list()
        for element in sorted(self.companies,
                              key=lambda i: i['cost'], reverse=True)[0:10]:
            company = Company(element)
            res_json.append(
                {'code': company.link.upper(),
                 'name': company.name,
                 'price': round(company.cost * self.cost_dollar, 2)})
        return json.dumps(res_json)

    def get_p_e_report(self):
        res_json = list()
        for element in sorted(self.companies,
                              key=lambda i: i['P/E'])[0:10]:
            company = Company(element)
            res_json.append({'code': company.link.upper(),
                             'name': company.name,
                             'P/E': company.pe_index})
        return json.dumps(res_json)

    def get_growth_report(self):
        res_json = list()
        for element in sorted(self.companies,
                              key=lambda i: i['growth'], reverse=True)[0:10]:
            company = Company(element)
            res_json.append({'code': company.link.upper(),
                             'name': company.name,
                             'growth': company.growth})
        return json.dumps(res_json)

    def get_potential_profit_report(self):
        res_json = list()
        for element in self.companies:
            company = Company(element)
            res_json.append({'code': company.link.upper(),
                             'name': company.name,
                             'potential profit':
                                 round((company.week_high_52 -
                                        company.week_low_52) *
                                       self.cost_dollar, 2)})
        return json.dumps(sorted(res_json,
                                 key=lambda i: i['potential profit'],
                                 reverse=True)[0:10])


async def main():
    firms = await CompanyRepository().get_info_companies()
    cost_dollar = await CompanyRepository().get_current_value_dollar()
    report = MakeReport(firms, cost_dollar)
    print(firms)
    print(report.get_cost_report())
    print(report.get_p_e_report())
    print(report.get_growth_report())
    print(report.get_potential_profit_report())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
