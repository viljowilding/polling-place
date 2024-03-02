try:
    import requests, subprocess, psutil
except:
    subprocess.run(shell=True,args=["pip3","install","python-dotenv","playwright","requests","psutil"])
    import requests, subprocess, psutil
from time import sleep
from dotenv import load_dotenv
from os import getenv
load_dotenv()
computerName = getenv('COMPUTERNAME')
url = f"https://pollctrl.app/api/station/{computerName}/"
payload = {'token': getenv('POLLCTRL_TOKEN')}
updatedAt = ""
status = ""

def runSubprocess(args,wait=False):
    if wait:
        subprocess.run(shell=True, args=args,cwd="C:\\Users\\Public")
    else:
        subprocess.Popen(shell=True, args=args,cwd="C:\\Users\\Public")

def getChrome():
    for proc in psutil.process_iter():
        if proc.name() == "chrome.exe":
             return proc.parent()

def openChrome():
    runSubprocess(["chrome.exe","--kiosk","--remote-debugging-port=9222", "--incognito", "https://msg.pollctrl.app"],False)

def getStatus():
    try:
        return requests.get(url).json()
    except:
        return False

def activate(studentID):
    openChrome()
    studentID = str(studentID)
    runSubprocess(["python","launchpoll.py", studentID],True)
    requests.post(url+'deactivate',data=payload)

while True:
    json = getStatus()
    if not json:
        exit()
    if updatedAt < json["updated_at"]:
        updatedAt = json["updated_at"]
        if json["status"] != status:
            status = json["status"]
            print(f"new status: {status}")
            match status:
                case "in-use":
                    print(json["currentUser"])
                    activate(json["currentUser"])
                case "available":
                    process = getChrome()
                    if process:
                        process.kill()
                    requests.post(url+'deactivate',data=payload)
    sleep(5)
