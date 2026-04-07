import random
from game_vars import *

def event_151_400():
    global population, stability, trust, food, drink, industry, pollution, infrast, weapon, ammo, convoys, heli, truck, heav_ammo, parlam, VVP, money
    
    random_value = random.randint(151, 400)
    
    if random_value <= 275:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Строительство нового завода")
        print("Инвесторы предлагают построить новый завод!")
        print("="*50)
        print("\nВаши действия:")
        print("1. Обычный завод (Пром +2, Загр +1, ВВП +1, Стаб +2%, Деньги -30M)")
        print("2. Эко-завод (Пром +1, Загр 0, ВВП +1, Стаб +3%, Дов +5%, Деньги -50M)")
        print("3. Высокотехнологичный завод (Пром +3, Загр +2, ВВП +2, Стаб +1%, Деньги -80M)")
        print("4. Привлечь инвестиции (Пром +2, ВВП +2, Деньги +20M, Дов +2%)")
        print("5. Отказаться")
        
        choice = input("\nВыберите действие (1-5): ")
        
        if choice == "1":
            industry += 2
            pollution += 1
            VVP += 1
            stability = min(1.0, stability + 0.02)
            money -= 30000000
            print("\nПостроен обычный завод.")
            print(f"Потрачено: 30M. Осталось: {money:,}")
        elif choice == "2":
            industry += 1
            VVP += 1
            stability = min(1.0, stability + 0.03)
            trust = min(1.0, trust + 0.05)
            money -= 50000000
            print("\nПостроен эко-завод!")
            print(f"Потрачено: 50M. Осталось: {money:,}")
        elif choice == "3":
            industry += 3
            pollution += 2
            VVP += 2
            stability = min(1.0, stability + 0.01)
            money -= 80000000
            print("\nПостроен высокотехнологичный завод!")
            print(f"Потрачено: 80M. Осталось: {money:,}")
        elif choice == "4":
            industry += 2
            VVP += 2
            money += 20000000
            trust = min(1.0, trust + 0.02)
            print("\nИнвестиции привлечены!")
            print(f"Получено: 20M. Всего: {money:,}")
        else:
            print("\nВы отказались.")
    else:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Авария на химическом заводе")
        print("Произошла утечка опасных веществ!")
        print("="*50)
        print("\nВаши действия:")
        print("1. Эвакуация (Нас -5000, Загр +3, Дов -5%, Стаб -3%, Деньги -15M)")
        print("2. Очистные фильтры (Загр +1, Нас -1000, Дов -2%, Деньги -30M)")
        print("3. Закрыть завод (Пром -2, Загр +1, Дов -2%, Стаб -4%, Деньги -5M)")
        print("4. Модернизация (Загр 0, Пром +1, Дов +5%, Деньги -100M)")
        print("5. Скрыть информацию (Загр +5, Дов -15%, Стаб -10%)")
        
        choice = input("\nВыберите действие (1-5): ")
        
        if choice == "1":
            pollution += 3
            population = max(0, population - 5000)
            trust = max(0, trust - 0.05)
            stability = max(0, stability - 0.03)
            money -= 15000000
            print("\nЭвакуация проведена.")
            print(f"Потрачено: 15M. Осталось: {money:,}")
        elif choice == "2":
            pollution += 1
            population = max(0, population - 1000)
            trust = max(0, trust - 0.02)
            money -= 30000000
            print("\nОчистные фильтры установлены.")
            print(f"Потрачено: 30M. Осталось: {money:,}")
        elif choice == "3":
            industry = max(0, industry - 2)
            pollution += 1
            trust = max(0, trust - 0.02)
            stability = max(0, stability - 0.04)
            money -= 5000000
            print("\nЗавод закрыт.")
            print(f"Потрачено: 5M. Осталось: {money:,}")
        elif choice == "4":
            industry += 1
            trust = min(1.0, trust + 0.05)
            money -= 100000000
            print("\nМодернизация проведена!")
            print(f"Потрачено: 100M. Осталось: {money:,}")
        else:
            pollution += 5
            trust = max(0, trust - 0.15)
            stability = max(0, stability - 0.10)
            print("\nИнформация скрыта, последствия катастрофичны!")
    
    return random_value