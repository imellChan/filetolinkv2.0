bot = telebot.TeleBot(token=os.getenv('TG_BOT_TOKEN'))

def forcesub
# Terimakasih untuk luly angga rahmadan untuk ide hebatnya
if Config.UPDATES_CHANNEL is not None:
        back = await handle_force_sub(bot, cmd)
        if back == 400:
            return
        else

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hai! Kirim file untuk di pendekkan \n Jangan lupa Subscribe.\nhttps://www.youtube.com/channel/UCPd9_ZT97R471WWRS01q9lg ya 📣\nBantuan: /help')

@bot.message_handler(commands=['help'])
def bantuan(message):
    bot.reply_to(message, 'Kirim file dan saya akan mengrimkanmu linknya \n Subscribe https://www.youtube.com/channel/UCPd9_ZT97R471WWRS01q9lg')

@bot.message_handler(content_types=['photo', 'video', 'audio', 'document'])
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        try:
            bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[0].file_id)))
        except AttributeError:
            try:
                bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
            except AttributeError:
                try:
                    bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
                except AttributeError:
                    pass


while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
