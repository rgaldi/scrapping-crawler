import csv
import requests
from bs4 import BeautifulSoup

#Abrindo arquivo csv
f = csv.writer(open('cars.csv', 'w'))
f.writerow(['Name','Motor','Description','Location','Price'])

pages = [] #lista de paginas

# loop para criar a url com as paginas
for i in range(1,26):
    url = 'https://alura-site-scraping.herokuapp.com/index.php?page='+str(i)
    pages.append(url)

# loop para acessar cada pagina
for page in pages:

    try:
        html = requests.get(page)
        soup = BeautifulSoup(html.text, 'html.parser')
        card_cars = soup.find_all('div', class_='well card')
        print(f'Parseando página {page}')
    except requests.ConnectionError as e:
        print(f'Algo deu errado! Motivo: {e}')


    # loop para pegar as infos em cada pagina 
    for car in card_cars:

        
        # Encontrando o Nome do carro
        name_car = car.find('p', class_='txt-name inline')
        name_car = name_car.text

        # Encontrando o motor
        motor_car = car.find('p', class_='txt-motor')
        motor_car = motor_car.text

        # Encontrando a descricao
        description_car = car.find('p', class_='txt-description')
        description_car = description_car.text

        # Encontrando a localizacao
        location_car = car.find('p', class_='txt-location')
        location_car = location_car.text

        # Encontrando o valor
        value_car = car.find('p', class_='txt-value')
        value_car = value_car.text

        print('Todas as informações foram localizadas...')

        # Escrevendo no arquivo aberto as informacoes
        f.writerow([name_car, motor_car, description_car, location_car, value_car])
        print('Escrevendo no arquivo csv...')

print('Finalizou... :)')


elif expression:
    pass