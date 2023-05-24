from src.lib import *

SAVE_PATH = f"C:/Users/vodin/Documents/Stock-Data-Crawling/data/Minkabu"
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--headless")
PATH = "C:\chromedriver.exe"

def SaveData(table,code):
    table.to_csv(f"{SAVE_PATH}/{code}.csv")

def FindTable(driver,html,selector):
    soup = BeautifulSoup(html,'html.parser')
    table = soup.select_one(selector)
    table = pd.read_html(str(table))
    return table

def ScrollAndClick(button,driver):
    button.click()
    time.sleep(0.5)
    driver.execute_script("window.scrollTo(0, window.scrollY + 300)")
    time.sleep(0.5)

def GetDataMinkabu(code):
    URL  = f"https://minkabu.jp/stock/{code}/daily_bar"
    driver = webdriver.Chrome(PATH,options=chrome_options)
    driver.get(URL)
    show_more = driver.find_element(By.XPATH,'//*[@id="contents"]/div[3]/div[2]/div/div/p/a')
    for i in range(10000):
        try:
            ScrollAndClick(show_more,driver)
        except:
            break
    html = driver.page_source
    # time.sleep(3)
    table = FindTable(driver,html,"#fourvalue_timeline")
    
    SaveData(table[0],code)

    driver.quit()

    print(f"Code: {code} Done!")
