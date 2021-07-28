"""
This should build a time sheet based on the number of hours provided
"""
from Util.ExtraTimeEntry import ExtraTime
from Util.TimeEntry import TimeEntry


class TimeSheet():
    __workweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    def __init__(self, destination_ws, name, date, hours):
        self.destination_ws = destination_ws
        self.name = name
        self.date = date
        self.hours = hours
        self.total_hours = hours
        self.setTimeSheetHeader()
        self.setTimeSheetHours()
        self.setTimeSheetFooter()

    def setTimeSheetHeader(self):
        self.destination_ws.append(["Name", self.name])
        self.destination_ws.append(["Date", self.date])
        self.destination_ws.append(["Day", "In", "Out", "Lunch", "In", "Out", "Total"])

    def setTimeSheetHours(self):

        weekday = 0
        daily_total = 0
        if (self.total_hours > 80):
            print("date: {}, name: {}, hours: {}".format(self.date, self.name, self.hours))
            base_hour = 13
        elif (self.total_hours > 72):
            print("date: {}, name: {}, hours: {}".format(self.date, self.name, self.hours))
            base_hour = 12
        elif (self.total_hours  > 64):
            print("date: {}, name: {}, hours: {}".format(self.date, self.name, self.hours))
            base_hour = 11
        elif (self.total_hours  > 56):
            print("date: {}, name: {}, hours: {}".format(self.date, self.name, self.hours))
            base_hour = 10
        elif (self.total_hours  > 48):
            print("date: {}, name: {}, hours: {}".format(self.date, self.name, self.hours))
            base_hour = 9
        else:
            base_hour = 8

        extra_time = self.hours % base_hour

        while self.hours != 0:

            if(self.hours % base_hour == 0 or self.hours >= base_hour):
                self.hours = self.hours - base_hour
                daily_total = base_hour

            elif(self.hours % extra_time == 0):
                self.hours = self.hours - extra_time
                daily_total = extra_time


            time_entry = ExtraTime(daily_total)
            default_times = time_entry.getTimeEntry()
            default_time_list = []


            if(weekday <= 5):
                default_time_list.append(self.__workweek[weekday])
                weekday += 1
            else:
                default_time_list.append("Sunday")

            for e in default_times.getTimeList():
                default_time_list.append(e)
            default_time_list.append(daily_total)

            self.destination_ws.append(default_time_list)
            self.destination_ws.append([""])

        while (weekday <= 4):
            weekday += 1
            self.destination_ws.append([self.__workweek[weekday]])
            self.destination_ws.append([""])



    def setTimeSheetFooter(self):

        self.destination_ws.append(["", "", "", "", "", "Total", self.total_hours])
        self.destination_ws.append([""])
        self.destination_ws.append([""])

    def setDefaultTimes(self):
        defaultTimeEntry = TimeEntry()
        defaultTimeEntry.setDefaults()
        return defaultTimeEntry

