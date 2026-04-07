import random
from game_vars import *

def event_476_750():
    global population, stability, trust, food, drink, industry, pollution, infrast, weapon, ammo, convoys, heli, truck, heav_ammo, parlam, VVP, money
    
    random_value = random.randint(476, 750)
    
    if random_value <= 613:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Приток беженцев")
        print("="*50)
        print("\nВаши действия:")
        print("1. Принять всех (Нас +15000, Еда +50K, Вода +25K, Дов +4%, Деньги -20M)")
        print("2. Организовать лагеря (Нас +12000, Еда +40K, Вода +20K, Стаб +2%, Деньги -10M)")
        print("3. Интегрировать (Нас +15000, Дов +8%, Пром +1, Деньги -50M)")
        print("4. Отказать (Нас -2000, Дов -5%, Стаб -3%)")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            population += 15000
            food += 50000
            drink += 25000
            trust = min(1.0, trust + 0.04)
            money -= 20000000
            print("\nБеженцы приняты.")
            print(f"Потрачено: 20M. Осталось: {money:,}")
        elif choice == "2":
            population += 12000
            food += 40000
            drink += 20000
            stability = min(1.0, stability + 0.02)
            money -= 10000000
            print("\nЛагеря организованы.")
            print(f"Потрачено: 10M. Осталось: {money:,}")
        elif choice == "3":
            population += 15000
            trust = min(1.0, trust + 0.08)
            industry += 1
            money -= 50000000
            print("\nБеженцы интегрированы!")
            print(f"Потрачено: 50M. Осталось: {money:,}")
        else:
            population = max(0, population - 2000)
            trust = max(0, trust - 0.05)
            stability = max(0, stability - 0.03)
            print("\nОтказано во въезде.")
    else:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Неурожай")
        print("="*50)
        print("\nВаши действия:")
        print("1. Использовать резервы (Еда -100K, Вода -50K, Стаб -5%)")
        print("2. Нормирование (Еда -80K, Вода -40K, Стаб -8%, Дов -5%)")
        print("3. Закупить за границей (Еда -50K, Вода -25K, Парл -2, ВВП -1, Деньги -40M)")
        print("4. Инвестировать в АПК (Еда -30K, Вода -15K, Стаб +5%, Дов +5%, Деньги -80M)")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            food = max(0, food - 100000)
            drink = max(0, drink - 50000)
            stability = max(0, stability - 0.05)
            print("\nРезервы использованы.")
        elif choice == "2":
            food = max(0, food - 80000)
            drink = max(0, drink - 40000)
            stability = max(0, stability - 0.08)
            trust = max(0, trust - 0.05)
            print("\nНормирование введено.")
        elif choice == "3":
            food = max(0, food - 50000)
            drink = max(0, drink - 25000)
            parlam = max(0, parlam - 2)
            VVP = max(0, VVP - 1)
            money -= 40000000
            print("\nЗакупки проведены.")
            print(f"Потрачено: 40M. Осталось: {money:,}")
        else:
            food = max(0, food - 30000)
            drink = max(0, drink - 15000)
            stability = min(1.0, stability + 0.05)
            trust = min(1.0, trust + 0.05)
            money -= 80000000
            print("\nИнвестиции в АПК!")
            print(f"Потрачено: 80M. Осталось: {money:,}")
    
    return random_value