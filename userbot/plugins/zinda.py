import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/91a00acf67d80235e11f0.jpg"
pm_caption = "**𐌑𐌀𐍂𐍃𐋏𐌑𐌄𐌋𐌋𐍈 is ONLINE\n"

pm_caption += "i am ALIVE MY MASTER.....

pm_caption += f"**M̴ y̴  ̴B̴ o̴s̴ s̴**        : {DEFAULTUSER}\n"

pm_caption += "support group           : [ᴊᴏɪɴ](https://t.me/marshmellobot_official)\n"

pm_caption += "support channel         : [ᴊᴏɪɴ](https://t.me/marshmello_userbot)\n"


pm_caption += " [───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───\n───█▒▒░░░░░░░░░▒▒█───\n────█░░█░░░░░█░░█────\n─▄▄──█░░░▀█▀░░░█──▄▄─\n█░░█─▀▄░░░░░░░▄▀─█░░█\n█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█\n█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█\n█░░║║║╠─║─║─║║║║║╠─░░█\n█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█\n█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n](https://t.me/pycodingwithayush)"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
