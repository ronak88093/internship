#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re


# # ANSWER-1

# In[2]:


txt="Ronak88093ismyUserID"
x=re.findall(r'^[a-zA-Z0-9]+$',txt)
if x:
    print("string contains ONLY a-z,A-Z,0-9 chracters")
else:
    print("string contains OTHER THEN a-z,A-Z,0-9 chracters")


# # ANSWER-2

# In[4]:


def function(x):
    match=re.findall(r'ab*',x)
    if match:
        print(match)
    else:
        print('None')
m='abb ki bar modi sarakar'
function(m)


# # ANSWER-3

# In[ ]:


def function(x):
    match=re.findall(r'ab+',x)
    if match:
        print(match)
    else:
        print('None')
m='abb ab a ac'
function(m)


# # ANSWER-4

# In[6]:


def function(x):
    match=re.findall(r'ab?',x)
    if match:
        print(match)
    else:
        print('None')
m='abb ab a ac'
function(m)


# # ANSWER-5

# In[8]:


txt=" abb ab a aa aac abbb abbbc acbbb"
match=re.findall(r'ab{3}',txt)
print(match)


# # ANSWER-6

# In[13]:


txt = "TheHeavyRainInDelhiToday"
x = re.findall(r"[A-Z][a-z]*", txt)
print(x)


# # ANSWER-7

# In[23]:


txt=" abb ab a aa aac abbb abbbc acbbb"
match=re.findall('abb|abbb',txt)
print(match)


# # ANSWER-8

# In[24]:


txt="my name_is ronak_chaudhari"
match=re.findall(r'[a-z]+_[a-z]+',txt)
print(match)


# # ANSWER-9

# In[35]:


txt="a acb abc acdb ashfb abx bxa"
match=re.findall(r'\ba.+b\b',txt)
print(match)


# # ANSWER-10

# In[41]:


txt="author of the book anotomy is andrew j smith"
match=re.findall(r'^author',txt)
match


# # ANSWER-11

# In[5]:


txt1='Hello_World123'         #ALLOWED
txt2='OpenAI_GPT'             #ALLOWED
txt3='1234567890'             #ALLOWED
txt4='123abc'                 #ALLOWED
txt5='!@#$%^&*'               # NOT ALLOWED
txt6='spaces are not allowed' # NOT ALLOWED
match=re.findall(r'^[a-zA-Z0-9_]+$',txt4) # change the txt for result
if match:
    print(match,'ALLOWED')
else:
    print("NOT ALLOWED")


# # ANSWER-12

# In[8]:


number=2645382957
txt=str(number)+"is my mobile number"
pattern=r'^[0-9]+'
match=re.findall(pattern,txt)
if match:
    print(match)
else:
    print("not match")


# # ANSWER-13

# In[13]:


ip_add=input(" enter ip address")
result=re.sub(r'\b0+(\d+)\b',"1",ip_add)
print(result)


# # ANSWER-14

# In[46]:


data='On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country.'
pattern=r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}th|\d{1,2}st|\d{1,2}nd|\d{1,2}rd)\s+(\d{4})\b'
result=re.search(pattern,data)
result.group()


# In[ ]:





# # ANSWER-15

# In[7]:


pattern = ['fox', 'dog', 'horse']
txt = 'The quick brown fox jumps over the lazy dog.'
for x in pattern:
    print('Searching "%s" word in "%s" is ' % (x, txt))
    m=re.search(x,txt)
    if m:
        print('Matched')
    else:
        print('Not Matched')


# # ANSWER-16

# In[6]:


pattern ='fox'
txt ='The quick brown fox jumps over the lazy dog.'
match =re.search(pattern, txt)
start=match.start()
end=match.end()
print('Find word "%s" in "%s" at position %d to %d '%(match.re.pattern,match.string,start,end))


# # ANSWER-17

# In[9]:


txt='Python exercises, PHP exercises, C# exercises'
pattern='exercises'
match=re.findall(pattern,txt)
for i in match:
    print("found match =",i)


