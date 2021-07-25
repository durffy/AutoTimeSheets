"""
This should build a time sheet based on the number of hours provided
"""
from Util.TimeEntry import TimeEntry


class TimeSheet():
    __workweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def __init__(self, destination_ws, name, date, hours):
        self.destination_ws = destination_ws
        self.name = name
        self.date = date
        self.hours = hours
        self.setTimeSheetHeader()
        self.setTimeSheetHours()
        self.setTimeSheetFooter()

    def setTimeSheetHeader(self):
        self.destination_ws.append(["Name", self.name])
        self.destination_ws.append(["Date", self.date])
        self.destination_ws.append(["Day", "In", "Out", "Lunch", "In", "Out", "Total"])

    def setTimeSheetHours(self):
        for weekday in self.__workweek:
            defaultTimes = self.setDefaultTimes()
            defaultTimeList = []

            defaultTimeList.append(weekday)
            for e in defaultTimes.getTimeList():
                defaultTimeList.append(e)
            defaultTimeList.append(8)
            self.destination_ws.append(defaultTimeList)
            self.destination_ws.append([""])

        self.destination_ws.append(["Saturday"])
        self.destination_ws.append([""])


    def setTimeSheetFooter(self):

        self.destination_ws.append(["", "", "", "", "", "Total", self.hours])

    def setDefaultTimes(self):
        defaultTimeEntry = TimeEntry()
        defaultTimeEntry.setDefaults()
        return defaultTimeEntry

