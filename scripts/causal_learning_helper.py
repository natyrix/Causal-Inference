

class CausalHelper():
    def __init__(self) -> None:
        pass

    def combine_get_driver_locations(self, df_trip, df_driver):
        # df_t = df_trip.copy()
        driver_lat_ls = []
        driver_lng_ls = []
        k = 0
        for i, df in df_trip.iterrows():
            try:
                trip_id = df['Trip ID']
                drivers = df_driver[df_driver['order_id']==trip_id]
                driver = drivers[drivers['driver_action']=="accepted"]
                if len(driver)>0:
                    driver_lat_ls.append(float(driver['lat']))
                    driver_lng_ls.append(float(driver['lng']))
                    # df['driver_lat'] = driver['lat']
                    # df['driver_lng'] = driver['lng']
                else:
                    if len(drivers) > 0:
                        driver_lat_ls.append(0.5)
                        driver_lng_ls.append(0.5)
                    else:
                        driver_lat_ls.append(0.0)
                        driver_lng_ls.append(0.0)
            # k+=1
            # if k > 1000:
            #     print(k)
            #     k=0
            except Exception as e:
                driver_lat_ls.append(0.0)
                driver_lng_ls.append(0.0)

        return driver_lat_ls, driver_lng_ls  
            


