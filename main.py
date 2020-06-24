import requests, random, time, os, colorama
from bs4 import BeautifulSoup, SoupStrainer
try:
    os.system(['clear','cls'][os.name == 'nt'])
except:
    pass
print("""\033[35m
   _  _  ___________________
__| || |_\_   _____/\_____  \.
\   __   /|    __)    _(__  <
 |  ||  | |     \    /       \.
/_  ~~  _\.\___ /   /______  /
  |_||_|      \/           \/
 __.   .__                 __
\_ |__ |  |   ____   ____ |  | __  ___________
 | __ \|  |  /  _ \_/ ___\|  |/ / / __ \_  __ \.
 | \_\ \  |_(  <_> )  \___|    < \  ___/|  | \/
 |___  /____/\____/ \___  >__|_ \.\___  >__|
     \/                 \/     \/    \/
\033[0m""")
print("   \033[31m!!!!|Use Tor|!!!\n\033[0m~ Termux-Lab | t.me/termuxlab")
name=input("\033[33mNick:~#\033[0m ")
messag = input("\033[33mMessage:~#\033[0m ")
count = input("\033[33mCount messages:~#\033[0m ")
url='https://f3.cool/'+name
r = requests.get(url)
i=0
delts="https://play.google.com/store/apps/details?id=cool.f3&referrer=user_id%3D"
soup = BeautifulSoup(r.content, 'html.parser', parse_only=SoupStrainer('a'))
for link in soup:
    if i == 1:
        if link.has_attr('href'):
            idsu = link['href'].replace(delts, "")
            print("\033[32mUser key => "+idsu+"\033[0m")
    i+=1
legs = "text="+messag
for t in range(int(count)):
    uagent = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
    ]
    url = "https://f3.cool/api/v1/users/"+idsu+"/questions"
    data = {"text":messag}
    headers={
    "User-Agent": uagent[random.randint(0, len(uagent)-1)],
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "X-App-Version": "F3-Web/v1.9.18",
    "Content-Type": "application/x-www-form-urlencoded",
    "Content-Length": str(len(legs)),
    "Origin": "https://f3.cool",
    "Connection": "keep-alive",
    "Referer": "https://f3.cool/"+name,
    "Cookie": "locale=en_US; _ga=GA1.2.2054047672.1592916584; _gid=GA1.2.743201242.1592916584",
    "Host": "f3.cool",
    }
    r = requests.post(url, data=data, headers=headers)
    time.sleep(1)
    print(r.text)
    print("\033[36mSend message: "+str(t+1)+"\033[0m")
