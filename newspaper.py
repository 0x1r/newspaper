import calendar
import string
import datetime
from datetime import date
from datetime import datetime
from bs4 import BeautifulSoup
import re
import requests
import os
choice=input("T for today and c for Custom date")
# print("choice")
if(choice=='t'):
    # mydate = string(date.today())
    # mydate = datetime.datetime.now()
    #remove string_date = a_date.strftime("%-m/%-d/%Y") - from this funct to get leading zero in date and use # in windows - wont work
    now = datetime.now()
    mon=now.strftime("%b")
    # print(mon)
    date_time = now.strftime("%d "+ mon  + " %Y")
    # print(date_time)
    mydate=date_time

    #for download date
    today = date.today()
elif(choice=='c'):
    mydate=input('enter the date')
    temp=mydate
    today=mydate.replace(" ", "")
    # print(mydate)


# URL = "https://dailyepaper.in/times-of-india-epaper-pdf-download-2020/"

# def switch():
    
 
 
 
# switch()

print(" 0:TOI \n 1:Financial express \n 2:Telegraph \n 3:Deccan chronicle \n 4:statesman \n 5:The Asian age \n 6:The Tribune \n")
option = int(input("which newspaper would u like to read"))
 
 
if option == 0:
    print("you have chosen THE TIMES OF INDIA")
    hang='TOI'
    URL="https://dailyepaper.in/times-of-india-epaper-pdf-download-2020/"
 
elif option == 1:
    print("you have chosen Financial express")
    hang='Financialexpress'
    URL="https://dailyepaper.in/financial-express-newspaper/"
 
elif option == 2:
    print("you have chosen Telegraph")
    hang='Telegraph'
    URL="https://dailyepaper.in/telegraph-newspaper/"
    
elif option == 3:
    print("you have chosen Deccan chronicle")
    hang='DeccanChronicles'
    URL="https://dailyepaper.in/deccan-chronicle-epaper/"
 
elif option == 4:
    print("you have chosen Statesman")
    hang='Statesman'
    URL="https://dailyepaper.in/statesman-newspaper-today/"
    
elif option == 5:
    print("you have chosen THE Asian age")
    hang='TheAsianAge'
    URL="https://dailyepaper.in/the-asian-age-epaper/"
    
elif option == 6:
    print("you have chosen THE Tribune")
    hang='TheTribune'
    URL="https://dailyepaper.in/the-tribune-epaper/"
       
else:
    print("Incorrect option")

r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib')
child_soup = soup.body.div.findAll('span',{'style':'font-size: 16px;'})

text = mydate
print(text)
gfg = soup.find_all(lambda tag: tag.name == "span" and text in tag.text)

paragraphs = []
for x in gfg:
    paragraphs.append(str(x))


# print(re.search("(?P<url>https?://[^\s]+)", paragraphs[0]).group("url"))

finallink=re.search("(?P<url>https?://[^\s]+)", paragraphs[0]).group("url")
name = finallink[:-1]
# print(name)
r = requests.get(name)
  
vkl = BeautifulSoup(r.content, 'html5lib')
# print(vkl.prettify())
# print(finallink)
vkllink=vkl.findAll('iframe')

paravkl = []
for x in vkllink:
    paravkl.append(str(x))

# print(paravkl)
mylink = re.search("(?P<url>https?://[^\s]+)", paravkl[0]).group("url")
cutlink=mylink[:-1]
print(mylink[:-1])
# os.system('wget ' + cutlink)
#now finding the downloadable link via vk scraping

#downlad with rename 

os.system('wget ' + cutlink + f' -O {hang}{today}.pdf')