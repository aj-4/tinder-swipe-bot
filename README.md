# Preparation
- Download chromedriver, unzip, move to `/usr/local/bin` (macOS/Linux)
- `pip install -r requirements.txt`

- Create a `secrets.py` file with variables:
``` 
username = 'your_username'
password = 'your_password'
```

# Start the bot
```
python swipe_bot.py <dating-site-1> <dating-site-2> <dating-site-n>
```
*Tinder*, *Badoo*, and *OKC* are the only dating sites supported but other site can be added by creating new subclass of Bot
