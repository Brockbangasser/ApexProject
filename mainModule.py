from mainGetLegendDataModule import *
import tkinter
from tkinter import *

master = Tk()
master.geometry('715x250')


def onClick():
    legend = legVariable.get()  # gets the option from Legend Option that is chosen when 'OK' is clicked
    evalData(legend)


def legendShow():
    globVariable.set("Select Metric")
    legOption.pack()
    globOption.pack_forget()
    globButton.pack(side=BOTTOM, pady=1)
    legendButton.pack_forget()


def showGlob():
    legVariable.set("Select Legend")
    globOption.pack()
    legOption.pack_forget()
    legendButton.pack(side=BOTTOM, pady=1)
    globButton.pack_forget()


# Evaluates the selection from stat drop box and changes it to number to match the JSON notation
def evalData(legend):
    match legend:
        case "Wraith":
            wraithChose(legend)
        case "Seer":
            seerChose(legend)
        case "Bloodhound":
            bloodChose(legend)
        case "Horizon":
            horizonChose(legend)
        case "Revenant":
            revChose(legend)
        case "Crypto":
            cryptoChose(legend)
        case "Gibraltar":
            gibbyChose(legend)
        case "Wattson":
            wattChose(legend)
        case "Fuse":
            fuseChose(legend)
        case "Bangalore":
            bangChose(legend)
        case "Octane":
            octChose(legend)
        case "Caustic":
            causticChose(legend)
        case "Lifeline":
            lifeChose(legend)
        case "Pathfinder":
            pathChose(legend)
        case "Loba":
            lobaChose(legend)
        case "Mirage":
            mirageChose(legend)
        case "Rampart":
            ramChose(legend)
        case "Valkyrie":
            valkChose(legend)
        case "Ash":
            ashChose(legend)
        case "Mad Maggie":
            magChose(legend)
        case "Newcastle":
            castleChose(legend)
        case "Vantage":
            vantageChose(legend)
        case "Select Legend":
            return


title = Label(master, text="Apex Legends Stats", font=["Arial", 30])
title.pack(side=TOP)

# Instantiate Option Box?
legVariable = StringVar(master)
legVariable.set("Select Legend")  # Option Box Title Text
globVariable = StringVar(master)
globVariable.set('Select Metric')

globOption = OptionMenu(master, globVariable, 'Select Metric', 'Platform', 'Rank')

legOption = OptionMenu(master, legVariable, "Select Legend", "Revenant", "Crypto", "Horizon", "Gibraltar", "Wattson",
                       "Fuse",
                       "Bangalore", "Wraith", "Octane", "Bloodhound", "Caustic", "Lifeline", "Pathfinder", "Loba",
                       "Mirage", "Rampart", "Valkyrie", "Seer", "Ash", "Mad Maggie", "Newcastle",
                       "Vantage")  # create the options
legOption.pack()  # Put on the Master Window

# Packs the Button and puts padding
myButton = tkinter.Button(text='Go', command=onClick)
myButton.pack(side=BOTTOM, pady=1, padx=100, fill='x')
legendButton = tkinter.Button(text='Click to Change to Legend Stats', command=legendShow)
# legendButton.pack(side=BOTTOM, pady=1)
globButton = tkinter.Button(text='Click to Change to Global Stats', command=showGlob)
globButton.pack(side=BOTTOM, pady=1)

mainloop()
