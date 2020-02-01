import tkinter
from tkinter import *
import requests
import json
from character import *
import time
from prettytable import PrettyTable
import re




def updateData(character, server, region, token):
    #confFile={}
    #rawFile=open("settings.conf","r")
    #for line in rawFile:
        #arg=line.split("=")
        #confFile[arg[0]]=arg[1]
    #address=url='https://www.fflogs.com:443/v1/parses/character/%s/%s/%s?encounter=Titan&api_key=%s'%( confFile['character'], confFile['server'], confFile['region'], confFile['token'] )
    address=url='https://www.fflogs.com:443/v1/parses/character/%s/%s/%s?encounter=Titan&api_key=%s'%( character, server, region, token )
    address = re.sub("\n",'',address) #Remove trailing \n spaces
    r = requests.get(url=address)
    print(r)
    return r.json()
    



def printAll(objList):
    table = PrettyTable()
    table.field_names = ["Job", "Eden Prime", "Voidwalker", "Leviathan","Titan"]
    for each in objList:
        table.add_row( [ each.getJob(), each.getEs1() , each.getEs2() , each.getEs3() ,each.getEs4() ] )
    print(table)

def printMinPerFight(objList):
    table = PrettyTable()
    table.field_names = ["Fight", "Job", "Percentile"]

    lowerPercent=101
    for each in objList:
        
        if each.getEs1() < lowerPercent:
            lowerPercent = each.getEs1()
            lowestEs1=each
    
    lowerPercent=101
    for each in objList:
        if each.getEs2() < lowerPercent:
            lowerPercent = each.getEs2()
            lowestEs2=each

    lowerPercent=101
    for each in objList:
        if each.getEs3() < lowerPercent:
            lowerPercent = each.getEs3()
            lowestEs3=each

    lowerPercent=101
    for each in objList:

        if each.getEs4() < lowerPercent:
            lowerPercent = each.getEs4()
            lowestEs4=each
        
    table.add_row( [ "Eden Prime", lowestEs1.getJob(), lowestEs1.getEs1() ] )
    table.add_row( [ "Voidwalker", lowestEs2.getJob(), lowestEs2.getEs2() ] )
    table.add_row( [ "Leviathan", lowestEs3.getJob(), lowestEs3.getEs3() ] )
    table.add_row( [ "Titan", lowestEs4.getJob(), lowestEs4.getEs4() ] )

    print(table)

def printMinOverall(objList):

    lowerPercent=101
    for each in objList:
        
        if each.getEs1() < lowerPercent:
            lowerPercent = each.getEs1()
            lowestEs1=each
    
    lowerPercent=101
    for each in objList:
        if each.getEs2() < lowerPercent:
            lowerPercent = each.getEs2()
            lowestEs2=each

    lowerPercent=101
    for each in objList:
        if each.getEs3() < lowerPercent:
            lowerPercent = each.getEs3()
            lowestEs3=each

    lowerPercent=101
    for each in objList:

        if each.getEs4() < lowerPercent:
            lowerPercent = each.getEs4()
            lowestEs4=each

    table = PrettyTable()
    table.field_names = ["Fight", "Job", "Percentile"]

    if all(lowestEs1.getEs1() < val for val in [ lowestEs2.getEs2(), lowestEs3.getEs3(), lowestEs4.getEs4()] ) : table.add_row( [ "Eden Prime", lowestEs1.getJob(), lowestEs1.getEs1()  ] )
    if all(lowestEs2.getEs2() < val for val in [ lowestEs1.getEs1(), lowestEs3.getEs3(), lowestEs4.getEs4()] ) : table.add_row( [ "Voidwalker", lowestEs2.getJob(), lowestEs2.getEs2()  ] )
    if all(lowestEs3.getEs3() < val for val in [ lowestEs1.getEs1(), lowestEs2.getEs2(), lowestEs4.getEs4()] ) : table.add_row( [ "Leviathan", lowestEs3.getJob(), lowestEs3.getEs3()  ] )
    if all(lowestEs4.getEs4() < val for val in [ lowestEs1.getEs1(), lowestEs2.getEs2(), lowestEs3.getEs3()] ) : table.add_row( [ "Titan", lowestEs4.getJob(), lowestEs4.getEs4() ] )

    print(table)

def execute(character, jobs, server, region, key):
    data = updateData(character, server, region, key)

    objList=[]
    for each in jobs.keys():
        if jobs[each].get() == 1:
            objList.append(Character(each, data))

    print("ALL")
    printAll(objList)

    print("\nLowest per fight")
    printMinPerFight(objList)

    print("\nLower Overall")
    printMinOverall(objList)

def main():


    window=tkinter.Tk()
    window.title("ffxivParseHelper")
    
    drkvar = IntVar()
    gnbvar = IntVar()
    pldvar = IntVar()
    warvar = IntVar()
    
    name = StringVar()
    key = StringVar()
    server = StringVar()
    region = StringVar()

    label = tkinter.Label(window, text = "FFLOGS Settings").grid(row=1)
    
    tkinter.Label(window, text = "Character Name").grid(row = 3)
    tkinter.Entry(window, textvariable = name).grid(row = 3, column = 2)

    tkinter.Label(window, text = "FFLOGS API Key").grid(row = 4)
    tkinter.Entry(window, textvariable = key).grid(row = 4, column = 2) 

    tkinter.Label(window, text = "Server").grid(row = 5) 
    tkinter.OptionMenu(window, server, "Cactuar", "Adamantoise").grid(row=5, column=2)
    
    tkinter.Label(window, text = "Region").grid(row = 6) 
    tkinter.OptionMenu(window, region, "NA", "EU").grid(row=6, column=2)
    
    tkinter.Checkbutton(window, text = "DRK",variable = drkvar,onvalue = 1, offvalue=0).grid(row=7)
    tkinter.Checkbutton(window, text = "GNB",variable = gnbvar,onvalue = 1, offvalue=0).grid(row=7, column=2)
    tkinter.Checkbutton(window, text = "PLD",variable = pldvar,onvalue = 1, offvalue=0).grid(row=7, column=3)
    tkinter.Checkbutton(window, text = "WAR",variable = warvar,onvalue = 1, offvalue=0).grid(row=7, column=4)

    jobs={}
    jobs={"Dark Knight":drkvar,
            "Gunbreaker":gnbvar,
            "Paladin":pldvar,
            "Warrior":warvar}


    button_widget = tkinter.Button(window, command = lambda: execute(name.get(),jobs,server.get(),region.get(),key.get()), text="Run").grid(row=9)
    window.mainloop()

        


    return 0

if __name__ == "__main__":
    main()