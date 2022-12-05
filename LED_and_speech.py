#CS 416 AI & Robotics
#George Medairy 
#Ashle Samczynski 
#Final Project 


import sys, event, time
import mbot2
import mbuild
import cyberpi

class Index:
    index = 0
    def get_index(self):
        return self.index
    def set_index(self,num):
        self.index = num

class Happy:
    selected = 0
    index = 0
    name = "happy"
    def get_selected(self):
        return self.selected
    def set_selected(self,num):
        self.selected = num
    def get_index(self):
        return self.index
    def get_name(self):
        return self.name

class Sad:
    selected = 0
    index = 1
    name = "sad"
    def get_selected(self):
        return self.selected
    def set_selected(self,num):
        self.selected = num
    def get_index(self):
        return self.index
    def get_name(self):
        return self.name

class Angry:
    selected = 0
    index = 2
    name = "angry"
    def get_selected(self):
        return self.selected
    def set_selected(self,num):
        self.selected = num
    def get_index(self):
        return self.index
    def get_name(self):
        return self.name

class Sleepy:
    selected = 0
    index = 3
    name = "sleepy"
    def get_selected(self):
        return self.selected
    def set_selected(self,num):
        self.selected = num
    def get_index(self):
        return self.index
    def get_name(self):
        return self.name

class Total_Emotions_Selected:
    total = 0
    def get_total(self):
        return self.total
    def set_total(self,num):
        self.total = num

@event.start
def on_start():
    #print program name 
    cyberpi.console.println("Light & Speech Program\n")
    time.sleep(3)
    
    #print instructions for use
    cyberpi.led.on('g', id = "all")
    cyberpi.console.println("\nPress A or Home to stop.\n")
    cyberpi.console.println("Use joystick to navigate up and down")
    time.sleep(4)
    cyberpi.console.println("\n\nPress center of joystick to select an emotion!")
    time.sleep(5)
    cyberpi.console.clear()
    cyberpi.console.println("happy")
    


emotions = ["happy", "sad", "angry", "sleepy"]
index = Index()
tes = Total_Emotions_Selected()
happy = Happy()
sad = Sad()
angry = Angry()
sleepy = Sleepy()

def emotion_action(emotion):
    cyberpi.console.clear()
    cyberpi.audio.set_vol(90)
    if emotion == 'happy':
        cyberpi.led.play(name = "rainbow")
        cyberpi.audio.play("laugh")
        cyberpi.console.println("I laugh. Therefore, I am happy.")
        time.sleep(3)
        cyberpi.led.on('g', id = "all")
    elif emotion == 'sad':
        cyberpi.led.on('blue', id = "all")
        cyberpi.audio.play("sad")
        cyberpi.console.println("I am so very sad.")
        time.sleep(3)
        cyberpi.led.on('g', id = "all")
    elif emotion == 'angry':
        cyberpi.led.play(name = "flash_red")
        cyberpi.audio.play("angry")
        cyberpi.console.println("I am extremely angry!!")
        cyberpi.led.on('r', id = "all")
        time.sleep(3)
        cyberpi.led.on('g', id = "all")
    elif emotion == 'sleepy':
        cyberpi.led.on(112,56,189)
        cyberpi.audio.play("sleepy")
        cyberpi.console.println("Yawn! I am sleepy.")
        time.sleep(3)
        cyberpi.led.on('g', id = "all")
    cyberpi.console.clear()
    cyberpi.console.println("Use joystick to navigate up and down")

def index_up():
    if index.get_index() == 0:
        index.set_index(len(emotions) - 1)
    else:
        index.set_index(index.get_index() - 1)
    

def index_down():
    if index.get_index() == len(emotions) - 1:
        index.set_index(0)
    else:
        index.set_index(index.get_index() + 1)

def increment_total():
    tes.set_total(tes.get_total() + 1)

def increment_emotion():
    emotion_class = find_emotion_class()
    emotion_class.set_selected(emotion_class.get_selected() + 1)
    

def find_emotion_class():
    emotion_class = happy
    if index.get_index() == happy.get_index():
        pass
    elif index.get_index() == sad.get_index():
        emotion_class = sad
    elif index.get_index() == angry.get_index():
        emotion_class = angry
    elif index.get_index() == sleepy.get_index():
        emotion_class = sleepy
    return emotion_class

def percent_selected():
    emotion_class = find_emotion_class()
    percentage = -1
    if emotion_class.get_selected() > 0:
        ratio = (emotion_class.get_selected() / tes.get_total())
        percentage = ratio * 100
    else:
        percentage = 0
    return(percentage)

#how to exit the program
@event.is_press('a')
def is_a_btn_press():
    cyberpi.console.println("Goodbye.")
    time.sleep(3)
    cyberpi.restart()

@cyberpi.event.is_press('up')
def is_up_btn_press():
    index_up()
    cyberpi.console.clear()
    cyberpi.console.println(emotions[index.get_index()])

@cyberpi.event.is_press('down')
def is_down_btn_press():
    index_down()
    cyberpi.console.clear()
    cyberpi.console.println(emotions[index.get_index()])


@cyberpi.event.is_press('middle')
def is_mid_btn_press():
    cyberpi.console.clear()
    cyberpi.console.println("\n" + emotions[index.get_index()] + " was selected.\n")
    increment_emotion()
    increment_total()
    cyberpi.console.println(str(emotions[index.get_index()]) + 
                            str(' has been selected\n') +
                            str(percent_selected()) +
                            str(' percent of this run.\n'))
    time.sleep(3)
    emotion_action(emotions[index.get_index()])
    
    
