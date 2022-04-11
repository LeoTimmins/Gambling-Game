from tkinter import * 
import random 
import sys 
import psutil 
import time 
 
MoneyTotal = 1000 
Upgrade = 1 
BackGround = Tk() 
BackGround.title("Black Background") 
BackGround.geometry("400x300+310+300") 
BackGround.attributes("-fullscreen", True) 
BackGround.configure(background='black') 
BackGround.overrideredirect(1) 
 
 
def UpdateCpu(): 
    for widget in Cpu.winfo_children(): 
        widget.destroy() 
    CpuStatTitle = Label(Cpu, text="Computer Stats", bg='grey') 
    CpuStatTitle.pack() 
    CSUB = Button(Cpu, text="Update Stats", command=lambda: UpdateCpu(), bg='grey') 
    CSUB.pack() 
    x = 30 
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)): 
        CpuInd = Label(Cpu, text=f"Core {i}: {percentage}%", bg='grey') 
        x += 20 
        CpuInd.place(x=10, y=x) 
    x += 20 
    CpuInd = Label(Cpu, text=f"Total CPU Usage: {psutil.cpu_percent()}%", bg='grey') 
    CpuInd.place(x=10, y=x) 
 
Cpu = Tk() 
Cpu.geometry("300x200+0+0") 
Cpu.attributes('-topmost',1) 
Cpu.configure(bg="grey") 
Cpu.overrideredirect(1) 
CpuStatTitle = Label(Cpu, text="CPU Stats", bg='grey') 
CpuStatTitle.pack() 
UpdateCpu() 
 
def NewGameRestart(): 
    global MoneyTotal 
    global Upgrade 
    global YourMoney 
    for widget in root.winfo_children(): 
        widget.destroy() 
    for widget in Upg.winfo_children(): 
        widget.destroy() 
    for widget in Stats.winfo_children(): 
        widget.destroy() 
        MoneyTotal = 1000 
        Upgrade = 1 
    YourMoney = Label(root, text=f"You have ${MoneyTotal} ", padx=160, pady=10, bg="green") 
    YourMoney.pack() 
    RestartFull() 
 
Exit = Button(text="Exit", command=lambda: sys.exit(), bg='grey', padx=21) 
NewGame = Button(text="New Game", command=lambda: NewGameRestart(), bg='grey') 
Exit.pack() 
NewGame.pack() 
 
root = Tk() 
root.geometry("400x300+310+300") 
root.attributes('-topmost', 1) 
root.overrideredirect(1) 
 
Upg = Tk() 
Upg.geometry("400x300+730+300") 
Upg.attributes('-topmost', 1) 
Upg.overrideredirect(1) 
 
Stats = Tk() 
Stats.geometry("820x100+310+620") 
Stats.attributes('-topmost', 1) 
Stats.overrideredirect(1) 
 
YourMoney = Label(root, text=f"You have ${MoneyTotal} ", padx=160, pady=10, bg="green") 
YourMoney.pack() 
 
Cheats = Tk() 
Cheats.geometry("300x100+1150+0") 
Cheats.attributes('-topmost', 1) 
Cheats.configure(bg = "grey") 
Cheats.overrideredirect(1) 
 
def cheat1(): 
    global MoneyTotal 
    global YourMoney 
    MoneyTotal = MoneyTotal + 500 
    YourMoney.config(text=f"You have ${MoneyTotal} ") 
 
CheatsTitle = Label(Cheats, text = "-Cheats-", font = 'bold', bg = 'grey') 
CheatsTitle.pack() 
Cheat1D = Label(Cheats, text="Add $500      ---------------------", bg='grey') 
Cheat1B = Button(Cheats, text="Activate Cheat", bg='grey', command=lambda: (cheat1())) 
Cheat1D.place(x=0, y=40) 
Cheat1B.place(x=190, y=37) 
Cheat1D = Label(Cheats, text="Increase Money gain  ------------", bg='grey') 
Cheat1B = Button(Cheats, text="Activate Cheat", bg='grey', command=exec("Upgrade += 1")) 
Cheat1D.place(x=0, y=70) 
Cheat1B.place(x=190, y=67) 
 
