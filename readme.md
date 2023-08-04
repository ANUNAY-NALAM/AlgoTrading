$ git config --global user.name "Your Name"
$ git config --global user.email "you@youraddress.com"
$ git config --global push.default matching
$ git config --global alias.co checkout
$ git init
$ git add .
$ git commit -m ""
-->create git repo
paste those in terminal
$git push

open anaconda terminal

$conda create --name algo python=3.7
$conda activate algo
$conda install pandas matplotlib requests statsmodels scikit-learn
$conda install spyder
$pip install --upgrade kiteconnect

create kite connect trading app

check for connection:


``` py
from kiteconnect import KiteConnect
import pandas as pd

api_key = "Your API Key"
api_secret = "Your API Secret"
kite = KiteConnect(api_key=api_key)
print(kite.login_url()) #use this url to manually login and authorize yourself

#generate trading session
request_token = "Your Request Token" #Extract request token from the redirect url obtained after you authorize yourself by loggin in
data = kite.generate_session(request_token, api_secret=api_secret)

#create kite trading object
kite.set_access_token(data["access_token"])


#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)
instrument_df.to_csv("NSE_Instruments.csv",index=False)
```

$pip install selenium

download driver-->
	
https://chromedriver.chromium.org/downloads

which matches your chrome version

after installing webdriver 
test weather any  website was opening or not using

from selenium import webdriver
browser=webdriver.Chrome()
browser.get('http://seleniumhq.org')

APIKEY-Obtained from the trading app in your developer account
API SECRET- Obtained from the trading app in your developer account

User id- your Zerodha kite user id

password - your Zerodha kite password

pin-zerodha pin

request token -Obtained after authenticating yourself on the url given by the print_ url( function of the kite Connect object

Acces_token-Obtained after generating trading session


create api_key.txt file 
and paste 5 keys of information you had

api key
api crete
zerodha user id
zerodha password
zerodha key

enable 2 factor authentication to get TOTP it checks present TOTP AND ENTERS AUTOMATICALLY USING pyotp






