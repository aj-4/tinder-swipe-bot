# Preparation
- Download chromedriver, unzip, move to `/usr/local/bin` (macOS/Linux)
- `pip install -r requirements.txt`

- Create Facebook credentials as environment variables or input your them during runtime:
``` 
export ID=<Facebook email>
export PASSWORD=<Facebook password>
```

# Start the bot
```
python main.py <dating-site-1> <dating-site-2> <dating-site-n>
```
*Tinder*, *Badoo*, and *OKC* are the only dating sites supported but other sites can be added by creating new subclasses of *Bot*
