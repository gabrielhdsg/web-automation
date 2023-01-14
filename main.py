import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#config chrome browser
browser = webdriver.Chrome()

#open google and search for dolar value
browser.get("https://www.google.com.br/")
browser.find_element(
    'xpath', 
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
browser.find_element(
    'xpath', 
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

dolar_value = browser.find_element(
    'xpath', 
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(dolar_value)

#open google and search for euro value
browser.get("https://www.google.com.br/")
browser.find_element(
    'xpath', 
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
browser.find_element(
    'xpath', 
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
euro_value = browser.find_element(
    'xpath', 
    '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

print(euro_value)

#get gold value
browser.get("https://www.melhorcambio.com/ouro-hoje")
gold_value = browser.find_element(
    'xpath', 
    '//*[@id="comercial"]').get_attribute('value')
gold_value = gold_value.replace(",",".")
print(gold_value)

#reading database
table = pd.read_excel('Produtos.xlsx')
print(table)

#updating database values
#dolar
table.loc[table["Moeda"]=="Dólar", "Cotação"] = float(dolar_value)
#euro
table.loc[table["Moeda"]=="Euro", "Cotação"] = float(euro_value)
#gold
table.loc[table["Moeda"]=="Ouro", "Cotação"] = float(gold_value)

#updating buy values 
table["Preço de Compra"] = table["Cotação"] * table["Preço Original"]

#updating sales values
table["Preço de Venda"] = table["Preço de Compra"] * table["Margem"]

print(table)

browser.quit()

#export database
table.to_excel("Produtos_Novo.xlsx", index = False)