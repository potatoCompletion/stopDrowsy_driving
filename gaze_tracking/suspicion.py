import time

class Stactic(object):
    count=0
    flag=0
class Suspicion(Stactic):
    """
    This class detect the one's state by using time and Blinking information
    """
    
    def suspicion_of_sleepiness(self,text,start):
        self.text=text
        self.start=start
        if self.text == "Blinking" and time.time()-self.start>4:
            Stactic.count+=1
            if Stactic.count>10:
                Stactic.count=0
                Stactic.flag+=1
                return True
        else:
            return False
    
    def sleepy_state(self,text,start):
        if self.suspicion_of_sleepiness(text,start) or Stactic.flag >3:
            return True
        else:
            return False


    
    



