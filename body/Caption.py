import os
import sys
import re
from pyrogram import *
from info import *
import asyncio
from Script import script
from .database import *
from pyrogram.errors import FloodWait
from pyrogram.types import *

@Client.on_message(filters.command("start") & filters.private)
async def strtCap(bot, message):
    user_id = int(message.from_user.id)
    await insert(user_id)
    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"https://t.me/CustomCaptionBot?startchannel=true")
            ],[
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
            ],[
                InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Silicon_Bot_Update"),
                InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url=r"https://t.me/Silicon_Botz")
        ]]
    )
    await message.reply_photo(
        photo=SILICON_PIC,
        caption=f"<b>Hᴇʟʟᴏ {message.from_user.mention}\n\nɪ ᴀᴍ ᴀᴜᴛᴏ ᴄᴀᴘᴛɪᴏɴ ʙᴏᴛ ᴡɪᴛʜ ᴄᴜsᴛᴏᴍ ᴄᴀᴘᴛɪᴏɴ.\n\nFᴏʀ ᴍᴏʀᴇ ɪɴғᴏ ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.\n\nMᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ »<a href='https://t.me/Silicon_Bot_Update'>Sɪʟɪᴄᴏɴ Bᴏᴛᴢ</a></b>",
        reply_markup=keyboard
    )

@Client.on_message(filters.private & filters.user(ADMIN)  & filters.command(["total_users"]))
async def all_db_users_here(client,message):
    silicon = await message.reply_text("Please Wait....")
    silicon_botz = await total_user()
    await silicon.edit(f"Tᴏᴛᴀʟ Usᴇʀ :- `{silicon_botz}`")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if (message.reply_to_message):
        silicon = await message.reply_text("Geting All ids from database..\n Please wait")
        all_users = await getid()
        tot = await total_user()
        success = 0
        failed = 0
        deactivated = 0
        blocked = 0
        await silicon.edit(f"ʙʀᴏᴀᴅᴄᴀsᴛɪɴɢ...")
        async for user in all_users:
            try:
                time.sleep(1)
                await message.reply_to_message.copy(user['_id'])
                success += 1
            except errors.InputUserDeactivated:
                deactivated +=1
                await delete({"_id": user['_id']})
            except errors.UserIsBlocked:
                blocked +=1
                await delete({"_id": user['_id']})
            except Exception as e:
                failed += 1
                await delete({"_id": user['_id']})
                pass
            try:
                await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴘʀᴏᴄᴇssɪɴɢ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")
            except FloodWait as e:
                await asyncio.sleep(t.x)
        await silicon.edit(f"<u>ʙʀᴏᴀᴅᴄᴀsᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ</u>\n\n• ᴛᴏᴛᴀʟ ᴜsᴇʀs: {tot}\n• sᴜᴄᴄᴇssғᴜʟ: {success}\n• ʙʟᴏᴄᴋᴇᴅ ᴜsᴇʀs: {blocked}\n• ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs: {deactivated}\n• ᴜɴsᴜᴄᴄᴇssғᴜʟ: {failed}")

@Client.on_message(filters.private & filters.user(ADMIN) & filters.command("restart"))
async def restart_bot(b, m):
    silicon = await b.send_message(text="**🔄 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙴𝚂 𝚂𝚃𝙾𝙿𝙴𝙳. 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶...**", chat_id=m.chat.id)       
    await asyncio.sleep(3)
    await silicon.edit("**✅️ 𝙱𝙾𝚃 𝙸𝚂 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳. 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝚄𝚂𝙴 𝙼𝙴**")
    os.execl(sys.executable, sys.executable, *sys.argv)

