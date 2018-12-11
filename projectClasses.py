import numpy as np
 
class RegSeason:
    def __init__(self,state,i,monthDate):
        self.state= state
        self.i= i
        self.monthDate= monthDate

    def regions(state,i):##input state and i 
        #West Regions 
        if state== "NV" or state=="ID" or state=="AZ" or state=="CO" or state== "NM" or state== "UT" or state=="WY" or state=="MT":
            region = "West"
        elif state== "CA" or state=="OR" or state=="HI" or state=="AK" or state=="WA":
            region = "West"

        #South East
        elif state=="DE" or state=="FL" or state=="GA" or state=="MD" or state=="NC" or state== "SC" or state=="VA" or state=="DC" or state=="WV":
            region= "Southeast"
        elif state=="AL" or state=="KY" or state=="MS" or state=="TN":
            region= "Southeast"
        elif state=="AR" or state=="LA":
            region= "Southeast"
        
        #SouthWest region
        elif state=="AZ" or state=="CO" or state=="OK" or state=="TX":
            region= 'Southwest'

        #Midwest regions 
        elif state=="WI" or state=="MI" or state=="IL" or state=="IN" or state=="OH":
            region= "Midwest"
        elif state=="ND" or state=="SD" or state=="MN" or state=="IA" or state=="MO" or state=="NE" or state=="KS":
            region= "Midwest"

        #Northwest regions
        elif state=="VT" or state=="NH" or state=="ME" or state=="MA" or state=="CT" or state=="RI":
            region= "Northeast"
        elif state=="NY" or state=="PA" or state=="NJ":
            region= "Northeast"
        else:
            region=''
        return region
    
    def seasons(monthDate):
        month= int(monthDate[5:7])
        date= int(monthDate[8:10])
        #Winter
        if month== 1 or month== 2 or (month== 3 and date<= 19) or(month==12 and date>= 21):
            season= 'Winter'
               
        #Spring
        elif month== 4 or month== 5 or (month== 6 and date<= 20) or (month==3 and date>= 20):
            season= 'Spring'

        #Summer                                                         
        elif month== 7 or month== 8 or (month== 9 and date<= 21) or (month==6 and date>=21):
            season= 'Summer'
                  
        #Fall
        elif month== 10 or month== 11 or (month== 12 and date<= 20) or (month==9 and date>=22):
            season= 'Fall'
              
        else:
            print('Fix Season',x,'<'*8)
            season= 'Fix'
        return season 