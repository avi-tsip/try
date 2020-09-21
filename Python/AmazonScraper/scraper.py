import  requests
from bs4 import BeautifulSoup
import smtplib
import  time

url = 'https://www.amazon.com/Casio-G-Shock-Analog-Digital-Carbon-GA2000-5A/dp/B07RB2T5BZ/ref=pd_rhf_se_s_pd_crcd_1_10'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

def check_price():
    page = requests.get(url, headers=headers, verify=False)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text().strip()
    print(title)
    price = soup.find(id='priceblock_ourprice').get_text()
    print(price)
    converted_price = float(price[1:])
    print(converted_price)

    if(converted_price < 200.00):
        send_mail(title, price, url)

def send_mail(title, price, url):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('green.onliner@gmail.com', 'Yarden12!@')
    subject = 'Price feel down!'
    body = f'The price for {title} is: {price}\n You can find it by clicking here:\n {url}'
    msg = f'Subject: {subject}\n\n{body}'
    server.sendmail('green.onliner@gmail.com','pmcpizza@gmail.com', msg)
    server.quit()
    print('Email has been sent')

while(True):
    check_price()
    time.sleep(86400)