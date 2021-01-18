# -*- coding: utf-8 -*-

import os
import csv
import sys
import datetime


CSV_DELIMITER = ","
CSV_HEADLINE = "secs,cad,hr,km,kph,nm,watts,alt,lon,lat,headwind,slope,temp,interval,lrbalance,lte,rte,lps,rps,smo2,thb,o2hb,hhb\n"


class ride_data_point:
    def __init__ (self):
        self.secs = ''
        self.cad = ''
        self.hr = ''
        self.km = ''
        self.kph = ''
        self.nm = ''
        self.watts = ''
        self.alt = ''
        self.lon = ''
        self.lat = ''
        self.headwind = ''
        self.slope = ''
        self.temp = ''
        self.interval = ''
        self.lrbalance = ''
        self.lte = ''
        self.rte = ''
        self.lps = ''
        self.rps = ''
        self.smo2 = ''
        self.thb = ''
        self.o2hb = ''
        self.hhb = ''
        
        

def write_ride_file(ride_data_points, target_file):
    
    fh = open(target_file,"w")
    fh.write(CSV_HEADLINE)
    
    csvLine = ""
    
    for point in ride_data_points:
        csvLine = str(point.secs) + CSV_DELIMITER
        csvLine += str(point.cad) + CSV_DELIMITER
        csvLine += str(point.hr) + CSV_DELIMITER
        csvLine += str(point.km) + CSV_DELIMITER
        csvLine += str(point.kph) + CSV_DELIMITER
        csvLine += str(point.nm) + CSV_DELIMITER
        csvLine += str(point.watts) + CSV_DELIMITER
        csvLine += str(point.alt) + CSV_DELIMITER
        csvLine += str(point.lon) + CSV_DELIMITER
        csvLine += str(point.lat) + CSV_DELIMITER
        csvLine += str(point.headwind) + CSV_DELIMITER
        csvLine += str(point.slope) + CSV_DELIMITER
        csvLine += str(point.temp) + CSV_DELIMITER
        csvLine += str(point.interval) + CSV_DELIMITER
        csvLine += str(point.lrbalance) + CSV_DELIMITER
        csvLine += str(point.lte) + CSV_DELIMITER
        csvLine += str(point.rte) + CSV_DELIMITER
        csvLine += str(point.lps) + CSV_DELIMITER
        csvLine += str(point.rps) + CSV_DELIMITER
        csvLine += str(point.smo2) + CSV_DELIMITER
        csvLine += str(point.thb) + CSV_DELIMITER
        csvLine += str(point.o2hb) + CSV_DELIMITER
        csvLine += str(point.hhb) + CSV_DELIMITER
        csvLine += "\n"

        fh.write (csvLine)

    fh.close()
    
    
    
def read_jergotrainer_file(filepath):
    
    jergoridedata = []
    
    with open(filepath, newline='') as csvfile:
        jergotrainer_file = csv.reader(csvfile, delimiter=';', quotechar='|')
        
        armed = False
        
        for row in jergotrainer_file:
            if (not armed) and (row[0] == '[Data]'):
                armed = True
            elif armed:
                new_point = ride_data_point()
                new_point.secs = row[4]
                new_point.watts = row[5]
                new_point.hr = row[6]
                new_point.cad = row[7]
                new_point.kph = row[8]
                new_point.km = row[9]

                jergoridedata.append(new_point)
                
    return jergoridedata



# for all csv files with jergotrainer format do....
def scan_and_convert_directoy (dir_path):

    directory = os.path.join(dir_path)
    for root,dirs,files in os.walk(directory):
        for file in files:
           if file.endswith(".csv"):
               
               try:
                   date_time_obj = datetime.datetime.strptime(file, 'P_%Y%m%d_%H%M%S.csv')
                   gc_file_name = date_time_obj.strftime("%Y_%m_%d_%H_%M_%S.csv")
    
                   print(file + " -> " + gc_file_name)
                   
                   ride_data = read_jergotrainer_file(os.path.join(dir_path, file))
                   write_ride_file (ride_data, os.path.join(dir_path, gc_file_name))
               except BaseException as e:
                   print('File ' + str(file) + ' not suitable to convert! \n   ' + str(e))



if len(sys.argv) == 2:
    scan_and_convert_directoy (str(sys.argv[1]))
else:
    scan_and_convert_directoy (os.getcwd())
    
