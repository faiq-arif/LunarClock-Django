from datetime import *
import time
import math
import pylunar

mi = pylunar.MoonInfo((-7, 33, 0), (110, 45, 0)) #Set Location to Assalaam Observatory    
tz = 7

cur_date = datetime.now()
day = cur_date.day
month = cur_date.month
year = cur_date.year
hour = cur_date.hour - tz #Jam sekarang dikurangi zona waktu
mi.update((year, month, day, hour, 0, 0))
phase = mi.fractional_phase()
age = mi.age()
altitude = mi.altitude()
azimuth = mi.azimuth()
elongation = mi.elongation()
magnitude = mi.magnitude()
fromNewMoon = mi.time_from_new_moon()
toFullMoon = mi.time_to_full_moon()
toNewMoon = mi.time_to_new_moon()
print("The current date is %s-%s" % (month, day))

if phase == 0:
    view = "New"
    
if phase > 0 and phase < 8:
    view = "waxing crescent"
    
if phase == 8:
    view = "first quarter"
    
if phase > 8 and phase < 15:
    view = "waxing gibbous"
        
if phase == 16:
    view = "full"
    
if phase > 16 and phase < 23:
    view = "waning gibbous"
    
if phase == 24:
    view = "third quarter"
    
if phase > 24:
    view = "waning crescent"
    
print("The moon is %s." % view)
print(phase) #per 1
print(age) #days
print(altitude) #all in degrees
print(azimuth)
print(elongation) 
print(magnitude)
print(fromNewMoon) #hours
print(toFullMoon) #day
print(toNewMoon) #hours