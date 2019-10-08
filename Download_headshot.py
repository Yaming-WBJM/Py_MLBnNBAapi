import urllib.request
import psycopg2
import time
from cryptography.hazmat.primitives.ciphers import base
 
#base_url = 'https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/'

base_url = 'https://securea.mlb.com/mlb/images/players/head_shot/'
path_name = 'D:\\Sport_JSON\\MLB\\Headshots\\'
 
conn = psycopg2.connect(database="sportge", user="postgres", password="4Rfv7ujm", host="127.0.0.1", port="5432")
print ("Opened database successfully")
cur = conn.cursor()

cur.execute("SELECT player_id from mlb_players")
rows = cur.fetchall()
for row in rows:
    file_name = str(row[0])+'.jpg'
    print(base_url + file_name)
    try:
        urllib.request.urlretrieve(base_url + file_name, path_name + file_name)
    except:
        print("File not exists: "+file_name)
    time.sleep(0.1)
    
print ("Operation done successfully")
conn.close()