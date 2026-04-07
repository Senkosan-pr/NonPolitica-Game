import random
from game_vars import *

def event_401_450():
    global population, stability, trust, food, drink, industry, pollution, infrast, weapon, ammo, convoys, heli, truck, heav_ammo, parlam, VVP, money
    
    random_value = random.randint(401, 450)
    
    if random_value <= 425:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Развитие инфраструктуры")
        print("="*50)
        print("\nВаши действия:")
        print("1. Дороги (Инфра +2, Стаб +5%, Дов +3%, Деньги -20M)")
        print("2. Метро (Инфра +3, Стаб +7%, Дов +5%, Деньги -50M)")
        print("3. Магистрали (Инфра +4, Загр +1, Стаб +4%, Деньги -80M)")
        print("4. Аэропорт (Инфра +5, ВВП +2, Дов +8%, Деньги -150M)")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            infrast += 2
            stability = min(1.0, stability + 0.05)
            trust = min(1.0, trust + 0.03)
            money -= 20000000
            print("\nДороги построены!")
            print(f"Потрачено: 20M. Осталось: {money:,}")
        elif choice == "2":
            infrast += 3
            stability = min(1.0, stability + 0.07)
            trust = min(1.0, trust + 0.05)
            money -= 50000000
            print("\nМетро построено!")
            print(f"Потрачено: 50M. Осталось: {money:,}")
        elif choice == "3":
            infrast += 4
            pollution += 1
            stability = min(1.0, stability + 0.04)
            money -= 80000000
            print("\nМагистрали построены!")
            print(f"Потрачено: 80M. Осталось: {money:,}")
        else:
            infrast += 5
            VVP += 2
            trust = min(1.0, trust + 0.08)
            money -= 150000000
            print("\nАэропорт построен!")
            print(f"Потрачено: 150M. Осталось: {money:,}")
    else:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Массовые протесты")
        print("="*50)
        print("\nВаши действия:")
        print("1. Подавить силой (Стаб -15%, Дов -12%, Нас -2000, Деньги -10M)")
        print("2. Переговоры (Стаб -5%, Дов +5%, Деньги -20M)")
        print("3. Выполнить требования (Стаб +3%, Дов +8%, Парл -2, Деньги -50M)")
        print("4. Повысить зарплаты (Стаб +5%, Дов +10%, Деньги -100M)")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            stability = max(0, stability - 0.15)
            trust = max(0, trust - 0.12)
            population = max(0, population - 2000)
            money -= 10000000
            print("\nСиловое подавление!")
            print(f"Потрачено: 10M. Осталось: {money:,}")
        elif choice == "2":
            stability = max(0, stability - 0.05)
            trust = min(1.0, trust + 0.05)
            money -= 20000000
            print("\nПереговоры проведены.")
            print(f"Потрачено: 20M. Осталось: {money:,}")
        elif choice == "3":
            stability = min(1.0, stability + 0.03)
            trust = min(1.0, trust + 0.08)
            parlam = max(0, parlam - 2)
            money -= 50000000
            print("\nТребования выполнены!")
            print(f"Потрачено: 50M. Осталось: {money:,}")
        else:
            stability = min(1.0, stability + 0.05)
            trust = min(1.0, trust + 0.10)
            money -= 100000000
            print("\nЗарплаты повышены!")
            print(f"Потрачено: 100M. Осталось: {money:,}")
    
    return random_value