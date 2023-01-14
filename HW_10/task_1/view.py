
from model import
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def greetings(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здравствуйту, {update.effective_user.first_name}! Вас приветствует телефонный справочник')
    await update.message.reply_text(show_menu()[0])
    show_menu =  (\show - Показать все контакты\n
    /open - Открыть файл с контактами\n
    /record- Записать файл с контактами\n
    /add - Добавить контакт\n
    /find - Поиск по контактам\n
    /edit- Выход\n,)
     return show_menu
def show_contacts(contacts: list):
    print(*(contact for contact in contacts), sep='\n')