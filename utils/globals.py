from datetime import date

# path to the file that contains the values send by the sensor in this day
global universal_sensor
universal_sensor = 'data/universal/universal_data_'+date.today().strftime("%d-%m-%Y")+".txt"