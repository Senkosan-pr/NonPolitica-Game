import random
from game_vars import *

def event_1_150():
    global population, stability, trust, food, drink, industry, pollution, infrast, weapon, ammo, convoys, heli, truck, heav_ammo, parlam, VVP, money
    
    random_value = random.randint(1, 150)
    
    if random_value <= 75:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Гуманитарный конвой")
        print("К вам прибыл гуманитарный конвой с продовольствием!")
        print("="*50)
        print("\nВаши действия:")
        print("1. Принять всю помощь (Еда +200K, Вода +100K, Доверие +5%, Стабильность +3%)")
        print("2. Распределить помощь через волонтёров (Еда +180K, Вода +90K, Доверие +8%, Стабильность +5%, Деньги -5M)")
        print("3. Докупить дополнительную помощь (Еда +300K, Вода +150K, Доверие +10%, Деньги -20M)")
        print("4. Отказаться от помощи")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            food += 200000
            drink += 100000
            trust = min(1.0, trust + 0.05)
            stability = min(1.0, stability + 0.03)
            print("\nВы приняли всю помощь!")
        elif choice == "2":
            food += 180000
            drink += 90000
            trust = min(1.0, trust + 0.08)
            stability = min(1.0, stability + 0.05)
            money -= 5000000
            print("\nВолонтёры эффективно распределили помощь!")
            print(f"Потрачено: 5M. Осталось: {money:,}")
        elif choice == "3":
            food += 300000
            drink += 150000
            trust = min(1.0, trust + 0.10)
            money -= 20000000
            print("\nДополнительная помощь закуплена!")
            print(f"Потрачено: 20M. Осталось: {money:,}")
        else:
            print("\nВы отказались от помощи.")
    else:
        print("\n" + "="*50)
        print("СОБЫТИЕ: Порча продуктов")
        print("На складах испортилась часть продуктов!")
        print("="*50)
        print("\nВаши действия:")
        print("1. Списать потери (Еда -50K, Вода -30K, Стабильность -2%)")
        print("2. Провести расследование (Еда -40K, Вода -20K, Стабильность -1%, Доверие +2%, Деньги -2M)")
        print("3. Улучшить систему хранения (Еда -30K, Вода -15K, Инфраструктура +1, Деньги -10M)")
        print("4. Закупить новое оборудование (Еда -20K, Вода -10K, Инфраструктура +2, Деньги -25M)")
        
        choice = input("\nВыберите действие (1-4): ")
        
        if choice == "1":
            food = max(0, food - 50000)
            drink = max(0, drink - 30000)
            stability = max(0, stability - 0.02)
            print("\nПотери списаны.")
        elif choice == "2":
            food = max(0, food - 40000)
            drink = max(0, drink - 20000)
            stability = max(0, stability - 0.01)
            trust = min(1.0, trust + 0.02)
            money -= 2000000
            print("\nРасследование проведено.")
            print(f"Потрачено: 2M. Осталось: {money:,}")
        elif choice == "3":
            food = max(0, food - 30000)
            drink = max(0, drink - 15000)
            infrast += 1
            money -= 10000000
            print("\nСистема хранения улучшена!")
            print(f"Потрачено: 10M. Осталось: {money:,}")
        else:
            food = max(0, food - 20000)
            drink = max(0, drink - 10000)
            infrast += 2
            money -= 25000000
            print("\nНовое оборудование установлено!")
            print(f"Потрачено: 25M. Осталось: {money:,}")
    
    return random_value