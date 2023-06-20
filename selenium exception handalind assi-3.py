#!/usr/bin/env python
# coding: utf-8

# # ANSWER-1

# In[66]:


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

# In[4]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.amazon.in/')
search = WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID, 'twotabsearchtextbox')))
product=input('AMAZON SEARCH')
search.send_keys(product)
search.submit() # submit the search form


# # ANSWER-2

# In[5]:


# Initialize lists to store product details
brand_names = []
product_names = []
prices = []
return_exchange = []
expected_delivery = []
availabilities = []
product_urls = []
start=0
end=3
for nxt in range(start,end):
   product_links=driver.find_elements(By.CSS_SELECTOR,'a.a-link-normal.a-text-normal')
   for i in product_links:
       product_urls.append(i.get_attribute("href"))
   nxt_btn=driver.find_element(By.XPATH,'//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]')
   nxt_btn.click()
   time.sleep(3)
for i in product_urls:
   driver.get(i)
   time.sleep(2)
   try:
       brand_name = driver.find_element(By.ID, 'bylineInfo').text.strip()
       brand_names.append(brand_name)
   except:
       brand_names.append("-")
   try:
       product_name = driver.find_element(By.ID, 'productTitle').text.strip()
       product_names.append(product_name)
   except:
       product_names.append("-")
   try:
       price = driver.find_element(By.XPATH, ".//span[@class='a-price-whole']").text
       prices.append(price)
   except:
       prices.append("-")
   try:
       return_exchange_info = driver.find_element(By.ID, 'RETURNS_POLICY').text.strip()
       return_exchange.append(return_exchange_info)
   except:
       return_exchange.append("-")
   try:# DILIVARY INFO
       expected_delivery_info = driver.find_element(By.XPATH, '//div[@class="a-spacing-base"]/span/span[1]').text.strip()
       expected_delivery.append(expected_delivery_info)
   except:
       expected_delivery.append("-")
   try:# AVAIBILITY INFO
       availability_info = driver.find_element(By.XPATH, '//div[@id="availability"]/span').text.strip()
       availabilities.append("In Stock")
   except:
       availabilities.append("Out of Stock")
       


# In[6]:


print(len(brand_names),len(product_names),len(prices),len(return_exchange),len(expected_delivery),len(availabilities),len(product_urls))


# In[7]:


df2=pd.DataFrame({"Brand Name": brand_names,
                 "Name of the Product": product_names,
                 "Price": prices,
                 "Return/Exchange": return_exchange,
                 "Expected Delivery": expected_delivery,
                 "Availability": availabilities,
                 "Product URL": product_urls})
df2


# In[8]:


# remove duplicates
newdf2 = df2.drop_duplicates(subset = ['Price', 'Product URL'],keep = 'last').reset_index(drop = True)
len(newdf2)
newdf2


# In[9]:


# Save the DataFrame to a CSV file
newdf2.to_csv('amazon_products.csv', index=False)


# # ANSWER-3

# In[60]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://images.google.com/')
time.sleep(3)
keywords = ['fruits', 'cars', 'Machine Learning', 'Guitar', 'Cakes']
img_url=[]

for i in keywords:
    try:
        search_bar=driver.find_element(By.XPATH,"//textarea[@title='Search']")
    except:
        search_bar=driver.find_element(By.XPATH,"/html/body/c-wiz/c-wiz/div/div[3]/div[2]/div/div[1]/form/div[1]/div[2]/div/div[2]/input")
    search_bar.clear()
    search_bar.send_keys(i)
    search_bar.submit()
    time.sleep(5)
    try:
        img_tag =driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
        counter=0
        for i in img_tag:
            img=i.get_attribute('src')
            if img is not None:
                if img.startswith('http'):
                    img_url.append(img)
                    counter += 1
                    if counter == 10:
                        break
        for i in range(len(img_url)):
            if i>10:
                break 
                
    except NoSuchElementException as e:
        print(f"Element not found while processing '{keyword}' - {e}")

    except StaleElementReferenceException as e:
        print(f"Stale element reference while processing '{keyword}' - {e}")

    except Exception as e:
        print(f"An error occurred while processing '{keyword}' - {e}")
len(img_url) 


# In[66]:


page=requests.get("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS74z3cphb1TmxlmtOqkQ0ZDhDI1qNqdLWazA&usqp=CAU")
page


# In[47]:


from bs4 import BeautifulSoup
import requests


# In[67]:


for i in range(len(img_url)):
    if i<=9:
        print("downloding",keywords[0], i,"/10")
    elif 9<i<=19:
        print("downloding",keywords[1], i,"/10")
    elif 19<i<=29:
        print("downloding",keywords[2], i,"/10")
    elif 29<i<=39:
        print("downloding",keywords[3], i,"/10")
    elif 39<i:
        print("downloding",keywords[4], i,"/10")
    # for downloadind img to spcific path
    responce=requests.get(img_url[i])
    file=open(r"C:\Users\Ronak\Desktop\images\img"+str(i)+".jpg","wb")
    file.write(responce.content)


# # ANSWER-4

# In[34]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.flipkart.com/')

