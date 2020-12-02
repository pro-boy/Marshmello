# 𐌑𐌀𐍂𐍃𐋏𐌑𐌄𐌋𐌋𐍈

Marshmello Is Most Powerful And awaited Bot.

# About

It is a userbot made for telegram. I made this userbot with help of Dark Cobra userbot. Credit Goes To Hellboi_atul.

This is the one and only official Marshmello Userbot made by [boss_DJ](https://t.me/beast_boy_shubh) Also join support channel and group :- https://t.me/Marshmellobot_officiall


# Wᴇ Aʀᴇ Nᴏᴛ Rᴇsᴘᴏɴsɪʙʟᴇ Fᴏʀ Aᴄᴄᴏᴜɴᴛ Bᴀɴs.


# For any query:-
### [Join](https://t.me/Marshmellobot_support)

# Before Fork Ask Permission
## Installing

### The Easy Way

 <a href="https://heroku.com/deploy?template=https://github.com/pro-boy/Marshmello/blob/main"> <img src="https://www2.assets.heroku.com/assets/elements/elements-buttons-2-4867044559069b937ba0fd078f5604f310a49928bd1b59fb3d2f0ff96e0d97c8.svg" alt="Deploy to Heroku" /></a></p>
## Generate String Session From Below Link:-

<a href="https://repl.it/@DjDuvvado/marshmello-4#main.py"><img alt="Run on Repl.it" src="https://camo.githubusercontent.com/05149b448485553c6f14f6430a45c12dcc79ed3c/68747470733a2f2f7265706c2e69742f62616467652f6769746875622f6a61727669733231303930342f4a6172766973" style="border-style: none; box-sizing: initial; max-width: 200%;" /></a></div>

## The Normal Way

Simply clone the repository and run the main file:
```sh
git clone https://github.com/shubhanshdj/Marshmello
cd marshmello
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**
Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`
    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
