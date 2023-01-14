import view, model
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



def start():

    while True:
        command = view.show_menu()
        match command:
            case '1':
                view.show_contacts(model.get_contacts())
            case '2':
                model.read_file()
            case '3':
                model.save_file()
            case '4':
                model.add_contact()
            case '0':
                break


    bot_token = ""
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", hello))
    app.add_handler(CommandHandler("start", viev.greetings))
    app.run_polling()