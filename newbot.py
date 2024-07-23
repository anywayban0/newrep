from telethon import TelegramClient, events  # type: ignore # Імпортуємо потрібні бібліотеки

api_id = 28066055  # Вводимо id нашого телеграм клієнта, та записуємо номер щоб не загубити +380938341285
api_hash = 'b5a2b6ee3f38a2e6e99e10a5ef9dea18'  # Вводимо hash нашого телеграм клієнта

client = TelegramClient("Test", api_id, api_hash)  # Збираемо клієнта до купи
target_can = -1002154302487  # Вводимо id каналу в який будемо пересилати повідомлення
key_words = ["#Київська_область"]  # Вводимо ключові слова які будемо шукати в повідомленнях

@client.on(events.NewMessage(chats=[-1002166312019]))  # Запускаємо наш клієнт та сказуемо на які саме канали реагувати
async def normal_handler(event):  # Обробляємо подію
    for i in range(len(key_words)):  # Перебираємо всі ключові слова з нашого списку
        if key_words[i] in event.message.message:  # Перевіряємо коне слово на наявність його в нашому повідомленні
            print(event.message)
            print(event.message.peer_id,
                  event.message.message)  # Роздруковуємо в консоль id чату/групи та текст знайденного повідомлення (не обов'язково)
            await client.send_message(target_can, event.message)  # Пересилаємо знайдене повідомлення

client.start()  # Запускаємо кліент
client.run_until_disconnected()  # Ставимо його в бескінечний цикл