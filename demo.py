import requests

url = "http://550w.fun/api/gpt3/api"
params = {
    "msg": "你好",
    "apiKey": "sk-5ffc658760e043359e8996f226145539"
}

r = requests.post(url, data=params)
print(r.text)