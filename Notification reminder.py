import time
from plyer import notification
from playsound import playsound

class Notification:
    def __init__(self,filename,song):
        self.filename=filename
        self.song=song
    
    #reading the text form the file
    def Read(self):
        file=open(self.filename,'r')
        text=(file.read())
        return text
    
    def Notify(self):
        #calling the Read function
        txt=self.Read()
        #calling the playsound module to play our sound
        playsound(self.song)
        #we called the plyer module in which an notification will be generated 
        notification.notify(
            title='Your work reminder which you saved in file!!!!',
            message=txt,
            #time to display our message
            timeout=2
            )
        #helps to show message again
        time.sleep(6)


#-----DriverCode------

def Test(filename,song):
    n=Notification(filename,song)
    n.Notify()


