import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Hell User"
PM_IMG = "https://telegra.ph/file/624bc140c03e9c28afcca.jpg"
pm_caption = "👿 **Marshmello ßot Is Online** 👿\n"

pm_caption += f"**M Y  B O S S **              : {DEFAULTUSER}\n"

pm_caption += "Mʏ Bᴏᴛ Sᴛᴀᴛᴜꜱ        : Wᴏʀᴋɪɴɢ ᴘᴇʀғᴇᴄᴛʟʏ 🔥\n"

pm_caption += "тєℓєтнσи                   : тєℓєтнσи-15.0.0 𖤐⃟🔷\n"

pm_caption += "ρутнσи                       : ρутнσи-3.8.5 𖤐⃟🔷\n"

pm_caption += "😈Hêll ẞø†😈               : Ɩɛɠɛŋɖʂ ßòt𖤐⃟🔷\n"

pm_caption += "'ℓℓ вє ωιтн му мαѕтєя тιℓℓ му ∂уиσ єи∂ѕ!!☠ 𖤐⃟🛰\n ραят σғ тнε נσυяηεү ιs тнε εη∂\n\n"

pm_caption += " [██████╗░░░░░░██╗\n ██╔══██╗░░░░░██║\n ██║░░██║░░░░░██║\n ██║░░██║██╗░░██║\n ██████╔╝╚█████╔╝\n ╚═════╝░░╚════╝░\n](https://https://t.me/Marshmellobot_official)\n"
#@command(outgoing=True, pattern="^.mello$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .mello command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
