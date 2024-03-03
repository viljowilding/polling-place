@set path=%path%;%PUBLIC%;%ProgramFiles%\Google\Chrome\Application
@pythonw daemon.py
@pythonw client-script.py
@pythonw daemon.py offline