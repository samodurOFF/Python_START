from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_token
import time

token = bot_token.token


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Здравствуйте, {update.effective_user.first_name}!\n'
                                    'Этот бот поможет перевести десятичное число в двоичное')
    time.sleep(3)
    await update.message.reply_text(f'Введите целое число после команды /bin для перевода в двоичное')


async def input_bin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    int_num = int(update.message.text.split()[1])
    print_num = int_num
    print(int_num)
    double_num = ''
    while int_num > 0:
        double_elem = int_num % 2
        int_num = int_num // 2
        double_num += str(double_elem)
    await update.message.reply_text(f'Двоичное представление числа {print_num}: {int(double_num[::-1])}')


app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("bin", input_bin))
app.run_polling()