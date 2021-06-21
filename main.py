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
        result.append([title, end_date, status])

with open("Результат веб-парсинга.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(['Название закупки', 'Дата окончания', 'Статус закупа'])
    writer.writerows(result)