"""
This script retrieves and processes weather data

Usage: 
Authos: Egoitz Martinez-Laserna
"""
import pandas as pd

class Weatherdata:
    def __init__(self):
        self.location = 'Gasteiz'
        self.inidate = '2020-01-01T00:00:00'
        self.endate = '2023-11-11T00:00:00'

    def querydata(self):

        return
    
    def process_fromfile(self, filename):
        df = pd.read_csv(filename)
        