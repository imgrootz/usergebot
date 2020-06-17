# Copyright (C) 2020 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/uaudith/Userge/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.errors.exceptions import FileIdInvalid, FileReferenceEmpty
from pyrogram.errors.exceptions.bad_request_400 import BadRequest

from userge import userge, Message, Config, versions

LOGO_STICKER_ID, LOGO_STICKER_REF = None, None


@userge.on_cmd("alive", about={'header': "This command is just for fun"})
async def alive(message: Message):
    await message.delete()
    output = f"""
× `I'm alive and running ^_^`
• **Python version** : `{versions.__python_version__}`
• **Pyrogram version** : `{versions.__pyro_version__}`
• **Userge version** : `{versions.__version_}`
• **Repository** : [UsergeRemix]({Config.UPSTREAM_REPO})
"""
    await userge.send_message(message.chat.id, output, disable_web_page_preview=True)
