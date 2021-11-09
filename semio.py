from tkinter import *
import tkinter.font as font

def startGame(a):
    newWindow = Toplevel(root)
    newWindow.title("Semio")
    newWindow.geometry("1000x1000")
    canvas = Canvas(newWindow, width=1000, height=800, bg = "white")
    canvas.pack()

    label = Label(canvas, bg = "AntiqueWhite2",fg = "gray13", text = "SEMIOOOOO",borderwidth = 0, relief = "solid",anchor = 'w', padx = 350)
    label.place(x = 0, y = 0, width =1000, height = 75)
    label["font"] = labelFont

    gammaBox1 = canvas.create_rectangle(0, 75, 250, 125, fill = "sky blue")
    gammaBox2 = canvas.create_rectangle(250, 75, 500, 125, fill = "sky blue")
    gammaBox3 = canvas.create_rectangle(500, 75, 750, 125, fill = "salmon")
    gammaBox4 = canvas.create_rectangle(750, 75, 1000, 125, fill = "salmon")

    scoreBox1 = canvas.create_rectangle(0, 125, 500, 275, fill = "DodgerBlue2")
    scoreBox2 = canvas.create_rectangle(500, 125, 1000, 275, fill = "tomato")

    hitTitleBox = canvas.create_rectangle(0, 275, 20, 400, fill = "White")
    hitsTitle = canvas.create_text(11, 335, text = "H", font = newFont)
    hitBox1 = canvas.create_rectangle(20, 275, 250, 400, fill = "sky blue")
    hitBox2 = canvas.create_rectangle(250, 275, 500, 400, fill = "sky blue")
    hitBox3 = canvas.create_rectangle(500, 275, 750, 400, fill = "salmon")
    hitBox4 = canvas.create_rectangle(750, 275, 1000, 400, fill = "salmon")

    aceTitleBox = canvas.create_rectangle(0, 400, 20, 475, fill = "White")
    aceTitle = canvas.create_text(11, 437, text = "A", font = newFont)
    aceBox1 = canvas.create_rectangle(20, 400, 250, 475, fill = "sky blue")
    aceBox2 = canvas.create_rectangle(250, 400, 500, 475, fill = "sky blue")
    aceBox3 = canvas.create_rectangle(500, 400, 750, 475, fill = "salmon")
    aceBox4 = canvas.create_rectangle(750, 400, 1000, 475, fill = "salmon")

    errorTitleBox = canvas.create_rectangle(0, 475, 20, 550, fill = "White")
    errorTitle = canvas.create_text(11, 512, text = "E", font = newFont)
    errorBox1 = canvas.create_rectangle(20, 475, 250, 550, fill = "sky blue")
    errorBox2 = canvas.create_rectangle(250, 475, 500, 550, fill = "sky blue")
    errorBox3 = canvas.create_rectangle(500, 475, 750, 550, fill = "salmon")
    errorBox4 = canvas.create_rectangle(750, 475, 1000, 550, fill = "salmon")

    socialTitleBox = canvas.create_rectangle(0, 550, 20, 625, fill = "White")
    socialTitle = canvas.create_text(11, 587, text = "So", font = newFont)
    socialBox1 = canvas.create_rectangle(20, 550, 250, 625, fill = "sky blue")
    socialBox2 = canvas.create_rectangle(250, 550, 500, 625, fill = "sky blue")
    socialBox3 = canvas.create_rectangle(500, 550, 750, 625, fill = "salmon")
    socialBox4 = canvas.create_rectangle(750, 550, 1000, 625, fill = "salmon")

    sinkTitleBox = canvas.create_rectangle(0, 625, 20, 700, fill = "White")
    sinkTitle = canvas.create_text(11, 662, text = "Si", font = newFont)
    sinkBox1 = canvas.create_rectangle(20, 625, 250, 700, fill = "sky blue")
    sinkBox2 = canvas.create_rectangle(250, 625, 500, 700, fill = "sky blue")
    sinkBox3 = canvas.create_rectangle(500, 625, 750, 700, fill = "salmon")
    sinkBox4 = canvas.create_rectangle(750, 625, 1000, 700, fill = "salmon")

    nTitleBox = canvas.create_rectangle(0, 700, 20, 775, fill = "White")
    nTitle = canvas.create_text(11, 737, text = "N", font = newFont)
    nBox1 = canvas.create_rectangle(20, 700, 250, 775, fill = "sky blue")
    nBox2 = canvas.create_rectangle(250, 700, 500, 775, fill = "sky blue")
    nBox3 = canvas.create_rectangle(500, 700, 750, 775, fill = "salmon")
    nBox4 = canvas.create_rectangle(750, 700, 1000, 775, fill = "salmon")

    player1 = str(player1box.get())
    player2 = str(player2box.get())
    player3 = str(player3box.get())
    player4 = str(player4box.get())

    player1g = Label(canvas, bg = "sky blue", fg = "gray12", text = player1, font = titleFont)
    player1g.place(x = 35, y = 80, width = 200, height = 40)
    player2g = Label(canvas, bg = "sky blue", fg = "gray12", text = player2, font = titleFont)
    player2g.place(x = 285, y = 80, width = 200, height = 40)
    player3g = Label(canvas, bg = "salmon", fg = "gray12", text = player3, font = titleFont)
    player3g.place(x = 535, y = 80, width = 200, height = 40)
    player4g = Label(canvas, bg = "salmon", fg = "gray12", text = player4, font = titleFont)
    player4g.place(x = 785, y = 80, width = 200, height = 40)

    instructions = Label(canvas, bg = "gold", fg = "gray12", text = "Hit letter in top right to add", font = newFont, anchor = 'w')
    instructions.place(x = 785, y = 30, width = 200, height = 20)
    instructions1 = Label(canvas, bg = "gold", fg = "gray12", text = "Hit letter jakfba to undo", font = newFont, anchor = 'w')
    instructions1.place(x = 785, y = 50, width = 200, height = 20)
    
