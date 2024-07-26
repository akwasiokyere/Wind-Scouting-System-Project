# import all the necessary libraries
from machine import ADC, Pin, UART
import utime

#Initialise the Adc pin
adc = ADC(Pin(26))

# Initialise UART module for blutooth communication
uart = UART(0, boadrate=9600, tx=Pin(1), rx=Pin(1))

# Reference Voltage and ADC rosulution
vref = 3.3 # maximum voltage

adc_resolution = 65535 # The range of values the Adc can read

# function to convert the values to voltage
def read_wind_speed():
    voltage = adc_value*vref / adc_resolution
    return voltage

# Function to add/append all incoming data file
def wind_speed_data_to_file(timestamp_str, voltage):
    try:
        with open("wind_speed_data_file.csv", "a") as data_file: #open data file in append mode
            data_file.write("(), (:.2f)\n".format(timestamp_str, voltage))
    except Exception as e:
        print("Error writing to file", e)
        
# Function to loop the program forever
def main():
    while True:
        voltage =  read_wind_speed() # store incoming data as voltage
        
        # Get the current timestamp
        timestamp = utime.localtime()
        
        # Define the format for the timestamp
        timestamp_str = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{02d}".format(timestamp[0],timestamp[1],timestamp[2],
                                                                          timestamp[3],timestamp[4],timestamp[5])
        
        #Append or add wind speed data to file
        wind_speed_data_to_file(timestamp_str, voltage)
        
        # Print the timestamp and voltage to be displayed
        print("Timestamp:(), Volts produced by wind speed[V]: {:.02f}V".format(timestamp_str, voltage))
        
        # Send voltage through blutooth to the app in Mit Inventer app
        uart.write(f"{timestmp_str},{Voltage}\n")
        
        utime.sleep(2)
        
# Initialise the data file with headers if it does not exist
try:
    with open("wind_append_data_file.csv", "r") as data_file:
        pass
except OSError:
    with open("wind_append_data_file.csv", "r") as data_file:
        data_file.write("timpstamp_str, Voltage\n")
        
# Program should stop running when a key on the keyboard is pressed        
try:
    main()
except KeyboardInterupt:
    print("Program Interrupted.")