@Client.on_message(filters.command("set_cap") & filters.channel)
async def setCap(bot, message):
    if len(message.command) < 2:
        return await message.reply(
            "Usᴀɢᴇ: **/set_cap 𝑌𝑜𝑢𝑟 𝑐𝑎𝑝𝑡𝑖𝑜𝑛 𝑈𝑠𝑒 <code>{file_name}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑁𝑎𝑚𝑒.\n\n𝑈𝑠𝑒<code>{file_size}</code> 𝑇𝑜 𝑠ℎ𝑜𝑤 𝑦𝑜𝑢𝑟 𝐹𝑖𝑙𝑒 𝑆𝑖𝑧𝑒/n/n✓ 𝑀𝑎𝑦 𝐵𝑒 𝑁𝑜𝑤 𝑌𝑜𝑢 𝑎𝑟𝑒 𝑐𝑙𝑒𝑎𝑟💫**"
        )
    chnl_id = message.chat.id
    caption = (
        message.text.split(" ", 1)[1] if len(message.text.split(" ", 1)) > 1 else None
    )
    chkData = await chnl_ids.find_one({"chnl_id": chnl_id})
    if chkData:
        await updateCap(chnl_id, caption)
        return await message.reply(f"Your New Caption: {caption}")
    else:
        await addCap(chnl_id, caption)
        return await message.reply(f"Yᴏᴜʀ Nᴇᴡ Cᴀᴘᴛɪᴏɴ Is: {caption}")

@Client.on_message(filters.command("del_cap") & filters.channel)
async def delCap(_, msg):
    chnl_id = msg.chat.id
    try:
        await chnl_ids.delete_one({"chnl_id": chnl_id})
        return await msg.reply("<b><i>✓ Sᴜᴄᴄᴇssғᴜʟʟʏ... Dᴇʟᴇᴛᴇᴅ Yᴏᴜʀ Cᴀᴘᴛɪᴏɴ Nᴏᴡ I ᴀᴍ Usɪɴɢ Mʏ Dᴇғᴀᴜʟᴛ Cᴀᴘᴛɪᴏɴ </i></b>")
    except Exception as e:
        e_val = await msg.replay(f"ERR I GOT: {e}")
        await asyncio.sleep(5)
        await e_val.delete()
        return

#def extract_language(default_caption):
    #language_pattern = r'\b(Hindi|English|Tamil|Telugu|Malayalam|Kannada|Hin)\b'#Contribute More Language If You Have
    #languages = set(re.findall(language_pattern, default_caption, re.IGNORECASE))
    #if not languages:
        #return "Hindi-English"
    #return ", ".join(sorted(languages, key=str.lower))

def extract_language(default_caption):
    language_map = {
        'hindi': 'Hindi',
        'hin': 'Hindi',
        'english': 'English',
        'eng': 'English',
        'tamil': 'Tamil',
        'tam': 'Tamil',
        'telugu': 'Telugu',
        'tel': 'Telugu',
        'malayalam': 'Malayalam',
        'mal': 'Malayalam',
        'kannada': 'Kannada',
        'bengali': 'Bengali',
        'marathi': 'Marathi',
        'gujarati': 'Gujarati',
        'punjabi': 'Punjabi',
        'bhojpuri': 'Bhojpuri',
        'urdu': 'Urdu',
        'oriya': 'Oriya',
        'assamese': 'Assamese',
        'konkani': 'Konkani',
        'kashmiri': 'Kashmiri',
        'sindhi': 'Sindhi',
        'tulu': 'Tulu'
    }
    pattern = r'\b(' + '|'.join(re.escape(lang) for lang in language_map.keys()) + r')\b'
    matches = re.findall(pattern, default_caption, re.IGNORECASE)
    found_languages = {
        language_map.get(match.lower(), '').strip().title()
        for match in matches if match.lower() in language_map
    } 
    return ", ".join(sorted(found_languages)) if found_languages else ""
    
#def extract_year(default_caption):
    #match = re.search(r'\b(19\d{2}|20\d{2})\b', default_caption)
    #return match.group(1) if match else None
    
def extract_year(default_caption):
    possible_years = re.findall(r'\b(19\d{2}|20\d{2})\b', default_caption)
    for year in possible_years:
        y = int(year)
        if 1900 <= y <= 2099:
            return str(y)
    return ""

