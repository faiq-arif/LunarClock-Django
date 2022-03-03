from django.shortcuts import render
from django.http import HttpResponse
from datetime import *
from hijri_converter import convert
import time
import math
import pylunar

mi = pylunar.MoonInfo((-7, 33, 0), (110, 45, 0)) #Set Location to Assalaam Observatory    
tz = 7
runLoop = 1

def updateTime():
    cur_date = datetime.utcnow()
    day = cur_date.day
    month = cur_date.month
    year = cur_date.year
    hour = cur_date.hour
    minute = cur_date.minute
    second = cur_date.second
    mi.update((year, month, day, hour, minute, second))

def dayname(request):
    now1 = datetime.now()
    gdn = now1.strftime("%A")
    return HttpResponse(gdn)

def hDate(request):
    hijri = convert.Gregorian.today().to_hijri()
    #hdn = hijri.day_name()
    hd = hijri.day
    hm = hijri.month_name()
    hy = hijri.year
    hijriDate = hd," ",hm," ",hy
    return HttpResponse(hijriDate)

def gDate(request):
    now2 = datetime.now()
    #gdn = now.strftime("%A")
    gd = now2.day
    gm = now2.strftime("%B")
    gy = now2.year
    greDate = gd," ",gm," ",gy
    return HttpResponse(greDate)

def getAlt(request):
    updateTime()
    altitude = round(mi.altitude(), 2)
    return HttpResponse(altitude)        

def getAz(request):
    updateTime()
    azimuth = round(mi.azimuth(), 2)
    return HttpResponse(azimuth)

def getElong(request):
    updateTime()    
    elong = round(mi.elongation(), 2)
    return HttpResponse(elong)

def getPhase(request):
    updateTime()
    phase = mi.phase_name()
    if phase == "NEW_MOON":
        view = "New"
    
    if phase == "WAXING_CRESCENT":
        view = "Waxing Crescent"
            
    if phase == "FIRST_QUARTER":
        view = "First Quarter"
            
    if phase == "WAXING_GIBBOUS":
        view = "Waxing Gibbous"
                
    if phase == "FULL_MOON":
        view = "Full"
            
    if phase == "WANING_GIBBOUS":
        view = "Waning Gibbous"
            
    if phase == "THIRD_QUARTER":
        view = "Third Quarter"
            
    if phase == "WANING_CRESCENT":
        view = "Waning Crescent"
    return HttpResponse(view)

def getImage(request):
    updateTime()
    phase = mi.phase_name()
    if phase == "NEW_MOON":
        numview = 1

    if phase == "WAXING_CRESCENT":
        numview = 2
            
    if phase == "FIRST_QUARTER":
        numview = 3
            
    if phase == "WAXING_GIBBOUS":
        numview = 4
                
    if phase == "FULL_MOON":
        numview = 5
            
    if phase == "WANING_GIBBOUS":
        numview = 6
            
    if phase == "THIRD_QUARTER":
        numview = 7
            
    if phase == "WANING_CRESCENT":
        numview = 8
    return HttpResponse(numview)        



def index(request):
    """
    lunar_phase = {
    'moonphase' : getPhase(),
    'altitude' : getAlt(),
    'azimuth' : getAz(),
    'fphase' : getfphase(),
    }

    context = {'lunar_phase' : lunar_phase}
    """
    return render(request, 'lunarphase/index.html', {})
#time.sleep(100)    
# Create your views here.

