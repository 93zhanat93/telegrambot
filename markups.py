from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

#Main Menu 


btnmain = ReplyKeyboardMarkup(resize_keyboard = True)
btnmain.row ('🗺 Адреса и контакты ☎️')
btnmain.row ('📚 Видео Обучение')



#Education

button7 = KeyboardButton ('⬅️ Главное меню')
btnEdu = ReplyKeyboardMarkup(resize_keyboard = True).row(button7)
btnEdu.row ('🧮Проверка расхождений перед закрытием смены🧮')
btnEdu.row ('🎟Продажа по топливной карте🎟')
btnEdu.row ('Закрытие смены на 2-х кассах в 00-00 🕛')
btnEdu.row ('Пересменка кассира в 20-00 🕗')
btnEdu.row ('💵Продажа по наличному расчету💵')
btnEdu.row ('⚖️ Калибровка ТРК⚖️')
btnEdu.row ('🚚 Приёмка топлива 🚚')
btnEdu.row ('🔙Возврат товара🔙')
btnEdu.row ('⛽️Отпуск полный бак⛽️')
btnEdu.row ('💳Продажа по безналичному расчету💳')
btnEdu.row ('🚗Отпуск за собственные нужды🚗')
btnEdu.row ('🔑Закрытие смены на Bosuser🔑')
btnEdu.row ('🌭🍔 Сибилла обучение 🍔🌭')












#City


btnAlmaty = KeyboardButton( '🌆 Алматы' )
btnShymkent = KeyboardButton( '🌆 Шымкент' )
btnNursultan = KeyboardButton( '🌆 Нурсултан' )
btnKyzylorda = KeyboardButton( '🌆 Кызылорда' )
btnTaraz = KeyboardButton( '🌆 Тараз' )
btnKaraganda = KeyboardButton( '🌆 Караганда' )
btnAktobe = KeyboardButton( '🌆 Актобе' )
btnUralsk = KeyboardButton( '🌆 Уральск' )
button0 = KeyboardButton ('⬅️ Главное меню')


mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnAlmaty,btnShymkent,btnNursultan,btnKyzylorda,btnTaraz,btnKaraganda,btnAktobe,btnUralsk).row(button0)



#AZS Almaty
button1 = KeyboardButton ('⬅️ Назад')
btnAlm = ReplyKeyboardMarkup(resize_keyboard = True).row(button1)
btnAlm.row ('⛽️А-1','⛽️А-2','⛽️А-3','⛽️А-4','⛽️А-5')
btnAlm.row ('⛽️А-6','⛽️А-7','⛽️А-8','⛽️А-9','⛽️А-10')
btnAlm.row ('⛽️А-11','⛽️А-12','⛽️А-13','⛽️А-14','⛽️А-15')
btnAlm.row ('⛽️А-16','⛽️А-17','⛽️А-18','⛽️А-19','⛽️А-20') 
btnAlm.row ('⛽️А-22','⛽️А-23','⛽️А-25','⛽️А-28','⛽️А-29')  
btnAlm.row ('⛽️А-34','⛽️А-36','⛽️А-38','⛽️А-39','⛽️А-40')
btnAlm.row ('⛽️А-41','⛽️А-42','⛽️А-43','⛽️А-44','⛽️А-45')
btnAlm.row ('⛽️А-46','⛽️А-47','⛽️А-49','⛽️А-50','⛽️А-52')
btnAlm.row ('⛽️А-53','⛽️А-54','⛽️А-55','⛽️А-56')


#AZS Karaganda
button2 = KeyboardButton ('⬅️ Назад')
btnKar = ReplyKeyboardMarkup(resize_keyboard = True).row(button2)
btnKar.row ('⛽️M-20','⛽️M-21','⛽️M-22','⛽️M-23','⛽️M-24')


#AZS Актобе
button3 = KeyboardButton ('⬅️ Назад')
btnAkt = ReplyKeyboardMarkup(resize_keyboard = True).row(button3)
btnAkt.row ('⛽️D-1')

#AZS Уральск
button4 = KeyboardButton ('⬅️ Назад')
btnUra = ReplyKeyboardMarkup(resize_keyboard = True).row(button4)
btnUra.row ('⛽️L-1')


#AZS Нурсултан
button5 = KeyboardButton ('⬅️ Назад')
btnNur = ReplyKeyboardMarkup(resize_keyboard = True).row(button5)
btnNur.row ('⛽️Z-1','⛽️Z-2','⛽️Z-3','⛽️Z-4','⛽️Z-5')
btnNur.row ('⛽️Z-6','⛽️Z-7','⛽️Z-8','⛽️Z-9','⛽️Z-10')
btnNur.row ('⛽️Z-11','⛽️Z-12','⛽️Z-13','⛽️Z-18','⛽️Z-21')
btnNur.row ('⛽️Z-22','⛽️Z-23','⛽️Z-24','⛽️Z-25','⛽️Z-26')
btnNur.row ('⛽️Z-27','⛽️Z-28','⛽️С-6','⛽️С-11')

#AZS Шымкент
button6 = KeyboardButton ('⬅️ Назад')
btnShym = ReplyKeyboardMarkup(resize_keyboard = True).row(button6)
btnShym.row ('⛽️X-1','⛽️X-2','⛽️X-3','⛽️X-4','⛽️X-6')
btnShym.row ('⛽️X-7','⛽️X-8','⛽️X-10','⛽️X-11','⛽️X-12')
btnShym.row ('⛽️X-13','⛽️X-14','⛽️X-16','⛽️X-17','⛽️X-17')
btnShym.row ('⛽️X-18','⛽️X-19','⛽️X-20','⛽️X-21','⛽️X-22')
btnShym.row ('⛽️X-23','⛽️X-24','⛽️X-25','⛽️X-26','⛽️X-28')
btnShym.row ('⛽️X-29','⛽️X-30','⛽️X-31','⛽️X-32','⛽️X-33')
btnShym.row ('⛽️X-34','⛽️X-35','⛽️X-36','⛽️X-37','⛽️X-38')
btnShym.row ('⛽️X-39','⛽️X-40','⛽️X-41','⛽️X-42','⛽️X-43')
btnShym.row ('⛽️X-44','⛽️X-45','⛽️X-46','⛽️X-47','⛽️X-48')
btnShym.row ('⛽️X-49','⛽️X-50','⛽️X-51')







