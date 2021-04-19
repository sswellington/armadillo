import json
import pandas as pd

PEOPLE = 'Dimas Soares Lima'
PEOPLE = 'Mariza Ferro'
PEOPLE = 'Otto Teixeira Fraga Netto'

with open('database/'+PEOPLE+'.json') as f:
  data = json.load(f)

df = pd.json_normalize(data["items"])
df.to_csv('database/'+PEOPLE+'.csv')