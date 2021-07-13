import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hrs= []

    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row['Coffee in ml']))
            sleep_in_hrs.append(float(row['sleep in hours']))
    return {'x':Coffee_in_ml,'y':sleep_in_hrs}

def find_correlation(data_source):
    correlation = np.corrcoef(data_source['x'],data_source['y'])
    print("Correlation is  : ",correlation[0,1])

def plotFig(data_path):
    df = csv.DictReader(data_path)
    fig = px.scatter(df,x='C',y='C')
    fig.show()


def setup():
    data_path = 'Coffee Cups vs hrs of sleep.csv'
    data_source = getDataSource(data_path)
    find_correlation(data_source)
    plotFig(data_path)


setup()
