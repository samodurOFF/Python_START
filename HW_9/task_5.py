from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_num = update.message.text.split()
    print('Приветствуем вас в калькуляторе Python')
    q1 = int(input('Введите число 1: '))
    q2 = int(input('Введите число 2: '))

    v = int(
        input('Какую операцию вы хотите выполнить? \nl 1 Сложение \nl 2 Вычитание \nl 3 Деление \nl 4 Умножение \n'))

    if v == 1:
        r = q1 + q2
        p = 'сложения'
        t = p
    if v == 2:
        r = q1 - q2
        l = 'вычитания'
        t = l
    if v == 3:
        r = float(q1 / q2)
        m = 'деления'
        t = m
    if v == 4:
        r = q1 * q2
        n = 'умножения'
        t = n
    print('Результат ', t, ' = ', r)

    await update.message.reply_text(f'Результат {t}  =  {r}')

bot_token = "5711017816:AAHl9-ju8GN-fckSbcycPFHJPGCi3-dPXdE"
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("cal", calc))

app.run_polling()
