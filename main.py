from turtle import update
import telegram.ext 
with open('token.txt','r') as f:
    TOKEN = f.read()


def start(update,context):
    update.message.reply_text('welcome ajma3a !')

def help(update,context):
    update.message.reply_text('wtf is this lol! i only coded start')

def myname(update,context):
    update.message.reply_text('sifou motherfucker!')

def what(update,context):
    update.message.reply_text('good night jarvis gang i love you too')
def gang(update,context):
    update.message.reply_text('sifou, alikha and anis')
def arabic(update,context):
    update.message.reply_text('ايه دا هو انا احكي عربي برضو؟')

def handle_message(update,context):
    
   
    update.message.reply_text(f"you said {update.message.text}")


updater =telegram.ext.Updater(TOKEN,use_context=True)
disp = updater.dispatcher
disp.add_handler(telegram.ext.CommandHandler("start",start))
disp.add_handler(telegram.ext.CommandHandler("help",help))
disp.add_handler(telegram.ext.CommandHandler("myname",myname))
disp.add_handler(telegram.ext.CommandHandler("love",what))
disp.add_handler(telegram.ext.CommandHandler("gang",gang))
disp.add_handler(telegram.ext.CommandHandler("arabic",arabic))


disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text,handle_message))
updater.start_polling()
updater.idle()