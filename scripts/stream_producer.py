# car_data =  {
#     "brake": 0,
#     "date": "2024-05-15T13:00:00.000000+00:00",
#     "driver_number": 0,
#     "drs": 0,
#     "meeting_key": 1,
#     "n_gear": 0,
#     "rpm": 0,
#     "session_key": 1,
#     "speed": 0,
#     "throttle": 0
#   }


# lap_data = {
# [
#   {
#     "date_start": "2023-09-16T13:59:07.606000+00:00",
#     "driver_number": 0,
#     "duration_sector_1": 0,
#     "duration_sector_2": 0,
#     "duration_sector_3": 0,
#     "i1_speed": 0,
#     "i2_speed": 0,
#     "is_pit_out_lap": false,
#     "lap_duration": 0,
#     "lap_number": 0,
#     "meeting_key": 1,
#     "session_key": 1,
#     "st_speed": 0
#   }
# ]
# }


# Generate fake data

# generate lap data

DRIVER_NUMBERS = [1,4,16,81,55,44,11,63,14,18,27,22,3,38,10,20,31,23,24,2,77]

class DataGenerator:
    """
    This class takes in producer object from producer script
    """
    def __init__(self, producer):
        self.producer = producer
        
    
    def generate_lap_data():
        
        # increment through driver numbers.
        # insert new object into lap data,
        # loop through driver numbers.
        # randomly increment the time between 2 seconds of each other for each driver
        # once 
        lap_data=[]
        
        
        