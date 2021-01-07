# Thanks to Sipak bro and Aryan.. 
# animation Idea by @(Sipakisking) && @Hell boy_pikachu
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
import asyncio
import os
import requests
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events
from userbot.utils import admin_cmd, sudo_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "DARK COBRA"
ALIVE_PHOTTO = os.environ.get("ALIVE_PHOTTO" , None)

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)
global ghanti
ghanti = borg.uid
edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/419a921708a9592578665.mp4"
file2 = "https://telegra.ph/file/419a921708a9592578665.mp4"
file3 = "https://telegra.ph/file/419a921708a9592578665.mp4"
file4 = "https://telegra.ph/file/419a921708a9592578665.mp4"
""" =======================CONSTANTS====================== """
pm_caption = " ᴍᴀʀsʜᴍᴇʟʟᴏ 🤟🤟 IS օռʟɨռɛ..!! **🔥🔥\n\n"
pm_caption += "⚔️⚔️ **master, Am Alive And Systems Are Working Perfectly As It Should Be...**⚔️⚔️\n\n"
pm_caption += "༆༄☠︎︎About My System \n\n"
pm_caption += "🔥🔥 **ᴛᴇʟᴇᴛʜᴏɴ**🔥🔥 >>》 15.0.0\n"
pm_caption += "🚨🚨 **group**🚨🚨   >>》 [ʝօɨռ](https://t.me/Marshmellobot_official)\n"
pm_caption += f"🔰🔰**ᴍᴀsᴛᴇʀ**🔰🔰  >>》 {DEFAULTUSER}\n"
pm_caption += "🌏🌏 **ᴄʀᴇᴀᴛᴏʀ**🌏🌏  >>》 [ᴏᴡɴᴇʀ](https://t.me/beast_boy_shubu)\n\n"
pm_caption += "🔶🔶 **ᴄʀᴇᴅɪᴛs**🔶🔶  >>》 [ᴛᴇᴀᴍ-ᴄᴏʙʀᴀ](https://t.me/dark_cobra_support)\n\n"
pm_caption += "[....▄███▄███▄\n....█████████\n.......▀█████▀\n...............▀█▀\n](https://t.me/itsproplugins)\n\n"

@borg.on(admin_cmd(pattern=r"mello"))
@borg.on(sudo_cmd(pattern=r"sudo", allow_sudo=True))

async def amireallyalive(yes):
    chat = await yes.get_chat()
    global ghanti
    ghanti = borg.uid
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file4)

    await alive.delete()
    
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@borg.on(admin_cmd(outgoing=True, pattern="salive"))
@borg.on(sudo_cmd(pattern=r"salive", allow_sudo=True))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    if ALIVE_PHOTTO:
        pm_caption = "**Marshmello 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
        pm_caption += f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
        pm_caption += "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
        pm_caption += "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
        pm_caption += "Creator                 : [BOSS-DJ](https://t.me/Beast_boy_shubu)\n"
        pm_caption += "Bot Status              : Working perfectly\n"
        pm_caption += "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/Beast_boy_shubu)\n"
        pm_caption += "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ MARSHMELLO ](https://t.me/Marshmello_op)\n"
        pm_caption += "[┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Cyber_legendss)"
        chat = await alive.get_chat()
        await alive.delete()
        """ For .allive command, check if the bot is running.  """
        await borg.send_file(alive.chat_id, ALIVE_PHOTTO,caption=pm_caption, link_preview = False)
        await allive.delete()
        return
    req = requests.get("https://telegra.ph/file/d39ef0f5a3d7d684f2e33.png")
    req.raise_for_status()
    file = BytesIO(req.content)
    file.seek(0)
    img = Image.open(file)
    with BytesIO() as sticker:
        img.save(sticker, "webp")
        sticker.name = "sticker.webp"
        sticker.seek(0)
        await borg.send_file(alive.chat_id, file=sticker)
        await borg.send_message(alive.chat_id,"**Marshmello 𝙸𝚂 🅾︎🅽🅻🅸🅽🅴**\n"
                      f"**𝕄𝕪 𝔹𝕠𝕤𝕤**            : {DEFAULTUSER}\n"
                      "𝚃𝙴𝙻𝙴𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽        : 1.17.5\n"
                      "𝙿𝚈𝚃𝙷𝙾𝙽 𝚅𝙴𝚁𝚂𝙸𝙾𝙽          : 3.9.0\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻         : [ᴊᴏɪɴ](https://t.me/PROBOY_GFX)\n"
                      "𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿           : [ᴊᴏɪɴ](https://t.me/CYBER_LEGENDSS)\n"
                      "𝘓𝘐𝘚𝘌𝘕𝘊𝘌                  : [AGPL-3.0  ʟɪᴄᴇɴꜱᴇ](https://jenaatul8.wixsite.com/BEAST_BOY_SHUBU)\n"
                      "𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏 𝘽𝙔            : [ DARK-COBRA ](https://t.me/DARK-COBRA)\n"
                                "[ ┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/CYBER_LEGENDSS)" , link_preview = False) 
        await alive.delete()
