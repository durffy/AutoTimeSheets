class TimeEntry:
    def __init__(self):
        self.lunch = ""
        self.am_in = ""
        self.am_out = ""
        self.pm_in = ""
        self.pm_out = ""

    def setAmIn(self, param = "7:00"):
        self.am_in = param

    def setAmOut(self, param = "11:00"):
        self.am_out = param

    def setLunch(self, param = "1hr"):
        self.lunch = param

    def setPmIn(self, param = "12:00"):
        self.pm_in = param

    def setPmOut(self, param = "4:00"):
        self.pm_out = param

    def getAmIn(self):
        return self.am_in

    def getAmOut(self):
        return self.am_out

    def getLunch(self):
        return self.lunch

    def getPmIn(self):
        return self.pm_in

    def getPmOut(self):
        return self.pm_out

    def getTimeList(self):
        return self.am_in, self.am_out, self.lunch, self.pm_in, self.pm_out

    def setDefaults(self):
        self.setAmIn()
        self.setAmOut()
        self.setLunch()
        self.setPmIn()
        self.setPmOut()