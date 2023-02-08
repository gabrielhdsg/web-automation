import pandas as pd
import values as va

#get dolar value
dolar_value = va.get_dolar_value()
#get euro value
euro_value = va.get_euro_value()
#get gold value
gold_value = va.get_gold_value()

#reading database
table = pd.read_excel('Produtos.xlsx')

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

#export database
table.to_excel("Produtos_Novo.xlsx", index = False)