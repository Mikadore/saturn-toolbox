import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
def start():
    headers = Headers(os="win", headers=True).generate()
    product_link = 'https://www.nike.com/launch/t/sb-dunk-low-sean-cliver-holiday-special'
    product_size = 10.5
    r = requests.get(product_link, headers=headers).text
    #print(r.status_code)
    soup1 = BeautifulSoup(r, 'lxml')
    product_id = soup1.find("meta", {"name":"branch:deeplink:productId"})['content']
    print(product_id)
    early_link = f"{product_link}?productId={product_id}&size={product_size}"
    print(early_link)

