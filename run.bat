@set path=%path%;%PUBLIC%;%ProgramFiles%\Google\Chrome\Application
@pip3 install python-dotenv playwright requests psutil
@python daemon.py