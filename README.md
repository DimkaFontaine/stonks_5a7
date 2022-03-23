# Stonks 5@7

## Installation
```
pip install -r requirements.txt
```

change name of `.env.sample` to `.env` and add the Access token (in Credentials on Square Developer)

## Use
add ```from square_sdk import SquareAPI``` in files to get acces to SquareAPI

Example:
```
from square_sdk import SquareAPI

api = SquareAPI()
cost = api.getPriceOf("Test_object1")
api.setPriceOf("Test_object1", 200)
```

