import json
import urllib.request

url = urllib.request.urlopen("http://api.worldweatheronline.com/premium/v1/weather.ashx?key=4d1ecc182ee6414bb5c94857180711&q=Budapest&format=json&num_of_days=5").read()
data = json.loads(url)

# Getting the whole json file
print(json.dumps(data, indent=2))
print("------------------------------------------------")

# Getting the monthly stats
monthly_stats = data["data"]["ClimateAverages"]
print(json.dumps(monthly_stats, indent=2))
print("------------------------------------------------")

# Getting the average minimum temperature and the average daily rainfall for every month
months = monthly_stats[0]["month"]
for month in months:
    print(month["name"], month["avgMinTemp"], month["avgDailyRainfall"])
print("------------------------------------------------")

# Getting the sunrise for a certain day
daily_stats = data["data"]["weather"]
for date in daily_stats:
    day = "2018-11-10"
    if date["date"] == day:
        print(date["astronomy"][0]["sunrise"])
