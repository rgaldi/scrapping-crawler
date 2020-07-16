import requests
from bs4 import BeautifulSoup
import csv
import json
from json import JSONDecodeError



lista_id = []
lista = []

with open('scraping.csv', 'w') as f:

    coluna = ['TIPO','NOME','ENDERECO','TELEFONE','EMAIL','ABL']
    w = csv.DictWriter(f, fieldnames=coluna)
    w.writeheader()

    tipo = 'SHOPPING'

    for x in range(0,20):
        

        data = {
        'page': f'{x}',
        'ope': 'all',
        'letter': '',
        'action': 'load_more_shopping'
            }

        html = requests.post('https://abrasce.com.br/wp-admin/admin-ajax.php', data=data)
        soup = BeautifulSoup(html.text, 'html.parser')
        cards = soup.find_all('div', class_='col-12 col-lg-4 mb-4')


        for card in cards:
            nome = card.find_all('div', class_='row')
            ids = card.find_all('span', class_='mfs_estado')
            
            for x in nome:
                name = x.get_text().strip()
                print(name)
                lista.append(name)
                
                            
            for id in ids:
                x = id['data-sugarid']
                lista_id.append(x)

    for x in lista_id:
        print(x)
        data = {
        'sugarid': f'{x}',
        'action': 'mfs_sugarcrm',
        'f': 'getShoppingValues'
        }

        a = requests.post('https://abrasce.com.br/wp-admin/admin-ajax.php', data=data)
        soup2 = BeautifulSoup(a.text, 'html.parser')

        try:
            site_json = json.loads(soup2.text)     
            endereco = site_json['endereco']
            tel = site_json['phone_office']
            email = site_json['email']
            abl = site_json['abl_c'] + ' m2'

            for l in lista:
                nome = str(l)
                w.writerow([tipo,l,endereco,tel,email,abl])

        except JSONDecodeError as e:
            print(f'Erro! Mensagem: {e}')
        break

    
    


        
    




    


