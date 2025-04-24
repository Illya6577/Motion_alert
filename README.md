# Motion_alert
Send to telegram messenge, when see motion


UA:
Передісторія:
Одного разу мені прийшла в голову ідея, щоб взяти плату Arduino UNO(Rev 3), підключити до неї датчик руху, і щоб коли вона помічає рух мені приходило сповіщення в телеграм. В теорії просто, на практиці наче теж. Спершу я зібрав розробив схему в Tinkercad, і написав код для ардуїнки, щоб коли вона бачила рух, то писала про це в serial monitor. Все працювало: перший етап завершено. Тепер реалізуємо це в життя. Я зібрав це все в реальності, закинув код на ардуїнку, і тепер залишалось тіки написати код на python, щоб той зчитував данні з (в моєму випадку) COM10, і надсилав це мені в телеграм. Цю роботу зробив ChatGPT, і фінальна версія коду у нього вийшла доволі швидко, лише з трьома правками. 

Для того щоб все запрацювало нам треба: 
1)Все скласти. [Схема](https://www.tinkercad.com/things/iIEmKsP64vl-datchic-ruhu-na-arduino-uno-z-svetodiodom?sharecode=x4xLwb5E_Cl4F9E56GDcRlzIQP1rSj3n58jsqAGszZo)
2)Драйвери на Arduino (йдуть разом з Arduino IDE)
3)python3
4)Бібліотека:
pip install pyserial requests
5) Токен телеграм (створити можна в @BotFather)
6) ID користувача, якому буде надсилатись що було помічено рух (взнати можна в @username_to_id_bot)
7) Замінити у коді YOUR_BOT_TOKEN і YOUR_CHAT_ID на токен вашого бота і ID чату.
8) Запустити скрипт

Сподіваюсь, що все розписав детально, і зрозуміло


ENG(by translate.google.com):

Prehistory:
Once I had the idea to take an Arduino UNO (Rev 3) board, connect a motion sensor to it, and when it detects movement, I would receive a notification in Telegram. In theory, it's simple, in practice, it's the same. First, I assembled and developed a circuit in Tinkercad, and wrote code for the Arduino so that when it saw movement, it would write about it in the serial monitor. Everything worked: the first stage is complete. Now let's put it into practice. I assembled it all in reality, threw the code on the Arduino, and now all that remained was to write the code in python so that it would read data from (in my case) COM10, and send it to me in Telegram. ChatGPT did this work, and the final version of the code came out quite quickly, with only three edits.

In order for everything to work, we need to:
1) Assemble everything [Schem](https://www.tinkercad.com/things/iIEmKsP64vl-datchic-ruhu-na-arduino-uno-z-svetodiodom?sharecode=x4xLwb5E_Cl4F9E56GDcRlzIQP1rSj3n58jsqAGszZo)
2) Arduino drivers (comes with Arduino IDE)
3) python3
4) Library:
pip install pyserial requests
5) Telegram token (you can create it in @BotFather)
6) User ID to whom the movement will be sent (you can find it in @username_to_id_bot)
7) Replace YOUR_BOT_TOKEN and YOUR_CHAT_ID in the code with your bot's token and chat ID.
8) Run the script

I hope I explained everything in detail and it's clear
