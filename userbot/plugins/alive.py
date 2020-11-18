
import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
# 🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "marshmello"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking)
# Made by @hellboi_atul ....and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for DC(DARK COBRA)

edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/d87c592d13e9a134ef3b0.jpg"
file2 = "https://telegra.ph/file/8970a0bb9f863e353bdc2.jpg"
file3 = "https://telegra.ph/file/a1161a87a679242ecde17.jpg"
file4 = "https://telegra.ph/file/2a280941fcdd30c77e65a.jpg"
""" =======================CONSTANTS====================== """
pm_caption += "**ᴍᴀʀsʜᴍᴇʟʟᴏ ɪs ᴏɴʟɪɴᴇ**\n"
pm_caption += "ɪ ᴀᴍ ᴏɴʟɪɴᴇ ᴍʏ ᴘᴇʀᴜ ᴍᴀsᴛᴇʀ\n"
pm_caption += "`• ᴘʏᴛʜᴏɴ : 3.8.6`\n"
pm_caption += "`• ᴛᴇʟᴇᴛʜᴏɴ : 15.0.0`\n"
pm_caption += f"`• ᴍʏ ᴍᴀsᴛᴇʀ` :{DEFAULTUSER}\n"
pm_caption += "`• ᴍᴀʀsʜᴍᴇʟʟᴏ ᴠᴇʀsɪᴏɴ : 1.0.0`\n"
pm_caption += "sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : [ᴊᴏɪɴ](http://t.me/Marshmellobot_officiall)\n"
pm_caption += "sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ : [ᴊᴏɪɴ](http://t.me/Marshmello_support)\n"

@borg.on(admin_cmd(pattern=r"mello"))

async def amireallyalive(yes):
    chat = await yes.get_chat()

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
    
    """ For .mello command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete()
