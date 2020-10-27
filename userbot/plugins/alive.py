import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/file/132e17041c9a8ae696474.jpg"
pm_caption = "**Dᴀʀᴋ Cᴏʙʀᴀ 🅸🆂 🅾🅽🅻🅸🅽🅴**\n"

pm_caption += f"**M ʏ  B ᴏ s s**              : {DEFAULTUSER}\n"

pm_caption += "Mʏ Bᴏᴛ Sᴛᴀᴛᴜꜱ        : Wᴏʀᴋɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ 🔥\n"

pm_caption += "тєℓєтнσи                   : тєℓєтнσи-15.0.0 𖤐⃟🔷\n"

pm_caption += "ρутнσи                       : ρутнσи-3.8.5 𖤐⃟🔷\n"

pm_caption += "ι'ℓℓ вє ωιтн му мαѕтєя тιℓℓ му ∂уиσ єи∂ѕ!!☠ 𖤐⃟🛰\n ραят σғ тнε נσυяηεү ιs тнε εη∂\n"

pm_caption += "[ ┏┓━┏┓━━━━┏┓━┏┓━━━━━\n ┃┃━┃┃━━━━┃┃━┃┃━━━━━\n ┃┗━┛┃┏━━┓┃┃━┃┃━┏━━┓\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━┃┏┓┃ \n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓┃┗┛┃ \n ┗┛━┗┛┗━━┛┗━┛┗━┛┗━━┛](https://t.me/Dark_cobra_support_group)"
#@command(outgoing=True, pattern="^.mello$")
@borg.on(admin_cmd(pattern=r"mello"))
async def amireallyalive(alive):
    chat = await mello.get_chat()
    await mello.delete()
    """ For .mello command, check if the bot is running.  """
    await borg.send_file(mello.chat_id, PM_IMG,caption=pm_caption)
    await mello.delete() 
