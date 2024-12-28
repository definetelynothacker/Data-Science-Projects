import pandas as pd
import matplotlib.pyplot as plt

dataDictionary = {i: 0 for i in range(0, 37)}
numbers: int = []
df = pd.read_csv('filename')
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
makeBarGraph()