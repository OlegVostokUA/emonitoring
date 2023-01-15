import time
from bs4 import BeautifulSoup as bs
from selenium import webdriver

def get_sourse_html(url):
    driver = webdriver.Chrome(
        executable_path="C:/Users/User/PycharmProjects/parser/chromedriver.exe"
    )
    driver.maximize_window()

    try:
        page_p = driver.get(url=url)
        time.sleep(1)
        with open("proz.html", "w", encoding='utf-8') as file:
            file.write(driver.page_source)
        time.sleep(1)
        with open("proz.html", 'r', encoding='utf-8') as file_r:
            page_prz = file_r.read()
            rezult_prozorro = bs(page_prz, "html.parser")
            search_sort_prozorro = []
            search_prz = rezult_prozorro.findAll("div", class_="ProductListStyles__Wrapper-zjrl76-4 bbGOMS")
            search_sort_prozorro.append("Prozorro:")
            for item in search_prz:
                sprz = item.find("a", class_ = "ProductListStyles__ProductLink-zjrl76-2 gsYoTt")
                name_proz = sprz.text
                try:
                    pprz = item.find("span", class_ = "Price__AmountWrapper-jq82it-4 fOrgfA")
                    price_proz = pprz.text
                except:
                    price_proz = " 0.00 "
                mess_proz = (f' {name_proz} - {price_proz}.')
                search_sort_prozorro.append(mess_proz)
            #print(search_sort_prozorro)
        return search_sort_prozorro
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


#get_sourse_html(url="https://zakupki.prom.ua/ru/ecatalog/gov/list/5e7b43eaa163e12f902a1965/5e7b43eaa163e12f902a1964")

