class Clock:
   def __init__(self, hour, minute):  
        time=hour*60+minute
        self.minute = time % 60
        self.hour = (time//60)%24
        

   def __repr__(self):
        return "%02d:%02d"%(self.hour,self.minute)

   def __eq__(self, time):
        return self.hour == time.hour and self.minute == time.minute

   def __add__(self, minute):
        return Clock(self.hour, self.minute+minute)

   def __sub__(self, minutes):
        return Clock(self.hour, self.minute-minute)
