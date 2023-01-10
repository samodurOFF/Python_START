from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def binary(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    a = int(input('Enter the number: '))
    b = ''
    while a > 0:
        b = str(a % 2) + b
        a = a // 2
    print(b)
    await update.message.reply_text(f'в двоичной системе число:{b}')




bot_token = "5711017816:AAHl9-ju8GN-fckSbcycPFHJPGCi3-dPXdE"
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("bin", binary))
app.run_polling()