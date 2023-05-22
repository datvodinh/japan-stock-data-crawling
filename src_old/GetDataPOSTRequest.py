from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import time

def GetAllData(id):
    PATH = f"https://s.cafef.vn/Lich-su-giao-dich-{id}-1.chn/"
    header = {
        "Accept": "*/*",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,vi;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "3925",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "ASP.NET_SessionId=ghfb42zglbxqvtwedzbuzri4; __uidac=0218b159daa72e6ea3841f6fcf96edd8; favorite_stocks_state=1; CONSENT=YES+",
        "DNT": "1",
        "Host": "s.cafef.vn",
        "Origin": "https://s.cafef.vn",
        "Referer": f"https://s.cafef.vn/Lich-su-giao-dich-{id}-1.chn/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
        "X-MicrosoftAjax":"Delta=true",
        "X-Requested-With": "XMLHttpRequest",
    }

    df = pd.DataFrame()
    running = True
    page = 1
    while running:
        try:
            time.sleep(0.05)
            data = f"ctl00%24ContentPlaceHolder1%24scriptmanager=ctl00%24ContentPlaceHolder1%24ctl03%24panelAjax%7Cctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTTARGET=ctl00%24ContentPlaceHolder1%24ctl03%24pager2&__EVENTARGUMENT={page}&__VIEWSTATE=quzQU5MILXtrIL%2FVE5rDWeALCv34eBs2EVZuQS3ckI43uIASjwweaj2k2oW09OlifgVHomWVW86mJ6DD%2BFmUeMig%2Ft0s1H%2BUb4BSvDhqzGVvHNRndUra7Ti9eXvI5MZ7BxHT8PaW%2BMyChw3MQcczO8n7Xq96Z2CVMx2gCxpueIYEmiTX%2FFglp4xJUWgAyOtO%2FbXXf4nYJ%2F10Bd5RvZi0sJu1xItbZLYuBcj%2Fy6UmaiqXm%2Feo5AakpMvkH5F8EynEcSXS2sTySV4fxawLQpva%2BbdRL1STRUM68hPh841epNvtLh2Vpp2irIUTcEe1%2FHUj04g6L6v5VOaoYdoILsLggJDYcBUN8o1ZS2KNy9J7nvQs%2B3WHpdTHgT05hMIUT5Jto1FREL7RRdo9n2zJydyNMASmMXyg0tQZD6GvOEm3cU4gkKWK5tEWou9M1sOrHm0WUBqBBapEJhRCyIzfOGUs%2FC4mLxqlG79H%2BcMQjykZcvPTBPNSire4PS4qdOBZ0P7N%2B0bjL%2BWjuzcwCGMkbWTMvdW1KoK9s%2FKR3Y3kY%2Fw5dJRZ%2FgasBty59jo2eOq1bWuRQg0K70YRG49pWnpowFuA8kbNJwPkbVCq8008%2BGg3MkPGzZg0CDoQsYfDCRpJm%2FXzDisEGAHHiTVqXBgxhZ62yJ900W99uUUk7Yj8RJILYWLjpfCH3PaRbIxXx1hQKylk44Frd22E4OLcMHe50r%2BHd6y0ECcjUWCwLwVkhtd3hkAY%2BV9qXjupX%2BDLGbAtUAI8YGURqtKtYVlqEyrVJB%2FSePvYNEEs0WRgmCHkQayuxNqTOKyQr7FLVVzgyRqwKbBUidj5cVnTSOeIhp8JKTxFfbPGmPGPFqXLEuYmjVQVGwfkLhY1RTO6dBKK8SLwslvoIiMt%2BrEahIKKqACxjY9k0rVnJ8iYJsuoN%2FofZzj142Olb%2FKdzhRopIac7iPoynTg5a5qX1DpYO%2B%2FEQgyWBXvLVypMu3f5DkyBppDXxwQIy9TW6yw6qO%2BclXMdeLIa958r9JbqOiBSkQylxcOd1gnRZyUi%2BYSBeisrTVONYcfPBO%2Fy0R84KrxS8MEQwugIz%2BT7dQYKmnKt3HSuPVz0Bq8VDamKqLi6PlnyrQB5ndd1SvKliDeQowmi%2BxN94bhq8w9nrbVVQxHuDCfD6Tv8e8zwKjtjtv8TYz%2Benxc0quddh8ObnYhKslPo61QRB8sgHeSBCpykF7JDcIw4LPmbmmc7GhXX70FavK8lnydD8lx%2F14lzNMFzImKVrQ8OlviqV6%2FVCv%2F6PzLwBwQ%2FOMxsRcdxFdbKWya4BOmipv%2BNg55SpnVmpX1NflICEF%2FswRwIEJ3p2XTHQZq6Fp7BcJd%2B9MboGZhZ%2FeHb2%2BvKWCAYvEDqt1uzbr7qm1wEf%2FaXvVEOXx8JDUOeIjly%2B4LuZVGIaEKmPWb8YxkUk8WUFuQJfeZ3cU%2FzwhoRctvbovCayMyC%2FFd9rCk0RJoJGTflThxwm1uGjgb8azSp0%2BqrS4lDNI5o4k6kPpmajSRrQQyXfdjHrkKG1U2%2B0araBefTc5j9uwjUwD611HKUcnAlmChs4jZuYi6MXre9NhnLTtR3%2FYeu%2FfNG%2FidyM8auucPdmS3wQ4fAEnBlyJdaKbGmYmd7Cvm%2FQ%2BZnTxQdYluBeioHaywEfoa8IW0T6QnYCZuTI1MKZ2C%2FM9%2FMErrVcD2UC4VS5i0CaA8uzMDKLHTqIqBz6BHUwhjPoIar0%2FpLshqAFmfKFpF%2BcrKV%2FD8TmZnFHUNkVCvLOrTPRowM0Pm9kkYazn9OK1fl0emM%2BBv%2B4aC9Q4xqODTQlQh4y6Cp5xw%2Fp2lQRjicIIxaeabvZUir00qFrxJVl2TFjPxeEkFJGiL5yytAdfcbZWneRT0zql0nS%2Bt8%2F7wvLT0C2SjdL6xqoqI5846vzFqGyh31TYy%2BUu2B0tz0lgy4fEI5jko5fH%2BHFptduSOsey4uylzW9KrYpIaPIPqonQlfygkxHYDoNzep6twOg8bD4D1YBp8gJnHooVRipQYLdmsR%2Bi73sL%2F%2Be2CXrWL3H1aY93o3WzKOD%2FpP5Q3n9fEKB%2F6c0ZuH%2Fn7DX%2FIDPjotezAiN4UFTfp%2BPe8HgSidbGoBOEfCh2e7121yqOuKdE1D0VUPf5iOuI92m6tqvfuA2m54ewOK8KpCIsUCBVr6dPUYM95%2BqTHOLJMZwyMFZeclMYQUSENB4MJGFkTI%2FH%2BN5%2B7KCOIKiV3QDIgAReNGRrPYLuYWGVVuLxB5IrWIYOD8nl9YpH2%2Fb0qzq9V1XQYuzrXL4oMcoaE9mjUhQiJ2fh6wzUbvckdLNETdzddMb%2FWhq%2BtL9Im5O4pquwN8dfWyKNPdQ29SVzaTTKisXWVQTXeDViHfBPvc%2BMBMFb%2Bi%2BgdNxm79n7ww95hEoVMvJpD30EixE%2FqeVg691iQELAP16u21xzewi300XZBhglsLFh1%2Bo1CVtVoecIWAZZH5DqrcqU7IBiLqFY4I14AAzLNNjm21oGFYxdqteU0w9avPI4uXRDDnq2J2h59j8nKdaWEm%2FRtANmLrOUstVZMW%2BMlkqzYcw8FrlMnIy1Hy%2FLLLKYiOTW5IvIGKSDpnB53fLClLGgayOvP4bOJehcLKuUkNpukrQ6iUEfgYBaM%2Fg5QF4mp%2BGg8mHYpKJOtY2D5ZL77rVti84T2omlORkWdRqRGxSLyB7mGc5KduEAFYgcqn76SqBUZ5zSQyk2OzvUs02r%2BAUZMihchqke2tkrqJbeXlRw7hgqxiFx5fMP7v8ZwvBqFS4gAKJzLmC3b6WGjzHE%2FXbqb%2FvV%2FjR3mi4BqPlQWZY3RlzoPgLwpoZomXjkSGI3huqSEFmrRndvc4hHSpxIOKC9P8NOXiW5guTpVvZMFOE%2BtVXL5ksMAl2ldpKurTdnuVsqtc5%2BxJ%2FKmE%2BYKHou%2Bq2s8mhWBEtYiVJ4UB1YLCUXRwonIEzv0%2FOQEUysk9fGKcBrX%2BSEwjdlRHyDsBCzUVqQmMaKymm%2Ffzhg7BGQ8FEgSPzDyCPGU5Mji8Wx3abk79AFyKvdx36Clbq2smmBH2QxOhspsoQddyah%2FtfGDwwr%2FwylX2JTAbUlZ%2BKr0cVaVcutz43pwMQjZx42FFKnCuV%2BBbDLtTqfeuckG7DvFB%2BZj%2BnHk5b%2F6gFgaP60F3blThl3FoDJlCElgQthewX1kCl239KqE5AZoAuFZ1e7G3mhslsAElZP0lVjWLx3bQ%2BR9NBKE898%3D&ctl00%24ContentPlaceHolder1%24ctl03%24txtKeyword=DLG&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate1%24txtDatePicker=&ctl00%24ContentPlaceHolder1%24ctl03%24dpkTradeDate2%24txtDatePicker=&__VIEWSTATEGENERATOR=2E2252AF&__ASYNCPOST=true&"
            html = requests.post(PATH,headers=header,data=data,timeout=1000)
            print(html.text)
            df_list = pd.read_html(html.text,flavor='bs4',attrs = {'id': 'GirdTable2'})
            if page>1000:
                running = False
            elif len(df)==0:
                df = df_list[0]
                # print(df)
            else:
                df = pd.concat([df, df_list[0]], ignore_index=True).reset_index(drop=True)
                print(page,end=" ")
                page+=1
        except:
            print('Try again after 1s')
            time.sleep(1)
    
    df = df.drop_duplicates(keep='first')
    df.to_csv(f"/data/{id}_data.csv")

GetAllData('HLG')