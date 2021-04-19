import json
import pandas as pd

PEOPLE = [
  'Dimas Soares Lima',
  'Mariza Ferro',
  'Otto Teixeira Fraga Netto'
]

for i in PEOPLE:
  with open('database/'+i+'.json') as f:
    data = json.load(f)

  df = pd.json_normalize(data["items"])
  df.to_csv('database/'+i+'.csv')