import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query/?function=TIME_SERIES_DAILY&symbol=TSLA&apikey={your_API_key}"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

data = requests.get(STOCK_ENDPOINT)
price = data.json()

dailyprices = {key:value for (key, value) in price.items()}

firstclosingprice = float(dailyprices['Time Series (Daily)']['2022-11-02']['4. close'])
print("Nov. 2nd closing price was: ", firstclosingprice) # dailyprices['Time Series (Daily)']['2022-11-02']['4. close'])
    # print(dailyprices['4. close'])

#TODO 2. - Get the day before yesterday's closing stock price
secondclosingprice = float(dailyprices['Time Series (Daily)']['2022-11-01']['4. close'])
print("Nov. 1st closing price was: ", secondclosingprice)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

difference = firstclosingprice - secondclosingprice
difference = round(difference)

if difference < 0:
    difference = difference * -1
else:
    pass
print('\nThe positive difference is: ', difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

percentagedifference = difference / ((firstclosingprice + secondclosingprice) / 2) * 100

print('\nThe percentage difference is: ', percentagedifference)
