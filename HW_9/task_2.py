import update as update
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def fib(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    n = int(input('Enter the number: '))
    fibo_nums = []
    a, b = 0, 1
    for i in range(n + 1):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    print(fibo_nums)
    await update.message.reply_text(f'последовательность: {fibo_nums}')

bot_token = ""
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("fibonacci",fib))

app.run_polling()