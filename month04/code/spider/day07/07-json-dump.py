import json

app_info = {'name': 'xixi', '嘻嘻': '钥玥'}
with open('json.json', 'a') as f:
    json.dump(app_info, f, ensure_ascii=False)
    json.dump(app_info, f, ensure_ascii=True)