# for close the popup window
driver.find_element(By.XPATH, "//button[text()='✕']").click()

search_bar=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search_bar.send_keys('oneplus nord')
search_bar.send_keys(Keys.ENTER)
time.sleep(5)


# In[11]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.flipkart.com/')

# for close the popup window
driver.find_element(By.XPATH, "//button[text()='✕']").click()

search_bar=driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input")
search_bar.send_keys('oneplus nord')
search_bar.send_keys(Keys.ENTER)
time.sleep(5)

brand_names=[]
phone_names=[]
colours=[]
rams=[]
roms=[]
prices=[]
pri_cams=[]
sec_cams=[]
displays=[]
batterys=[]
pro_urls=[]


product_links=driver.find_elements(By.XPATH,'//div[@class="_4rR01T"]')
for i in product_links:
        i.click()
        # Switch to the new window
        driver.switch_to.window(driver.window_handles[-1])
        try:
            brand_name = driver.find_element(By.XPATH,'//span[@class="B_NuCI"]').text.split(' ',1)[0]
            brand_names.append(brand_name)
            
            pn = driver.find_element(By.XPATH,'//span[@class="B_NuCI"]').text.split('(')[0]
            phn=pn.split(' ',1)[1]
            phone_names.append(phn)
            
            cr= driver.find_element(By.XPATH,'//span[@class="B_NuCI"]').text.split('(')[1]
            colour=cr.split(',')[0]
            colours.append(colour)
            
            rm= driver.find_element(By.XPATH,'//span[@class="B_NuCI"]').text.split(')',1)[1]
            rams.append(rm)
            
            ro= driver.find_element(By.XPATH,'//span[@class="B_NuCI"]').text.split('(')[1]
            rom=ro.split(',')[1]
            roms.append(rom)
            
            price=driver.find_element(By.XPATH,'//div[@class="_30jeq3 _16Jk6d"]').text
            prices.append(price)
            
            display=driver.find_element(By.XPATH,'//li[2][@class="_21Ahn-"]').text
            displays.append(display)
            
            pri_cam=driver.find_element(By.XPATH,'//li[3][@class="_21Ahn-"]').text
            pri_cams.append(pri_cam)
            
            sec_cams.append("-")
                
            battery=driver.find_element(By.XPATH,'//li[4][@class="_21Ahn-"]').text
            batterys.append(battery)
            
            pro_urls.append(driver.current_url)
            
        except NoSuchElementException as e:
            print("Element not found while processing: ",e)

        except StaleElementReferenceException as e:
            print("Stale element reference while processing: ",e)

        except Exception as e:
            print("An error occurred while processing: ",e)
        finally:
            # Switch back to the search results window
            driver.switch_to.window(driver.window_handles[0])


# In[12]:


len(brand_names),len(phone_names),len(colours),len(rams),len(roms),len(prices),len(displays),len(pri_cams),len(sec_cams),len(batterys),len(pro_urls)


# In[13]:


import pandas as pd
df4=pd.DataFrame({"Brand Name": brand_names,
                 "phone name": phone_names,
                 "Price": prices,
                 "ram": rams,
                 "rom": roms,
                 "colour": colours,
                  "primary camera":pri_cams,
                  "secondary camera":sec_cams,
                  "display":displays,
                  "battery":batterys,
                 "Product URL": pro_urls})
df4


# In[17]:


# save to csv file
df4.to_csv('oneplus_nord_mobile.csv', index=False)


# # ANSWER-5

# In[24]:



driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://maps.google.com')
search_input = driver.find_element(By.NAME,"q")
city=input("ENTER CITY NAME : ")
search_input.send_keys(city)
search_input.send_keys(Keys.ENTER)
time.sleep(4)
coordinates_element = driver.current_url # find data from url detail
lat = coordinates_element.split('@')[1]
latitude=lat.split(',',2)[0]
longitude = lat.split(',',2)[1]
print("coordinate of ",city,"is latitude",latitude,"longitude",longitude)   


# # ANSWER-6

# In[68]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.digit.in/')
time.sleep(3)
# laptops click
driver.find_element(By.XPATH,'//span[@class="arrow_down laptops"]').click()
time.sleep(3)
# click on best 
driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[2]/div[2]/div/div[1]/span[4]/strong').click()
# click on best gaming laptop in india
driver.find_element(By.XPATH,'/html/body/div[2]/div/ul/li[2]/div[2]/div/div[5]/div/div[2]/a/span').click()
time.sleep(4)

brands=[]
names=[]
OS=[]
displays=[]
Processor=[]
Memory=[]
prices=[]
image_url=[]
product_urls=[]

product_links=driver.find_elements(By.XPATH,'//div[@class="left_side"]/span[2]')
for i in product_links[0:7]:
    product_urls.append(i.get_attribute("data-href"))
