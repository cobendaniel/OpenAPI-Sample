import requests
import pandas as pd

response      = requests.get("http://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey=insert_api_key&numOfRows=10&resultType=json")
response_dict = response.json()

data_dictionary = {}  
for i in response_dict["response"]["body"]["items"]["item"][1].keys():
    data_dictionary[i] = []

for i in range(len(response_dict["response"]["body"]["items"]["item"])):
    sub_dict = response_dict["response"]["body"]["items"]["item"][i]

    for (key, value) in sub_dict.items():
        data_dictionary[key].append(value)
      
pd.DataFrame(data_dictionary)
