from configparser import ConfigParser
from bs4 import BeautifulSoup
import  requests
import smtplib
import  time
import json
import logging
from logging.handlers import RotatingFileHandler

formatting = logging.Formatter("%(levelname)s %(asctime)s: %(message)s")
log_handler = RotatingFileHandler('log.log', mode='a', maxBytes=10*1024*1024, backupCount=2)
log_handler.setFormatter(formatting)
log_handler.setLevel(logging.INFO)
logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(log_handler)

config = ConfigParser()
config.read('config.ini')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

def check_price():

    with open('products.json', 'r', encoding="utf-8") as f:
        json_data = json.load(f)
        for url, wanted_price in json_data['products'].items():
            page = requests.get(url, headers=headers, verify=False)
            soup = BeautifulSoup(page.content, 'html.parser')
            try:
                title = soup.find(id='productTitle').get_text().strip()
                logger.info(f'found: {title}')
                price = soup.find(id='priceblock_ourprice').get_text()
                logger.info(f'Current price of {title} is {price}')
                converted_price = float(price[1:])
                if(converted_price <= wanted_price):
                    send_mail(title, price, url)
                else:
                    logger.info(f'Email not sent. Price of {title} is still not below {wanted_price}')
            except AttributeError as err:
                logger.info('Looks like the title or price tag are empty')
                logger.error(err)
            

def send_mail(title, price, url):

    server = smtplib.SMTP(config['settings']['smtp'], 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(config['settings']['send_email'], config['settings']['pass'])
    subject = 'Price feel down!'
    body = f'The price for {title} is: {price}\n You can find it by clicking here:\n {url}'
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail(config['settings']['send_email'], config['settings']['receive_email'], msg)
    server.quit()
    logger.info(f'Email sent for: {title}')

while(True):
    logger.info('Starting to look into the prices of the products')
    check_price()
    time.sleep(86400)
    logger.info('See you tomorrow!')