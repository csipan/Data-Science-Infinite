import json
import urllib.request

url = urllib.request.urlopen("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=4d1ecc182ee6414bb5c94857180711&q=Budapest&format=json&num_of_days=5").read()
data = json.loads(url)

# print(data)
monthly_stats = data["data"]["ClimateAverages"]
print(monthly_stats)
months = monthly_stats["month"]

for month in months:
    print(month["name"], month["avgMinTemp"])
