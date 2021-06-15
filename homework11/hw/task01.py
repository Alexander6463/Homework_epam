import asyncio
import json
from concurrent.futures import ProcessPoolExecutor
from itertools import chain

import aiohttp
from bs4 import BeautifulSoup


class CompanyRepository:
    def __init__(self):
        self.companies = list()
        self.dollar_value = float()
        self.pages = list()
        self.companies_info_link_cost_growth = list()
        self.new_urls = list()
        self.companies_info_name_pe_52wl_52wh = list()

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
    def get_urls_for_parse_link_cost_growth():
        base_url = 'https://markets.businessinsider.com/' \
                   'index/components/s&p_500?p='
        urls = [base_url + str(i) for i in range(1, 11)]
        return urls

    @staticmethod
    def get_url_for_parse_name_pe_52wl_52wh(companies_info):
        urls = list()
        for company_info in chain(*companies_info):
            urls.append('https://markets.businessinsider.com' +
                        company_info['link'])
        return urls

    @staticmethod
    def get_link_cost_growth_from_html(html):
        company_info = list()
        soup = BeautifulSoup(html, 'html.parser')
        for tr in soup.find_all('tr'):
            temp_dict = {"link": None, "cost": 0, 'growth': 0}
            info = tr.get_text().replace('\n\t', '').split()
            growth = info[-1]
            for td in tr:
                if 'title' in str(td):
                    link = td.find('a')['href']
                    temp_dict.update({'link': link})
                elif "table__td" in str(td):
                    cost = float(td.get_text().split()[0].replace(',', ''))
                    temp_dict.update({'cost': cost,
                                      'growth':
                                          float(growth.replace('%', ''))})
                    company_info.append(temp_dict)
                    break
        return company_info

    @staticmethod
    def get_name_pe_52wl_52wh_from_html(html):
        company_info = {'name': None, 'P/E': 0, '52WL': 0, '52WH': 0}
        soup = BeautifulSoup(html, 'html.parser')
        for h1 in soup.find_all('h1'):
            for span in h1.find('span'):  # get name company
                company_info.update({'name': span.strip()})
        for div_tag in soup.find_all('div',
                                     {'class': "snapshot__data-item"}):
            text = div_tag.get_text()
            if 'P/E' in text:
                company_info.update({
                    "P/E": float(text.split()[0].replace(',', ''))})
            if '52 Week Low' in text:
                company_info.update({
                    '52WL': float(text.split()[0].replace(',', ''))})
            if '52 Week High' in text:
                company_info.update({
                    '52WH': float(text.split()[0].replace(',', ''))})
        return company_info

    async def get_value_dollar(self):
        html = await self.fetch_response(
            'http://www.cbr.ru/scripts/XML_daily.asp?date_req=07/06/2021')
        soup = BeautifulSoup(html, 'html.parser')
        for valute in soup.find_all('valute'):
            if 'USD' in valute.get_text():
                return float(valute.find('value').get_text().
                             replace(',', '.'))

    @staticmethod
    def unite_information_about_companies(company_info_1, company_info_2):
        companies_info = list()
        for company in zip(chain(*company_info_1), company_info_2):
            unite_company_info = dict()
            link = company[0]['link']
            company[0]['link'] = link.replace('/stocks/', '').\
                replace('-stock', '')
            unite_company_info.update(company[1])
            unite_company_info.update(company[0])
            companies_info.append(unite_company_info)
        return companies_info

    @staticmethod
    def parse_info_multiprocess(func, html):
        with ProcessPoolExecutor(max_workers=4) as pool:
            res = pool.map(func, html)
        return list(res)

    async def get_info_companies(self):
        self.pages = await self.get_result_tasks(
            self.get_urls_for_parse_link_cost_growth(),
            self.fetch_response)
        self.companies_info_link_cost_growth = self.parse_info_multiprocess(
            self.get_link_cost_growth_from_html,
            self.pages)
        self.new_urls = self.get_url_for_parse_name_pe_52wl_52wh(
            self.companies_info_link_cost_growth)
        self.pages = await self.get_result_tasks(
            self.get_url_for_parse_name_pe_52wl_52wh(
                self.companies_info_link_cost_growth), self.fetch_response)
        self.companies_info_name_pe_52wl_52wh = self.parse_info_multiprocess(
            self.get_name_pe_52wl_52wh_from_html,
            self.pages)
        return self.unite_information_about_companies(
            self.companies_info_link_cost_growth,
            self.companies_info_name_pe_52wl_52wh)


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
    def __init__(self, companies_info, dollar):
        self.companies_info = companies_info
        self.cost_dollar = dollar

    def get_cost_report(self):
        res_json = list()
        for company_info in sorted(self.companies_info,
                                   key=lambda i: i['cost'],
                                   reverse=True)[0:10]:
            company = Company(company_info)
            res_json.append(
                {'code': company.link.upper(),
                 'name': company.name,
                 'price': round(company.cost * self.cost_dollar, 2)})
        with open('cost_report.json', 'w') as outfile:
            json.dump(res_json, outfile)

    def get_p_e_report(self):
        res_json = list()
        for company_info in sorted(self.companies_info,
                                   key=lambda i: i['P/E'])[0:10]:
            company = Company(company_info)
            res_json.append({'code': company.link.upper(),
                             'name': company.name,
                             'P/E': company.pe_index})
        with open('p_e_report.json', 'w') as outfile:
            json.dump(res_json, outfile)

    def get_growth_report(self):
        res_json = list()
        for company_info in sorted(self.companies_info,
                                   key=lambda i: i['growth'],
                                   reverse=True)[0:10]:
            company = Company(company_info)
            res_json.append({'code': company.link.upper(),
                             'name': company.name,
                             'growth': company.growth})
        with open('growth_report.json', 'w') as outfile:
            json.dump(res_json, outfile)

    def get_potential_profit_report(self):
        res_json = list()
        for company_info in self.companies_info:
            company = Company(company_info)
            res_json.append({'code': company.link.upper(),
                             'name': company.name,
                             'potential profit':
                                 round((company.week_high_52 -
                                        company.week_low_52) *
                                       self.cost_dollar, 2)})
        with open('potential_profit_report.json', 'w') as outfile:
            json.dump(sorted(res_json,
                             key=lambda i: i['potential profit'],
                             reverse=True)[0:10], outfile)


async def main():
    companies_information = await CompanyRepository().get_info_companies()
    cost_dollar = await CompanyRepository().get_value_dollar()
    report = MakeReport(companies_information, cost_dollar)
    report.get_cost_report()
    report.get_p_e_report()
    report.get_growth_report()
    report.get_potential_profit_report()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
