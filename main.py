import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

my_email = "YOUR SENDING EMAIL"
password = "YOUR SENDING EMAIL PASSWORD"

URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07WL1XBBD/ref=sr_1_1?qid=1597662463&fbclid=IwAR3kbPFcACCZ_4rApoPZjotxn0rxr3tm6y60W9PPRpUIWDNY1bXB_RnWf4g&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url= URL, headers= headers)
soup = BeautifulSoup(response.text, "lxml")

price_tag= soup.find(name="span", id="size_name_1_price").text
object = soup.find(name="span", id="productTitle").text.strip()
thing = object.encode('utf-8')
price = float(price_tag.split()[-1][1:])


msg = f"{thing} is now ${price}\n {URL}"

if price < 200:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="YOUR RECEIVING EMAIL",
            msg=f"Subject: Amazon low price alert\n\n{msg}"
        )