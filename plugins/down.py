from urllib.parse import unquote_plus
from userge.plugins.misc.upload import os, Path, url_download, upload
from userge import userge , Message
from pyrogram import filters

@userge.on_cmd("down",about={"header":"custom downloader"
})
async def down_file(m):
 try:
   _url = m.input_str
   file = unquote_plus(os.path.basename(_url))
   file_name = f"@FreepikRequests_{file.split('?')[0]}"
   f_url = _url + '|' + file_name

   url_, t = await url_download(m, f_url)
   await m.edit(f"Downloaded in <code>{t} sec</code>")
   strin = Path(url_)
   string = str(strin).replace(".zip","")
   os.rename(strin, f"{string}.zip")
   await upload(m,Path(f"{string}.zip"), True)
 except Exception as e:
      await m.err(e)