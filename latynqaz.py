import telebot

TOKEN = '491105928:AAGRdsl9vqtAPQjCmbLBpwuvK0ubZQvSNmg'
bot = telebot.TeleBot(TOKEN)

qaz = [1040,1240,1041,1044,1045,1060,1043,1170,1061,1210,1030,1048,1049,1046,1050,1051,1052,
       1053,1186,1054,1256,1055,1178,1056,1057,1058,1200,1198,1042,1067,1059,1047,1064,1063,
       1072,1241,1073,1076,1077,1092,1075,1171,1093,1211,1110,1080,1081,1078,1082,1083,1084,
       1085,1187,1086,1257,1087,1179,1088,1089,1090,1201,1199,1074,1099,1091,1079,1096,1095]
eng = ['A','Á','B','D','E','F','G','Ǵ','H','H','I','I','I','J','K','L','M','N','Ń','O','Ó','P','Q',
       'R','S','T','U','Ú','V','Y','Ý','Z','Sh','Ch','a','á','b','d','e','f','g','ǵ','h','h','i',
       'ı','ı','j','k','l','m','n','ń','o','ó','p','q','r','s','t','u','ú','v','y','ý','z','sh','ch']

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    if message.text == '/start':
        bot.send_message(message.chat.id, 'Привет, я бот от @linuks85. Просто напиши текст на казахском и нажми отправить, а он переведет вам на латиницу. Наслаждайса :)')
    else:
        lat = ['']
        for ch in message.text:
            code = ord(ch)
            for i in range(len(qaz)):
                if code == qaz[i]:
                    lat.append(eng[i])
                    break
            else:
                lat.append(ch)

        txt = ''.join(lat)
        bot.send_message(message.chat.id, txt)

if __name__ == '__main__':
    bot.polling(none_stop = True)
