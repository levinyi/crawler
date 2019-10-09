import os
import requests
from bs4 import BeautifulSoup
url = "https://archive.org/download/englishpod_all"
html = requests.get(url)
print(html.status_code)

download_list = []
if html.status_code == 200:
    soup = BeautifulSoup(html.text, "html.parser")
    for link in soup.find_all('a'):
        new_link = str(link.get('href'))
        if new_link.endswith(('.pdf', '.mp3')):
            pdf_url = url + '/' + new_link
            download_list.append(pdf_url)

for each in download_list:
    pdf_output_name = each.split("/")[-1]
    if not os.path.exists(pdf_output_name):
        pdf_r = requests.get(each)
        with open(pdf_output_name, "wb") as pdf_file:
            pdf_file.write(pdf_r.content)
            print("finished download pdf file {}".format(pdf_output_name))
