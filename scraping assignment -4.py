#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import warnings
warnings.filterwarnings('ignore')
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd


# # ANSWER-1

# In[2]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos')
time.sleep(3)

RANK=[]
rank=driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[1]')
for i in rank[:30]:
    r=i.text
    RANK.append(r)
VEDIO_NAME=[]
vedio_name=driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[2]')
for i in vedio_name[:30]:
    v=i.text
    VEDIO_NAME.append(v)
UPLODER=[]
uploder=driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[3]')
for i in uploder[:30]:
    u=i.text
    UPLODER.append(u)

VIEWS=[]
views=driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[4]')
for i in views[:30]:
    vi=i.text
    VIEWS.append(vi)
    
UPLOAD_DATE=[]
upload_date=driver.find_elements(By.XPATH, '//table[@class="wikitable sortable jquery-tablesorter"]/tbody/tr/td[5]')
for i in upload_date[:30]:
    ud=i.text
    UPLOAD_DATE.append(ud)
print(len(RANK),len(VEDIO_NAME),len(UPLODER),len(VIEWS),len(UPLOAD_DATE))


# In[3]:


df1=pd.DataFrame({"RANK":RANK,
                 "VEDIO NAME":VEDIO_NAME,
                 "UPLODER":UPLODER,
                 "VIEWS":VIEWS,
                 "UPLOAD DATE":UPLOAD_DATE})
df1


# # ANSWER-2

# In[4]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.bcci.tv/')
time.sleep(3)
# click on international
driver.find_element(By.XPATH,'/html/body/nav/div[1]/div[2]/ul[1]/li[2]/a').click()
time.sleep(3)


# In[5]:


match_title=[]
series=[]
date=[]
place=[]
match_time=[]

Match_title=driver.find_elements(By.XPATH, '//span[@class="matchOrderText ng-binding ng-scope"]')
for i in Match_title:
    m=i.text
    match_title.append(m)
    
Series=driver.find_elements(By.XPATH, '//h5[@class="match-tournament-name ng-binding"]')
for i in Series:
    s=i.text
    series.append(s)
    
Date=driver.find_elements(By.XPATH, '//div[@class="match-dates ng-binding"]')
for i in Date:
    d=i.text
    date.append(d)
    
Place=driver.find_elements(By.XPATH, '//div[@class="match-place ng-scope"]')
for i in Place:
    p=i.text.split("-")[1]
    place.append(p)
    
Match_time=driver.find_elements(By.XPATH, '//div[@class="match-info"]/div[2]')
for i in Match_time:
    mt=i.text
    match_time.append(mt)
print(len(match_title),len(series),len(date),len(place),len(match_time))


# In[6]:


df2=pd.DataFrame({"MATCH TITLE":match_title,
                 "SERIES":series,
                 "PLACE":place,
                  "DATE":date,
                 "MATCH TIME":match_time})
df2


# # ANSWER-3

# In[14]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('http://statisticstimes.com/')
time.sleep(3)
# click on economy india
driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[2]/div[2]/button').click()
driver.find_element(By.XPATH,'//div[@class="navbar"]/div[2]/div/a[3]').click()
time.sleep(3)
# for bypass popup 
driver.back()
time.sleep(3)
driver.forward()
time.sleep(2)
# click on GDP of indian state
driver.find_element(By.XPATH,'/html/body/div[2]/div[2]/div[2]/ul/li[1]/a').click()
time.sleep(3)


# In[15]:


RANK=[]
STATE=[]
GSDP1920=[]
GSDP1819=[]
SHARE=[]
GDP=[]
rank=driver.find_elements(By.XPATH,'//tr[@class="odd" or @class="even"]/td[1]')
for i in rank[:33]:
    r=i.text
    RANK.append(r)
    
state=driver.find_elements(By.XPATH,'//tr[@class="odd" or @class="even"]/td[2]')
for i in state[:33]:
    s=i.text
    STATE.append(s)

gsdp1920=driver.find_elements(By.XPATH,'//tr[@class="odd" or @class="even"]/td[3]')
for i in gsdp1920[:33]:
    g=i.text
    GSDP1920.append(g)

