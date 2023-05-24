from src.lib import *

SAVE_PATH = f"C:/Users/vodin/Documents/Stock-Data-Crawling/data/MarketWatch"
today = date.today()
# dd/mm/YY

current_date_month = today.strftime("%m/%d")

def SaveData(data,path,code):
    with open(f'{path}/{code}.csv','w') as file:
        for line in data:
            file.write(line)
            file.write('\n')

def GetPathDataByYear(year,code):
    waiting = True
    while waiting:
        # try:
        d_start = current_date_month + f'/{year-1}'
        d_end = current_date_month + f'/{year}'
        link = f"https://www.marketwatch.com/investing/stock/{code}/downloaddatapartial?startdate={d_start}%2000:00:00&enddate={d_end}%2000:00:00&daterange=d30&frequency=p1d&csvdownload=true&downloadpartial=false&newdates=false&countrycode=jp"
        PATH = urllib.request.urlretrieve(link)[0]
        waiting = False
        # except:
        #     time.sleep(3)
    return PATH

def GetDataMarketWatch(code): 
    running = True
    year = 2023
    list_data = ['Date,Open,High,Low,Close,Volume']
    len_old = len(list_data)
    while running:
        PATH = GetPathDataByYear(year,code)
        with open(PATH,'r') as f:
            data = f.read()
        data = data.split("\n") 
        data.pop(0)
        try:
            data.remove("")
        except:
            pass
        list_data+=data
        year-=1
        # print(year)

        if len_old == len(list_data): #dont have any new data
            running = False
        else:
            len_old = len(list_data)

    list_data = list(dict.fromkeys(list_data)) #remove duplicate

    SaveData(list_data,SAVE_PATH,code)

    print(f"Code: {code} Done!")