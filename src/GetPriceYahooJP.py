from src.lib import *

today = date.today()
# SAVE_PATH = f"C:/Users/vodin/Documents/Stock-Data-Crawling/data/YahooJP"
past = "19500101"
now = today.strftime("%Y%m%d")

def SaveData(df,code,SAVE_PATH):
    df.to_csv(f"{SAVE_PATH}/{code}.csv")

def FindTableSinglePage(html):
    df = pd.read_html(html.text,flavor='bs4',attrs={"class":"_13C_m5Hx _1aNPcH77"})[0]
    return df

def GetUrl(page,code):
    return f"https://finance.yahoo.co.jp/quote/{code}.T/history?from={past}&to={now}&timeFrame=d&page={page}"

def GetRequest(URL):
    waiting = True
    while waiting: #get again if page isn't respone
        try:
            html = requests.get(URL)
            waiting = False
        except:
            time.sleep(3)
    return html

def GetDataYahooJP(code,SAVE_PATH):
    df_all = pd.DataFrame()
    for page in range(1,10000):
        URL = GetUrl(page,code)
        
        html = GetRequest(URL)

        try: #get table
            df_single = FindTableSinglePage(html)
            df_all = pd.concat([df_all, df_single], ignore_index=True).reset_index(drop=True)
        except:
            break
    
    SaveData(df_all,code,SAVE_PATH)

    print(f"Code: {code} Done!")