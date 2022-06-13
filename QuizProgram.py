import random
from tkinter import *
import tkinter
from tkinter.font import Font
questionList = [["Astrology is a pseudoscience.","True","False"],["Why does the moon have a bigger effect on the tides than the sun?","It is closer to Earth","It is bigger","It is smaller","It is further away from Earth"],["What is a solar eclipse?","When the sun is behind the moon","When Earth is in between the moon and sun","When the moon is behind the sun","when the sun is below Earth"],["What is a lunar eclipse?","When Earth is in between the moon and sun","When the sun is behind the moon","When the moon is behind the sun","When the sun is below Earth"],["How long does it take for the moon to complete 1 revolution around the Earth?","29.5 Days","30 Days","24 Hours","28 Days"],["How many km is 1 Astronomical Unit (A.U.)?","150,000,000 km","150,000 km","100,000,000 km","100,000 km"],["When the moon phase is waning it means it is getting bigger.","False","True"],["The New Moon is a moon phase where the moon is completely dark.","True","False"],["The moon produces its own light.","False","True"],["How many high tides are there on average per 24 hour day?","2","1","3","4"],["The area of partial shadow of the Earth is called?","Penumbra","Umbra","Terrumbra","Sombra"],["The area of complete shadow of the Earth is called?","Umbra","Penumbra","Terrumbra","Sombra"],["What causes the Earth's seasons?","The Earth’s tilt","The distance from the sun to the Earth","The Earth’s speed around the sun","he Earth’s distance from the moon"],["Astronomy is a pseudoscience.","False","True"],["How many phases of the moon are there?","8","6","10","12"],["The term ‘Gibbous’ is used to describe the moon when it is…","Almost full","Half full","Full","Almost empty"],["The sun’s core fuses Hydrogen into _____ when releasing energy.","Helium","Nitrogen","Oxygen","Neon"],["How many astronomical units away is the sun from the Earth?","1","2","5","8"],["How many planets do we have in our solar system?","8","6","7","9"],["Pluto is not a planet.","True","False"]]
messageList = ["UNLUCKY!","GOOD EFFORT!","NICE JOB!","INCREDIBLE!"]
gradeList = ["NOT ACHIEVED","ACHIEVED","MERIT","EXCELLENCE"]
scoreRequire = [0, 4, 7, 10, 12]
global score
score = 0
questionList = random.sample(questionList, len(questionList))


def answerPhase():
    root.destroy()
    

def titleScreen():
    global root
    root = Tk()
    root.title("Year 10 Astronomy Quiz")
    root.config(bg="#ffd3a6")
    root.geometry("660x555")
    global pageFont
    pageFont = Font(family = "Gill Sans MT",weight="bold",size=18)

    title = Label(root, text="YEAR 10 SCIENCE QUIZ", font=pageFont, bg="#fd5050", fg="#FFFFFF",padx=5,pady=50)
    title.place(x=173,y=50)
    
    #Image here

    playButton = Button(root, text="PLAY", font=pageFont, bg="#fd5050", fg="#FFFFFF", command=answerPhase, borderwidth=1, padx=40, pady=10)
    playButton.place(x=100, y=400)
    exitButton = Button(root, text="EXIT", font=pageFont, bg="#fd5050", fg="#FFFFFF", command=exit, borderwidth=1, padx=40, pady=10)
    exitButton.place(x=400, y=400)

    


    root.mainloop()





titleScreen()