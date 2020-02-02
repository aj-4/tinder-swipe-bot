## Install
Fedora:
``` 
sudo dnf -y install chromedriver
``` 

 - download chromedriver, unzip, move to `/usr/local/bin` (mac os / other linuxes linux)
 - `pip install selenium`


## create a secrets.py file with variables:
``` 
cat << EOF > secrets.py \
 tinder_username = ''
 tinder_password = ''
 okcupid_username = ''
 okcupid_password = ''
EOF 
```

```
python -i tinder_bot.py

python -i okcupid_bot.py

```

please add more features to this, would be awesome to see what you can come up w

cheers
