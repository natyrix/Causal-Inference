from datetime import datetime as dtime
import datetime

class WeatherAPIConnector():
    def __init__(self) -> None:
        self.URL = "https://api.weatherbit.io/v2.0/history/"
        self.visited_dates = {}

    def make_weather_api_request(self,endpoint, lat, lng, start_date, end_date):
        try:
            pass
        except Exception as e:
            pass

    def get_daily_weather(self, df_str_date, lat, lng):
        dt = dtime.strptime(df_str_date, '%Y-%m-%d %H:%M:%S').date()
        start_date = f"{dt.year}-{dt.month}-{dt.day}"
        end_dt = dt + datetime.timedelta(days=1)
        end_date = f"{end_dt.year}-{end_dt.month}-{end_dt.day}"
        if start_date not in self.visited_dates:
            self.visited_dates[start_date] = "PERC"
            return 1
        else:
            return self.visited_dates[start_date]
        

if __name__ == "__main__":
    w = WeatherAPIConnector()
    # print(w.make_request(endpoint="daily",data="SKMCK"))
    w.get_daily_weather("2021-01-01 07:28:04")
    w.get_daily_weather("2021-01-01 07:28:04")