import requests
import time
from random import getrandbits
from bs4 import BeautifulSoup
url = 'https://RSVPGALLERY.us1.list-manage.com/subscribe/post-json?u=3c5152418ea66cfe94686365b&amp;id=1e7263dae2'

headers = {'User-Agent':
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
		   
print("RSVPGALLERY RAFFLE SCRIPT BY @FAYEEZUS"),
print("STARTING NOW..."), 
# CHANGE the fields as the comments say
def main(limit):
    for i in range(1, limit):
        session = requests.Session()
        email = 'YOUR_EMAIL+{}@gmail.com'.format(getrandbits(40)) # CHANGE YOUR_EMAIL to your email prefix. don't change the +{} after.
        payload = {
                    'FULLNAME'  : '', #Full Name
                    'EMAIL'  : email, #dont change
                    'SHOESIZE'  : '10', #shoe size
                    'subscribe'  : 'Submit' #Dont change


        }
        time.sleep (30)
        resp = session.post(url, data=payload, headers=headers)
        print('Raffle has been entered {}/{} times.'.format(i, limit))

if __name__ == "__main__":
    main(10000)
