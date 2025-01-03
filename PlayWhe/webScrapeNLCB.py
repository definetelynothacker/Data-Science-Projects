import requests, csv, time, os, re
from bs4 import BeautifulSoup

baseUrl     = "https://www.nlcbplaywhelotto.com/nlcb-play-whe-results/?drawnumber="
drawStart=9000
drawEnd=10000#there are more but we will stop there
data = [
    ['Draw #', 'Mark #', 'Mark name', 'Time Of Day', 'isVerified', 'Date']
]


def getMarkNum(string: str)->int:
    match = re.search(r'\d+', string)
    if match:
        markNumInt = int(match.group())
    else:
        markNumInt = -1
    return markNumInt
            

def getTimeOfDay(string: str)->str:
    timeOfDay: str = string[23:]
    timeOfDay = timeOfDay.replace("</div>", "")
    return timeOfDay


def getMarkName(string: str)->str:
    markName = string[23:]
    markName = markName.replace("</div>", "")
    return markName


def getIsVerified(string: str)->str:
    isVerified = string[22:]
    isVerified = isVerified.replace("</div>", "")
    return isVerified


def getDate(string: str)->str:
    regex = r'\b\d{2}-[A-Za-z]{3}-\d{2}\b'
    date = re.findall(regex, string)
    return date

def createOrReadFile():
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    csvPath = os.path.join(scriptDir, 'nlcb_res.csv')
    if not os.path.exists(csvPath):
        file = open(csvPath, mode='w', newline='')
        writer = csv.writer(file)
        writer.writerows(data)
        print(f"{csvPath} created!")
    else:
        file = open(csvPath, mode='a', newline='')
        writer = csv.writer(file)
        print(f"{csvPath} already exist, adding data to it.")
    return file, writer

file, writer = createOrReadFile()

def writeToFile(newRow):
    print(newRow)
    writer.writerow(newRow)
    file.flush()


forLoopStartTime = time.time()
for i in range(drawStart, drawEnd):
    try:
        r = requests.get(baseUrl+str(i))
        soup = BeautifulSoup(r.content, 'html.parser')
        v = soup.find(id='results')
        s = soup.find('div', class_='drawDetails')

        if not s:
            print(f"No draw details for draw: {drawStart}")
            newRow = ['000', '000', '000', '000', '000']
            writeToFile(newRow)
            data.append(newRow)
            continue
        
        link = s.find_all('a')
        includesDate = v.find_all('strong')
        if includesDate:
            date = includesDate[0]
        else:
            date = "000"

        tOfD = s.find('div', class_="timeOfDay")
        mN = s.find('div', class_="mark-name")

        if not link or not tOfD or not mN:
            print(f"Missing data for Draw: {drawStart}")
            markNum = 0
        else:
            markNum = getMarkNum(str(link))
            
        timeOfDay = getTimeOfDay(str(tOfD))
        markName = getMarkName(str(mN))
        newDate = getDate(str(date))
        newRow = [str(i), str(markNum), markName, timeOfDay, newDate]
        writeToFile(newRow)
        data.append(newRow)
        #time.sleep(0.25)
    except Exception as e:
        print(f"Error processing Draw: {drawStart}: {e}")
forLoopEndTime = time.time()
file.close()
duration = forLoopEndTime - forLoopStartTime
print(f"Duration of {drawEnd-drawStart} request: {duration}\nDuration of 1 request: {duration/(drawEnd-drawStart)}")
