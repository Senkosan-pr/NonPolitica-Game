import random
from game_vars import *

def event_751_1000():
    global population, stability, trust, food, drink, industry, pollution, infrast, weapon, ammo, convoys, heli, truck, heav_ammo, parlam, VVP, money
    
    random_value = random.randint(751, 1000)
    
    if random_value <= 875:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Дипломатический успех")
        print("="*50)
        print("\nВаши действия:")
        print("1. Подписать договор (Парл +3, Конв +5, Дов +8%, Стаб +6%)")
        print("2. Торговаться (Парл +2, Конв +7, Дов +10%, Стаб +4%, Деньги +30M)")
        print("3. Расширить сотрудничество (Парл +5, Конв +10, ВВП +2, Дов +12%, Деньги -50M)")
        print("4. Отказаться")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            parlam += 3
            convoys += 5
            trust = min(1.0, trust + 0.08)
            stability = min(1.0, stability + 0.06)
            print("\nДоговор подписан!")
        elif choice == "2":
            parlam += 2
            convoys += 7
            trust = min(1.0, trust + 0.10)
            stability = min(1.0, stability + 0.04)
            money += 30000000
            print("\nУспешные переговоры!")
            print(f"Получено: 30M. Всего: {money:,}")
        elif choice == "3":
            parlam += 5
            convoys += 10
            VVP += 2
            trust = min(1.0, trust + 0.12)
            money -= 50000000
            print("\nСотрудничество расширено!")
            print(f"Потрачено: 50M. Осталось: {money:,}")
        else:
            print("\nОтказ.")
    else:
        if random_value <= 937:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Коррупционный скандал")
            print("="*50)
            print("\nВаши действия:")
            print("1. Чистка (Парл -3, Стаб -5%, Дов -2%, Деньги -20M)")
            print("2. Антикоррупционный комитет (Парл -2, Стаб -8%, Дов +5%, Деньги -50M)")
            print("3. Замять скандал (Парл -5, Стаб -15%, Дов -12%)")
            print("4. Новый премьер (Парл -1, Стаб -10%, Дов +8%, Деньги -30M)")
            print("5. Конфискация (Парл -4, Стаб -3%, Деньги +80M, Дов +10%)")
            
            choice = input("\nВыберите действие (1-5): ")
            
            if choice == "1":
                parlam = max(0, parlam - 3)
                stability = max(0, stability - 0.05)
                trust = max(0, trust - 0.02)
                money -= 20000000
                print("\nЧистка проведена.")
                print(f"Потрачено: 20M. Осталось: {money:,}")
            elif choice == "2":
                parlam = max(0, parlam - 2)
                stability = max(0, stability - 0.08)
                trust = min(1.0, trust + 0.05)
                money -= 50000000
                print("\nКомитет создан!")
                print(f"Потрачено: 50M. Осталось: {money:,}")
            elif choice == "3":
                parlam = max(0, parlam - 5)
                stability = max(0, stability - 0.15)
                trust = max(0, trust - 0.12)
                print("\nСкандал замят, но последствия хуже!")
            elif choice == "4":
                parlam = max(0, parlam - 1)
                stability = max(0, stability - 0.10)
                trust = min(1.0, trust + 0.08)
                money -= 30000000
                print("\nНовый премьер назначен!")
                print(f"Потрачено: 30M. Осталось: {money:,}")
            else:
                parlam = max(0, parlam - 4)
                stability = max(0, stability - 0.03)
                trust = min(1.0, trust + 0.10)
                money += 80000000
                print("\nИмущество конфисковано!")
                print(f"Получено: 80M. Всего: {money:,}")
        else:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Экономический бум")
            print("="*50)
            print("\nВаши действия:")
            print("1. Инвестиции в промышленность (Пром +3, ВВП +2, Деньги -60M)")
            print("2. Инвестиции в соцсферу (Дов +10%, Стаб +8%, Деньги -50M)")
            print("3. Снизить налоги (Дов +15%, Деньги -80M, Стаб +5%)")
            print("4. Накопить резервы (Деньги +100M, Стаб +3%)")
            
            choice = input("\nВыберите действие (1-4): ")
            
            if choice == "1":
                industry += 3
                VVP += 2
                money -= 60000000
                print("\nИнвестиции в промышленность!")
                print(f"Потрачено: 60M. Осталось: {money:,}")
            elif choice == "2":
                trust = min(1.0, trust + 0.10)
                stability = min(1.0, stability + 0.08)
                money -= 50000000
                print("\nИнвестиции в соцсферу!")
                print(f"Потрачено: 50M. Осталось: {money:,}")
            elif choice == "3":
                trust = min(1.0, trust + 0.15)
                stability = min(1.0, stability + 0.05)
                money -= 80000000
                print("\nНалоги снижены!")
                print(f"Потрачено: 80M. Осталось: {money:,}")
            else:
                money += 100000000
                stability = min(1.0, stability + 0.03)
                print("\nРезервы пополнены!")
                print(f"Получено: 100M. Всего: {money:,}")
    
    return random_value