import requests
import json

city = "Seoul"
apikey = "d906a2e33f857f40b72a5aae6b91d23e"
api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

data = json.loads(result.text)

# print(type(result.text))
# print(type(data))

print(data["name"], "의 날씨입니다.")
print("날씨는", data["weather"][0]["main"], "입니다.")
print("현재 온도는", data["main"]["temp"], "입니다.")
print("하지만 체감 온도는", data["main"]["feels_like"], "입니다.")