import datetime
import httpx

import credentials

url = 'https://api.sam.gov/prod/opportunities/v1/search'
ncode = 541511
ptype = 'r,p,o,k'
limit = 1000

today = datetime.date.today()

params = {
    'api_key': credentials.api_key,
    'ncode': ncode,
    'ptype': ptype,
    'limit': limit,
    'postedFrom': (today - datetime.timedelta(days=30)).strftime('%m/%d/%Y'),
    'postedTo': today.strftime('%m/%d/%Y'),
}

ops = []

r = httpx.get(url, params=params)
ops = r.json()['opportunitiesData']

for op in ops:
    op['description_text'] = get_description(op['description'])

def get_description(url: str) -> str:
    r = httpx.get(url + 'api_key=' + credentials.api_key)
    return r.text

print(ops)