gsdp1819=driver.find_elements(By.XPATH,'//tr[@class="odd" or @class="even"]/td[4]')
for i in gsdp1819[:33]:
    g1=i.text
    GSDP1819.append(g1)

share=driver.find_elements(By.XPATH,'//tr[@class="odd" or @class="even"]/td[5]')
for i in share[:33]:
    sh=i.text
    SHARE.append(sh)

gdp=driver.find_elements(By.XPATH,'//tr[@class="odd" or @class="even"]/td[6]')
for i in gdp[:33]:
    gd=i.text
    GDP.append(gd)


# In[16]:


df3=pd.DataFrame({"RANK":RANK,
                 "STATE":STATE,
                 "GSDP 19-20":GSDP1920,
                 "GSDP 18-19":GSDP1819,
                  "SHARE":SHARE,
                 "GDP(in billion)":GDP})
df3


# # ANSWER-4 

# In[10]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://github.com/')
time.sleep(3)
# click on explore
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/button').click()
time.sleep(2)
#click on trending
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/header/div/div[2]/div/nav/ul/li[3]/div/div[3]/ul/li[2]/a').click()
time.sleep(3)


# In[11]:


REPOSITORY_TITLE=[]
REPOSITORY_DES=[]
CONTRIBUTORS_COUNT=[]
LANGUAGE_USED=[]
repo_urls=[]
repo_links=driver.find_elements(By.XPATH,'//h2[@class="h3 lh-condensed"]/a')
for i in repo_links:
    repo_urls.append(i.get_attribute("href"))
    REPOSITORY_TITLE.append(i.text)
for i in repo_urls:
    driver.get(i)
    time.sleep(2)
    try:
        dis=driver.find_element(By.XPATH,'//p[@class="f4 my-3"]').text
        REPOSITORY_DES.append(dis)
    except:
        REPOSITORY_DES.append(" no discription")
    try:
        lan=driver.find_element(By.XPATH,'//li[@class="d-inline"]/a/span').text
        LANGUAGE_USED.append(lan)
    except:
        LANGUAGE_USED.append("-")
    try:
        count=driver.find_element(By.XPATH,'(//span[@class="Counter ml-1"])[2]').text
        CONTRIBUTORS_COUNT.append(count)
    except:
        CONTRIBUTORS_COUNT.append("-")


# In[12]:


print(len(REPOSITORY_TITLE),len(REPOSITORY_DES),len(LANGUAGE_USED),len(CONTRIBUTORS_COUNT))


# In[13]:


df4=pd.DataFrame({"REPOSITORY TITLE":REPOSITORY_TITLE,
                 "REPOSITORY DISCRIPTION":REPOSITORY_DES,
                 "LANGUAGE USED":LANGUAGE_USED,
                 "CONTRIBUTIORS COUNT":CONTRIBUTORS_COUNT})
df4


# # ANSWER-5

# In[14]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https:/www.billboard.com/')

# click on charts
driver.find_element(By.XPATH,'/html/body/div[3]/header/div/div[2]/div/div/div[2]/div[2]/div/div/nav/ul/li[1]/a').click()
time.sleep(2)
#click on hot 100
driver.find_element(By.XPATH,'/html/body/div[3]/main/div[2]/div[1]/div[1]/div/div/div[1]/div/div[2]/span/a').click()
time.sleep(3)


# In[15]:


RANK=[]
SONG_NAME=[]
ARTIST_NAME=[]
LWR=[]
PEAK_RANK=[]
WOB=[]
try:
    rank=driver.find_elements(By.XPATH,'//span[@class="c-label  a-font-primary-bold-l u-font-size-32@tablet u-letter-spacing-0080@tablet"]')
    for i in rank:
        RANK.append(i.text)
except:
    RANK.append("-")
try:
    name=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li/h3')
    for i in name:
        SONG_NAME.append(i.text)        
except:
    SONG_NAME.append("-")
try:
    a=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[1]/span')
    for i in a:
        ARTIST_NAME.append(i.text)
except:
    ARTIST_NAME.append("-")
try:
    lwr=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[4]/span')
    for i in lwr:
        LWR.append(i.text)    
except:
    LWR.append("-")
try:
    peak=driver.find_elements(By.XPATH,'//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[5]/span')
    for i in peak:
        PEAK_RANK.append(i.text)
except:
    PEAK_RANK.append("-")
