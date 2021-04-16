import telegram
import logging
import json
import os

from telegram import ParseMode
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters

#enable logging
logging.basicConfig(level=logging.INFO)

TOKEN = "botTOken" # Bot Token Dari @botfather
CreatorID = 0 # ID Anda


Variable = bool(os.environ.get('Var', False))
if Variable:
    TOKEN = os.environ.get('lim-token', False)
    CreatorID = os.environ.get('lim-id',False)

else:
    TOKEN = TOKEN
    CreatorID = CreatorID

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher 

def Start(update, context):
    data = 'Welcome To Pɪɴᴜʀᴜɴ Lɪᴍɪᴛᴀᴛɪ\nTinggalkan Pesan Anda Dengan Menggunakan Perintah \n• /msg <pesan> \n\ncontoh: /msg hai'
    update.message.reply_text("```\n" + data + "\n```", parse_mode=ParseMode.MARKDOWN)

def Reply(update, context):
    msg = update.message.text
    update.message.reply_text(msg)

def SendToCreator(update, context):
    name = update.effective_message.from_user.first_name
    msg = update.effective_message
    text = update.effective_message.text
    frst = text.replace("/msg", "")
    scn = frst.replace("Welcome To Pɪɴᴜʀᴜɴ Lɪᴍɪᴛᴀᴛɪ\nTinggalkan Pesan Anda Dengan Menggunakan Perintah \n• /msg <pesan> \n\n", "")
    gg = scn.replace("contoh: /msg hai", "")
    chat_id = update.effective_chat.id
    message = "*1 Pesan Baru dari* [{name}](tg://user?id={id})\n{message}".format(name=name, id=msg.from_user.id, message=gg)
    bot.sendMessage(CreatorID, message, parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("Pesan telah terkirim!")

def Log(update, context):
    message = update.message
    eventdict = message.to_dict()
    jsondump = json.dumps(eventdict, indent=4)
    update.message.reply_text(jsondump)

start_handler = CommandHandler("start", Start)
reply_handler = CommandHandler("reply", Reply)
feedback_handler = CommandHandler("msg", SendToCreator)
logger_handler = CommandHandler("log", Log)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(reply_handler)
dispatcher.add_handler(feedback_handler)
dispatcher.add_handler(logger_handler)

__log__ = logging.getLogger()
__log__.info("Pinurun-lim Started..")
updater.start_polling()
