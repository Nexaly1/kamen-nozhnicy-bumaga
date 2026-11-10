import random
import getpass
r = 0
propusk = 1
rulet = None
rulet1 = None
rulet2 = None
print("Добро пожаловать в игру <Камень - Ножницы - Бумага>")
print("Суть игры: Вам дают выбор, в котором Вы можете выбрать 1 из 3 предложенных вариантов, с вариантами Вы ознакомитесь в игре")
while True:
    vbr = input("С чего начнем?\n   1 - Играть против бота\n   2 - Играть против друг друга\n   3 - Ознакомиться с правилами игры")
    if vbr.isdigit():
        if 1 <= int(vbr) <= 3:
            break
        else:
            print("❌ Ошибка, введите 1, 2 или 3")
            continue         
    else:
        print("❌ Ошибка, введите 1, 2 или 3")
        continue
 
while True:
    if int(vbr) == 3:
        break
    r = input("Какой раунд будет последним перед победой для команды (распространяется на 2 команды)? [Введите число]")
    if r == "0":
        print("0 раундов быть не может!❌")
        continue
    elif r.isdigit():
        print("Принято✅")
        break
    else:
        print(f"{r} быть не может!❌")
        continue

ch1 = 0 
ch2 = 0
c = 0
x = 0
if int(vbr) == 3:
    propusk = 0
while ch1 < int(r) and ch2 < int(r) and propusk == 1:
    if int(vbr) != 1:
        break
    x = 1
    while True:
        vbr2 = input("Какой предмет выберем?\n   1 - Камень\n   2 - Ножницы\n   3 - Бумага")
        if vbr2.isdigit():
            if 1 <= int(vbr2) <= 3:
                vbr_bota = random.randint(1, 3)
                break
            else:
                print("❌ Ошибка, выберите только 1, 2 или 3")
                continue
        else:
            print("❌ Ошибка, выберите только 1, 2 или 3")
            continue
    vbr2 = int(vbr2)
    if vbr2 == 1 and vbr_bota == 1:
        c = c + 1
        print(f"Раунд {c}")
        print("Ничья🤝!")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 2 and vbr_bota == 1:
        ch2 = ch2 + 1
        c = c + 1
        print(f"Раунд {c}")
        print("🤖Выиграл Бот!👑")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 3 and vbr_bota == 1:
        ch1 = ch1 + 1 
        c = c + 1
        print(f"Раунд {c}")
        print("👤Вы выиграли!👑")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 1 and vbr_bota == 2:
        ch1 = ch1 + 1
        c = c + 1
        print(f"Раунд {c}")
        print("👤Вы выиграли!👑")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 1 and vbr_bota == 3:
        ch2 = ch2 + 1
        c = c + 1
        print(f"Раунд {c}")
        print("🤖Выиграл Бот!👑")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")  
    elif vbr2 == 2 and vbr_bota == 2:
        c = c + 1
        print(f"Раунд {c}")
        print("Ничья!🤝")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}") 
    elif vbr2 == 3 and vbr_bota == 3:
        c = c + 1
        print(f"Раунд {c}")
        print("Ничья!🤝")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")  
    elif vbr2 == 2 and vbr_bota == 3:
        ch1 = ch1 + 1
        c = c + 1
        print(f"Раунд {c}")
        print("👤Вы выиграли!👑")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")    
    elif vbr2 == 3 and vbr_bota == 2:
        ch2 = ch2 + 1
        c = c + 1
        print(f"Раунд {c}")
        print("🤖Выиграл Бот!👑")
        print(f"Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")                 


if x == 1:
    if ch1 > ch2:
        rulet = random.choice(["Примите Наши Поздравления", "Супер", "Счастливый конец этой игры"])
        print(f"{rulet}🎉! Вы выиграли эту игру!")
        print("Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")
        print(f"Всего прошло {c} раундов!")
    else:
        rulet1 = random.choice(["Такое тоже бывает", "Вот неудача", "В следущий раз будет иначе"])
        print(f"🟥 {rulet1}! Вы проиграли эту игру!")
        print("Вы👤 | Бот🤖")
        print(f"{ch1} | {ch2}")
        print(f"Всего прошло {c} раундов!")

