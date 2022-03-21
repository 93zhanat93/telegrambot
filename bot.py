import logging
from aiogram import Bot, Dispatcher, executor, types
import markups as nav



TOKEN = "953565753:AAG4SDbnEO6HUQ_tK9e2xEI5gz3Qt1WFhVk"
bot = Bot(token=TOKEN)
dp=Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
  sti = open('welcome.tgs', 'rb')
  await bot.send_sticker(message.chat.id, sti)
  await bot.send_message(message.from_user.id,  'Добро пожаловать {0.first_name} к нам 😊 GasEnergy 😊. Нажимая на кнопки 👇🏻 \n\n Вы сможете узнать:  \n\n 📚Видео обучения📚\n\n 🗺Адреса и Контакты☎️'.format(message.from_user), reply_markup = nav.btnmain)
   


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.text == '📚 Видео Обучение':
        await bot.send_message(message.from_user.id,'📚 Видео Обучение', reply_markup = nav.btnEdu )
    elif message.text == '🧮Проверка расхождений перед закрытием смены🧮':
        await message.reply('<a href="https://youtu.be/_sQjr5CY8YA">GasEnergy</a>',parse_mode="HTML") 
    elif message.text == '🎟Продажа по топливной карте🎟':
        await message.reply('<a href="https://www.youtube.com/watch?v=F02ZBifop50">GasEnergy</a>',parse_mode="HTML")    
    elif message.text == 'Закрытие смены на 2-х кассах в 00-00 🕛':
        await message.reply('<a href="https://www.youtube.com/watch?v=7_Sr-jXF05o">GasEnergy</a>',parse_mode="HTML")
    elif message.text == 'Пересменка кассира в 20-00 🕗':
        await message.reply('<a href="https://www.youtube.com/watch?v=TgPJbiFGhec">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '💵Продажа по наличному расчету💵':
        await message.reply('<a href="https://www.youtube.com/watch?v=Ggf0Ih4BSAE">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '⚖️ Калибровка ТРК⚖️':
        await message.reply('<a href="https://www.youtube.com/watch?v=LCIiY4PBIe4">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '🚚 Приёмка топлива 🚚':
        await message.reply('<a href="https://www.youtube.com/watch?v=3zhAYnGSAzQ">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '🔙Возврат товара🔙':
        await message.reply('<a href="https://www.youtube.com/watch?v=JG0rEdmMF78">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '⛽️Отпуск полный бак⛽️':
        await message.reply('<a href="https://www.youtube.com/watch?v=i0NBiGqtq0U">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '💳Продажа по безналичному расчету💳':
        await message.reply('<a href="https://www.youtube.com/watch?v=CsqgxB8mV7k">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '🚗Отпуск за собственные нужды🚗':
        await message.reply('<a href="https://www.youtube.com/watch?v=9L2oPbrKqTI">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '🔑Закрытие смены на Bosuser🔑':
        await message.reply('<a href="https://www.youtube.com/watch?v=WpzpbTCKdp4">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '🌭🍔 Сибилла обучение 🍔🌭':
        await message.reply('<a href="https://www.youtube.com/watch?v=_zeOkfHOP3M">GasEnergy</a>',parse_mode="HTML")
    elif message.text == '🗺 Адреса и контакты ☎️':
        await bot.send_message(message.from_user.id,'🗺 Адреса и контакты ☎️', reply_markup = nav.mainMenu )
    elif message.text == '⬅️ Главное меню':
        await bot.send_message(message.from_user.id,'⬅️ Главное меню', reply_markup = nav.btnmain )
    elif message.text == '🌆 Алматы':
        await bot.send_message(message.from_user.id,'🌆 Алматы', reply_markup = nav.btnAlm )
    elif message.text == '⬅️ Назад':
        await bot.send_message(message.from_user.id,'⬅️ Назад', reply_markup = nav.mainMenu )
    elif message.text == '⛽️А-1':    
        await bot.send_chat_action(message.chat.id, 'find_location')   
        await bot.send_location(message.chat.id, 43.296167, 76.987167)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Медеуский р-н, пр.Рыскулова, 1/4 \nКонтакты: +77710557188 ')
    elif message.text == '⛽️А-2':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.312194, 76.968139)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Турксибский р-н, ул.Шемякина, 241 \nКонтакты: +77710557170 ')
    elif message.text == '⛽️А-3':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.338667, 76.933694)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Турксибский р-н, ул.Бурундайская, 79 В \nКонтакты: +77710557199 ')
    elif message.text == '⛽️А-4':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.313111, 76.901361)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Жетысуский р-н, ул.Северное кольцо, 31/13 \nКонтакты: +77710557091 ')
    elif message.text == '⛽️А-5':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.260444, 76.847389)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Алатауский р-н, ул.Центральная, 82 \nКонтакты: +77710557137 ')
    elif message.text == '⛽️А-6':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.226361, 76.741389)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Карасайский район, трасса Алматы-Бишкек, 19,6 км \nКонтакты: +77710557217 ')
    elif message.text == '⛽️А-7':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.212333, 76.857361)
        await bot.send_message(message.chat.id, 'Адрес: г. Алматы, Ауэзовский район, микрорайон «Астана» 2 «А» \nКонтакты: +77710557106 ')
    elif message.text == '⛽️А-8':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.332806, 76.912889)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Жетысуский р-н, мкр.Карасу, ул.Шоссейная 2Г \nКонтакты: +77710557096 ')
    elif message.text == '⛽️А-9':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.229956, 76.890074)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Бостандыкский район, ул.Розыбакиева, д.190А \nКонтакты: +77710557198 ')
    elif message.text == '⛽️А-10':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.225722, 76.910611)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Бостандыкский район, ул. Темирязева, 38 \nКонтакты: +77710557180 ')
    elif message.text == '⛽️А-11':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.263083, 76.898778)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Алматинский район, пр. Райымбека, 251 В \nКонтакты: +77710557180 ')
    elif message.text == '⛽️А-12':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.274250, 76.977056)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Медеуский район, ул. Оренбургская, 2 д \nКонтакты: +77710557200 ')
    elif message.text == '⛽️А-13':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.177111, 76.799861)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Карасайский р-н, с.о. Таусамалы, с.Акжар б/н \nКонтакты: +77710557235 ') 
    elif message.text == '⛽️А-14':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.206500, 76.663861)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Карасайский район, г.Каскелен,б/н \nКонтакты: +77710557194 ')  
    elif message.text == '⛽️А-15':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.228628, 76.757754)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, автодорога Алматы-Бишкек 18,2 км. \nКонтакты: +77710557120 ')
    elif message.text == '⛽️А-16':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.242111, 76.821028)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы ,пр. Райымбека 515 \nКонтакты: +77710557168 ')
    elif message.text == '⛽️А-17':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.402806, 77.188333)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Панфиловский район, трасса Алматы-Хоргос 29 км. \nКонтакты: +77710557125 ')
    elif message.text == '⛽️А-18':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.377639, 76.639944)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Карасайский район, п.Шамалган \nКонтакты: +77710557141 ') 
    elif message.text == '⛽️А-19':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.477194, 76.810667)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Илийский район, с.Чапай \nКонтакты: +77710557211 ')
    elif message.text == '⛽️А-20':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.856417, 77.041417)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Капчагай, трасса Алматы-Талдыкорган, 70 км \nКонтакты: +77710557099 ') 
    elif message.text == '⛽️А-22':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.366583, 76.866861)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Илийский район, п.Боралдай, мкр.Водник \nКонтакты: +77710557145 ')
    elif message.text == '⛽️А-23':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.412139, 77.019611)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, ул.Рыскулова 103Д \nКонтакты: +77710557232 ') 
    elif message.text == '⛽️А-25':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.178417, 76.801861)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы Наурызбайский район, трасса Алматы-Жандосово, северная сторона, западнее с. Акжар \nКонтакты: +77710557155 ')                                                                        
    elif message.text == '⛽️А-28':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.303361, 77.223056)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Талгарский район, г.Талгар, угол улицы Тулебаева \nКонтакты: +77710557178 ')
    elif message.text == '⛽️А-29':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.289611, 77.007389)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Медеуский район, ул.Халилулина 179 \nКонтакты: +77710557104 ') 
    elif message.text == '⛽️А-34':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.289611, 77.007389)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Карасайский район, пос.Береке, ул.Бабаева 11 А \nКонтакты: +7 ')
    elif message.text == '⛽️А-36':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.220890, 76.311010)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Жамбылский район, с.Узынагаш \nКонтакты: +77710557090 ')      
    elif message.text == '⛽️А-38':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.295610, 76.832915)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Алатауский район, мкр.Коккайнар, ул.Басар Кобыза 1/14 \nКонтакты: +77710557107 ')  
    elif message.text == '⛽️А-39':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.292956, 77.019881)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Талгарский район, с.о.Бесагашский, с.Бесагаш зд.3/1 \nКонтакты: +77710557085 ') 
    elif message.text == '⛽️А-40':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.312194, 76.968139)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Талгарский район, с.о.Туздыбастауский, с.Туздыбастау, мкр.Жайлау д.102 \nКонтакты: +77710557238 ') 
    elif message.text == '⛽️А-41':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.222062, 76.575559)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Карасайский район, г.Каскелен, уч.1 трасса Алматы-Бишкек 33 км \nКонтакты: +77710557156 ') 
    elif message.text == '⛽️А-42':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.378678, 76.959743)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Жетысуский район, мкр.Кемел, ул.Капчагайская, уч.80/1 \nКонтакты: +77710557132 ')
    elif message.text == '⛽️А-43':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.289902, 76.827047)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Алатауский район, мкр.Коккайнар, ул.Басар Кобыза 1/15 \nКонтакты: +77710557142 ')
    elif message.text == '⛽️А-44':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.401098, 75.111164)
        await bot.send_message(message.chat.id, 'Адрес: Жамбылская область, Карданский район, Кенекский с/о уч.кв.055 уч.258 трасса Алматы-Бишкек 158 км. г.Отар \nКонтакты: +77710557225 ')
    elif message.text == '⛽️А-45':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 44.042741, 79.972261)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Панфиловский район, с.Шолакай (Жаркент), трасса Алматы-Чилик-Хоргос \nКонтакты: +77710557119 ')
    elif message.text == '⛽️А-46':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.216363, 76.840090)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Ауэзовский район, мкр.Мамыр-4, д.1Б \nКонтакты: +77710557167 ')
    elif message.text == '⛽️А-47':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.315957, 76.902810)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Жетысуский район, ул.Северное Кольцо, д.33Г \nКонтакты: +77710557191 ')
    elif message.text == '⛽️А-49':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.219725, 76.849706)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Ауезовский район, микрорайон "Жетысу-2", 86 \nКонтакты: +7 ')
    elif message.text == '⛽️А-50':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.351622, 76.985384)
        await bot.send_message(message.chat.id, 'Адрес: г. Алматы, Турксибский район, ул.Наманганская, 1"В", угол.ул. Гризодубова ч.4. \nКонтакты: +77710557202 ')
    elif message.text == '⛽️А-52':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.250455, 76.837583)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы, Ауезовский район, ул,Рыскулова 147, угол.ул. Саина. \nКонтакты: +77710557240 ') 
    elif message.text == '⛽️А-53':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.578120, 78.207924)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область,Енбекшиказахский район,Шелек-1 \nКонтакты: +77710557181 ')
    elif message.text == '⛽️А-54':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.578889, 78.205253)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область,Енбекшиказахский район,Шелек-2 \nКонтакты: +77710557114 ')
    elif message.text == '⛽️А-55':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.220371, 76.710564)
        await bot.send_message(message.chat.id, 'Адрес: Алматинская область, Карасайский район, Умтылский с.о., с.Жалпаксай, ул.УК.89, д.1465, оф.169 \nКонтакты: +7 ')
    elif message.text == '⛽️А-56':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 43.340934299769444, 76.98098547298366)
        await bot.send_message(message.chat.id, 'Адрес: г.Алматы,Турксибский район, ул.Бекмаханова 101/1 \nКонтакты: +77710557100 ')                            
    elif message.text == '🌆 Караганда':
        await bot.send_message(message.from_user.id,'🌆 Караганда', reply_markup = nav.btnKar )
    elif message.text == '⛽️M-20':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 49.74065399793992, 72.92076828919345)
        await bot.send_message(message.chat.id, 'Адрес: г.Караганда, село Дубовка 068, учетный квартал 1/78 М-20 село \nКонтакты: +77710557201 ')
    elif message.text == '⛽️M-21':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 49.79352426288566, 73.09911986274035)
        await bot.send_message(message.chat.id, 'Адрес: г.Караганда, ул. Складская 8, Караганда 100000 \nКонтакты: +77710557193 ')
    elif message.text == '⛽️M-22':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 49.825244085482346, 73.07275320609368)
        await bot.send_message(message.chat.id, 'Адрес: г.Караганда, проспект Бухар-Жырау, 2/8 \nКонтакты: +77710557113 ')
    elif message.text == '⛽️M-23':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 49.80331538125804, 73.1502943901627)
        await bot.send_message(message.chat.id, 'Адрес: г.Караганда, учетный квартал 134 участок №893 М-23 \nКонтакты: +77710557144 ')    
    elif message.text == '⛽️M-24':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 49.683291255078224, 73.1918295505075)
        await bot.send_message(message.chat.id, 'Адрес: г.Караганда, село Новостройка 105 учетный квартал участок 700 М-24 \nКонтакты: +77710557187 ')
    elif message.text == '🌆 Актобе':
        await bot.send_message(message.from_user.id,'🌆 Актобе', reply_markup = nav.btnAkt )
    elif message.text == '⛽️D-1':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 48.509001, 61.008207)
        await bot.send_message(message.chat.id, 'Адрес: Актюбинская область, Иргизский район, вдоль трассы "Самара-Шымкент" \nКонтакты: +7 ')
    elif message.text == '🌆 Уральск':
        await bot.send_message(message.from_user.id,'🌆 Актобе', reply_markup = nav.btnUra )
    elif message.text == '⛽️L-1':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.654056, 51.008924)
        await bot.send_message(message.chat.id, 'Адрес: Западно-Казахстанская область, район Байтерек, Красновский с/о \nКонтакты: +7 ')
    elif message.text == '🌆 Нурсултан':
        await bot.send_message(message.from_user.id,'🌆 Нурсултан', reply_markup = nav.btnNur )
    elif message.text == '⛽️Z-1':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.147552,71.502389)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Алматы», проспект Абылай хана, 44 \nКонтакты: +77710557220 ')
    elif message.text == '⛽️Z-2':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.111570,71.684076)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Алматы», тр. Аст.-Караг., р-н въезда в п.Куйгенжар, 113 (тр. Екатеринб.-Алматы, 1277 км, выезд из г.Аст. в г.Караг.) \nКонтакты: +77710557219 ')
    elif message.text == '⛽️Z-3':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.098278, 71.412936)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, ул.Сауран 38 (ранее ул.24, между ул. Сауран и Акмешит) \nКонтакты: +77710557216 ')
    elif message.text == '⛽️Z-4':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 50.976481, 71.355492)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Алматы», Рождественская трасса на поселок Кощи (возле кольцевой дороги в аэропорт) \nКонтакты: +77710557124 ')
    elif message.text == '⛽️Z-5':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.146074,71.374012)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, Коргальжинская трасса,15 \nКонтакты: +77710557231 ')
    elif message.text == '⛽️Z-6':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.121944, 71.285133)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Есиль», Коргалжинское шоссе, 120 (район микрорайона «Уркер») \nКонтакты: +77710557227 ')
    elif message.text == '⛽️Z-7':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.202037, 71.305362)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Сарыарка», проспект Тлендиева, 54 \nКонтакты: +77710557151 ')
    elif message.text == '⛽️Z-8':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.268342, 71.369376)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Сарыарка», Северное шоссе, 118 \nКонтакты: +77710557213 ')
    elif message.text == '⛽️Z-9':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 50.997169,71.371892)
        await bot.send_message(message.chat.id, 'Адрес: п.Косшы,Лесная поляна \nКонтакты: +77710557093 ')
    elif message.text == '⛽️Z-10':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.190816,71.458498)
        await bot.send_message(message.chat.id, 'Адрес: Софиевское шоссе,70 выезд в сторону города Павлодар \nКонтакты: +77710557098 ')
    elif message.text == '⛽️Z-11':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.179478, 71.489975)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Алматы», улица Можайского, 26. \nКонтакты: +77710557241 ')
    elif message.text == '⛽️Z-12':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.156485, 71.527113)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Алматы», улица Байырқұм, 26  \nКонтакты: +77710557131 ')
    elif message.text == '⛽️Z-13':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.166526, 71.463785)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, Жубанова 20 АЗС-ВЕГА  \nКонтакты: +77710557103 ')
    elif message.text == '⛽️Z-18':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.101169,71.717576)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, район «Алматы», трасса Астана-Караганда, 94 (ранее трасса Екатеринбург-Алматы, 1277 км, в районе села Куйгенжар)  \nКонтакты: +77710557177 ')
    elif message.text == '⛽️Z-21':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.202409, 71.498483)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, 69 презд, участок №5 (район рынка Шанхай)  \nКонтакты: +77710557092 ')
    elif message.text == '⛽️Z-22':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.111538, 71.408553)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, улица Кабанбай Батыра 45В  \nКонтакты: +77710557224 ')
    elif message.text == '⛽️Z-23':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.061737, 71.408094)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, проспект Мангилик Ел 89 А  \nКонтакты: +77710557147 ')
    elif message.text == '⛽️Z-24':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.061260, 71.413004)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, проспект Мангилик Ел 89 Б  \nКонтакты: +77710557210 ')
    elif message.text == '⛽️Z-25':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.061302, 71.415854)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, проспект Мангилик Ел 90  \nКонтакты: +77710557204 ')
    elif message.text == '⛽️Z-26':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.155051, 71.372508)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана, Айтматова 50  \nКонтакты: +77710557196 ')
    elif message.text == '⛽️Z-27':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.159151, 71.371065)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана,Айтматова 69  \nКонтакты: +77710557234 ')
    elif message.text == '⛽️Z-28':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.261881, 71.373258)
        await bot.send_message(message.chat.id, 'Адрес: г.Астана,Ондирис 80  \nКонтакты: +77710557161 ')
    elif message.text == '⛽️С-6':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.341492, 70.661591)
        await bot.send_message(message.chat.id, 'Адрес: поселок Тасты  \nКонтакты: +77710557139 ')
    elif message.text == '⛽️С-11':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 51.698552,71.016993)
        await bot.send_message(message.chat.id, 'Адрес: поселок Шортанды  \nКонтакты: +77710557140 ')
    elif message.text == '🌆 Шымкент':
        await bot.send_message(message.from_user.id,'🌆 Шымкент', reply_markup = nav.btnShym )
    elif message.text == '⛽️X-1':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 42.383824, 69.486828)
        await bot.send_message(message.chat.id, 'Адрес: г.Шымкент, р-н Абайский, Трасса Темирлановское, 464 \nКонтакты: +7 ')
    elif message.text == '⛽️X-1':
        await bot.send_chat_action(message.chat.id, 'find_location')
        await bot.send_location(message.chat.id, 42.383824, 69.486828)
        await bot.send_message(message.chat.id, 'Адрес: КАЗЫГУРТ, п.Ащыбулак, ул. Береке 2А \nКонтакты: +7 ')
    else:
        await bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
            


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates = False)




