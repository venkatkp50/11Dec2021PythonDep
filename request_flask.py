import requests

url = 'http://localhost:5000/predict_api'

import pandas as pd

r = requests.post(url,json={'X':2})

print(r.json())