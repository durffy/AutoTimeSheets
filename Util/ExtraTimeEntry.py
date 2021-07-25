from Util.TimeEntry import TimeEntry

class ExtraTime:

    def __init__(self, extra_time):
        self.time_entry = TimeEntry()
        self.extra_time = extra_time
        self.calculateHour()

    def calculateMinute(self):
        ones_decimal_place = str(self.extra_time).split('.')[1][0]

        if (ones_decimal_place == "1"):
            return ":10"
        if (ones_decimal_place == "2"):
            return ":15"
        if (ones_decimal_place == "3"):
            return ":20"
        if (ones_decimal_place == "4"):
            return ":25"
        if (ones_decimal_place == "5"):
            return ":30"
        if (ones_decimal_place == "6"):
            return ":35"
        if (ones_decimal_place == "7"):
            return ":40"
        if (ones_decimal_place == "8"):
            return ":45"
        if (ones_decimal_place == "9"):
            return ":50"
        else:
            return ":00"


    def calculateHour(self):
        if (self.extra_time >= 8):
            self.time_entry.setAmIn()
            self.time_entry.setAmOut()
            self.time_entry.setLunch()
            self.time_entry.setPmIn()
            self.time_entry.setPmOut("4"+self.calculateMinute())

        elif (self.extra_time >= 7):
            self.time_entry.setAmIn()
            self.time_entry.setAmOut()
            self.time_entry.setLunch()
            self.time_entry.setPmIn()
            self.time_entry.pm_out = "3" + self.calculateMinute()

        elif (self.extra_time  >= 6):
            self.time_entry.setAmIn()
            self.time_entry.setAmOut()
            self.time_entry.setLunch()
            self.time_entry.setPmIn()
            self.time_entry.setPmOut("2" + self.calculateMinute())

        elif (self.extra_time  >= 5):
            self.time_entry.setAmIn()
            self.time_entry.setAmOut()
            self.time_entry.setLunch()
            self.time_entry.setPmIn()
            self.time_entry.setPmOut("1" + self.calculateMinute())

        elif (self.extra_time  >= 4):
            self.time_entry.setAmIn()
            self.time_entry.setAmOut()
            self.time_entry.setLunch()
            self.time_entry.setPmIn()
            self.time_entry.pm_out = "12" + self.calculateMinute()

        elif (self.extra_time >= 3):
            self.time_entry.setAmIn()
            self.time_entry.setAmOut("10" + self.calculateMinute())

        elif (self.extra_time >= 2):
            self.time_entry.setAmIn()
            "10" + self.calculateMinute()
            self.time_entry.setAmOut("9" + self.calculateMinute())


        elif (self.extra_time >= 1):
            self.time_entry.setAmIn()
            self.time_entry.setAmOut("8" + self.calculateMinute())

    def getTimeEntry(self):
        return self.time_entry