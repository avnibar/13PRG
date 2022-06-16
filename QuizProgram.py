import random
from socket import getprotobyname
from tkinter import *
from tkinter.font import Font
questionList = [["Astrology is a pseudoscience.","True","False"],["Why does the moon have a bigger effect on the tides than the sun?","It is closer to Earth","It is bigger","It is smaller","It is further away from Earth"],["What is a solar eclipse?","When the sun is behind the moon","When Earth is in between the moon and sun","When the moon is behind the sun","When the sun is below Earth"],["What is a lunar eclipse?","When Earth is in between the moon and sun","When the sun is behind the moon","When the moon is behind the sun","When the sun is below Earth"],["How long does it take for the moon to complete 1 revolution around the Earth?","29.5 Days","30 Days","24 Hours","28 Days"],["How many km is 1 Astronomical Unit (A.U.)?","150,000,000 km","150,000 km","100,000,000 km","100,000 km"],["When the moon phase is waning it means it is getting bigger.","False","True"],["The New Moon is a moon phase where the moon is completely dark.","True","False"],["The moon produces its own light.","False","True"],["How many high tides are there on average per 24 hour day?","2","1","3","4"],["The area of partial shadow of the Earth is called?","Penumbra","Umbra","Terrumbra","Sombra"],["The area of complete shadow of the Earth is called?","Umbra","Penumbra","Terrumbra","Sombra"],["What causes the Earth's seasons?","The Earth’s tilt","The distance from the sun to the Earth","The Earth’s speed around the sun","The Earth’s distance from the moon"],["Astronomy is a pseudoscience.","False","True"],["How many phases of the moon are there?","8","6","10","12"],["The term ‘Gibbous’ is used to describe the moon when it is…","Almost full","Half full","Full","Almost empty"],["The sun’s core fuses Hydrogen into _____ when releasing energy.","Helium","Nitrogen","Oxygen","Neon"],["How many astronomical units away is the sun from the Earth?","1","2","5","8"],["How many planets do we have in our solar system?","8","6","7","9"],["Pluto is not a planet.","True","False"]]
messageList = ["UNLUCKY!","GOOD EFFORT!","NICE JOB!","INCREDIBLE!"]
gradeList = ["NOT ACHIEVED","ACHIEVED","MERIT","EXCELLENCE"]
scoreRequire = [0, 4, 7, 10, 12]
global score
score = 0
questionList = random.sample(questionList, len(questionList))

def calcGrade():
    
    if score >= scoreRequire[0] and score < scoreRequire[1]:
        message = messageList[0]
        finalGrade = gradeList[0]
    elif score >= scoreRequire[1] and score < scoreRequire[2]:
        message = messageList[1]
        finalGrade = gradeList[1]
    elif score >= scoreRequire[2] and score < scoreRequire[3]:
        message = messageList[2]
        finalGrade = gradeList[2]
    elif score >= scoreRequire[3] and score <= scoreRequire[4]:
        message = messageList[3]
        finalGrade = gradeList[3]
    
    global groot
    groot = Tk()
    groot.config(bg="#ffd3a6")
    groot.geometry("500x555")
    groot.title("Final Grade")
    pageFont = Font(family = "Gill Sans MT",weight="bold",size=18)
    
    title = Label(groot, text="YEAR 10 SCIENCE QUIZ", font=pageFont, bg="#fd5050", fg="#FFFFFF",padx=5,pady=50)
    title.place(x=250,y=80, anchor="center")
    messageBox = Label(groot, text="YOUR SCORE: "+str(score)+"/12\nYOUR GRADE: "+str(finalGrade)+"\n\n"+str(message), font=pageFont, bg="#fd5050", fg="#FFFFFF",padx=5,pady=50)
    messageBox.place(x=250,y=300, anchor="center")

