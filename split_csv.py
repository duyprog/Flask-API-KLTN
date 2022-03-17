import pandas as pd 
from datetime import date
class split_csv:
    def create_sensor_csv(self, path):
        today = str(date.today())
        df = pd.read_csv(path)
        self.sensor_to_csv(df, 'PRES', 'pres_'+ today + '.csv')


    
    def sensor_to_csv(self, og_df, sensor_name, file_name):
        df_sensor = og_df[og_df.sensor == sensor_name]
        df_sensor_value = df_sensor['value']
        df_sensor_value.to_csv(file_name, index=False)
pass
        