# # ANSWER-18

# In[27]:


txt='Python exercises, PHP exercises, C# exercises'
pattern='exercises'
match=re.finditer(pattern,txt)

for i in match:
    s=i.start()
    e=i.end()
    
    print('found match "%s" at %d to %d '%(txt[s:e],s,e))


# # ANSWER-19

# In[33]:


org_date="2023-8-15"
new_date=re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})','\\3-\\2-\\1', org_date)
new_date


# # ANSWER-20

# In[8]:


txt="The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene formalized the concept of a regular language. They came into common use with Unix text-processing utilities. Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard and another, widely used, being the Perl syntax."
match=re.findall(r'\b[a|e|A|E]\w+\b',txt)
match


# # ANSWER-21

# In[13]:


txt="The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene formalized the concept of a regular language. They came into common use with Unix text-processing utilities. Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard and another, widely used, being the Perl syntax."
match=re.finditer(r'\d+',txt)
for i in match:
    s=i.start()
    e=i.end()
    print(txt[s:e],'at position',s,'to',e)


# # ANSWER-22

# In[14]:


txt=" he is a 34 yr old with weight 85 kg. in pocket 500 rs but in bank 10000 rs."
match=re.findall(r'\d+',txt)
max(map(int,match)) # map will help all str list into int


# # ANSWER-23

# In[18]:


txt=" OpenAIIsAnArtificialIntelligenceResearchLabBasedInSanFranciscoCaliforniaTheCompanyWasFoundedInDecember2015ByElonMuskSamAltmanGregBrockmanIlyaSutskeverJohnSchulmanAndWoijciechZarembaItsMissionIsToEnsureThatArtificialGeneralIntelligenceBenefitsAllOfHumanityTheCompanyDevelopsAndPromotesFriendlyAIForAGlobalImpactOpenAIsGPT3ModelIsOneOfTheMostAdvancedLanguageModelsCapableOfPerformingVariousTasksSuchAsWritingCodingTranslationAndMoreWithContinuedResearchAndDevelopmentOpenAIsAimIsToPushTheBoundariesOfAIAndFosterInnovationWhilePrioritizingEthicsAndSafetyInTechnologyAdvancements"
match=re.sub(r'(\w)([A-Z])','\\1 \\2',txt)
match


# # ANSWER-24

# In[19]:


txt="The concept of regular expressions began in the 1950s, when the American mathematician Stephen Cole Kleene formalized the concept of a regular language. They came into common use with Unix text-processing utilities. Different syntaxes for writing regular expressions have existed since the 1980s, one being the POSIX standard and another, widely used, being the Perl syntax."
match=re.findall(r'[A-Z]\w+',txt)
match


# # ANSWER-25

# In[20]:


txt="my name is ronak ronak chaudhari."
match=re.sub(r'\b(\w+)\b\s*(?=.*\b\1\b)','',txt)
match


# # ANSWER-26

# In[31]:


txt=['ronak88093', 'sagar221533',  'mahesh@','aakash.','parthc']
for i in txt:
    match=re.search(r'[a-zA-Z0-9]$',i)
    if match:
        print("accepted")
    else:
        print("not accepted")   


# # ANSWER-27

# In[25]:


txt="""RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
match=re.findall(r'\#\w+',txt)
match


# # ANSWER-28

# In[30]:


txt="@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
match=re.sub(r'<U\+[0-9a-zA-Z]+>','',txt)
match


# # ANSWER-29

# In[49]:


file=open("answer-29.txt",'r')
txt=file.read()
match=re.findall(r"\b(\d{1,2}/\d{1,2}/\d{4}|\d{1,2}-\d{1,2}-\d{4})\b",txt)# for formet dd-mm-yyyy or dd/mm/yyyy
for i in match:
    print(i)
                  


# # ANSWER-30

# In[51]:


txt="Write a Python program to replace all occurrences of a space, comma, or dot with a colon."
match=re.sub(r'[ ,.]',':',txt)
match


# In[ ]:




