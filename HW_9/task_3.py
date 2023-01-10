from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def coding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text
    data = data.replace('/cod','')
    print(data)
    code = ""
    previous_symbol = ""
    count = 1
    if not data:
        return ""
    for current_sumbol in data:
        if current_sumbol !=previous_symbol:
            if previous_symbol:
                code += str(count) + previous_symbol
            count = 1
            previous_symbol = current_sumbol
    else:
        if count == 9:
            code += str(count) + previous_symbol
            count = 1
        count += 1
    code += str(count) + previous_symbol
    await update.message.reply_text(f'ввели код {code}')

    print(code)

async def REL_decoding(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    data = update.message.text
    data = data.replace("/ans ", "")
    print(data)
    decode = ""
    for i in range(0, len(data), 2):
        count, symbol = data[i:i + 2:]
        decode += symbol + int(count)
    print(decode)
    await update.message.reply_text(f'раскодировкаЖ {decode}')

bot_token = ""
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("cod", coding))
app.run_polling()