for i in product_urls:
    driver.get(i)
    time.sleep(2)
    try:
        brand = driver.find_element(By.CLASS_NAME, "heading-wraper").text.split(' ',1)[0]
        brands.append(brand)
    except:
        brands.append("-")
    try:
        name= driver.find_element(By.XPATH,'//*[@id="specs"]/div/div[1]/div[1]/table/tbody/tr[1]/td[3]').text
        names.append(name)
    except:
        names.append("-")
    try:
        processor = driver.find_element(By.XPATH,'//*[@id="specs"]/div/div[1]/div[6]/table/tbody/tr[1]/td[3]').text
        Processor.append(processor)
    except:
        Processor.append("-")
    try:
        os = driver.find_element(By.XPATH,'//*[@id="specs"]/div/div[1]/div[1]/table/tbody/tr[3]/td[3]').text
        OS.append(os)
    except:
        OS.append("-")
    try:
        display = driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[3]/div[2]/div[3]/div/ul/li[2]/div/p[2]/strong').text
        displays.append(display)
    except:
        displays.append("-")
    
    try:
        memory = driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[3]/div[2]/div[3]/div/ul/li[4]/div/p[2]/strong').text
        Memory.append(memory)
    except:
        Memory.append("-")
    try:
        price = driver.find_element(By.XPATH,'/html/body/div[7]/div[2]/div[3]/div[2]/div[4]/div/h2/strong').text
        prices.append(price)
    except:
        prices.append(price)
    try:
        img = driver.find_element(By.CLASS_NAME, 'maxi')
        im = img.get_attribute('src')
        image_url.append(im)
    except:
        image_url.append("-")
print(len(brands),len(names),len(prices),len(displays),len(Processor),len(OS),len(Memory),len(image_url),len(product_urls))
    


# In[69]:


df6=pd.DataFrame({"Brand": brands,
                 "Name": names,
                 "Price": prices,
                  "DISPLAY":displays,
                  "processor":Processor,
                 "oparating system": OS,
                 "MEMORY": Memory,
                 "image url": image_url,
                 "Product URL": product_urls})
df6


# # ANSWER-7

# In[2]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.forbes.com/billionaires/')


# In[13]:


# click on 1st rank name
driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div').click()
RANK=[]
NAME=[]
NETWORTH=[]
AGE=[]
COUNTRY=[]
SOURCE=[]
INDUSTRY=[]


# In[16]:


try:
    rank=driver.find_elements(By.XPATH,'//div[@class="Table_rank___YBhk Table_dataCell__2QCve"]')
    for i in rank:
        r=i.text
        RANK.append(r)
except:
    RANK.append('-')


# In[14]:


try:
    name=driver.find_elements(By.XPATH,'//*[@class="TableRow_row__L-0Km"]/div[2]/div')
    for i in name:
        n=i.text
        NAME.append(n)
except:
    NAME.append('-')
try:
    networth=driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[3]/div')
    for i in networth:
        ne=i.text
        NETWORTH.append(ne)
except:
    NETWORTH.append('-')
try:
    age=driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[4]/div')
    for i in age:
        a=i.text
        AGE.append(a)
except:
    AGE.append('-')
try:
    country=driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[5]')
    for i in country:
        c=i.text
        COUNTRY.append(c)
except:
    COUNTRY.append('-')
try:
    source=driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[6]/div/span')
    for i in source:
        s=i.text
        SOURCE.append(s)
except:
    SOURCE.append('-')
try:
    industry=driver.find_elements(By.XPATH,'//div[@class="TableRow_row__L-0Km"]/div[7]')
    for i in industry:
        Id=i.text
        INDUSTRY.append(Id)
except:
    INDUSTRY.append('-')


# In[17]:


print(len(RANK),len(NAME),len(NETWORTH),len(AGE),len(COUNTRY),len(SOURCE),len(INDUSTRY))


# In[25]:


df7=pd.DataFrame({"RANK": RANK,
                 "NAME": NAME,
                 "NETWORTH": NETWORTH,
                  "AGE":AGE,
                  "COUNTRY":COUNTRY,
                 "SOURCE": SOURCE,
                 "INDUSTRY": INDUSTRY})
df7


# # ANSWER-8

# In[65]:


driver=webdriver.Chrome(r'C:\Users\Ronak\Downloads\chromedriver_win32\chromedriver.exe')
driver.maximize_window() # for maximize window
driver.get('https://www.youtube.com/watch?v=dYBbbdq7fuw')
time.sleep(5)


# In[81]:


for _ in range(20):
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    
    comment=[]
    upvote=[]
    Time=[]
    comments = driver.find_elements(By.XPATH, '//yt-formatted-string[@class="style-scope ytd-comment-renderer"]')
    for i in comments[:500]:
        c=i.text
        comment.append(c)
    upvotes = driver.find_elements(By.XPATH, '//span[@id="vote-count-middle"]')
    for i in upvotes[:500]:
        u=i.text
        upvote.append(u)
    timestamp = driver.find_elements(By.XPATH, '//yt-formatted-string[@class="published-time-text style-scope ytd-comment-renderer"]')
    for i in timestamp[:500]:
        t=i.text
        Time.append(t)


# In[82]:


len(comment),len(upvote),len(Time)


# In[83]:


df8=pd.DataFrame({"COMMENT":comment,
                 "UPVOTE": upvote,
                 "TIME": Time})
df8


# # ANSWER-9

# In[ ]:




