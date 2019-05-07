# Dependencies
from bs4 import BeautifulSoup
import requests
import re

midcap = "http://investsnips.com/list-of-publicly-traded-mid-cap-oil-gas-exploration-and-production-companies/"
largecap = "http://investsnips.com/list-of-publicly-traded-large-cap-oil-gas-exploration-and-production-companies/"

def midcap_ls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    midcap_html = soup.find(class_="et_pb_text_inner").find_all('a')
    company_list = []
    for text in midcap_html:
        company = text.get_text()
        if re.findall("Mid-Cap+", company):
            company_list = []        
            continue        
        company_list.append(company)    
        if re.findall("WPX+", company):
            break
    return company_list

def largecap_ls(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    largecap_html = soup.find(class_="et_pb_text_inner").find_all('a')
    company_list = []
    for text in largecap_html:
        company = text.get_text()
        if re.findall("Oil and+", company):
            company_list = []        
            continue        
        company_list.append(company)    
        if re.findall("Pioneer+", company):
            break
    return company_list

all_companies = midcap_ls(midcap) + (largecap_ls(largecap))

def ticker_name(company_list):
    ticker_ls = []
    for company in company_list:
        start = company.find("(") + 1
        end = company.find(")")
        ticker_ls.append(company[start:end])
    return ticker_ls

ticker_list = ticker_name(all_companies)