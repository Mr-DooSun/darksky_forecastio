import forecastio

def main():

    api_key = "User Key" #user key 유저 키

    lat = 35.663106 #Latitude 위도
    lng = 128.413759 #longitude 경도

    forecast = forecastio.load_forecast(api_key, lat, lng)
    weather=forecast.currently()

    print(weather.icon)
    print(weather.temperature)

if __name__ == "__main__":
    main()