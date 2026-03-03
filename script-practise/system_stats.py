import os
import datetime
print(datetime.datetime.today())

window = f"This is window system info: {os.system('systeminfo')}"
print(window)
