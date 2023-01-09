from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def fib(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
a = int(input('Enter the number: '))
print(a)
negofibonacci = [1,-1]
fibonacci = [1]

for i in range(2,a):
    list = fibonacci[i-1]+fibonacci[i-2]
    fibonacci.append(list)
    list_nego = negofibonacci[i-2] - negofibonacci[i-1]
    negofibonacci.append(list_nego)

negofibonacci.reverse()
negofibonacci.append(0)

print(f' for a = {a} =>{negofibonacci+fibonacci}')

await update.message.reply_text(f'for a = {a} =>{negofibonacci+fibonacci}')

bot_token = ""
app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("fib",fibonacci))

app.run_polling()