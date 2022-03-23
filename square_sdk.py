import json
import urllib3
from decouple import config

http = urllib3.PoolManager()

token = config("API_TOKEN")

head={
        'Content-Type': 'application/json',
        'Square-Version': '2022-03-16',
        'Authorization': token
  }

def SquareAPI_GET(request):

  r = http.request(
      'GET',
      'https://connect.squareupsandbox.com/v2/' + request,
      headers=head
  )

  return json.loads(r.data.decode('utf-8'))


def SquareAPI_POST(request,data):

  encoded_data = json.dumps(data).encode('utf-8')

  r = http.request(
      'POST',
      'https://connect.squareupsandbox.com/v2/' + request,
      body=encoded_data,
      headers=head
  )

  return json.loads(r.data.decode('utf-8'))

catalog_list = SquareAPI_GET('catalog/list')

for index in range(len(catalog_list['objects'])):
  if catalog_list['objects'][index]['id'] == "JHLK3GQZUUQHOCKYMYVWILRR":
    catalog_list['objects'][index]['item_data']['variations'][0]['item_variation_data']['price_money']['amount'] = 199


data = {
  "batches":[
    {
      "objects":catalog_list['objects']
    }
  ],
  "idempotency_key":"e2a749db-2fac-4167-ae21-45215ab936b3",
}


reponse = SquareAPI_POST('catalog/batch-upsert',data)





