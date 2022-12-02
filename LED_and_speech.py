#CS 416 AI & Robotics
#George Medairy 
#Ashle Samczynski 
#Final Project 


import sys, event, time
import mbot2
import mbuild
import cyberpi

@event.start
def on_start():
    #print program name 
    cyberpi.console.println("Light & Speech Program\n")
    time.sleep(3)
    
    #print instructions for use
    cyberpi.led.on('g', id = "all")
    cyberpi.console.println("Press center of joystick to select an emotion!")
    time.sleep(2)
    cyberpi.console.println("Press A or Home to stop.")
    cyberpi.console.println("Use joystick to navigate up and down")
    time.sleep(2)
    cyberpi.console.clear()
    cyberpi.console.println("happy")
    
while not cyberpi.controller.is_press('b'):
    pass

emotions = ["happy", "sad"]
index = 0


emotion = ''

if emotion == 'happy':
    cyberpi.led.on('yellow', id = "all")
    cyberpi.audio.play('SPEAKER.happy')
    cyberpi.console.println("I laugh. Therefore, I am happy.")
elif emotion == 'sad':
    cyberpi.led.on('blue', id = "all")
    cyberpi.audio.play('SPEAKER.sad')
    cyberpi.console.println("I am so very sad.")

def get_index(index1, emotions1):
    if index1 == 0:
        index1 = len(emotions1) - 1
    else:
        index1 = index1 - 1
    return (index1)

#how to exit the program
@event.is_press('a')
def is_a_btn_press():
    cyberpi.restart()

@cyberpi.event.is_press('up')
def is_up_btn_press(index2, emotions2):
    index3 = get_index(index2, emotions2)
    cyberpi.console.println(emotions2[index3])


@cyberpi.event.is_press('middle')
def is_mid_btn_press(index4):
    cyberpi.console.clear()
    cyberpi.console.println(emotions[index4] + "was selected.")
    emotion = emotions[index4]
    
    