try:
    wob = driver.find_elements(By.XPATH, '//ul[@class="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max"]/li[6]/span')
    for i in wob:
        WOB.append(i.text)
except:
    WOB.append("-")


# In[17]:


df5=pd.DataFrame({"RANK":RANK ,
                 "SONG NAME":SONG_NAME,
                 "ARTIST NAME":ARTIST_NAME,
                 "LAST WEEK RANK": LWR,
                 "PEAK RANK":PEAK_RANK ,
                 "WEEKS ON BOARD":WOB})
df5


# # ANSWER-6

# In[18]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.theguardian.com/news/datablog/2012/aug/09/best-selling-books-all-time-fifty-shades-grey-compare')
time.sleep(3)


# In[24]:


RANK=[]
BOOK_NAME=[]
AUTHOR_NAME=[]
VOLUMES_SOLD=[]
PUBLISHER=[]
GENRE=[]
try:
    rank=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[1]')
    for i in rank:
        RANK.append(i.text)
except:
    RANK.append("-")
try:
    book=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[2]')
    for i in book:
        BOOK_NAME.append(i.text)
except:
    BOOK_NAME.append("-")
try:
    author=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[3]')
    for i in author:
        AUTHOR_NAME.append(i.text)
except:
    AUTHOR_NAME.append("-")
try:
    volume=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[4]')
    for i in volume:
        VOLUMES_SOLD.append(i.text)
except:
    VOLUMES_SOLD.append("-")
try:
    pub=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[5]')
    for i in pub:
        PUBLISHER.append(i.text)
except:
    PUBLISHER.append("-")
try:
    genre=driver.find_elements(By.XPATH,'//table[@class="in-article sortable"]/tbody/tr/td[6]')
    for i in genre:
        GENRE.append(i.text)
except:
    GENRE.append("-")


# In[25]:


print(len(RANK),len(BOOK_NAME),len(AUTHOR_NAME),len(VOLUMES_SOLD),len(PUBLISHER),len(GENRE))


# In[26]:


df6=pd.DataFrame({"RANK":RANK ,
                 "BOOK NAME":BOOK_NAME,
                 "AUTHOR NAME":AUTHOR_NAME,
                 "VOLUME SOLD": VOLUMES_SOLD,
                 "PUBLISHER":PUBLISHER ,
                 "GENRE":GENRE})
df6


# # AMSWER-7

# In[27]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.imdb.com/list/ls095964455/')
time.sleep(3)


# In[30]:


NAME=[]
YEAR_SPAN=[]
GENRE=[]
RUN_TIME=[]
RATINGS=[]
VOTES=[]

try:
    name=driver.find_elements(By.XPATH,'//div[@class="lister-item mode-detail"]/div[2]/h3/a')
    for i in name:
        NAME.append(i.text)
except:
    NAME.append("-")
try:
    year=driver.find_elements(By.XPATH,'//div[@class="lister-item mode-detail"]/div[2]/h3/span[2]')
    for i in year:
        YEAR_SPAN.append(i.text)
except:
    YEAR_SPAN.append("-")
try:
    genre=driver.find_elements(By.XPATH,'//div[@class="lister-item mode-detail"]/div[2]/p/span[5]')
    for i in genre:
        GENRE.append(i.text)
except:
    GENRE.append("-")
try:
    rtime=driver.find_elements(By.XPATH,'//div[@class="lister-item mode-detail"]/div[2]/p/span[3]')
    for i in rtime:
        RUN_TIME.append(i.text)
except:
    RUN_TIME.append("-")
try:
    ratings=driver.find_elements(By.XPATH,'//div[@class="lister-item mode-detail"]/div[2]/div/div/span[2]')
    for i in ratings:
        RATINGS.append(i.text)
except:
    RATINGS.append("-")
try:
    votes=driver.find_elements(By.XPATH,'//div[@class="lister-item mode-detail"]/div[2]/p[4]/span[2]')
    for i in votes:
        VOTES.append(i.text)
except:
    VOTES.append("-")


# In[33]:


df7=pd.DataFrame({"NAME":NAME,
                 "YEAR SPAN":YEAR_SPAN,
                 "GERNE": GENRE,
                 "RUN TIME":RUN_TIME,
                 "RATINGS":RATINGS})
