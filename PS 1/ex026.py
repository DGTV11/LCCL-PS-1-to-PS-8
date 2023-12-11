from datetime import datetime
from easygui import *

now = datetime.now()
c_time = now.strftime(r"%d/%m/%Y %H:%M:%S")
msgbox("Current time: %s"%c_time)