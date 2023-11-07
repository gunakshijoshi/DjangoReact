
from django.http import HttpResponse, JsonResponse
import pandas as pd
from .models import Coinstock
import time
from rest_framework.decorators import api_view
import json
import requests
from bs4 import BeautifulSoup


def web_scraping(*args):
    base_url = "https://coinmarketcap.com/"
    all_columns = ["id", "Name", "Price", "1h%", "24h%", "7d%",
                   "Market Cap", "Volume(24h)", "Circulating Supply"]
    df = pd.DataFrame(columns=all_columns)
    values = []
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        table = soup.find("table", class_="cmc-table")

        if table:
            rows = table.find_all("tr")
            for row in rows[1:11]:
                data = row.find_all("td")
                #print(data)
                # for i in range(1,11):
                #     if(i==1):
                #          id_val+=1
                #     if(i<len(data) and data[i].text is not None):
                #         values.append(data[i].text)
                #     elif((i<len(data) and data[i].text is None and i!=1) or i>len(data)):
                #          values.append(None)
                #     elif(i<len(data) and data[i].text is None and i==1):
                #          values.append(id_val)
                values = [data[1].text, data[2].text, data[3].text, data[4].text,
                          data[5].text, data[6].text, data[7].text, data[8].text, data[9].text]
                # print(values)
                df.loc[len(df)] = values
            #print(df)
            json_data = df.to_json(orient='records')

            post_url = "http://localhost:8000/stockui/put_coin_data/"
            response = requests.post(post_url, data=json_data)
            if response.status_code == 200:
                return HttpResponse(response)
            else:
                return (f"Failed to send data. Status code: {response.status_code}")

    else:
        return (f"Failed to retrieve data for page. Status code: {response.status_code}")


@api_view(['POST'])
def put_coin_data(request):
    json_data = json.loads(request.body)
    dataframe = pd.DataFrame(json_data)
    for _, row in dataframe.iterrows():
        instance = Coinstock(
                id=row['id'],
                name=row['Name'],
                price=row['Price'],
                _1h_percent=row['1h%'],
                _24h_percent=row['24h%'],
                _7d_percent=row['7d%'],
                market_cap=row['Market Cap'],
                volume_24h=row['Volume(24h)'],
                circulating_supply=row['Circulating Supply']
            )
        instance.save()
    return JsonResponse({"message": "Data added to the database successfully."})


@api_view(['Get'])
def fetch_coin_data(*args):
    data = Coinstock.objects.all()
    table_data = [
        {
            'id': item.id,
            'name': item.name,
            'price': item.price,
            '1h_percent': item._1h_percent,
            '24h_percent': item._24h_percent,
            '7d_percent': item._7d_percent,
            'market_cap': item.market_cap,
            'volume_24h': item.volume_24h,
            'circulating_supply': item.circulating_supply,
        }
        for item in data
    ]
    # print(table_data[0]['market_cap'])
    return JsonResponse(table_data, safe=False)
