class Character:
    '''character class receives json from fflogs'''
    def __init__(self,job,jsonData):
        self.job=job
        self.jsonData=jsonData
        self.e1s = self._getMaxPercent_("Eden Prime")
        self.e2s = self._getMaxPercent_("Voidwalker")
        self.e3s = self._getMaxPercent_("Leviathan")
        self.e4s = self._getMaxPercent_("Titan")
        

    def _getMaxDPS_(self,fight):
        fightlist=[]
        dpsList=[]

        for eachItem in self.jsonData:
            if eachItem['spec'] == self.job:
                if eachItem['encounterName'] == fight:
                    fightlist.append(eachItem)
        for encounter in fightlist:
            dpsList.append(encounter['total'])
            return max(dpsList)

    def _getMaxPercent_(self,fight):
        fightlist=[]
        dpsList=[]

        for eachItem in self.jsonData:
            if eachItem['spec'] == self.job:
                if eachItem['encounterName'] == fight:
                    fightlist.append(eachItem)
        for encounter in fightlist:
            dpsList.append(encounter['percentile'])
            return max(dpsList)
    
    def getEs1(self):
        return (self.e1s)

    def getEs2(self):
        return (self.e2s)

    def getEs3(self):
        return (self.e3s)

    def getEs4(self):
        return (self.e4s)
    
    def getJob(self):
        return self.job
    



