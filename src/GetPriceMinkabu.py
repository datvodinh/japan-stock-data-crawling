from lib import *

# SAVE_PATH = f"C:/Users/vodin/Documents/Stock-Data-Crawling/data/Minkabu"
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
# chrome_options.add_argument("--headless")
PATH = "C:\chromedriver.exe"

def SaveData(table,code,SAVE_PATH):
    table.to_csv(f"{SAVE_PATH}/{code}.csv")

def FindTable(html,selector):
    soup = BeautifulSoup(html,'html.parser')
    table = soup.select_one(selector)
    table = pd.read_html(str(table))
    return table

def ScrollAndClick(button,driver):
    button.click()
    time.sleep(0.1)
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")

def GetDataMinkabu(code,SAVE_PATH):
    URL  = f"https://minkabu.jp/stock/{code}/daily_bar"
    driver = webdriver.Chrome(PATH,options=chrome_options)
    driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
    driver.get(URL)
    try:
        show_more = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[1]/div[3]/div[1]/div/div/p/a')
    except:
        show_more = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[4]/div[1]/div[1]/div[3]/div[2]/div/div/p/a')
    for i in range(10000):
        waiting = True
        c = 0
        done = False
        while waiting:
            try:
                ScrollAndClick(show_more,driver)
                waiting = False
            except:
                c += 1
                # print(c)
                if c >50:
                    waiting = False
                    done = True
        if done:
            break
    html = driver.page_source
    # time.sleep(3)
    table = FindTable(html,"#fourvalue_timeline")
    
    SaveData(table[0],code,SAVE_PATH)

    driver.quit()

    print(f"Code: {code} Done!")

if __name__ == "__main__":
    SAVE_PATH = "C:/Users/vodin/Documents/Stock-Data-Crawling/data/Minkabu"
    GetDataMinkabu("7697",SAVE_PATH)
