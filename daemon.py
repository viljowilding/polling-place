try:
    import subprocess
    import sys, requests
except:
    subprocess.run(shell=True,args=["pip3","install","python-dotenv","playwright","requests","psutil"])
    import sys, requests
from dotenv import load_dotenv
from os import getenv
load_dotenv()
computerName = getenv('COMPUTERNAME')

url = f"https://pollctrl.app/api/station/{computerName}/"
payload = {'token': getenv('POLLCTRL_TOKEN')}

def runSubprocess(args,wait=False):
    if wait:
        subprocess.run(shell=True, args=args,cwd="C:\\Users\\Public")
    else:
        subprocess.Popen(shell=True, args=args,cwd="C:\\Users\\Public")

def online():
    requests.post(url+'online',data=payload)
    runSubprocess(["python","client-script.py"],True)

def offline():
    requests.post(url+'offline',data=payload)

args = sys.argv[1:]
if len(args)==0:
    online()
elif args[0] == "offline":
    offline()