import requests #pip install requests
import lxml #pip install lxml
import bs4 #pip install bs4
import json 
import time
from smtplib import SMTP

# Opens the config.json file and stores the data in the 'config' variable
with open('config.json','r') as f:
    config = json.load(f)

# The URL we'll be working with
url = config["url"]

# Retrieves the price from the product's page
def get_price():

    # Asks for the webpage's HTML text
    res = requests.get(url)

    # Parses the webpage 
    soup = bs4.BeautifulSoup(res.text, "lxml")

    # Isolates the price from the rest of the page, and then removes the currency symbols and the comma
    price = soup.find(id = 'priceblock_ourprice').get_text()[1:]
    price = float(price.replace(',',''))

    return price

def email_notify():
    
    # Starts the SMTP server and logs in
    server = SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(config["email_address"],config["email_password"])

    # Composes the e-mail
    subject = 'Price drop!'
    body = 'The price for one of your items has recently fallen :D \n' + url
    message = f"Subject: {subject}\n\n{body}"

    # Sends the e-mail and closes the server
    server.sendmail(config["email_address"], config["email_address"], message)
    server.close()

def telegram_notify():

    # Sends a message via the Telegram bot
    t_url = "https://api.telegram.org/bot"+config["telegram_token"]
    params = {"chat_id": config["telegram_id"], "text": f"Price drop!\n\n{url}"}
    r = requests.get(t_url + "/sendMessage", params=params)

if __name__ == '__main__':
  while True:
        
        current_price = get_price()

        if float(config["budget"]) >= current_price:
            if config["method"].lower().replace('-','') == 'email':
                email_notify()
            elif config["method"].lower() == 'telegram':
                telegram_notify()
        
        print('Script ran.')

        # How often the script runs
        time.sleep(config["interval"])