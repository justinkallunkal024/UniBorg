"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 6

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "hack":

        await event.edit(input_str)

        animation_chars = [
        
            "`Connecting To Anandus Private Server...`",
            "`Target Selected.`",
            "`Hacking... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Hacking... 4%\n█▒▒▒▒▒searching for all pics and clips▒▒ `",
            "`Hacking... 8%\n██connecting to anandus satelite system🛰️🛰️ `",    
            "`Hacking... 20%\n█████copying started with 120Mb per second `",
            "`Hacking... 36%\n█████████compressing hidden pictures and videos🤭🤭🤭 `",
            "`Hacking... 52%\n█████████████▒▒copying to my cloud `",
            "`Hacking... 84%\n███████████████████completed in 12.765 sec `",
            "`Hacking... 100%\n███completed hacking contact hacker and pay `",
            "`Targeted Account Hacked...\n\nPay @ANANDUS To free your data`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
