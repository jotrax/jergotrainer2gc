# -*- coding: utf-8 -*-

import os
import json

from datetime import datetime

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
        

def write_ride_file(ride_data_points):
    filename = "filename" + ".csv"
    
    fh = open(filename,"w")
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
    
    



# TODO: for all csv files with jergotrainer format do....
def  scan_and_convert_directoy (dir_path):
    pass

