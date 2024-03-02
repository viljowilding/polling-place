@set path=%path%;%PUBLIC%;%ProgramFiles%\Google\Chrome\Application
@pip3 install python-dotenv playwright requests psutil
@pythonw daemon.py
@pythonw client-script.py
@pythonw daemon.py offline