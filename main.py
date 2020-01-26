import requests
import json
from character import *
import time
from prettytable import PrettyTable
import re




def updateData():
    confFile={}
    rawFile=open("settings.conf","r")
    for line in rawFile:
        arg=line.split("=")
        confFile[arg[0]]=arg[1]
    address=url='https://www.fflogs.com:443/v1/parses/character/%s/%s/%s?encounter=Titan&api_key=%s'%( confFile['character'], confFile['server'], confFile['region'], confFile['token'] )
    address = re.sub("\n",'',address) #Remove trailing \n spaces
    print(address)
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
    
    if all(lowestEs1.getEs1() < val for val in [ lowestEs2.getEs2(), lowestEs3.getEs3(), lowestEs4.getEs4()] ) : print ("%s %s %s"%("Eden Prime", lowestEs1.getJob(), lowestEs1.getEs1()  ) )
    if all(lowestEs2.getEs2() < val for val in [ lowestEs1.getEs1(), lowestEs3.getEs3(), lowestEs4.getEs4()] ) : print ("%s %s %s"%("Voidwalker", lowestEs2.getJob(), lowestEs2.getEs2()  ) )
    if all(lowestEs3.getEs3() < val for val in [ lowestEs1.getEs1(), lowestEs2.getEs2(), lowestEs4.getEs4()] ) : print ("%s %s %s"%("Leviathan", lowestEs3.getJob(), lowestEs3.getEs3()  ) )
    if all(lowestEs4.getEs4() < val for val in [ lowestEs1.getEs1(), lowestEs2.getEs2(), lowestEs3.getEs3()] ) : print ("%s %s %s"%("Titan", lowestEs4.getJob(), lowestEs4.getEs4()  ) )



def main():

        
    data = updateData()

    AguaLocaDarkKnight = Character('Dark Knight',data)
    AguaLocaGunbreaker = Character('Gunbreaker',data)
    AguaLocaPaladin = Character('Paladin',data)
    AguaLocaWarrior = Character('Warrior',data)

    objList=[AguaLocaDarkKnight,AguaLocaGunbreaker,AguaLocaPaladin,AguaLocaWarrior]

    print("ALL")
    printAll(objList)

    print("\nLowest per fight")
    printMinPerFight(objList)

    print("\nLower Overall")
    printMinOverall(objList)

    return 0

if __name__ == "__main__":
    main()