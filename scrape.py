import requests
from sgselenium import SgChrome
from bs4 import BeautifulSoup as bs

driver = SgChrome(executable_path="chromedriver.exe").driver()
url = 'https://www.sytner.co.uk/dealer-locator/?postcode=ECV1'

driver.get(url)

headers = driver.requests[0].headers

html = driver.page_source
soup = bs(html, "html.parser")

script = soup.find_all("script")[-2]["src"]

s = requests.session()


cookie_url = "https://www.sytner.co.uk/" + script

s.get(cookie_url)

response = s.get(url, headers=headers).text

with open('file.txt', 'w', encoding='utf-8') as f:
    print(response, file=f)