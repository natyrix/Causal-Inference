import pandas as pd
import dvc.api
from datetime import datetime
import holidays
from geopy import distance

class EDAPipeline():

    def __init__(self) -> None:
        self.ng_holidays = holidays.country_holidays('NG')


    def read_data(self, path, version="v1_nb"):
        try:
            repo = "/home/n/Documents/10_Academy/Causal Inference"
            data_url = dvc.api.get_url(path=path, repo=repo, rev=version)
            data_url = str(data_url)[6:]
            # print(data_url)
            df = pd.read_csv(data_url, sep=",", low_memory=False)
        except Exception as e:
            df = None
        return df
    
    def isWeekend(self, df_date_str):
        # 2021-07-01 07:28:04
        datetime_object = datetime.strptime(df_date_str, '%Y-%m-%d %H:%M:%S')
        # print(datetime_object.weekday())
        if datetime_object.weekday() < 5:
            return 0
        else:  # 5 Sat, 6 Sun
            return 1
    
    def isHoliday(self, df_date_str):
        try:
            dt = datetime.strptime(df_date_str, '%Y-%m-%d %H:%M:%S').date()
            if dt in self.ng_holidays:
                return 1
            else: return 0
        except Exception as e:
            return 0

    def calculate_distances(self, starting_coordinates, ending_coordinates):
        calculated_distances = []
        for i in range(len(starting_coordinates)):
            val = str(starting_coordinates[i]).split(',')
            starting_tuple = (val[0], val[1])
            val_end = str(ending_coordinates[i]).split(',')
            ending_tuple = (val_end[0], val_end[1])
            if val_end[0] == "0.0" or val_end[1] == "0.0":
                calculated_distances.append(-1)
            else:
                calculated_distances.append(distance.distance(starting_tuple, ending_tuple).km)
        return calculated_distances

    def check_distances_based_on_time(self, df, start_date_col='Trip Start Time', end_date_col='Trip End Time', distance_col='distance'):
        start_datetime_object = datetime.strptime(df[start_date_col], '%Y-%m-%d %H:%M:%S')
        end_datetime_object = datetime.strptime(df[end_date_col], '%Y-%m-%d %H:%M:%S')
        time_taken = end_datetime_object-start_datetime_object
        hrs = time_taken.total_seconds()/3600
        
    def calculate_speeds(self, starting_time_list, ending_time_list, distance_list):
        speed_list = []
        for i in range(len(starting_time_list)):
            try:
                start_datetime_object = datetime.strptime(starting_time_list[i], '%Y-%m-%d %H:%M:%S')
                end_datetime_object = datetime.strptime(ending_time_list[i], '%Y-%m-%d %H:%M:%S')
                time_taken = end_datetime_object-start_datetime_object
                hrs = time_taken.total_seconds()/3600
                speed_list.append(distance_list[i]/hrs)
            except Exception as e:
                speed_list.append(0.0)
        return speed_list

    def generateLatAndLng(self, df):
        lat, lng = df['Trip Origin'].apply(lambda x: str(x).split(','))
        return lat, lng


if __name__ == '__main__':
    # ed = EDAPipeline()
    # ed.isHoliday("2021-01-01 07:28:04")
    start_datetime_object = datetime.strptime("2021-01-01 07:28:04", '%Y-%m-%d %H:%M:%S')
    end_datetime_object = datetime.strptime("2021-01-01 07:38:04", '%Y-%m-%d %H:%M:%S')
    distance = 60

    time_taken = end_datetime_object-start_datetime_object
    hrs = time_taken.total_seconds()/3600
    print('Difference: ', hrs)
    print('Speed: ', distance/hrs)
