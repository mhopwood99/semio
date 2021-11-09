from tkinter import *
import tkinter.font as font

def startGame(asdf):
    def hits1update(a):
        global hits1
        hits1 = hits1 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        hits1number.config(text=str(hits1))
    def hits2update(b):
        global hits2
        hits2 = hits2 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        hits2number.config(text=str(hits2))
    def hits3update(c):
        global hits3
        hits3 = hits3 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        hits3number.config(text=str(hits3))
    def hits4update(d):
        global hits4
        hits4 = hits4 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        hits4number.config(text=str(hits4))
    def aces1update(e):
        global aces1
        aces1 = aces1 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        aces1number.config(text=str(aces1))
    def aces2update(f):
        global aces2
        aces2 = aces2 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        aces2number.config(text=str(aces2))
    def aces3update(g):
        global aces3
        aces3 = aces3 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        aces3number.config(text=str(aces3))
    def aces4update(h):
        global aces4
        aces4 = aces4 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        aces4number.config(text=str(aces4))
    def errors1update(i):
        global errors1
        errors1 = errors1 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        errors1number.config(text=str(errors1))
    def errors2update(j):
        global errors2
        errors2 = errors2 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        errors2number.config(text=str(errors2))
    def errors3update(k):
        global errors3
        errors3 = errors3 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        errors3number.config(text=str(errors3))
    def errors4update(l):
        global errors4
        errors4 = errors4 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        errors4number.config(text=str(errors4))
    def socials1update(m):
        global socials1
        socials1 = socials1 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        socials1number.config(text=str(socials1))
    def socials2update(n):
        global socials2
        socials2 = socials2 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        socials2number.config(text=str(socials2))
    def socials3update(o):
        global socials3
        socials3 = socials3 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        socials3number.config(text=str(socials3))
    def socials4update(p):
        global socials4
        socials4 = socials4 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        socials4number.config(text=str(socials4))
    def sinks1update(q):
        global sinks1
        sinks1 = sinks1 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        sinks1number.config(text=str(sinks1))
    def sinks2update(r):
        global sinks2
        sinks2 = sinks2 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        sinks2number.config(text=str(sinks2))
    def sinks3update(s):
        global sinks3
        sinks3 = sinks3 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        sinks3number.config(text=str(sinks3))
    def sinks4update(t):
        global sinks4
        sinks4 = sinks4 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        sinks4number.config(text=str(sinks4))
    def noogies1update(u):
        global noogies1
        noogies1 = noogies1 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        nBox1number.config(text=str(noogies1))
    def noogies2update(v):
        global noogies2
        noogies2 = noogies2 + 1
        team1score = hits1 + hits2 + aces1 + aces2 - errors1 - errors2 + socials1 + socials2 + socials3 + socials4 + noogies1 + noogies2 + sinks1 + sinks2 + errors3 + errors4
        score1.config(text = str(team1score))
        nBox2number.config(text=str(noogies2))
    def noogies3update(w):
        global noogies3
        noogies3 = noogies3 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        nBox3number.config(text=str(noogies3))
    def noogies4update(x):
        global noogies4
        noogies4 = noogies4 + 1
        team2score = hits3 + hits4 + aces3 + aces4 - errors3 - errors4 + socials1 + socials2 + socials3 + socials4 + noogies3 + noogies4 + sinks3 + sinks4 + errors1 + errors2
        score2.config(text = str(team2score))
        nBox4number.config(text=str(noogies4))
        
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

    scoreUpdate = Button(canvas, text = "Score Update", width = 10, height = 1)
    scoreUpdate.bind("a", hits1update)
    scoreUpdate.bind("b", hits2update)
    scoreUpdate.bind("c", hits3update)
    scoreUpdate.bind("d", hits4update)
    scoreUpdate.bind("e", aces1update)
    scoreUpdate.bind("f", aces2update)
    scoreUpdate.bind("g", aces3update)
    scoreUpdate.bind("h", aces4update)
    scoreUpdate.bind("i", errors1update)
    scoreUpdate.bind("j", errors2update)
    scoreUpdate.bind("k", errors3update)
    scoreUpdate.bind("l", errors4update)
    scoreUpdate.bind("m", socials1update)
    scoreUpdate.bind("n", socials2update)
    scoreUpdate.bind("o", socials3update)
    scoreUpdate.bind("p", socials4update)
    scoreUpdate.bind("q", sinks1update)
    scoreUpdate.bind("r", sinks2update)
    scoreUpdate.bind("s", sinks3update)
    scoreUpdate.bind("t", sinks4update)
    scoreUpdate.bind("u", noogies1update)
    scoreUpdate.bind("v", noogies2update)
    scoreUpdate.bind("w", noogies3update)
    scoreUpdate.bind("x", noogies4update)
    scoreUpdate.place(x = 10, y = 18)
    
    
    scoreBox1 = canvas.create_rectangle(0, 125, 500, 275, fill = "DodgerBlue2")
    score1 = Label(canvas, bg = "DodgerBlue2", fg = "gray12", text = str(team1score), font = scoreFont)
    score1.place(x = 220, y = 170, width = 60, height = 60)
    scoreBox2 = canvas.create_rectangle(500, 125, 1000, 275, fill = "tomato")
    score2 = Label(canvas, bg = "tomato", fg = "gray12", text = str(team2score), font = scoreFont)
    score2.place(x = 720, y = 170, width = 60, height = 60)
    
    hitTitleBox = canvas.create_rectangle(0, 275, 20, 400, fill = "White")
    hitsTitle = canvas.create_text(11, 335, text = "H", font = newFont)
    hitBox1 = canvas.create_rectangle(20, 275, 250, 400, fill = "sky blue")
    hitBox1key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'A', font = titleFont)
    hitBox1key.place(x = 220, y = 276, width = 30, height = 30)
    hits1number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(hits1), font = labelFont)
    hits1number.place(x = 100, y = 305, width = 60, height = 60)
    hitBox2 = canvas.create_rectangle(250, 275, 500, 400, fill = "sky blue")
    hitBox2key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'B', font = titleFont)
    hitBox2key.place(x = 470, y = 276, width = 30, height = 30)
    hits2number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(hits2), font = labelFont)
    hits2number.place(x = 350, y = 305, width = 60, height = 60)
    hitBox3 = canvas.create_rectangle(500, 275, 750, 400, fill = "salmon")
    hitBox3key = Label(canvas, bg = "salmon", fg = "gray12", text = 'C', font = titleFont)
    hitBox3key.place(x = 720, y = 276, width = 30, height = 30)
    hits3number = Label(canvas, bg = "salmon", fg = "gray12", text = str(hits3), font = labelFont)
    hits3number.place(x = 600, y = 305, width = 60, height = 60)
    hitBox4 = canvas.create_rectangle(750, 275, 1000, 400, fill = "salmon")
    hitBox4key = Label(canvas, bg = "salmon", fg = "gray12", text = 'D', font = titleFont)
    hitBox4key.place(x = 968, y = 276, width = 30, height = 30)
    hits4number = Label(canvas, bg = "salmon", fg = "gray12", text = str(hits4), font = labelFont)
    hits4number.place(x = 850, y = 305, width = 60, height = 60)

    aceTitleBox = canvas.create_rectangle(0, 400, 20, 475, fill = "White")
    aceTitle = canvas.create_text(11, 437, text = "A", font = newFont)
    aceBox1 = canvas.create_rectangle(20, 400, 250, 475, fill = "sky blue")
    aceBox1key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'E', font = titleFont)
    aceBox1key.place(x = 220, y = 401, width = 30, height = 30)
    aces1number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(aces1), font = titleFont)
    aces1number.place(x = 100, y = 405, width = 60, height = 60)
    aceBox2 = canvas.create_rectangle(250, 400, 500, 475, fill = "sky blue")
    aceBox2key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'F', font = titleFont)
    aceBox2key.place(x = 470, y = 401, width = 30, height = 30)
    aces2number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(aces2), font = titleFont)
    aces2number.place(x = 350, y = 405, width = 60, height = 60)
    aceBox3 = canvas.create_rectangle(500, 400, 750, 475, fill = "salmon")
    aceBox3key = Label(canvas, bg = "salmon", fg = "gray12", text = 'G', font = titleFont)
    aceBox3key.place(x = 720, y = 401, width = 30, height = 30)
    aces3number = Label(canvas, bg = "salmon", fg = "gray12", text = str(aces3), font = titleFont)
    aces3number.place(x = 600, y = 405, width = 60, height = 60)
    aceBox4 = canvas.create_rectangle(750, 400, 1000, 475, fill = "salmon")
    aceBox4key = Label(canvas, bg = "salmon", fg = "gray12", text = 'H', font = titleFont)
    aceBox4key.place(x = 968, y = 401, width = 30, height = 30)
    aces4number = Label(canvas, bg = "salmon", fg = "gray12", text = str(aces4), font = titleFont)
    aces4number.place(x = 850, y = 405, width = 60, height = 60)
    
    errorTitleBox = canvas.create_rectangle(0, 475, 20, 550, fill = "White")
    errorTitle = canvas.create_text(11, 512, text = "E", font = newFont)
    errorBox1 = canvas.create_rectangle(20, 475, 250, 550, fill = "sky blue")
    errorBox1key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'I', font = titleFont)
    errorBox1key.place(x = 220, y = 476, width = 30, height = 30)
    errors1number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(errors1), font = titleFont)
    errors1number.place(x = 100, y = 480, width = 60, height = 60)
    errorBox2 = canvas.create_rectangle(250, 475, 500, 550, fill = "sky blue")
    errorBox2key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'J', font = titleFont)
    errorBox2key.place(x = 470, y = 476, width = 30, height = 30)
    errors2number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(errors2), font = titleFont)
    errors2number.place(x = 350, y = 480, width = 60, height = 60)
    errorBox3 = canvas.create_rectangle(500, 475, 750, 550, fill = "salmon")
    errorBox3key = Label(canvas, bg = "salmon", fg = "gray12", text = 'K', font = titleFont)
    errorBox3key.place(x = 720, y = 476, width = 30, height = 30)
    errors3number = Label(canvas, bg = "salmon", fg = "gray12", text = str(errors3), font = titleFont)
    errors3number.place(x = 600, y = 480, width = 60, height = 60)
    errorBox4 = canvas.create_rectangle(750, 475, 1000, 550, fill = "salmon")
    errorBox4key = Label(canvas, bg = "salmon", fg = "gray12", text = 'L', font = titleFont)
    errorBox4key.place(x = 968, y = 476, width = 30, height = 30)
    errors4number = Label(canvas, bg = "salmon", fg = "gray12", text = str(errors4), font = titleFont)
    errors4number.place(x = 850, y = 480, width = 60, height = 60)
    
    socialTitleBox = canvas.create_rectangle(0, 550, 20, 625, fill = "White")
    socialTitle = canvas.create_text(11, 587, text = "So", font = newFont)
    socialBox1 = canvas.create_rectangle(20, 550, 250, 625, fill = "sky blue")
    socialBox1key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'M', font = titleFont)
    socialBox1key.place(x = 220, y = 556, width = 30, height = 30)
    socials1number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(socials1), font = titleFont)
    socials1number.place(x = 100, y = 555, width = 60, height = 60)
    socialBox2 = canvas.create_rectangle(250, 550, 500, 625, fill = "sky blue")
    socialBox2key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'N', font = titleFont)
    socialBox2key.place(x = 470, y = 556, width = 30, height = 30)
    socials2number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(socials2), font = titleFont)
    socials2number.place(x = 350, y = 555, width = 60, height = 60)
    socialBox3 = canvas.create_rectangle(500, 550, 750, 625, fill = "salmon")
    socialBox3key = Label(canvas, bg = "salmon", fg = "gray12", text = 'O', font = titleFont)
    socialBox3key.place(x = 720, y = 556, width = 30, height = 30)
    socials3number = Label(canvas, bg = "salmon", fg = "gray12", text = str(socials3), font = titleFont)
    socials3number.place(x = 600, y = 555, width = 60, height = 60)
    socialBox4 = canvas.create_rectangle(750, 550, 1000, 625, fill = "salmon")
    socialBox4key = Label(canvas, bg = "salmon", fg = "gray12", text = 'P', font = titleFont)
    socialBox4key.place(x =968, y = 556, width = 30, height = 30)
    socials4number = Label(canvas, bg = "salmon", fg = "gray12", text = str(socials4), font = titleFont)
    socials4number.place(x = 850, y = 555, width = 60, height = 60)

    sinkTitleBox = canvas.create_rectangle(0, 625, 20, 700, fill = "White")
    sinkTitle = canvas.create_text(11, 662, text = "Si", font = newFont)
    sinkBox1 = canvas.create_rectangle(20, 625, 250, 700, fill = "sky blue")
    sinkBox1key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'Q', font = titleFont)
    sinkBox1key.place(x = 220, y = 631, width = 30, height = 30)
    sinks1number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(sinks1), font = titleFont)
    sinks1number.place(x = 100, y = 630, width = 60, height = 60)
    sinkBox2 = canvas.create_rectangle(250, 625, 500, 700, fill = "sky blue")
    sinkBox2key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'R', font = titleFont)
    sinkBox2key.place(x = 470, y = 631, width = 30, height = 30)
    sinks2number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(sinks2), font = titleFont)
    sinks2number.place(x = 350, y = 630, width = 60, height = 60)
    sinkBox3 = canvas.create_rectangle(500, 625, 750, 700, fill = "salmon")
    sinkBox3key = Label(canvas, bg = "salmon", fg = "gray12", text = 'S', font = titleFont)
    sinkBox3key.place(x = 720, y = 631, width = 30, height = 30)
    sinks3number = Label(canvas, bg = "salmon", fg = "gray12", text = str(sinks3), font = titleFont)
    sinks3number.place(x = 600, y = 630, width = 60, height = 60)
    sinkBox4 = canvas.create_rectangle(750, 625, 1000, 700, fill = "salmon")
    sinkBox4key = Label(canvas, bg = "salmon", fg = "gray12", text = 'T', font = titleFont)
    sinkBox4key.place(x = 968, y = 631, width = 30, height = 30)
    sinks4number = Label(canvas, bg = "salmon", fg = "gray12", text = str(sinks4), font = titleFont)
    sinks4number.place(x = 850, y = 630, width = 60, height = 60)

    nTitleBox = canvas.create_rectangle(0, 700, 20, 775, fill = "White")
    nTitle = canvas.create_text(11, 737, text = "N", font = newFont)
    nBox1 = canvas.create_rectangle(20, 700, 250, 775, fill = "sky blue")
    nBox1key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'U', font = titleFont)
    nBox1key.place(x = 220, y = 706, width = 30, height = 30)
    nBox1number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(noogies1), font = titleFont)
    nBox1number.place(x = 100, y = 705, width = 60, height = 60)
    nBox2 = canvas.create_rectangle(250, 700, 500, 775, fill = "sky blue")
    nBox2key = Label(canvas, bg = "sky blue", fg = "gray12", text = 'V', font = titleFont)
    nBox2key.place(x = 470, y = 706, width = 30, height = 30)
    nBox2number = Label(canvas, bg = "sky blue", fg = "gray12", text = str(noogies2), font = titleFont)
    nBox2number.place(x = 350, y = 705, width = 60, height = 60)
    nBox3 = canvas.create_rectangle(500, 700, 750, 775, fill = "salmon")
    nBox3key = Label(canvas, bg = "salmon", fg = "gray12", text = 'W', font = titleFont)
    nBox3key.place(x = 720, y = 706, width = 30, height = 30)
    nBox3number = Label(canvas, bg = "salmon", fg = "gray12", text = str(noogies3), font = titleFont)
    nBox3number.place(x = 600, y = 705, width = 60, height = 60)
    nBox4 = canvas.create_rectangle(750, 700, 1000, 775, fill = "salmon")
    nBox4key = Label(canvas, bg = "salmon", fg = "gray12", text = 'X', font = titleFont)
    nBox4key.place(x = 968, y = 706, width = 30, height = 30)
    nBox4number = Label(canvas, bg = "salmon", fg = "gray12", text = str(noogies4), font = titleFont)
    nBox4number.place(x = 850, y = 705, width = 60, height = 60)


root = Tk()
root.geometry("1000x1000")
hits1 = 0
hits2 = 0
hits3 = 0
hits4 = 0
aces1 = 0
aces2 = 0
aces3 = 0
aces4 = 0
errors1 = 0
errors2 = 0
errors3 = 0
errors4 = 0
socials1 = 0
socials2 = 0
socials3 = 0
socials4 = 0
sinks1 = 0
sinks2 = 0
sinks3 = 0
sinks4 = 0
noogies1 = 0
noogies2 = 0
noogies3 = 0
noogies4 = 0
team1score = 0
team2score = 0
labelFont = font.Font(family="Times New Roman", size=40)
scoreFont = font.Font(family="Times New Roman", size=55)
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

root.mainloop()