root = Tk()
root.geometry("1000x1000")

labelFont = font.Font(family="Times New Roman", size=40)
titleFont = font.Font(family = "Times New Roman", size = 20, weight = "bold")
newFont = font.Font(family = "Times New Roman", size = 15, weight = "bold")

frontPage = Canvas(root, width=1000, height=800, bg = "white")
frontPage.place(x = 0, y = 0)
blueBox = frontPage.create_rectangle(0, 75, 500, 1000, fill = "DodgerBlue2")
redBox = frontPage.create_rectangle(500, 75, 1000, 2000, fill = "tomato")

btn = Button(frontPage, text = "Press 'a' to start a new game", width = 20, height = 5)
btn.bind("a", startGame)
btn.place(x = 400, y = 650)

welcome = Label(frontPage, bg = "ivory2" ,fg = "gray12", text = "Start a new Semio game",borderwidth = 0, relief = "solid",anchor = 'w', padx = 300)
welcome.place(x = 0, y = 0, width =1000, height = 75)
welcome["font"] = labelFont

team1 = Label(frontPage, bg = "DodgerBlue2" ,fg = "gray12", text = "Team 1",borderwidth = 0, relief = "solid",anchor = 'w')
team1.place(x = 200, y = 150, width = 200, height = 75)
team1["font"] = labelFont

team2 = Label(frontPage, bg = "tomato" ,fg = "gray12", text = "Team 2",borderwidth = 0, relief = "solid",anchor = 'w')
team2.place(x = 700, y = 150, width = 200, height = 75)
team2["font"] = labelFont

player1box = Entry(root)
frontPage.create_window(250, 300, window = player1box)
player2box = Entry(root)
frontPage.create_window(250, 500, window = player2box)
player3box = Entry(root)
frontPage.create_window(750, 300, window = player3box)
player4box = Entry(root)
frontPage.create_window(750, 500, window = player4box)



