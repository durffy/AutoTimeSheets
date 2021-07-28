import os

import openpyxl
from openpyxl import Workbook
from pathlib import Path

#Contains the worksheet, the names, and hours

class Worksheet:

    def __init__(self, worksheet, names, date, hours):
        self.worksheet = worksheet
        self.names = names
        self.date = date
        self.hours = hours

    def addNames(self, name):
        self.names.append(name)

    def addHours(self, hours):
        self.hours.append(hours)

