import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from bs4 import BeautifulSoup
# create a base code of scrapper, where the page has pagination and the base url is https://www.bcv.org.ve/estadisticas/tipo-cambio-de-referencia-smc
base_url = "https://www.bcv.org.ve/estadisticas/tipo-cambio-de-referencia-smc"
# create a list to store the data
data = []
# create a list to store the headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246",
    "Accept": "*/*",
    "Connection": "keep-alive"
}
# create a list to store the url

# create a function to get the data from the page
def get_data(page = 0):
    response = requests.get(base_url + '?page=' + str(page), headers=headers, verify=False)
    soup = BeautifulSoup(response.text, 'html.parser')
    nextpage = soup.find('li', class_='next')
    tables = soup.find_all('table')
    for table in tables:
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            for col in cols:
                link = col.find('a')
                if link is not None:
                    data.append(link.get('href'))
    

    if nextpage is not None:
        page += 1
        get_data(page)

def download_files():
    for url in data:
        response = requests.get(url, headers=headers, verify=False)
        print(response.status_code)
        filename = url.split('/')[-1]
        with open('files/'+ filename, 'wb') as f:
            f.write(response.content)

def main():
    get_data()
    download_files()


if __name__ == "__main__":
    main()