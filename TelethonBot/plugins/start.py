# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/xditya")],
                        [Button.inline("T&C",data="example")]
                    ])

# callback for t&c button
@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    to_show = """
T&C Apply

This is a sample paragraph.
.
.
"""
    await event.edit(to_show,
                    buttons=[Button.inline("Back", data="backbutt")])

# callback for back button 
@BotzHub.on(events.callbackquery.CallbackQuery(data="backbutt"))
async def bacckk(event):
    await event.edit("Hello!",
                    buttons=[
                        [Button.url("ButtonUrl", url="https://t.me/xditya")],
                        [Button.inline("T&C",data="example")]
                    ])