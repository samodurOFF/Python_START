from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import bot_token
import time


token = bot_token.token

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}!\n'
                                    '\nThis is an RLE string encryption bot.')

    time.sleep(5)
    await update.message.reply_text(f'Enter the characters after the command /rle ')


async def rle_code(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    input_line = update.message.text[5:]
    print(input_line)
    count = 1
    new_line = ''

    for i in range(1, len(input_line)):
        if input_line[i] == input_line[i - 1]:
            if count == 9:
                new_line += str(count) + input_line[i - 1]
                count = 0
            count += 1
        else:
            new_line += str(count) + input_line[i - 1]
            count = 1
            continue

    new_line += str(count) + input_line[-1]
    await update.message.reply_text(f'RLE code:\n {new_line}')

    def decoding(code):
        decode = ''
        for i in range(0, len(code), 2):
            count2, symbol = code[i: i + 2]
            decode += symbol * int(count2)
        return decode

    print(decoding(new_line))
    await update.message.reply_text(f'Back restored string:\n {decoding(new_line)}')
    


app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("start", hello))
app.add_handler(CommandHandler("rle", rle_code))
app.run_polling()