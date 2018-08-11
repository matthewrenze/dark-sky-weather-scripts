#%% Convert Dark Sky JSON to CSV

# Purpose: Converts Dark Sky JSON files to a CSV file

# Author: Matthew Renze

# Usage: python.exe Convert.py input-folder output-file
#   - input-folder = the folder containing Dark Sky JSON files
#   - output-file = the CSV file to write the Dark SKY data to

# Example: python.exe Convert.py C:\InputFolder\ C:\OutputFile

#%% Load libraries
import sys
import os
import json
import csv

#%% Get console arguments
input_folder_path = sys.argv[1]
output_file_path = sys.argv[2]

#%% Create target CSV file
output_file = open(
    file = output_file_path,
    mode = "wt",
    newline = "")

#%% Create a csv writer
csv_writer = csv.writer(output_file)

#%% Write header to file
csv_writer.writerow(["Date", "Latitude", "Longitude", "Time Zone", "Offset", "Humidity", "Temperature Low", "Temperature High"])

#%% Get list of files in source folder
input_files = os.listdir(input_folder_path)

#%% Process each source file
for input_file_name in input_files:

    # Create source file path
    source_file_path = os.path.join(
        input_folder_path, 
        input_file_name)
    
    # Open the source file
    source_file = open(source_file_path)
    
    # Load the JSON data
    json_data = json.load(source_file)
    
    # Close the source file
    source_file.close()
    
    # Get fields from JSON data
    date = input_file_name.replace(".json", "")
    latitude = json_data["latitude"]
    longitude = json_data["longitude"]
    time_zone = json_data["timezone"]
    offset = json_data["offset"]
    
    # Get daily data from JSON data
    daily_data = json_data["daily"]["data"][0]
    
    # Get fields from daily data
    humidity = daily_data["humidity"]
    temperature_low = daily_data["temperatureLow"]
    temperature_high = daily_data["temperatureHigh"]
    
    # Write CSV data to target file
    csv_writer.writerow([date, latitude, longitude, time_zone, offset, humidity, temperature_low, temperature_high])

#%% Close the target file
output_file.close()