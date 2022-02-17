#Author: Box In A Box [TG: @Box_Boi ]

from userge import userge, Message
from userge.utils import runcmd

@userge.on_cmd("ginvite", about={
    'header': "Invite Users To Private GitHub Repo!",
    'usage': "{tr}ginvite (GitHub-UserName) (GitHub-RepoName)",
    'examples': "{tr}ginvite boxboi689 xiaomi_ginkgo_dump"})
async def test_(message: Message):
    """ Initiate Invite Process """
    cmd = message.input_str
    if cmd is None:
        return
    await message.edit("**Inviting User To Mentioned Private Repo ...**")
    try:
        out, err, ret, pid = await runcmd("bash invite.sh " + '"' + cmd + '"')
    except Exception as t_e:
        await message.err(str(t_e))
        return
    out = out or "no output"
    out = "\n".join(out.split("\n"))
    output = f"**Invite Status:**\n\n``{out}`` "
    await message.edit_or_send_as_file(text=output,
                                       parse_mode='md',
                                       filename="exec.txt",
                                       caption=cmd)
