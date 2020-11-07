from telethon import events
import asyncio
from ..utils import admin_cmd
from .. import ALIVE_NAME
from .. import CMD_HELP
import importlib.util

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

@borg.on(admin_cmd(pattern="intro"))

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 2
    animation_ttl = range(0, 16)
    await event.edit("Introducing M A R S H M E L L O userbot")
    animation_chars = [          
              "**Hello! Master This is Marshmello Userbot\n Created by : [Dj](https://t.me/Beast_boy_shubh\n support group : [join](https://t.me/Marshmellobot_official)**",
              "**How Are You Master I Hope You Will Good**",
              "[ㅤ](https://telegra.ph/file/57ee16ad9cde95a55c0c1.jpg)",
              "**Marshmello Is Very Powerful and awaited Userbot**",
              "**Type `.help` To see my Commands I Have +400 plugins*",
              "**you can fork this bot easily**"  
          ]
    for i in animation_ttl:#By @hellojibot for MARSHMELLO
        	
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %16 ], link_preview=True)#By @NOOB_GUY_OP for Dark CObra
