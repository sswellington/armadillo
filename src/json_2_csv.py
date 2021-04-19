import json
import pandas as pd

with open('database/sampling.json') as f:
  data = json.load(f)

df = pd.json_normalize(data["items"])
df.to_csv('database/sampling.csv')