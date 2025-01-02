import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

dataDictionary = {i: 0 for i in range(0, 37)}
numbers: int = []
df = pd.read_csv('nlcb_res.csv')
markNum_data = df['Mark #'].tolist()

#plotting format
categories = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']
#dataDictionary

def calcMean(data: list)->float:
    sum: int = 0
    for num in data:
        sum += num
    return sum/len(data)

def numbersByFrequency(data: list):
    for num in data:
        dataDictionary[num]+=1


def trendAnalysis(dataFrame):
    dataFrame['Date'] = pd.to_datetime(dataFrame['Date'], format='%d-%b-%y', errors='coerce')
    dataFrame = dataFrame.dropna(subset=['Date'])
    dataFrame.set_index('Date', inplace=True)
    monthlyCounts = dataFrame.resample('ME').size()
    monthlyCounts.plot(title="Monthly Counts over Time")
    plt.show()

def distro(df):
    df['Mark #'].hist(bins=30, color='blue', edgecolor='grey')
    plt.title('Distribution of Draw #')
    plt.xlabel('Mark #')
    plt.ylabel('Frequency')
    plt.show()

def makeBarGraph():
    #dataSetSize: int = len(markNum_data)
    frequencyList = list(dataDictionary.values())
    plt.bar(categories, frequencyList)
    plt.title('Mark Number Frequency for # draws')
    plt.xlabel('MarkNum')
    plt.ylabel('Frequency')
    plt.show()


mean = calcMean(markNum_data)
numbersByFrequency(markNum_data)
print(f"Mean: {mean}")
print(f"Number Frequency: {dataDictionary}")
print(dataDictionary)

#Visuallize data
summary = df.describe()
print(summary)
makeBarGraph()
trendAnalysis(df)
distro(df)

