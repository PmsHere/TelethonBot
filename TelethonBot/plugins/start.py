# By < @xditya >
# // @BotzHub //
from .. import BotzHub
from telethon import events, Button

@BotzHub.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hҽყ ƚԋҽɾҽ! Mყ ɳαɱҽ ιʂ [คυŕҽɭเค..♜..⚑](https://telegra.ph/file/9abcb7f46a10c43e99c3a.jpg)"
                      "-I'ɱ ԋҽɾҽ ƚσ ԋҽʅρ ყσυ ƚσ ɱαɳαɠҽ ყσυɾ ɠɾσυρʂ ƈσσʅ"
                      "Wαɳƚ ƚσ αԃԃ ɱҽ ιɳ ɠɾσυρ?"
                      "Cʅιƈƙ [ԋҽɾҽ!](http://t.me/Miss_Aurelia_bot?startgroup=true)",
                    buttons=[
                        [Button.url("Update Channel", url="https://t.me/AureliaBot_Support")],
                        [Button.inline("T&C",data="example")]
                    ])

# callback for t&c button
@BotzHub.on(events.callbackquery.CallbackQuery(data="example"))
async def ex(event):
    to_show = """
**Terms and Conditions:**

- Only your first name, last name (if any) and username (if any) is stored for a convenient communication!
- No group ID or it's messages are stored, we respect everyone's privacy.
- Messages between Bot and you is only infront of your eyes and there is no backuse of it.
- Watch your group, if someone is spamming your group, you can use the report feature of your Telegram Client.
- Do not spam commands, buttons, or anything in bot PM.

**NOTE:** __Terms and Conditions might change anytime__

**Updates Channel: @AureliaBot_Support**
"""
    await event.edit(to_show,
                    buttons=[Button.inline("Back", data="backbutt")])

# callback for back button 
@BotzHub.on(events.callbackquery.CallbackQuery(data="backbutt"))
async def bacckk(event):
    await event.edit("Hҽყ ƚԋҽɾҽ! Mყ ɳαɱҽ ιʂ [คυŕҽɭเค..♜..⚑](https://telegra.ph/file/9abcb7f46a10c43e99c3a.jpg)"
                     "-I'ɱ ԋҽɾҽ ƚσ ԋҽʅρ ყσυ ƚσ ɱαɳαɠҽ ყσυɾ ɠɾσυρʂ ƈσσʅ"
                     "Wαɳƚ ƚσ αԃԃ ɱҽ ιɳ ɠɾσυρ?"
                     "Cʅιƈƙ [ԋҽɾҽ!](http://t.me/Miss_Aurelia_bot?startgroup=true)",
                    buttons=[
                        [Button.url("Updates Channel", url="https://t.me/AureliaBot_Support")],
                        [Button.inline("T&C",data="example")]
                    ])