df7


# # ANSWER-8

# In[45]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://archive.ics.uci.edu/')

# click on datasets
driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[1]/header/nav/ul/li[1]/a').click()
time.sleep(2)


# In[6]:


DATASET_NAME=[]
DATA_TYPE=[]
TASK=[]
ATT_TYPE=[]
INT_NO=[]
ATTR_NO=[]
YEAR=[]
LINKS=[]
start=0
end=63
for page in range(start,end):
    try:
        
        data_links=driver.find_elements(By.XPATH,'//h2[@class="truncate text-primary"]/a')
        for i in data_links:
            L=i.get_attribute("href")
            LINKS.append(L)
            DATASET_NAME.append(i.text)
        nxt=driver.find_element(By.XPATH,'//div[@class="btn-group"]/button[2]')
        nxt.click()
        time.sleep(2)
    except:
        print(" ALL PAGE DONE ")


# In[47]:


for i in LINKS:
    driver.get(i)
    time.sleep(2)
    try:
        dtype=driver.find_element(By.XPATH,'//div[1][@class="col-span-4"]/p').text
        DATA_TYPE.append(dtype)
    except:
        DATA_TYPE.append("-")
    try:
        task=driver.find_element(By.XPATH,'//div[3][@class="col-span-4"]/p').text
        TASK.append(task)
    except:
        TASK.append("-")
    try:
        attype=driver.find_element(By.XPATH,'//div[4][@class="col-span-4"]/p').text
        ATT_TYPE.append(attype)
    except:
        ATT_TYPE.append("-")
    try:
        int_no=driver.find_element(By.XPATH,'//div[5][@class="col-span-4"]/p').text
        INT_NO.append(int_no)
    except:
        INT_NO.append("-")
    try:
        att_no=driver.find_element(By.XPATH,'//div[6][@class="col-span-4"]/p').text
        ATTR_NO.append(att_no)
    except:
        ATTR_NO.append("-")
    try:
        year=driver.find_element(By.XPATH,'//h2[@class="text-primary-content"]').text
        y=year.split(' ',2)[2]                           
        YEAR.append(y)
    except:
        YEAR.append("-")


# In[48]:


print(len(DATASET_NAME),len(DATA_TYPE),len(TASK),len(ATT_TYPE),len(INT_NO),len(ATTR_NO),len(YEAR))


# In[49]:


df8=pd.DataFrame({"DATASET NAME":DATASET_NAME,
                 "DATA TYPE":DATA_TYPE,
                 "TASK": TASK,
                 "ATTRIBUTE TYPE":ATT_TYPE,
                 "NO OF INSTANCES":INT_NO,
                 "NO OF ATTRIBUTE":ATTR_NO,
                 "YEAR":YEAR})
df8


# # ANSWER-9

# In[41]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.naukri.com/hr-recruiters-consultants ')
time.sleep(3)


# In[42]:


NAME=[]
DESIGNATION=[]
COMPANY=[]
SKILLES=[]
LOCATION=[]
links=[]
sk=[]
link=driver.find_elements(By.XPATH,'//a[@class="title ellipsis"]')
for i in link:
    links.append(i.get_attribute("href"))
for i in links:
    driver.get(i)
    time.sleep(2)
    try:
        name=driver.find_element(By.XPATH,'//div[@class="jd-top-head"]/header/h1').text
        NAME.append(name)
    except:
        NAME.append("-")
    try:
        com=driver.find_element(By.XPATH,'//div[@class="jd-top-head"]/div/a[1]').text
        COMPANY.append(com)
    except:
        COMPANY.append("Accenture") 
    try:
        skill=driver.find_elements(By.XPATH,'//a[@class="chip clickable"]')
        for i in skill:
            sk.append(i.text)
        SKILLES.append(sk)
    except:
        SKILLES.append("-")
    try:
        loc=driver.find_element(By.XPATH,'//span[@class="location "]').text
        LOCATION.append(loc)
    except:
        LOCATION.append("-")


# In[43]:


df9=pd.DataFrame({"COMPANY":COMPANY,
                  "DESIGNATION":NAME ,
                 "SKILLES": SKILLES,
                 "LOCATION":LOCATION})
df9


# In[ ]:




