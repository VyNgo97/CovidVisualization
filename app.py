import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv

with open('COVID-19Cases.csv') as covid_data:
    data_reader = csv.reader(covid_data, delimiter=',')
    line_count = 0
    for row in data_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            pass