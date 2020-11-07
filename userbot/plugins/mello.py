import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Don't Change This"
PM_IMG = "https://telegra.ph/file/c735db5b11ded78784257.jpg"
pm_caption = "**𐌑𐌀𐍂𐍃𐋏𐌑𐌄𐌋𐌋𐍈 is ONLINE\n\n"

pm_caption += "ι αм αℓινє мγ ρєяο мαѕτєя ωιτн иєϲєѕѕαяγ ∂γиοѕ 😘\n\n"

pm_caption += "sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ : [ᴊᴏɪɴ](https://t.me/marshmellobot_official)\n"

pm_caption += "sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ : [ᴊᴏɪɴ](https://t.me/marshmello_userbot)\n"

pm_caption += "ᴘʏᴛʜᴏɴ : 3.5.8 ᴘʏᴛʜᴏɴ 𖤐⃟🔷\n"

pm_caption += "Mʏ Bᴏᴛ Sᴛᴀᴛᴜꜱ : Wᴏʀᴋɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ 🔥\n"

pm_caption += "тєℓєтнσи : тєℓєтнσи-15.0.0 𖤐⃟🔷\n"

pm_caption += f"**My Master : {DEFAULTUSER}\n\n"

pm_caption += " [██████╗░░░░░░██╗\n ██╔══██╗░░░░░██║\n ██║░░██║░░░░░██║\n ██║░░██║██╗░░██║\n ██████╔╝╚█████╔╝\n ╚═════╝░░╚════╝░\n](https://t.me/Marshmello_userbot)"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
