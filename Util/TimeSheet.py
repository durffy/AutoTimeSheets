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
        """
        for the hours in a time sheet
        if(underFiftySixHours()):
            iterate by 8 until you cant and iterate the day
        then iterate by the extra hours left in the day

        """
        weekday = 0
        extra_time = self.hours % 8
        daily_total = 0
        while self.hours != 0:

            if(self.hours % 8 == 0):
                print("Divisible by 8")
                self.hours = self.hours - 8
                daily_total = 8
            elif(self.hours % extra_time ==0):
                print("Divisible by {}".format(extra_time))
                self.hours = self.hours - extra_time
                daily_total = extra_time
            else:
                self.hours = 0

            print(self.hours)
            default_times = self.setDefaultTimes()
            default_time_list = []

            default_time_list.append(self.__workweek[weekday])
            if(weekday <= 4):
                weekday += 1

            for e in default_times.getTimeList():
                default_time_list.append(e)
            default_time_list.append(daily_total)

            self.destination_ws.append(default_time_list)
            self.destination_ws.append([""])



    def setTimeSheetFooter(self):

        self.destination_ws.append(["", "", "", "", "", "Total", self.hours])

    def setDefaultTimes(self):
        defaultTimeEntry = TimeEntry()
        defaultTimeEntry.setDefaults()
        return defaultTimeEntry

