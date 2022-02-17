#Author: Box In A Box [TG: @Box_Boi ]

from userge import userge, Message
from userge.utils import runcmd

@userge.on_cmd("release", about={
    'header': "Release Files To SourceForge!",
    'usage': "{tr}release romname devicename romlink (rom-codename)",
    'examples': "{tr}release generic merlin (link)"})
async def release_(message: Message):
    """ Initiate Release Process """
    cmd = message.input_str
    if cmd is None:
        return
    await message.edit("**Releasing Rom to SourceForge.**")
    try:
        out, err, ret, pid = await runcmd("bash release.sh " + '"' + cmd + '"')
        await message.edit("**Releasing Rom to SourceForge..**")
        await message.edit("**Releasing Rom to SourceForge...**")
        await message.edit("**Releasing Rom to SourceForge....**")
        await message.edit("**Releasing Rom to SourceForge.....**")
        await message.edit("**Releasing Rom to SourceForge......**")
        await message.edit("**Releasing Rom to SourceForge.......**")
        await message.edit("**Releasing Rom to SourceForge........**")
        await message.edit("**Releasing Rom to SourceForge.........**")
    except Exception as t_e:
        await message.err(str(t_e))
        return
    out = out or "no output"
    out = "\n".join(out.split("\n"))
    output = f"**Rom Release Status:**\n(Link Will Be Availaible **Only** After 10Min Cause Sourceforge is Slow)\n\n``{out}`` "
    await message.edit_or_send_as_file(text=output,
                                       parse_mode='md',
                                       filename="exec.txt",
                                       caption=cmd)
