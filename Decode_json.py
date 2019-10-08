import json
with open('D:\\MLB_players.json' , 'r') as reader:
    jf = json.loads(reader.read(),encoding="utf-8")
js=jf.get('copyright')[0].get('id')
print(js)