from bs4 import BeautifulSoup
import requests
import csv
result = []
for i in range(1, 40):
    url = requests.get('https://zakup.kbtu.kz/zakupki/sposobom-zaprosa-cenovyh-predlozheniy&page=' + str(i)).text
    soup = BeautifulSoup(url, 'lxml')
    bodies = soup.find_all('div', {'class': 'card-body'})
    for body in bodies:
        title = body.a.text.strip()
        end_date = body.strong.text
        status = body.p.span.text
        podrobnosti = body.find('a', href=True)['href']
        links_url = requests.get('https://zakup.kbtu.kz/' + podrobnosti).text
        links_soup = BeautifulSoup(links_url, 'lxml')
        info = links_soup.find_all('div', {'class': 'col'})[1].p
        info = info.text if info else 'Нет информации'

        content = links_soup.find_all('table')[1].find_all('span')
        start_date = content[3].text.strip()
        end_date_time = content[5].text.strip()
        result.append([title, end_date, status, info, start_date, end_date_time])


with open("Результат веб-парсинга.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['Название закупки', 'Дата окончания', 'Статус закупа','Информация', 'Начало', 'Окончание'])
    writer.writerows(result)
