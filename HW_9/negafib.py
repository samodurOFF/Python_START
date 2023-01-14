from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_token
import time

token = bot_token.token


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}!\n'
                                    '\nЭтот бот составляет список чисел Фибоначчи размерностью '
                                    '2N + 1 для отрицательной и положительной части (Негафибоначчи)')
    time.sleep(5)
    await update.message.reply_text(f'Введи целое число после команды /fib для составления списка')


async def fibonacci(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    n = int(update.message.text.split()[1])
    fib_list = [0] * (2 * n + 1)
    fib_list[n + 1], fib_list[n - 1] = 1, 1
    koef = -1
    for i in range(n + 2, 2 * n + 1):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        fib_list[-i - 1] = fib_list[i] * koef
        koef *= -1
    await update.message.reply_text(f'Числа НегаФибоначчи:\n\n {fib_list}')


app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("fib", fibonacci))
app.run_polling()