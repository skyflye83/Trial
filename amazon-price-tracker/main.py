from bs4 import BeautifulSoup
import smtplib
import requests
import lxml

URL = "https://www.amazon.it/SUPER-MARIO-BROS-WONDER-Videogioco-Nintendo/dp/B0C8ZCR12S/" \
      "ref=sr_1_31?__mk_it_IT=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=N291DIRMQ8CB&keywords=" \
      "mario&qid=1689085644&sprefix=mario%2Caps%2C128&sr=8-31"

MY_EMAIL = "eduardo.cafiero83@gmail.com"
PASSWORD = "tulfjohfmdusiocp"
TARGET_PRICE = 59.9

headers = {
    "User-Agent": "Chrome/114.0.0.0",
    "Accept": "text/html",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=headers)
print(response.status_code)


soup = BeautifulSoup(response.text, "lxml")
tag = soup.find(name= "span", class_="a-offscreen")
tag_name = soup.find(name= "span", class_="selection")

name = " ".join(tag_name.getText().split())
price = float(tag.getText().split("€")[0].replace(",","."))


if price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        mail_to_send = f"Subject: Amazon price alert!\n\n{name} has now reached the desired cost of {price}€\n"\
                       f"Here is the link to buy:\n {URL}"
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=mail_to_send.encode("UTF-8"))
