#Credit To @Beast_boy_shubu . Keep credit if you are going to edit it.


import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="ping ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("✨🎶Ping")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping✨🎶Pong")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping✨🎶Pong✨🎶")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping✨🎶Pong✨🎶✨🎶")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping✨🎶Pong✨🎶✨🎶Ping")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping✨🎶Pong✨🎶✨🎶Ping✨🎶Ping")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping✨🎶Pong✨🎶✨🎶Ping✨🎶Ping✨🎶✨🎶")
        await asyncio.sleep(0.4)
        await event.edit("✨🎶Ping✨🎶Pong✨🎶✨🎶✨🎶Ping✨🎶Pong✨🎶✨🎶Ping✨🎶Ping✨🎶✨🎶Pong✨🎶...")
        
