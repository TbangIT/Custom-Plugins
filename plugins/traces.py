from pyrogram.errors import ChannelPrivate, PeerIdInvalid
from userge import userge, Message


@userge.on_cmd(
    "rmt",
    about={
        "header": "Delete all your traces (message) from a specific chat. Only works for groups.",
        "usage": "{tr}rmt [id | username]",
        "examples": [
            "{tr}rmt - will delete all the messages sent by you from the current chat.",
            "{tr}rmt @UsergeSpam - will delete all the messages sent by you from the chat with username @UsergeSpam.",
            "{tr}rmt -123456789 - will delete all the messages sent by you from the chat with ID -123456789.",
        ],
        "others": "NOTE: Due to a caching delay of Telegram chats, this function needs a cooldown of at least 5 minutes (probably) before it can be used again.",
    },
)
async def remove_traces(m: Message):
    if m.input_str:
        if m.input_str.startswith("@"):
            try:
                c = await userge.get_chat(m.input_str)
            except:
                await m.err(
                    "Chat doesn't exist or you haven't joined it yet!", del_in=5
                )
                return
        else:
            try:
                c = await userge.get_chat(int(m.input_str))
            except ValueError or PeerIdInvalid:
                await m.err(
                    "Chat doesn't exist or you haven't joined it yet!", del_in=5
                )
                return
            except ChannelPrivate:
                await m.err(
                    "Can't access private chat which you're not a member of.", del_in=5
                )
                return

        if c.type not in ["group", "supergroup"]:
            await m.err("This command is only supported for groups.", del_in=5)
            return
        res = await m.edit(f"Removing your traces from **{c.title}** ...")
        n = await _remove_traces(c)
        if n == 0:
            await m.edit(
                "No traces to remove!\n\n**NOTE**: This may be due to the cooldown.",
                del_in=5,
            )
        else:
            await m.edit(
                f"Done! Purged {n} messages from **{c.title}**", del_in=5, log=True
            )
    else:
        if m.chat.type not in ["group", "supergroup"]:
            await m.err("This command is only supported for groups.", del_in=5)
            return
        res = await m.edit("Removing your traces ...")
        n = await _remove_traces(m.chat)
        if n == 0:
            await m.edit(
                "No traces to remove!\n\n**NOTE**: This may be due to the cooldown.",
                del_in=5,
            )
        else:
            await m.edit(f"Done! Purged {n} messages.", del_in=5, log=True)


async def _remove_traces(chat):
    n = 0
    async for m in userge.search_messages(chat_id=chat.id, from_user=userge.id):
        await m.delete()
        n += 1
    return n