def RestartFull(): 
    global MoneyTotal 
    global RollResults 
    global RollResults1 
    global winmessage 
    global MoneyGain 
    global cost 
    global Upg1button 
    global Upg2button 
    global Upg3button 
    global Upg4button 
    global Upg5button 
    global Upgrade 
 
 
    Madeby = Label(Stats, text="Made by Leo Timmins", padx=70, pady=0) 
    Madeby1 = Label(Stats, text="If the 'save bet' button does not work, it is because you have " 
                                "entered a number that is less than 0, more money than you have," 
                                " or you entered a word.", padx=70, pady=0) 
    Madeby2 = Label(Stats, text="If you are unable to buy an upgrade, it is because you do not " 
                                "have enough money, or because buying it would leave you with 0 dollars.", padx=70, pady=0) 
    Madeby3 = Label(Stats, text="The upgrades increase the amount of money you get for winning a game," 
                                " the more the upgrade costs, the higher % boost it gives", padx=70, pady=0) 
    Madeby4 = Label(Stats, text="The formula for how much you will win is (Bet x 2 x Upgrade % boost)", padx=70, pady=0) 
    Madeby.pack() 
    Madeby1.pack() 
    Madeby2.pack() 
    Madeby3.pack() 
    Madeby4.pack() 
 
    def Upg1Cost(): 
        global Upgrade 
        global Upg1button 
        global MoneyTotal 
        MAW = MoneyTotal-500 
        if MAW <= 0: 
            return() 
        MoneyTotal = MoneyTotal - 500 
        YourMoney.config(text=f"You have ${MoneyTotal} ") 
        Upgrade= Upgrade+0.3 
        Upg1button.config(text= "you own this", state= DISABLED, padx=8) 
 
    def Upg2Cost(): 
        global Upgrade 
        global Upg2button 
        global MoneyTotal 
        MAW = MoneyTotal-600 
        if MAW <= 0: 
            return() 
        MoneyTotal = MoneyTotal - 600 
        YourMoney.config(text=f"You have ${MoneyTotal} ") 
        Upgrade= Upgrade+0.4 
        Upg2button.config(text= "you own this", state= DISABLED, padx=8) 
 
    def Upg3Cost(): 
        global Upgrade 
        global Upg3button 
        global MoneyTotal 
        MAW = MoneyTotal-700 
        if MAW <= 0: 
            return() 
        MoneyTotal = MoneyTotal - 700 
        YourMoney.config(text=f"You have ${MoneyTotal} ") 
        Upgrade= Upgrade+0.5 
        Upg3button.config(text= "you own this", state= DISABLED, padx=8) 
 
    def Upg4Cost(): 
        global Upgrade 
        global Upg4button 
        global MoneyTotal 
        MAW = MoneyTotal-800 
        if MAW <= 0: 
            return() 
        MoneyTotal = MoneyTotal - 800 
        YourMoney.config(text=f"You have ${MoneyTotal} ") 
        Upgrade= Upgrade+0.6 
        Upg4button.config(text= "you own this", state= DISABLED, padx=8) 
 
    def Upg5Cost(): 
        global Upgrade 
        global Upg5button 
        global MoneyTotal 
        MAW = MoneyTotal-900 
        if MAW <= 0: 
            return() 
        MoneyTotal = MoneyTotal - 900 
        YourMoney.config(text=f"You have ${MoneyTotal} ") 
        Upgrade+=0.7 
        Upg5button.config(text= "you own this", state= DISABLED, padx=8) 
 
    UpgTitle = Label(Upg, text="Upgrades", padx=70, pady=10, font= 'bold') 
    UpgDescript = Label(Upg, text="Buying upgrades increase the money won", padx=70, pady=0) 
    UpgTitle.place(x=95, y=-7) 
    UpgDescript.place(x=30, y=25) 
 
    Upg1descript = Label(Upg, text="Lucky charm             --------------------------", padx=70, pady=0) 
    Upg1button = Button(Upg, text="$500", padx=30, pady=0, command=lambda: Upg1Cost()) 
    Upg1descript.place(x=-55,y=60) 
    Upg1button.place(x=275, y=57) 
 
    Upg2descript = Label(Upg, text="Family heirloom       --------------------------", padx=70, pady=0) 
    Upg2button = Button(Upg, text="$600", padx=30, pady=0, command=lambda: Upg2Cost()) 
    Upg2descript.place(x=-55, y=90) 
    Upg2button.place(x=275, y=87) 
 
    Upg3descript = Label(Upg, text="Rabbits foot              --------------------------", padx=70, pady=0) 
    Upg3button = Button(Upg, text="$700", padx=30, pady=0, command=lambda: Upg3Cost()) 
    Upg3descript.place(x=-55, y=120) 
    Upg3button.place(x=275,y=117) 
 
    Upg4descript = Label(Upg, text="4 leaf clover              --------------------------", padx=70, pady=0) 
    Upg4button = Button(Upg, text="$800", padx=30, pady=0, command=lambda: Upg4Cost()) 
    Upg4descript.place(x=-55, y=150) 
    Upg4button.place(x=275, y=147) 
 
    Upg5descript = Label(Upg, text="Magic potion            --------------------------", padx=70, pady=0) 
    Upg5button = Button(Upg, text="$900", padx=30, pady=0, command=lambda: Upg5Cost()) 
    Upg5descript.place(x=-55, y=180) 
    Upg5button.place(x=275, y=177) 
 
    Upg5descript = Label(Upg, text="If the button does not work, you can't afford it", padx=70, pady=0) 
    Upg5descript.place(x=0, y=230) 
 
    def Start(): 
        restart() 
        YourMoney.config(text=f"You have ${MoneyTotal} ") 
    def BetMaxF(betammount, BetEntered, Betmessage, BetMax): 
        BetEntered.place_forget() 
        Betmessage.pack_forget() 
        BetMax.place_forget() 
        Bet = MoneyTotal 
        restart1(betammount, Bet) 
 
    def restart(): 
        Betmessage = Label(root, text="Enter the amount you would like " 
                                      "to bet bellow (positive integer only)", padx=70, pady=10) 
        betammount = Entry(root, textvariable = IntVar()) 
        BetEntered = Button(root, text="Save Bet", padx=50, pady=50, bg='black', fg='white', 
                            command=lambda: BetSave(betammount, BetEntered, Betmessage, BetMax)) 
        BetMax = Button(root, text= f"Bet Max", padx=50, pady=15, bg='black', fg='white', 
                            command=lambda: (BetMaxF(betammount, BetEntered, Betmessage, BetMax))) 
        BetMax.place(x=125,y=110) 
        Betmessage.pack() 
        betammount.pack() 
        BetEntered.place(x=125, y=170) 
 
    def Restartprep2(RollResults, RollResults1, OldDiceSum, Bet, Roll1, Roll2): 
        RollResults1.pack_forget() 
        RollResults.pack_forget() 
        DidNotRoll(OldDiceSum, Bet, Roll1, Roll2) 
 
    def Restartprep1 (RollResults, RollResults1, winmessage, MoneyGain): 
        MoneyGain.pack_forget() 
        winmessage.pack_forget() 
        RollResults1.pack_forget() 
        RollResults.pack_forget() 
        restart() 
 
    def RollDice(WYLTR, Bet): 
        global MoneyTotal 
        Roll1 = random.randint(1, 6) 
        Roll2 = random.randint(1, 6) 
        RollTotal = Roll2 + Roll1 
        WYLTR.pack_forget() 
        RollResults = Label(root, text=f"You rolled a '{Roll1}' and a '{Roll2}'", padx=70, pady=10) 
        RollResults1 = Label(root, text=f"this makes the total '{RollTotal}'", padx=70, pady=10) 
        RollResults.pack() 
        RollResults1.pack() 
 
        if RollTotal in {7, 11}: 
            winmessage = Label(root, text=f"yay, you won, enjoy the cash! ", padx=50, pady=10) 
            winmessage.pack() 
            Bet *= 2 * Upgrade 
            MoneyTotal += Bet 
            MoneyGain = Label(root, text=f"you gained ${Bet} ", padx=70, pady=10) 
            MoneyGain.pack() 
            YourMoney.config(text=f"You have ${MoneyTotal} ") 
 
            if MoneyTotal <= 0: 
                BnkRpt = Label(root, text=f"uh oh, looks like you've gone bankrupt, try again next time! ", 
                               padx=70, pady=10, bg="red") 
                BnkRpt.pack() 
                return() 
 
            else: 
                restartprep = Button(root, text="Press to play a new game", padx=50, pady=50, bg='black', fg='white', 
                                 command=lambda: [Restartprep1(RollResults, RollResults1, winmessage, MoneyGain), 
                                          restartprep.pack_forget()]) 
                restartprep.pack() 
 
        elif RollTotal in {2, 3, 12}: 
            winmessage = Label(root, text=f"That's Unfortunate, you lost", padx=70, pady=10) 
            winmessage.pack() 
            MoneyTotal = (MoneyTotal - Bet) 
            MoneyGain = Label(root, text=f"you lost ${Bet} ", padx=70, pady=10) 
            MoneyGain.pack() 
            YourMoney.config(text=f"You have ${MoneyTotal} ") 
 
            if MoneyTotal <= 0: 
                BnkRpt = Label(root, text=f"uh oh, looks like you've gone bankrupt, try again next time! ", padx=70, 
                               pady=10, bg="red") 
                BnkRpt.pack() 
                return() 
 
            else: 
                restartprep = Button(root, text="Press to play a new game", padx=50, pady=50, bg='black', fg='white', 
                                 command=lambda: [Restartprep1(RollResults, RollResults1, winmessage, MoneyGain), 
                                          restartprep.pack_forget()]) 
                restartprep.pack() 
 
        else: 
            OldDiceSum = RollTotal 
            Restartprep2(RollResults, RollResults1, OldDiceSum, Bet, Roll1, Roll2) 
 
    def restart1(betammount, Bet): 
        betammount.pack_forget() 
        WYLTR = Label(root, text = "Click The button to roll", padx = 70, pady = 10) 
        RollButton = Button(root, text="Roll", padx=50, pady=50, bg='black', fg='white', 
                            command=lambda: [RollDice(WYLTR, Bet), RollButton.place_forget()]) 
        WYLTR.pack() 
        RollButton.place(x=135, y=180) 
 
    def BetSave(betammount,BetEntered, Betmessage, BetMax): 
        BetEntered.place_forget() 
        Betmessage.pack_forget() 
        BetMax.place_forget() 
        if len(betammount.get()) == 0: 
            betammount.pack_forget() 
            Start() 
        Bet = float(str(betammount.get())) 
        global MoneyTotal 
        if Bet <= 0 or Bet > MoneyTotal: 
            betammount.pack_forget() 
            Start() 
        restart1(betammount, Bet) 
 
    def DidNotRoll(OldDiceSum, Bet, Roll1, Roll2): 
        DNR1 = Label(root, text=f"You rolled a '{Roll1}' and a '{Roll2}'", padx=70, pady=10) 
        DNR2 = Label(root, text=f"The total of your roll did not equal either 2, 3, 7, 11, 12", padx=70, pady=10) 
        DNR3 = Label(root, text=f"but If you roll the total of your old dice total ({OldDiceSum}), you will win", padx=70, pady=10) 
        DNR1.pack() 
        DNR2.pack() 
        DNR3.pack() 
        RollButton = Button(root, text="Roll", padx=50, pady=50, bg='black', fg='white', 
                            command=lambda:[RollDice2(OldDiceSum, Bet, RollButton, DNR1, DNR2, DNR3)]) 
        RollButton.place(x=130,y=180) 
 
    def RollDice2(OldDiceSum,Bet, RollButton, DNR1, DNR2, DNR3): 
        global MoneyTotal 
        RollButton.place_forget() 
        DNR1.pack_forget() 
        DNR2.pack_forget() 
        DNR3.pack_forget() 
        Roll1 = random.randint(1, 6) 
        Roll2 = random.randint(1, 6) 
        RollTotal = Roll2 + Roll1 
        RollResults = Label(root, text=f"You rolled a '{Roll1}' and a '{Roll2}'", padx=70, pady=10) 
        RollResults1 = Label(root, text=f"this makes the total '{RollTotal}'", padx=70, pady=10) 
        RollResults.pack() 
        RollResults1.pack() 
 
        if RollTotal == OldDiceSum: 
            winmessage = Label(root, text=f"yay, you won, enjoy the cash! ", padx=70, pady=10) 
            winmessage.pack() 
            Bet *= 2*Upgrade 
            MoneyTotal += Bet 
            MoneyGain = Label(root, text=f"you gained ${Bet} ", padx=70, pady=10) 
            MoneyGain.pack() 
            YourMoney.config(text=f"You have ${MoneyTotal} ") 
 
            if MoneyTotal <= 0: 
                BnkRpt = Label(root, text=f"uh oh, looks like you've gone bankrupt, try again next time! ", padx=70, 
                               pady=10, bg="red") 
                BnkRpt.pack() 
                return() 
 
            else: 
                restartprep = Button(root, text="Press to play a new game", padx=50, pady=50, bg='black', fg='white', 
                                 command=lambda: [Restartprep1(RollResults, RollResults1, winmessage, MoneyGain), 
                                    restartprep.pack_forget()]) 
                restartprep.pack() 
 
        elif RollTotal != OldDiceSum: 
            winmessage = Label(root, text=f"That's Unfortunate, you lost", padx=70, pady=10) 
            winmessage.pack() 
            MoneyTotal = (MoneyTotal - Bet) 
            MoneyGain = Label(root, text=f"you lost ${Bet} ", padx=70, pady=10) 
            MoneyGain.pack() 
            YourMoney.config(text=f"You have ${MoneyTotal} ") 
 
            if MoneyTotal <= 0: 
                BnkRpt = Label(root, text=f"uh oh, looks like you've gone bankrupt, try again next time! ", padx=70, 
                               pady=10, bg="red") 
                BnkRpt.pack() 
                return () 
 
            else: 
                restartprep = Button(root, text="Press to play a new game", padx=50, pady=50, bg='black', fg='white', 
                                 command=lambda: [Restartprep1(RollResults, RollResults1, winmessage, MoneyGain), 
                                                  restartprep.pack_forget()]) 
                restartprep.pack() 
    Start() 
 
RestartFull() 
 
root.mainloop() 
 
 
