
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
lista_de_noticias = []



driver = webdriver.Edge()

driver.get("https://g1.globo.com/")
html_content = driver.page_source

soup = BeautifulSoup(html_content, features='html.parser')

noticias = soup.find_all('a', class_='feed-post-link')


try:
    for noticia in noticias:
        link = noticia['href']
        titulo = noticia.find('p')
        if not titulo:
            continue
        titulo = titulo.get_text()
    
        driver.get(link)
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, features='html.parser')
        resumo = soup.find('p', class_ ='content-text__container')
        resumo_txt = ''
        if resumo:
            resumo_txt = resumo.get_text()
        else:
            resumo_txt = 'Resumo não encontrado'
    
        dados = {
                'titulo': titulo,
                'link': link,
                'resumo': resumo_txt
            }
        lista_de_noticias.append(dados)
finally:
    driver.quit()
    print('Driver fechado.')
if lista_de_noticias:
    df = pd.DataFrame(lista_de_noticias)
    df.to_excel('noticias_g1.xlsx', index=False)
else:
    print('Nenhuma notícia foi encontrada.')