def answerPhase():
    root.destroy()
    
    global questionLCV
    questionLCV = 0
    global skipCounter
    skipCounter = 0
    global totalQuestions
    totalQuestions = 12
    global answerOne
    global answerTwo
    global answerThree
    global answerFour
    global skipButton

    while questionLCV < totalQuestions:
        global qroot
        qroot = Tk()
        qroot.config(bg="#ffd3a6")
        qroot.geometry("1000x720")
        qroot.title("Question "+str(questionLCV+1-skipCounter))
        pageFont = Font(family = "Gill Sans MT",weight="bold",size=18)

        qNumber = Label(qroot, text="QUESTION "+str(questionLCV+1-skipCounter)+".", font=pageFont, fg="white", bg="#fd5050",padx=20,pady=20)
        qNumber.place(x=15,y=15)

        questionText = Label(qroot, text=questionList[questionLCV][0], font=pageFont, fg="white", bg="#fd5050", padx=20, pady=20)
        questionText.place(x=500, y=175, anchor="center")

        if skipCounter < 3:
            skipButton = Button(qroot, text="SKIP", font=pageFont, bg="#fd5050", fg="white", borderwidth=1, padx=40, pady=10, command=skipQuestion)
            skipButton.place(x=815, y=620)
        
        exitButton = Button(qroot, text="EXIT", font=pageFont, bg="#fd5050", fg="#FFFFFF", command=exit, borderwidth=1, padx=40, pady=10)
        exitButton.place(x=30, y=620)
        
        global temp
        temp = []
        temp.append(questionList[questionLCV][1])
        temp.append(questionList[questionLCV][2])
        
        if len(questionList[questionLCV]) == 5:
            temp.append(questionList[questionLCV][3])
            temp.append(questionList[questionLCV][4])
            temp = random.sample(temp, len(temp))
            loop = 0
            while loop <= (len(temp) - 1):
                if len(temp[loop]) > 30:
                    pageFontAlt = Font(family = "Gill Sans MT",weight="bold",size=12)
                    loop = loop + 10
                else:
                    pageFontAlt = Font(family = "Gill Sans MT",weight="bold",size=18)
                loop += 1

            answerOne = Button(qroot, text=temp[0],font=pageFontAlt, bg="#fd5050", fg="white", borderwidth=1, padx=40, pady=10, command=lambda:answerClick(0))
            answerOne.place(x=305, y=350, anchor="center")

            answerTwo = Button(qroot, text=temp[1],font=pageFontAlt, bg="#fd5050", fg="white", borderwidth=1, padx=40, pady=10, command=lambda:answerClick(1))
            answerTwo.place(x=690, y=350, anchor="center")

            answerThree = Button(qroot, text=temp[2],font=pageFontAlt, bg="#fd5050", fg="white", borderwidth=1, padx=40, pady=10, command=lambda:answerClick(2))
            answerThree.place(x=305, y=450, anchor="center")

            answerFour = Button(qroot, text=temp[3],font=pageFontAlt, bg="#fd5050", fg="white", borderwidth=1, padx=40, pady=10, command=lambda:answerClick(3))
            answerFour.place(x=690, y=450, anchor="center")
        else:
            temp = random.sample(temp, len(temp))

            answerOne = Button(qroot, text=temp[0],font=pageFont, bg="#fd5050", fg="white", borderwidth=1, padx=40, pady=10, command=lambda:answerClick(0))
            answerOne.place(x=315, y=400, anchor="center")

            answerTwo = Button(qroot, text=temp[1],font=pageFont, bg="#fd5050", fg="white", borderwidth=1, padx=40, pady=10, command=lambda:answerClick(1))
            answerTwo.place(x=675, y=400, anchor="center")

        qroot.mainloop()
        questionLCV += 1
    calcGrade()

def skipQuestion():
    global skipCounter
    skipCounter += 1
    global totalQuestions
    totalQuestions += 1
    qroot.destroy()

def answerClick(ansNum):
    pageFontAltTwo = Font(family = "Gill Sans MT",weight="bold",size=20)
    pageFont = Font(family = "Gill Sans MT",weight="bold",size=18)
    if temp[ansNum] == questionList[questionLCV][1]:
        confirmation = Label(qroot, text="CORRECT",font=pageFontAltTwo, bg="#fd5050", fg="white", padx=20, pady=20)
        confirmation.place(x=500, y=400, anchor="center")

        global score
        score += 1
    else:
        confirmation = Label(qroot, text="INCORRECT",font=pageFontAltTwo, bg="#fd5050", fg="white", padx=20, pady=20)
        confirmation.place(x=500, y=400, anchor="center")
    
    answerOne.destroy()
    answerTwo.destroy()

    if len(questionList[questionLCV]) == 5:
        answerThree.destroy()
        answerFour.destroy()
    
    if skipCounter < 3:
        skipButton.destroy()

    nextButton = Button(qroot, text="NEXT", font=pageFont, bg="#fd5050", fg="white", borderwidth=1, padx=32, pady=10, command=next)
    nextButton.place(x=815, y=620)

def next():
    qroot.destroy()

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