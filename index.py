from ast import Pass
import mysql.connector
import report
from buy import Cc
from transact import Transact
import database
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import Chat

updater=Updater("5133775572:AAFIrS7QrPqn8uVpJAPa0mguQMD34VJmN4w",use_context=True)



def start(update:Update,context:CallbackContext):


    update.message.reply_text(
        "Welcome to TradeBot were tools are sold\n type /help to see avaliable commands"
    )

def buy(update:Update,context:CallbackContext):
    
    def cc (update:Update,context:CallbackContext):
        update.message.reply_text("Enter cc bin")
        
            # this even keeps occuring in a loop i dont know how to shut it down
        def check_input (update:Update,context:CallbackContext):

            if len(str(update.message.text)) ==6:
                     bin=update.message.text
                     new_cc=Cc(update.effective_chat.id)
                     res1=new_cc.query(bin)

                     if res1 > 0:
                         update.message.reply_text(f"There are {res1} cc's \n How many do you want ?")
                     else:
                        update.message.reply_text("No cc with your bin avaliable")
  
            elif len(str(update.message.text)) < 3:
                    bin=update.message.text
                    new_cc=Cc(update.effective_chat.id)
                    res1=new_cc.query(bin)
                    ia=update.message.text
                    pr=int(ia)*int(new_cc.price())
                    newtran=Transact(update.effective_chat.id,pr,"cc")
                    newtran.pay()
                    update.message.reply_text(f"HERE's your invoice_id{newtran.get_id}\n current order status {newtran.status()}")
            else:
                update.message.reply_text("Wrong option selected")
                    
        updater.dispatcher.add_handler(MessageHandler(Filters.text,check_input)) 
            
    update.message.reply_text(" Choose item type\n /cc\n /rdp\n /scampage\n /leads\n")
    updater.dispatcher.add_handler(CommandHandler('cc', cc))
    

def report(update:Update,context:CallbackContext):
    update.message.reply_text("Select your option\n /new_report\n /report_status\n /list_report\n /report_help\n ")
    def new_report (update:Update,context:CallbackContext):
        pass
    def report_status(update:Update,context:CallbackContext):
        pass
    def list_report (update:Update,context:CallbackContext):
        pass
    def report_help (update:Update,context:CallbackContext):
        update.message.reply_text("List of avaliable command\n /buy to buy item\n /report to make a report\n ")

    updater.dispatcher.add_handler(CommandHandler('new_report', new_report))
    updater.dispatcher.add_handler(CommandHandler('report_status', report_status))
    updater.dispatcher.add_handler(CommandHandler('list_report',list_report))
    updater.dispatcher.add_handler(CommandHandler('report_help',report_help))



def help (update:Update,context:CallbackContext):
    update.message.reply_text("List of avaliable command\n  /buy to buy item\n /report to make a report\n ")

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('buy', buy))
updater.dispatcher.add_handler(CommandHandler('report',report))
updater.dispatcher.add_handler(CommandHandler('help', help))
#updater.dispatcher.add_handler(MessageHandler(Filters.text,help))
#updater.dispatcher.add_handler(MessageHandler(Filters.command,help))


updater.start_polling()




