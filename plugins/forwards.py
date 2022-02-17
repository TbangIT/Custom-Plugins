import os

from userge import userge, filters, Message
from pyrogram.errors import FloodWait

LOGS = userge.getLogger(__name__)
X1, X2 = os.environ.get("FORWARDS_DATA").split()


@userge.bot.on_message(filters.chat(int(X1)) & (filters.document | filters.video | filters.animation | filters.media_group))
async def mcopy(_, m):
    try:
        await m.copy(int(X2))
    except FloodWait as ex:
        LOGS.info(ex)
        await asyncio.sleep(fw.x + 10)
    except Exception as e:
        LOGS.exception(e)
