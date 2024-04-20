import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
# contatos_df = pd.read_excel("Enviar.xlsx")
# display(contatos_df) #visualizar


excel = pd.read_excel("env-message-bskt.xlsx")
print(excel)

navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_element("side")) < 1:
    time.sleep(1)

# enviar mensagem

for i, mensagem in enumerate(excel['Mensagem']):
    pessoa = excel.loc(i, "Pessoa")
    numero = excel.loc(i, "Numero")
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={55}{numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_element("side")) < 1:
        time.sleep(1)