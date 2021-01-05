# Darkcobra Original 🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍🐍
# kangers Keep Credits 😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒😒
# Made by Dc-Team
# Don't remove these lines u fool ,,, 
#
#
#hehehhe

from math import ceil
import asyncio
import json
import random
import os,re
import urllib
from telethon.tl.custom import Button 
from telethon import events, errors, custom, functions
from userbot import CMD_LIST, CMD_HELP
import io
import math
import time

from telethon import Button, custom, events
#Making The Back Command Was The Toughest Work #by @Shivam_Patel,@The_Siddharth_Nigam,sexygirlbhaibhigandu sab@danish_00,@ProgrammingError also v changed Pop up or inline help to text
if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:

    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        hmm = re.compile("secret (.*) (.*)")
        match = re.findall(hmm, query)
        if event.query.user_id == bot.uid and match:
            query = query[7:]
            user, txct = query.split(" ", 1)
            builder = event.builder
            secret = os.path.join("./userbot", "secrets.txt")
            try:
                jsondata = json.load(open(secret))
            except:
                jsondata = False
            try:
                # if u is user id
                u = int(user)
                try:
                    u = await event.client.get_entity(u)
                    if u.username:
                        sandy = f"@{u.username}"
                    else:
                        sandy = f"[{u.first_name}](tg://user?id={u.id})"
                except ValueError:
                    # ValueError: Could not find the input entity
                    sandy = f"[user](tg://user?id={u})"
            except ValueError:
                # if u is username
                try:
                    u = await event.client.get_entity(user)
                except ValueError:
                    return
                if u.username:
                    sandy = f"@{u.username}"
                else:
                    sandy = f"[{u.first_name}](tg://user?id={u.id})"
                u = int(u.id)
            except:
                return
            timestamp = int(time.time() * 2)
            newsecret = {str(timestamp): {"userid": u, "text": txct}}

            buttons = [
                custom.Button.inline("show message 🔐", data=f"secret_{timestamp}")
            ]
            result = builder.article(
                title="secret message",
                text=f"🔒 A whisper message to {sandy}, Only he/she can open it.",
                buttons=buttons,
            )
            await event.answer([result] if result else None)
            if jsondata:
                jsondata.update(newsecret)
                json.dump(jsondata, open(secret, "w"))
            else:
                json.dump(newsecret, open(secret, "w"))
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"secret_(.*)")))
    async def on_plug_in_callback_query_handler(event):
        timestamp = int(event.pattern_match.group(1).decode("UTF-8"))
        if os.path.exists("./userbot/secrets.txt"):
            jsondata = json.load(open("./userbot/secrets.txt"))
            try:
                message = jsondata[f"{timestamp}"]
                userid = message["userid"]
                ids = [userid, bot.uid]
                if event.query.user_id in ids:
                    encrypted_tcxt = message["text"]
                    reply_pop_up_alert = encrypted_tcxt
                else:
                    reply_pop_up_alert = "why were you looking at this shit go away and do your own work, idiot"
            except KeyError:
                reply_pop_up_alert = "This message no longer exists in bot server"
        else:
            reply_pop_up_alert = "This message no longer exists "
        await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back")))
   
    async def backr(event):
            if event.query.user_id == bot.uid :
                current_page_number=0
                dc = paginate_help(current_page_number, CMD_LIST, "helpme")
                await event.edit("`>>>>\nHere Is The Main Menu Of\n©Marshmello`", buttons=dc)
            else:
                reply_pop_up_alert = "Bhaggg Behenchod Khud ka bana mera kyu le raha hai Gandu!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"open")))
   
    async def opner(event):
            if event.query.user_id == bot.uid :
                current_page_number=0
                dc = paginate_help(current_page_number, CMD_LIST, "helpme")
                await event.edit("`>>>\n\nReopened The Main Menu of \n©MARSHMELLO` ", buttons=dc)
            else:
                reply_pop_up_alert = "AYE MADARCHOD KHUD KA BANA MERA USE MAT KAR!"
                await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
               

    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == bot.uid and query.startswith("Userbot"):
            rev_text = query[::-1]
            dc = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article("© Userbot Help",text="{}\nCurrently Loaded Plugins: {}".format(query, len(CMD_LIST)),buttons=dc,link_preview=False)
            await event.answer([result] if result else None)
        else:
              reply_pop_up_alert = "TERI MAA KA BHOSDA KHUD KA BANA MERA MAT DEKH"
              await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
#hehehehehheh           
            await event.edit(buttons=dc)
        else:
            reply_pop_up_alert = "TERI MAA KA BHOSDA KHUD KA BANA MERA MAT DEKH!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)

#hehhehehehhehhehhehehhe
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:  # pylint:disable=E0602
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            
            dc = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            
            await event.edit(buttons=dc)
        else:
              reply_pop_up_alert = "Please get your own Userbot😁😁! 😎😎"
              await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
 #hehehehehhehhehhehe   
    @tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"close")))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == bot.uid:
            dc = custom.Button.inline("ορєи мαιи мєиυ αgαιи", data="open")
            await event.edit("`Main Menu Has Been Closed by Marshmello`", buttons=dc)
        else:
            reply_pop_up_alert = "Please get your own Userbot😁😁 😎😎"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
    
  
    @tgbot.on(
        events.callbackquery.CallbackQuery(  # pylint:disable=E0602
            data=re.compile(b"us_plugin_(.*)")
        )
    )
    async def on_plug_in_callback_query_handler(event):
        if not event.query.user_id == bot.uid:
            cobra = "Please get your own Userbot😁😁 😎😎"
            await event.answer(cobra, cache_time=0, alert=True)
            return
        plugin_name = event.data_match.group(1).decode("UTF-8")
        help_string = "Commands found in {}:\n".format(plugin_name)
        for i in CMD_LIST[plugin_name]:
            help_string += "💎 " + i + "\n\n"
        if plugin_name in CMD_HELP:
            help_string += (
                f"**📤 PLUGIN NAME 📤 :** `{plugin_name}` \n\n{CMD_HELP[plugin_name]}"
            )
        else:
            help_string += " CMD_HELP not set yet for {} 😅😅".format(plugin_name)

        reply_pop_up_alert = help_string
        reply_pop_up_alert += (
            "\n\n Use .unload {} to remove this plugin\n ©MARSHMELLO Userbot".format(plugin_name)
        )
        dc = [
            custom.Button.inline("мαιи мєиυ", data="back"),
            custom.Button.inline("clօsҽ", data="close"),
        ]
        if len(reply_pop_up_alert) >= 4096:
            crackexy = "`Pasting Your Help Menu.`"
            await event.answer(crackexy, cache_time=0, alert=True)
            out_file = reply_pop_up_alert
            url = "https://del.dog/documents"
            r = requests.post(url, data=out_file.encode("UTF-8")).json()
            url = f"https://del.dog/{r['key']}"
#hehehhehhehehheheh
            await event.edit(
                f"Pasted {plugin_name} to {url}", link_preview=False, buttons=dc
            )
        else:
            await event.edit(message=reply_pop_up_alert, buttons=dc)

def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = Config.NO_OF_BUTTONS_DISPLAYED_IN_H_ME_CMD
    number_of_cols = Config.NO_OF_COLOUMS_DISPLAYED_IN_H_ME_CMD
    multi = Config.EMOJI_TO_DISPLAY_IN_HELP
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {}".format(random.choice(list(multi)), x),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("ճαck", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("clօsҽ", data="close"),
             custom.Button.inline("иєxτ", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs

# chal nikal 
# gtfo
