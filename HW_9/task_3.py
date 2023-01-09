from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def coding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    alfavit_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    smeshenie = int(input('Шаг шифровки: '))
    message = input("Сообщение для ДЕшифровки: ").upper()
    itog = ''
    lang = input('Выберите язык RU/EU: ')
    if lang == 'RU':
        for i in message:
            mesto = alfavit_RU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_RU:
                itog += alfavit_RU[new_mesto]
            else:
                itog += i
    else:
        for i in message:
            mesto = alfavit_EU.find(i)
            new_mesto = mesto + smeshenie
            if i in alfavit_EU:
                itog += alfavit_EU[new_mesto]
            else:
                itog += i
    print(itog)

    await update.message.reply_text(f' {itog}')

bot_token = ""
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("coding",REL_coding))

app.run_polling