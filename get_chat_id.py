import requests
TOKEN = "751491094:AAG4MdHoCf70Pgfi2XtdXPTEggmPIGBn0FU"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