def clean_filename(file_name, enable_debug=False, enable_metadata=False):
    allowed_extensions = ('mkv', 'mp4', 'avi', 'mov', 'flv', 'webm')
    extension = ''
    original_name = file_name
    ext_match = re.search(r'\.({})$'.format('|'.join(allowed_extensions)), file_name, re.IGNORECASE)
    if ext_match:
        extension = f".{ext_match.group(1).lower()}"
        file_name = file_name[:ext_match.start()]
        
    file_name = re.sub(r'@\w+', '', file_name)
    spam_patterns = [
        r'https?://\S+',         # URLs
        r't\.me/\S+',            # Telegram links
        r'\b(join|subscribe|visit|channel|movieverse|by|admin)\b',  # Common spam
        r'[^\w\s\.-]',   # Emojis or special chars
    ]
    for pattern in spam_patterns:
        file_name = re.sub(pattern, '', file_name, flags=re.IGNORECASE)
        
    file_name = re.sub(r'[_.]+', ' ', file_name)
    file_name = re.sub(r'[<>:"/\\|?*]', '', file_name)
    file_name = re.sub(r'\s+', ' ', file_name).strip()
    tags = re.findall(r'(.*?)', file_name)
    file_name = re.sub(r'\s*.*?', '', file_name).strip()
    if tags:
        file_name += ' ' + ' '.join(f'[{tag}]' for tag in tags)
        
    file_name = file_name.title()
    file_name = f"{file_name}{extension}"
    if enable_debug:
        print("Original:", original_name)
        print("Cleaned: ", file_name)
        print("Extension:", extension)

    return file_name

def extract_title(file_name):
    title = re.sub(r'[].*?[]', '', file_name)  # Remove tags
    title = re.sub(r'\b(19\d{2}|20\d{2})\b', '', title)  # Remove year
    title = re.sub(r'\b(720p|1080p|2160p|HDRip|BluRay|x264|HEVC|WEBRip|HD)\b', '', title, flags=re.IGNORECASE)
    title = re.sub(r'\s+', ' ', title).strip()
    return title
    
@Client.on_message(filters.channel)
async def reCap(bot, message):
    chnl_id = message.chat.id
    default_caption = message.caption
    if message.media:
        for file_type in ("video", "audio", "document", "voice"):
            obj = getattr(message, file_type, None)
            if obj and hasattr(obj, "file_name"):
                file_name = obj.file_name
                file_size = obj.file_size
                language = extract_language(default_caption)
                year = extract_year(default_caption)
                file_name = (
                    re.sub(r"@\w+\s*", "", file_name)
                    .replace("_", " ")
                    .replace(".", " ")
                )
                cap_dets = await chnl_ids.find_one({"chnl_id": chnl_id})
                try:
                    if cap_dets:
                        cap = cap_dets["caption"]
                        replaced_caption = cap.format(file_name=file_name, file_size=get_size(file_size), default_caption=default_caption, language=language, year=year)
                        await message.edit(replaced_caption)
                    else:
                        replaced_caption = DEF_CAP.format(file_name=file_name, file_size=get_size(file_size), default_caption=default_caption, language=language, year=year)
                        await message.edit(replaced_caption)
                except FloodWait as e:
                    await asyncio.sleep(e.x)
                    continue
    return

# Size conversion function
def get_size(size):
    units = ["Bytes", "Kʙ", "Mʙ", "Gʙ", "Tʙ", "Pʙ", "Eʙ"]
    size = float(size)
    i = 0
    while size >= 1024.0 and i < len(units) - 1:  # Changed the condition to stop at the last unit
        i += 1
        size /= 1024.0
    return "%.2f %s" % (size, units[i])

@Client.on_callback_query(filters.regex(r'^start'))
async def start(bot, query):
    await query.message.edit_text(
        text=script.START_TXT.format(query.from_user.mention),  
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton("➕️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ➕️", url=f"http://t.me/CustomCaptionBot?startchannel=true")
                ],[
                InlineKeyboardButton("Hᴇʟᴘ", callback_data="help"),
                InlineKeyboardButton("Aʙᴏᴜᴛ", callback_data="about")
            ],[
                InlineKeyboardButton("🌐 Uᴘᴅᴀᴛᴇ", url=f"https://t.me/Silicon_Bot_Update"),
                InlineKeyboardButton("📜 Sᴜᴘᴘᴏʀᴛ", url=r"https://t.me/Silicon_Botz")
            ]]
        ),
        disable_web_page_preview=True
)

@Client.on_callback_query(filters.regex(r'^help'))
async def help(bot, query):
    await query.message.edit_text(
        text=script.HELP_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('About', callback_data='about')
            ],[
            InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True    
)


@Client.on_callback_query(filters.regex(r'^about'))
async def about(bot, query):
    await query.message.edit_text(
        text=script.ABOUT_TXT,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton('ʜᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ ❓', callback_data='help')
            ],[
            InlineKeyboardButton('↩ ʙᴀᴄᴋ', callback_data='start')
            ]]
        ),
        disable_web_page_preview=True 

)

