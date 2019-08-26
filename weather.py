import forecastio #pip install python-forecastio

def main():

    api_key = "User Key" #user key 유저 키 ※수정필요

    lat = 35.663106 #Latitude 위도 ※수정필요
    lng = 128.413759 #longitude 경도 ※수정필요

    forecast = forecastio.load_forecast(api_key, lat, lng)
    weather=forecast.currently()

    print(weather.icon)
    print(weather.temperature)

if __name__ == "__main__":
    main()