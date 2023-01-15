from bs4 import BeautifulSoup as bs
import requests
from seleniums import get_sourse_html

resp = "/Сири_тверді" #/Крупа_рис

def send_message(resp):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0"
    }

    url_rozet = "https://rozetka.com.ua/ua"
    url2_rozet = None

    url_prom = 'https://prom.ua/ua'
    url_prom2 = None

    url_proz = 'https://www.dzo.com.ua/tenders/catalog/products'
    url_proz2 = None
    # #### boroshno, crupy ta makaronni vuroby ##### #
    if resp == "/Крупа_гречана":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=grechka/"
        url_prom2 = "/Grechnevaya-krupa?a14146=265707&sort=price"
        url_proz2 = "/1561-GREC-9923595940791-235012"
    elif resp == "/Крупа_рис":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=ris/"
        url_prom2 = "/Risovaya-krupa?a14146=265707&sort=price&a5__lte=39&a5__gte=1"
        url_proz2 = "/1561-AAAA-9920238645211-000000"
    elif resp == "/Крупа_булгур":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=bulgur/"
        url_prom2 = "/Bulgur?a5__gte=1&sort=price"
        url_proz2 = "/1561-BULG-9919949519928-297774"
    elif resp == "/Крупа_кукурудзяна":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=kukuruznaya-krupa/"
        url_prom2 = "/Kukuruznaya-krupa?a5__gte=1&sort=price"
        url_proz2 = "/1561-MRIYA-9911791886579-522220"
    elif resp == "/Крупа_вівсяна":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=ovsyanka/"
        url_prom2 = "/Ovsyanaya-krupa?a14146=265707&a14146=265709&sort=price&a5__gte=1"
        url_proz2 = "/1561-AAAA-9921354117095-000000"
    elif resp == "/Крупа_перлова":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=perlovaya-krupa/"
        url_prom2 = "/Perlovaya-krupa?a5__gte=1&sort=price"
        url_proz2 = "/1561-PERL-9933522194272-034588"
    elif resp == "/Крупа_пшенична":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=pshenichnaya-krupa/"
        url_prom2 = "/Psheno?a5__gte=1&sort=price"
        url_proz2 = "/1561-AAAA-9921769073559-000000"
    elif resp == "/Крупа_пшоно":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=psheno/"
        url_prom2 = "/Pshennaya-krupa?sort=price&price_local__gte=26"
        url_proz2 = "/1561-MRIYA-9932213815724-705342"
    elif resp == "/Крупа_ячнева":
        url2_rozet = "/krupy/c4628397/sort=cheap;ves147016=501-g-750-g;vid-225787=yachnevaya-krupa/"
        url_prom2 = "/Yachnaya-krupa?a5__gte=1&sort=price"
        url_proz2 = "/1561-YACH-9970049332701-102357"
    elif resp == "/Макаронні_вироби":
        url2_rozet = "/makaronnie-izdeliia/c4627666/sort=cheap;ves147016=1-1-kg-3-kg,3-1-kg-10-kg,501-g-750-g/"
        url_prom2 = "/Makaronnye-izdeliya?a4761=189711&a5__gte=2&sort=price&a228=7399"
        url_proz2 = "/1585-AAAA-9903755084015-000000"
    elif resp == "/Борошно_І_гатунку":
        url2_rozet = "/muka/c4628446/sort-101987=pervyj;vid-101980=pshenichnaya-iz-myagkikh-sortov-pshenicy/"
        url_prom2 = "/Muka?a14133=143034&a12164=120138&sort=price"
        url_proz2 = "/1561-AAAA-9912374736632-000000"
    elif resp == "/Олія":
        url2_rozet = "/rastitelnoe-maslo-sousi-pripravi/c4633009/obem-96146=bolshe-2;sort=cheap;ves147016=1-1-kg-3-kg,3-1-kg-10-kg/"
        url_prom2 = "/Maslo-rastitelnoe?a13541=156662&a1559=106280&a128__gte=4000&sort=price"
        url_proz2 = "/1542-OLDI-4820128880164-498354"
        # #### conserwacia ##### #
    elif resp == "/Горошок_консервований":
        url2_rozet = "/ovoschnaya-konservaciya/c4628061/sort=cheap;tip-97717=goroshek/"
        url_prom2 = "/Ovoschnaya-konservatsiya?a16919=199663&sort=price"
        url_proz2 = "/1533-ECON-4820049140033-145118"
    elif resp == "/Овочева_ікра":
        url2_rozet = "/ovoschnaya-konservaciya/c4628061/sort=cheap;tip-97717=ovoschnaya-ikra/"
        url_prom2 = "/Ovoschnaya-konservatsiya?a16919=199459"
        url_proz2 = "/1533-DARY-4820039710352-012966"
    elif resp == "/Огірки_консервовані":
        url2_rozet = "/ovoschnaya-konservaciya/c4628061/sort=cheap;tip-97717=ogurcy/"
        url_prom2 = "/Ovoschnaya-konservatsiya?a16919=199461&sort=price&a5__gte=2"
        url_proz2 = "/1533-TOMA-4820196560074-487659"
    elif resp == "/Помідори_консервовані":
        url2_rozet = "/ovoschnaya-konservaciya/c4628061/sort=cheap;tip-97717=tomaty;upakovka147152=steklyanaya;vid-216260=v-marinade/"
        url_prom2 = "/Ovoschnaya-konservatsiya?sort=price&a5__gte=3&a16919=199453&a1559=189866"
        url_proz2 = "/1533-ZOLO-4820061300378-599488"
        # #### med, djem #### #
    elif resp == "/Мед":
        url2_rozet = "/med/c4645608/sort=cheap;ves147016=1-1-kg-3-kg,3-1-kg-10-kg/"
        url_prom2 = "/Med?a1559=106280&a18326__gte=1000&sort=price"
        url_proz2 = "/0314-AAAA-9920978246945-000000"
    elif resp == "/Джем":
        url2_rozet = "/djemy-i-vareniya/c4626718/tip-87004=424570;ves147016=1-1-kg-3-kg,501-g-750-g/"
        url_prom2 = "/Varene?a714=199418&a5__gte=1"
        url_proz2 = "/1533-AAAA-4823105402144-000000"
    # ### miaso ruba ta suput prod #### #
    elif resp == "/Конс_рибна_Бички":
        url2_rozet = "/rybnye-konservy-i-moreprodukty/c4628075/sort=cheap;upakovka147152=metallicheskaya;vid-ryby-97871=bichki/"
        url_prom2 = "/Rybnye-konservy?a14646=153536&sort=price"
        url_proz2 = "/1524-AAAA-4820065706923-000000"
    elif resp == "/Конс_рибна_Сардина":
        url2_rozet = "/rybnye-konservy-i-moreprodukty/c4628075/sort=cheap;upakovka147152=metallicheskaya;vid-ryby-97871=sardina/"
        url_prom2 = "/Rybnye-konservy?sort=price&a14646=153649&a1559=137548"
        url_proz2 = "/709c8ded01804054adfe062d3777e960"
    elif resp == "/Мясо_курки":
        url2_rozet = "/myaso/c4632859/chast=golen;tip131404=kuritsa/"
        url_prom2 = "/Myaso-salo-myasnye-izdeliya?a10868=188987&a714=188997&sort=-score"
        url_proz2 = "/1511-KURI-9913719466931-719466"
    elif resp == "/Риба_Хек":
        url2_rozet = "/riba-i-moreprodukti/c4672173/tip-242318=riba;vid-ribi-242328=hek/"
        url_prom2 = "/Ryba-morozhenaya?a14646=153673"
        url_proz2 = "/1522-FISH-9927353546980-603735"
    # #### specii ##### #
    elif resp == "/Лавровий_лист":
        url2_rozet = "/spetsii-i-pripravy/c4645648/sort=cheap;tip-176388=lavroviy-list;ves147016=1-1-kg-3-kg,101-g-300-g,501-g-750-g/"
        url_prom2 = "/Pryanosti-spetsii-pripravy?sort=price&a16728=190818"
        url_proz2 = "/1587-LAVR-9981353151605-523478"
    elif resp == "/Гірчичий_порошок":
        url2_rozet = "/spetsii-i-pripravy/c4645648/sort=cheap;tip-176388=gorchitsa;ves147016=1-1-kg-3-kg,101-g-300-g,501-g-750-g/"
        url_prom2 = "/Pryanosti-spetsii-pripravy?sort=price&a16728=190810"
        url_proz2 = "/1587-MUST-9911253111393-402530"
    elif resp == "/Перець_мелений":
        url2_rozet = "/perets/c4649310/sort=cheap;tip-216295=molotiy;ves147016=1-1-kg-3-kg,101-g-300-g,501-g-750-g;vid-pertsa=perets-cherniy/"
        url_prom2 = "/Pryanosti-spetsii-pripravy?a16728=190830&sort=price"
        url_proz2 = "/1587-MRIY-4820005021062-166690"
    elif resp == "/Сіль":
        url2_rozet = "/sol/c4649298/sort=cheap;tsvet-176334=belaya;ves147016=1-1-kg-3-kg,3-1-kg-10-kg,501-g-750-g/"
        url_prom2 = "/Povarennaya-sol?a714=170123&a5__gte=1&sort=price"
        url_proz2 = "/bc8cec6481a64142af6ef532876e4026"
    elif resp == "/Цукор":
        url2_rozet = "/sahar/c4625039/tip-sakhara-71651=298122;ves147016=1-1-kg-3-kg,3-1-kg-10-kg,501-g-750-g;vid-71413=sakhar-pesok/"
        url_prom2 = "/Sahar?a5308=200010&a5__gte=1&sort=price&price_local__gte=33&a16952=200044"
        url_proz2 = "/1583-AGRO-9915650995105-748347"
    # ### khlib ta suput prod ### #
    elif resp == "/Хліб_пшен":
        url2_rozet = "/hlebobulochnie-izdeliya/c4644304/sort=cheap;tip156192=pshenichniy;vid-225763=hleb/"
        url_prom2 = "/Hleb-?a18352=265815&a714=207799"
        url_proz2 = "/1581-MYZY-4820209500615-109109"
    # ### ovochi ### #
    elif resp == "/Картопля":
        url2_rozet = "/ovoshchi/c4655054/sort=cheap;ves147016=1-1-kg-3-kg,3-1-kg-10-kg,501-g-750-g/"
        url_prom2 = "/Sushenye-ovoschi?a12164=118843&a12068=160111"
        url_proz2 = "/0321-LOBA-9999132434139-291088"
    # ### molochna prod ### #
    elif resp == "/Сири_тверді":
        url2_rozet = "/siri4645472/c4645472/girnost=1472264;sort=cheap;tip-218821=tverdie-siri;tip-sirya158904=korove/"
        url_prom2 = "/Syry?a714=198992&a16795__gte=50&sort=price&a16795__lte=50"
        url_proz2 = "/1554-RADY-9917729579032-072851"
    elif resp == "/Масло_вершкове":
        url2_rozet = "/slivochnoe-maslo/c4645960/girnost=3193261;ves147016=1-1-kg-3-kg/"
        url_prom2 = "/Maslo-slivochnoe-1?a13759__gte=73&sort=price&a5__gte=1000"
        url_proz2 = "/1553-AAAA-9958740000792-000000"


    # ROZETKA parcer
    rozetka = url_rozet+url2_rozet
    page = requests.get(rozetka)
    result_rozetka = bs(page.text, "html.parser")
    search_sort_rozetka = []
    search_r = result_rozetka.findAll("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
    search_sort_rozetka.append('\n<<Rozetka>>:')
    for item in search_r:
        s = item.find("a", class_="goods-tile__heading ng-star-inserted")
        name = s.text
        try:
            p = item.find("span", class_="goods-tile__price-value")
            price = p.text
        except:
            price = " 0.00 "
        mess_rozetka = (f'{name}-{price}грн.')
        search_sort_rozetka.append(mess_rozetka)

    # PROM UA parser
    prom = url_prom+url_prom2
    page_p = requests.get(prom)
    result_prom = bs(page_p.text, "html.parser")
    search_sort_prom = []
    search_p = result_prom.findAll("div", class_="M3v0L DUxBc sMgZR _5R9j6 qzGRQ IM66u J5vFR hxTp1")
    search_sort_prom.append("\n<<Prom>>:")
    for item in search_p:
        sp = item.find("span", class_="_3Trjq htldP _7NHpZ h97_n")
        name_prom = sp.text
        try:
            pp = item.find("span", class_="_3Trjq aeJVe")
            price_prom = pp.text
        except:
            price_prom = " 0.00 "
        mess_prom = (f' {name_prom} - {price_prom} грн.')
        search_sort_prom.append(mess_prom)

    # PROZORRO parser
    prozorro = url_proz+url_proz2
    page_prz = requests.get(prozorro, headers=headers)
    rezult_prozorro = bs(page_prz.text, "html.parser")
    search_sort_prozorro = []
    search_prz_label = rezult_prozorro.find("div", class_="wide-grid-item-description")
    search_prz = rezult_prozorro.findAll("div", class_="offerItem clear")
    search_sort_prozorro.append("<<Prozorro market>>:")
    search_sort_prozorro.append(search_prz_label.text)
    for item in search_prz:
        sprz = item.find("div", class_ = "name")
        name_proz = sprz.text
        try:
            pprz = item.find("div", class_ = "price")
            price_proz = pprz.text[:6]
        except:
            price_proz = " 0.00 "
        mess_proz = (f' {name_proz} - {price_proz}грн.')
        search_sort_prozorro.append(mess_proz)
    # proZorro ver 2
    """
    prozorro = url_proz + url_proz2
    search_sort_prozorro = []
    search_sort_prozorro = get_sourse_html(prozorro)
    """
    message = 'Чудовий вибір \n\n'

    for i in search_sort_prozorro[:16]:
        message = message+(f'{i}\n')

    for i in search_sort_prom[:16]:
        message = message+(f'{i}\n')

    for i in search_sort_rozetka[:16]:
        message = message+(f'{i}\n')
    return message
    #print(message)

#send_message(resp)