v_i = 0
ch1 = 0 
ch2 = 0
c = 0
player1 = None
player2 = None

if int(vbr) == 3:
    propusk = 0
while ch1 < int(r) and ch2 < int(r) and propusk == 1:
    if int(vbr) != 2:
        break
    x = 2
    if v_i == 0:
        player1 = input("Введите имя 1️⃣  игрока:")
        print("Принято✅")
        player2 = input("Введите имя 2️⃣  игрока:")
        print("Принято✅")
        v_i = 1
    while True:
        vbr2 = getpass.getpass(f"{player1}, какой предмет выберем?\n   1 - Камень\n   2 - Ножницы\n   3 - Бумага")
        if vbr2.isdigit():
            if 1 <= int(vbr2) <= 3:
                print("Выбрано✅")
                break
            else:
                print("❌ Ошибка, выберите только 1, 2 или 3")
                continue
        else:
            print("❌ Ошибка, выберите только 1, 2 или 3")
            continue
    while True:
        vbr3 = getpass.getpass(f"{player2}, какой предмет выберем?\n   1 - Камень\n   2 - Ножницы\n   3 - Бумага")
        if vbr3.isdigit():
            if 1 <= int(vbr3) <= 3:
                print("Выбрано✅")
                break
            else:
                print("❌ Ошибка, выберите только 1, 2 или 3")
                continue
        else:
            print("❌ Ошибка, выберите только 1, 2 или 3")
            continue          
    vbr2 = int(vbr2)
    vbr3 = int(vbr3)
    if vbr2 == 1 and vbr3 == 1:
        c = c + 1
        print(f"Раунд {c}")
        print("Ничья🤝!")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 2 and vbr3 == 1:
        ch2 = ch2 + 1
        c = c + 1
        print(f"Раунд {c}")
        print(f"Выиграл 2️⃣  {player2}!👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 3 and vbr3 == 1:
        ch1 = ch1 + 1 
        c = c + 1
        print(f"Раунд {c}")
        print(f"Выиграл 1️⃣  {player1}!👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 1 and vbr3 == 2:
        ch1 = ch1 + 1
        c = c + 1
        print(f"Раунд {c}")
        print(f"Выиграл 1️⃣  {player1}!👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")
    elif vbr2 == 1 and vbr3 == 3:
        ch2 = ch2 + 1
        c = c + 1
        print(f"Раунд {c}")
        print(f"Выиграл 2️⃣  {player2}!👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")  
    elif vbr2 == 2 and vbr3 == 2:
        c = c + 1
        print(f"Раунд {c}")
        print("Ничья!🤝")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}") 
    elif vbr2 == 3 and vbr3 == 3:
        c = c + 1
        print(f"Раунд {c}")
        print("Ничья!🤝")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")  
    elif vbr2 == 2 and vbr3 == 3:
        ch1 = ch1 + 1
        c = c + 1
        print(f"Раунд {c}")
        print(f"Выиграл 1️⃣  {player1}!👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")    
    elif vbr2 == 3 and vbr3 == 2:
        ch2 = ch2 + 1
        c = c + 1
        print(f"Раунд {c}")
        print(f"Выиграл 2️⃣  {player2}!👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")   


if x == 2:
    rulet2 = random.choice(["выиграл!", "одержал победу", "победил"])
    if ch1 > ch2:
        print(f"1️⃣  {player1} {rulet2}👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")   
    else:
        print(f"2️⃣  {player2} {rulet2}👑")
        print(f"1️⃣  {player1} | 2️⃣  {player2}")
        print(f"{ch1} | {ch2}")  
        
if int(vbr) == 3:
    print("🧱 Камень бьёт ✂️ Ножницы")
    print("✂️ Ножницы бьют 📄 Бумагу")
    print("📄 Бумага бьёт 🧱 Камень")

