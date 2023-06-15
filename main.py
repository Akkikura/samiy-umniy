import requests
import json
from pprint import pprint

id_list = ['332.json', '149.json', '655.json'] 
names_dict = {'332.json':'Hulk', '149.json': 'Captain america', '655.json': ' Thanos'}
intelligence_dict = {}
url = 'https://akabab.github.io/superhero-api/api/id/'

for id in id_list:
    name_dict = json.loads(requests.get(url + id).content)
    intelligence_dict[id] = int(name_dict['powerstats']['intelligence'])
max_intelligence = max(intelligence_dict)
pprint(names_dict[max_intelligence])