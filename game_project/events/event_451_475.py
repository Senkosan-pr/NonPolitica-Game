import random
from game_vars import *

def event_451_475():
    global population, stability, trust, food, drink, industry, pollution, infrast, weapon, ammo, convoys, heli, truck, heav_ammo, parlam, VVP, money
    
    random_value = random.randint(451, 475)
    
    if random_value <= 463:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Военная помощь")
        print("="*50)
        print("\nВаши действия:")
        print("1. Принять всё (Ор +100, Бп +5000, ТВ +25, Стаб +7%)")
        print("2. Модернизировать (Ор +120, Бп +6000, Стаб +10%, Деньги -30M)")
        print("3. Продать часть (Ор +50, Бп +2500, Деньги +40M, Стаб +3%)")
        print("4. Отказаться")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            weapon += 100
            ammo += 5000
            heav_ammo += 25
            stability = min(1.0, stability + 0.07)
            print("\nАрмия усилена!")
        elif choice == "2":
            weapon += 120
            ammo += 6000
            heav_ammo += 30
            stability = min(1.0, stability + 0.10)
            money -= 30000000
            print("\nВооружение модернизировано!")
            print(f"Потрачено: 30M. Осталось: {money:,}")
        elif choice == "3":
            weapon += 50
            ammo += 2500
            money += 40000000
            stability = min(1.0, stability + 0.03)
            print("\nЧасть вооружения продана!")
            print(f"Получено: 40M. Всего: {money:,}")
        else:
            print("\nПомощь отклонена.")
    else:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Засада на конвой")
        print("="*50)
        print("\nВаши действия:")
        print("1. Подкрепление (Конв -1, Ор -20, Стаб -3%, Деньги -5M)")
        print("2. Авиация (Конв -2, Груз -3, Ор -15, Стаб -2%, Деньги -15M)")
        print("3. Переговоры (Конв -3, Груз -5, Ор -10, Стаб -1%, Дов +3%, Деньги -20M)")
        print("4. Масштабная операция (Ор -5, Стаб +2%, Дов +5%, Деньги -50M)")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            convoys = max(0, convoys - 1)
            weapon = max(0, weapon - 20)
            stability = max(0, stability - 0.03)
            money -= 5000000
            print("\nПодкрепление отправлено.")
            print(f"Потрачено: 5M. Осталось: {money:,}")
        elif choice == "2":
            convoys = max(0, convoys - 2)
            truck = max(0, truck - 3)
            weapon = max(0, weapon - 15)
            stability = max(0, stability - 0.02)
            money -= 15000000
            print("\nАвиация использована.")
            print(f"Потрачено: 15M. Осталось: {money:,}")
        elif choice == "3":
            convoys = max(0, convoys - 3)
            truck = max(0, truck - 5)
            weapon = max(0, weapon - 10)
            stability = max(0, stability - 0.01)
            trust = min(1.0, trust + 0.03)
            money -= 20000000
            print("\nПереговоры успешны!")
            print(f"Потрачено: 20M. Осталось: {money:,}")
        else:
            weapon = max(0, weapon - 5)
            stability = min(1.0, stability + 0.02)
            trust = min(1.0, trust + 0.05)
            money -= 50000000
            print("\nОперация успешна!")
            print(f"Потрачено: 50M. Осталось: {money:,}")
    
    return random_value