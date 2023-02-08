import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_dolar_value()->int:
    """Function searches dolar value on internet"""
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

    value = browser.find_element(
        'xpath', 
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    #quit chrome browser
    browser.quit()
    return value

def get_euro_value()->int:
    """Function searches euro value on internet"""
    #config chrome browser
    browser = webdriver.Chrome()

    #open google and search for dolar value
    browser.get("https://www.google.com.br/")
    browser.find_element(
    'xpath', 
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
    browser.find_element(
        'xpath', 
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
    value = browser.find_element(
        'xpath', 
        '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

    #quit chrome browser
    browser.quit()
    return value

def get_gold_value()->int:
    """Function searches gold value on internet"""
    #config chrome browser
    browser = webdriver.Chrome()
    browser.get("https://www.melhorcambio.com/ouro-hoje")
    value = browser.find_element(
        'xpath', 
        '//*[@id="comercial"]').get_attribute('value')
    value = value.replace(",",".")

    #quit chrome browser
    browser.quit()
    return value