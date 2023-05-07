import mysql.connector
import requests
from bs4 import BeautifulSoup

palavra = input("Digite a palavra: " )
response = requests.get ('https://www.lexico.pt/' + palavra)

content = response.content
site = BeautifulSoup(content, 'html.parser')

wraps = site.find_all('div', attrs={'class' : 'card card-pl'})
card_sinonimos = wraps[0]
card_antonimos = wraps[1]
find_sinonimos = card_sinonimos.find_all('a')
find_antonimos = card_antonimos.find_all('a')

sinonimos=[]
for sinonimo in find_sinonimos:
    get = sinonimo.getText()
    sinonimos.append(get)

if len(sinonimos) == 0:
    print("Não possui sinonimos")
else:
    print(sinonimos)

antonimos=[]
for antonimo in find_antonimos:
    get = antonimo.getText()
    antonimos.append(get)

if len(antonimos) == 0:
    print("Não possui antonimos")
else:
    print(antonimos)

mydb = mysql.connector.connect(
  host="sql10.freemysqlhosting.net",
  user="sql10612581",
  password="Qhd7b3PWb4",
  database="sql10612581",
  port=3306
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM palavra WHERE nome = '" + palavra + "';")
myresult = mycursor.fetchall()
if len(myresult) == 0:
    insert_palavra_sql = "INSERT INTO palavra (nome) VALUES ('" + palavra +"')"
    mycursor.execute(insert_palavra_sql)
    mydb.commit()
    print("Palavra adicionada com sucesso")
    id_palavra = mycursor.execute("SELECT idpalavra FROM palavra WHERE nome = '" + palavra + "';")
    table_id = mycursor.fetchone()[0]
    for sin in sinonimos:
        insert_sinonimo_sql = "INSERT INTO sinonimo (nome, palavra_idpalavra) VALUES ('" + sin + "','" + id_palavra + "')"
        mycursor.execute(insert_sinonimo_sql)
        mydb.commit()
    for ant in antonimos:
        insert_antonimos_sql = "INSERT INTO antonimo (nome, palavra_idpalavra) VALUES ('" + ant + "','" + id_palavra + "')"
        mycursor.execute(insert_antonimos_sql)
        mydb.commit()

