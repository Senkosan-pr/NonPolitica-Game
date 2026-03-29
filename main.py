import random
import json
import os
import subprocess
import platform
from datetime import datetime


SAVE_DIR = "saves"


if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)


SAVE_FILES = {
    1: os.path.join(SAVE_DIR, "save_slot_1.json"),
    2: os.path.join(SAVE_DIR, "save_slot_2.json"),
    3: os.path.join(SAVE_DIR, "save_slot_3.json"),
    4: os.path.join(SAVE_DIR, "save_slot_4.json"),
    5: os.path.join(SAVE_DIR, "save_slot_5.json")
}


pollution_flags = {
    "pollution_20_applied": False,
    "pollution_40_applied": False,
    "pollution_60_applied": False,
    "pollution_80_applied": False
}


def open_saves_folder():
    full_path = os.path.abspath(SAVE_DIR)
    
    try:
        if platform.system() == "Windows":
            os.startfile(full_path)
        elif platform.system() == "Darwin":
            subprocess.run(["open", full_path])
        else:
            subprocess.run(["xdg-open", full_path])
        print(f"\nОткрыта папка: {full_path}")
        return True
    except Exception as e:
        print(f"\nНе удалось открыть папку: {e}")
        print(f"Путь к папке сохранений: {full_path}")
        return False


def get_save_info():
    saves_info = {}
    for slot, filepath in SAVE_FILES.items():
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    save_data = json.load(f)
                    saves_info[slot] = {
                        "step": save_data.get("step", 0),
                        "date": save_data.get("save_date", "Неизвестно"),
                        "population": save_data.get("population", 0),
                        "stability": save_data.get("stability", 0),
                        "money": save_data.get("money", 0)
                    }
            except:
                saves_info[slot] = None
        else:
            saves_info[slot] = None
    return saves_info


def show_save_slots():
    print("\n" + "="*60)
    print("СЛОТЫ СОХРАНЕНИЙ")
    print("="*60)
    
    saves_info = get_save_info()
    
    for slot in range(1, 6):
        if saves_info[slot]:
            info = saves_info[slot]
            print(f"Слот {slot}: Шаг {info['step']} | Население: {info['population']:,} | "
                  f"Деньги: {info['money']:,} | Стабильность: {info['stability']:.1%} | {info['date']}")
        else:
            print(f"Слот {slot}: [ПУСТО]")
    
    print("="*60)
    print("6. Открыть папку с сохранениями")
    print("0. Отмена")
    print("="*60)


def save_game(step, game_over, slot):
    global VVP, industry, infrast, pollution, population, stability, trust
    global food, drink, convoys, heli, truck, weapon, ammo, heav_ammo, parlam, money
    global pollution_flags
    
    game_state = {
        "VVP": VVP,
        "industry": industry,
        "infrast": infrast,
        "pollution": pollution,
        "population": population,
        "stability": stability,
        "trust": trust,
        "food": food,
        "drink": drink,
        "convoys": convoys,
        "heli": heli,
        "truck": truck,
        "weapon": weapon,
        "ammo": ammo,
        "heav_ammo": heav_ammo,
        "parlam": parlam,
        "money": money,
        "step": step,
        "game_over": game_over,
        "pollution_flags": pollution_flags,
        "save_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        with open(SAVE_FILES[slot], 'w', encoding='utf-8') as f:
            json.dump(game_state, f, ensure_ascii=False, indent=4)
        print(f"\nИгра сохранена в слот {slot}!")
        return True
    except Exception as e:
        print(f"\nОшибка сохранения: {e}")
        return False


def load_game(slot):
    global VVP, industry, infrast, pollution, population, stability, trust
    global food, drink, convoys, heli, truck, weapon, ammo, heav_ammo, parlam, money
    global step, game_over, pollution_flags
    
    if not os.path.exists(SAVE_FILES[slot]):
        print(f"\nСлот {slot} пуст!")
        return False, 0, False
    
    try:
        with open(SAVE_FILES[slot], 'r', encoding='utf-8') as f:
            game_state = json.load(f)
        
        VVP = game_state["VVP"]
        industry = game_state["industry"]
        infrast = game_state["infrast"]
        pollution = game_state["pollution"]
        population = game_state["population"]
        stability = game_state["stability"]
        trust = game_state["trust"]
        food = game_state["food"]
        drink = game_state["drink"]
        convoys = game_state["convoys"]
        heli = game_state["heli"]
        truck = game_state["truck"]
        weapon = game_state["weapon"]
        ammo = game_state["ammo"]
        heav_ammo = game_state["heav_ammo"]
        parlam = game_state["parlam"]
        money = game_state["money"]
        step = game_state["step"]
        game_over = game_state["game_over"]
        
        if "pollution_flags" in game_state:
            pollution_flags = game_state["pollution_flags"]
        
        print(f"\nИгра загружена из слота {slot}!")
        print(f"   Шаг: {step} | Население: {population:,} | Деньги: {money:,} | Стабильность: {stability:.1%}")
        print(f"   Дата сохранения: {game_state.get('save_date', 'Неизвестно')}")
        return True, step, game_over
    except Exception as e:
        print(f"\nОшибка загрузки: {e}")
        return False, 0, False


def delete_save(slot):
    if os.path.exists(SAVE_FILES[slot]):
        try:
            os.remove(SAVE_FILES[slot])
            print(f"\nСохранение из слота {slot} удалено!")
            return True
        except Exception as e:
            print(f"\nОшибка удаления: {e}")
            return False
    else:
        print(f"\nСлот {slot} пуст!")
        return False


def save_menu(step, game_over):
    while True:
        show_save_slots()
        
        try:
            choice = input("\nВыберите слот для сохранения (1-5), 6 - открыть папку, 0 - отмена: ")
            
            if choice == "0":
                return False
            elif choice == "6":
                open_saves_folder()
                continue
            else:
                slot = int(choice)
                if 1 <= slot <= 5:
                    return save_game(step, game_over, slot)
                else:
                    print("Неверный номер слота! Введите число от 0 до 6.")
        except ValueError:
            print("Введите число!")


def load_menu():
    while True:
        show_save_slots()
        
        try:
            choice = input("\nВыберите слот для загрузки (1-5), 6 - открыть папку, 0 - отмена: ")
            
            if choice == "0":
                return False, 0, False
            elif choice == "6":
                open_saves_folder()
                continue
            else:
                slot = int(choice)
                if 1 <= slot <= 5:
                    return load_game(slot)
                else:
                    print("Неверный номер слота! Введите число от 0 до 6.")
        except ValueError:
            print("Введите число!")


def manage_saves_menu():
    while True:
        print("\n" + "="*50)
        print("УПРАВЛЕНИЕ СОХРАНЕНИЯМИ")
        print("="*50)
        print("1. Сохранить игру")
        print("2. Загрузить игру")
        print("3. Удалить сохранение")
        print("4. Показать все сохранения")
        print("5. Открыть папку с сохранениями")
        print("6. Вернуться в игру")
        print("="*50)
        
        choice = input("Выберите действие (1-6): ")
        
        if choice == "1":
            save_menu(step, game_over)
        elif choice == "2":
            loaded, new_step, new_game_over = load_menu()
            if loaded:
                return True, new_step, new_game_over
        elif choice == "3":
            show_save_slots()
            try:
                slot = int(input("\nВыберите слот для удаления (1-5): "))
                if 1 <= slot <= 5:
                    delete_save(slot)
                else:
                    print("Неверный номер слота!")
            except ValueError:
                print("Введите число!")
        elif choice == "4":
            show_save_slots()
            input("\nНажмите Enter для продолжения...")
        elif choice == "5":
            open_saves_folder()
        elif choice == "6":
            return False, step, game_over
        else:
            print("Неверный выбор!")



VVP = 1
industry = 3
infrast = 0 
pollution = 1
population = 100000
stability = 0.4
trust = 0.75
food = 1000000
drink = 500000
convoys = 10
heli = 1
truck = 50
weapon = 250
ammo = 10000
heav_ammo = 50
parlam = 15
money = 10000000000

random_value = 0
step = 0
game_over = False



def random_event_with_choice():
    global population, stability, trust, food, drink, industry, pollution, infrast, weapon, ammo, convoys, heli, truck, heav_ammo, parlam, VVP, money
    
    random_value = random.randint(1, 1000)
    
    
    if 1 <= random_value <= 150:
        if random_value <= 75:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Гуманитарный конвой")
            print("К вам прибыл гуманитарный конвой с продовольствием!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Принять всю помощь (Еда +200K, Вода +100K, Доверие +5%, Стабильность +3%)")
            print("2. Распределить помощь через волонтёров (Еда +180K, Вода +90K, Доверие +8%, Стабильность +5%, Деньги -5M)")
            print("3. Докупить дополнительную помощь (Еда +300K, Вода +150K, Доверие +10%, Деньги -20M)")
            print("4. Отказаться от помощи (Ничего не изменится)")
            
            choice = input("\nВыберите действие (1-4): ")
            
            if choice == "1":
                food += 200000
                drink += 100000
                trust = min(1.0, trust + 0.05)
                stability = min(1.0, stability + 0.03)
                print("\nВы приняли всю помощь! Ресурсы пополнены.")
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
                print("\nДополнительная помощь закуплена! Население в восторге!")
                print(f"Потрачено: 20M. Осталось: {money:,}")
            else:
                print("\nВы отказались от помощи. Конвой ушёл.")
        else:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Порча продуктов")
            print("На складах испортилась часть продуктов из-за неправильного хранения!")
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
                print("\nРасследование показало ошибки логистики.")
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
                print("\nУстановлено новейшее оборудование!")
                print(f"Потрачено: 25M. Осталось: {money:,}")
    
    
    elif 151 <= random_value <= 400:
        if random_value <= 275:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Строительство нового завода")
            print("Инвесторы предлагают построить новый промышленный завод!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Построить обычный завод (Промышленность +2, Загрязнение +1, ВВП +1, Стабильность +2%, Деньги -30M)")
            print("2. Построить эко-завод (Промышленность +1, Загрязнение 0, ВВП +1, Стабильность +3%, Доверие +5%, Деньги -50M)")
            print("3. Построить высокотехнологичный завод (Промышленность +3, Загрязнение +2, ВВП +2, Стабильность +1%, Деньги -80M)")
            print("4. Привлечь иностранные инвестиции (Промышленность +2, ВВП +2, Деньги +20M, Доверие +2%)")
            print("5. Отказаться от строительства")
            
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
                print("\nПостроен экологичный завод!")
                print(f"Потрачено: 50M. Осталось: {money:,}")
            elif choice == "3":
                industry += 3
                pollution += 2
                VVP += 2
                stability = min(1.0, stability + 0.01)
                money -= 80000000
                print("\nВысокотехнологичный завод построен!")
                print(f"Потрачено: 80M. Осталось: {money:,}")
            elif choice == "4":
                industry += 2
                VVP += 2
                money += 20000000
                trust = min(1.0, trust + 0.02)
                print("\nИностранные инвестиции привлечены!")
                print(f"Получено: 20M. Всего: {money:,}")
            else:
                print("\nВы отказались от строительства.")
        else:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Авария на химическом заводе")
            print("Произошла утечка опасных веществ!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Эвакуировать население (Население -5000, Загрязнение +3, Доверие -5%, Стабильность -3%, Деньги -15M)")
            print("2. Установить очистные фильтры (Загрязнение +1, Население -1000, Доверие -2%, Деньги -30M)")
            print("3. Закрыть завод (Промышленность -2, Загрязнение +1, Доверие -2%, Стабильность -4%, Деньги -5M)")
            print("4. Провести полную модернизацию (Загрязнение 0, Промышленность +1, Доверие +5%, Деньги -100M)")
            print("5. Скрыть информацию (Загрязнение +5, Доверие -15%, Стабильность -10%)")
            
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
                print("\nПроведена полная модернизация!")
                print(f"Потрачено: 100M. Осталось: {money:,}")
            else:
                pollution += 5
                trust = max(0, trust - 0.15)
                stability = max(0, stability - 0.10)
                print("\nИнформация скрыта, последствия катастрофичны!")
    
    
    elif 401 <= random_value <= 450:
        if random_value <= 425:
            print("\n" + "="*50)
            print("СОБЫТИЕ: План развития инфраструктуры")
            print("Появилась возможность улучшить транспортную сеть!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Построить дороги (Инфраструктура +2, Стабильность +5%, Доверие +3%, Деньги -20M)")
            print("2. Построить метро (Инфраструктура +3, Стабильность +7%, Доверие +5%, Деньги -50M)")
            print("3. Построить скоростные магистрали (Инфраструктура +4, Загрязнение +1, Стабильность +4%, Деньги -80M)")
            print("4. Построить аэропорт (Инфраструктура +5, ВВП +2, Доверие +8%, Деньги -150M)")
            
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
                print("\nСкоростные магистрали построены!")
                print(f"Потрачено: 80M. Осталось: {money:,}")
            else:
                infrast += 5
                VVP += 2
                trust = min(1.0, trust + 0.08)
                money -= 150000000
                print("\nМеждународный аэропорт построен!")
                print(f"Потрачено: 150M. Осталось: {money:,}")
        else:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Массовые протесты")
            print("Население недовольно условиями жизни!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Подавить силой (Стабильность -15%, Доверие -12%, Население -2000, Деньги -10M)")
            print("2. Провести переговоры (Стабильность -5%, Доверие +5%, Деньги -20M)")
            print("3. Выполнить требования (Стабильность +3%, Доверие +8%, Парламент -2, Деньги -50M)")
            print("4. Повысить зарплаты (Стабильность +5%, Доверие +10%, Деньги -100M)")
            
            choice = input("\nВыберите действие (1-4): ")
            
            if choice == "1":
                stability = max(0, stability - 0.15)
                trust = max(0, trust - 0.12)
                population = max(0, population - 2000)
                money -= 10000000
                print("\nСиловое подавление проведено!")
                print(f"Потрачено: 10M. Осталось: {money:,}")
            elif choice == "2":
                stability = max(0, stability - 0.05)
                trust = min(1.0, trust + 0.05)
                money -= 20000000
                print("\nПереговоры помогли снизить напряжённость.")
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
    
    
    elif 451 <= random_value <= 475:
        if random_value <= 463:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Военная помощь")
            print("Союзники предлагают военную поддержку!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Принять всё (Оружие +100, Боеприпасы +5000, Тяжёлое вооружение +25, Стабильность +7%)")
            print("2. Принять и модернизировать (Оружие +120, Боеприпасы +6000, Стабильность +10%, Деньги -30M)")
            print("3. Принять часть и продать (Оружие +50, Боеприпасы +2500, Деньги +40M, Стабильность +3%)")
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
            print("СОБЫТИЕ: Засада на военный конвой")
            print("Военная колонна попала в засаду!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Отправить подкрепление (Конвои -1, Оружие -20, Стабильность -3%, Деньги -5M)")
            print("2. Использовать авиацию (Конвои -2, Грузовики -3, Оружие -15, Стабильность -2%, Деньги -15M)")
            print("3. Провести переговоры (Конвои -3, Грузовики -5, Оружие -10, Стабильность -1%, Доверие +3%, Деньги -20M)")
            print("4. Организовать масштабную операцию (Оружие -5, Стабильность +2%, Доверие +5%, Деньги -50M)")
            
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
                print("\nАвиация помогла отбить атаку.")
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
                print("\nМасштабная операция успешна!")
                print(f"Потрачено: 50M. Осталось: {money:,}")
    
    
    elif 476 <= random_value <= 750:
        if random_value <= 613:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Приток беженцев")
            print("В страну прибывают беженцы из соседних регионов!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Принять всех (Население +15000, Еда +50K, Вода +25K, Доверие +4%, Деньги -20M)")
            print("2. Организовать лагеря (Население +12000, Еда +40K, Вода +20K, Стабильность +2%, Деньги -10M)")
            print("3. Интегрировать в общество (Население +15000, Доверие +8%, Промышленность +1, Деньги -50M)")
            print("4. Отказать во въезде (Население -2000, Доверие -5%, Стабильность -3%)")
            
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
                print("\nОрганизованы временные лагеря.")
                print(f"Потрачено: 10M. Осталось: {money:,}")
            elif choice == "3":
                population += 15000
                trust = min(1.0, trust + 0.08)
                industry += 1
                money -= 50000000
                print("\nБеженцы успешно интегрированы!")
                print(f"Потрачено: 50M. Осталось: {money:,}")
            else:
                population = max(0, population - 2000)
                trust = max(0, trust - 0.05)
                stability = max(0, stability - 0.03)
                print("\nОтказ вызвал международное осуждение.")
        else:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Неурожай")
            print("Из-за погодных условий урожай значительно ниже нормы!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Использовать резервы (Еда -100K, Вода -50K, Стабильность -5%)")
            print("2. Ввести нормирование (Еда -80K, Вода -40K, Стабильность -8%, Доверие -5%)")
            print("3. Закупить за границей (Еда -50K, Вода -25K, Парламент -2, ВВП -1, Деньги -40M)")
            print("4. Инвестировать в сельское хозяйство (Еда -30K, Вода -15K, Стабильность +5%, Доверие +5%, Деньги -80M)")
            
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
                print("\nИнвестиции в сельское хозяйство!")
                print(f"Потрачено: 80M. Осталось: {money:,}")
    
    
    elif 751 <= random_value <= 1000:
        if random_value <= 875:
            print("\n" + "="*50)
            print("СОБЫТИЕ: Дипломатический успех")
            print("Международные партнёры предлагают выгодные соглашения!")
            print("="*50)
            print("\nВаши действия:")
            print("1. Подписать договор (Парламент +3, Конвои +5, Доверие +8%, Стабильность +6%)")
            print("2. Торговаться о лучших условиях (Парламент +2, Конвои +7, Доверие +10%, Стабильность +4%, Деньги +30M)")
            print("3. Расширить сотрудничество (Парламент +5, Конвои +10, ВВП +2, Доверие +12%, Деньги -50M)")
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
                print("\nСтратегическое партнёрство!")
                print(f"Потрачено: 50M. Осталось: {money:,}")
            else:
                print("\nВы отказались.")
        else:
            if random_value <= 937:
                print("\n" + "="*50)
                print("СОБЫТИЕ: Коррупционный скандал")
                print("Вскрылись факты коррупции среди чиновников!")
                print("="*50)
                print("\nВаши действия:")
                print("1. Провести чистку (Парламент -3, Стабильность -5%, Доверие -2%, Деньги -20M)")
                print("2. Создать антикоррупционный комитет (Парламент -2, Стабильность -8%, Доверие +5%, Деньги -50M)")
                print("3. Замять скандал (Парламент -5, Стабильность -15%, Доверие -12%)")
                print("4. Назначить нового премьера (Парламент -1, Стабильность -10%, Доверие +8%, Деньги -30M)")
                print("5. Конфисковать имущество коррупционеров (Парламент -4, Стабильность -3%, Деньги +80M, Доверие +10%)")
                
                choice = input("\nВыберите действие (1-5): ")
                
                if choice == "1":
                    parlam = max(0, parlam - 3)
                    stability = max(0, stability - 0.05)
                    trust = max(0, trust - 0.02)
                    money -= 20000000
                    print("\nКоррупционеры наказаны.")
                    print(f"Потрачено: 20M. Осталось: {money:,}")
                elif choice == "2":
                    parlam = max(0, parlam - 2)
                    stability = max(0, stability - 0.08)
                    trust = min(1.0, trust + 0.05)
                    money -= 50000000
                    print("\nАнтикоррупционный комитет создан!")
                    print(f"Потрачено: 50M. Осталось: {money:,}")
                elif choice == "3":
                    parlam = max(0, parlam - 5)
                    stability = max(0, stability - 0.15)
                    trust = max(0, trust - 0.12)
                    print("\nСкандал замяли, но последствия оказались хуже!")
                elif choice == "4":
                    parlam = max(0, parlam - 1)
                    stability = max(0, stability - 0.10)
                    trust = min(1.0, trust + 0.08)
                    money -= 30000000
                    print("\nНовый премьер восстановил доверие!")
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
                print("В стране наблюдается экономический рост!")
                print("="*50)
                print("\nВаши действия:")
                print("1. Инвестировать в промышленность (Промышленность +3, ВВП +2, Деньги -60M)")
                print("2. Инвестировать в социальную сферу (Доверие +10%, Стабильность +8%, Деньги -50M)")
                print("3. Снизить налоги (Доверие +15%, Деньги -80M, Стабильность +5%)")
                print("4. Накопить резервы (Деньги +100M, Стабильность +3%)")
                
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
                    print("\nИнвестиции в социальную сферу!")
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
    
    
    stability = max(0, min(1.0, stability))
    trust = max(0, min(1.0, trust))
    population = max(0, population)
    food = max(0, food)
    drink = max(0, drink)
    weapon = max(0, weapon)
    ammo = max(0, ammo)
    money = max(0, money)
    
    return random_value



def check_game_over_conditions():
    global game_over
    
    if stability <= 0:
        print("\nИГРА ОКОНЧЕНА!")
        print("Причина: Стабильность упала до нуля. Государство collapsed!")
        game_over = True
        return True
    elif trust <= 0:
        print("\nИГРА ОКОНЧЕНА!")
        print("Причина: Доверие населения упало до нуля. Началась революция!")
        game_over = True
        return True
    elif food <= 0:
        print("\nИГРА ОКОНЧЕНА!")
        print("Причина: Закончилась еда! Начался голод!")
        game_over = True
        return True
    elif drink <= 0:
        print("\nИГРА ОКОНЧЕНА!")
        print("Причина: Закончилась вода! Началась засуха!")
        game_over = True
        return True
    elif population <= 1000:
        print("\nИГРА ОКОНЧЕНА!")
        print("Причина: Население почти вымерло!")
        game_over = True
        return True
    elif pollution >= 100:
        print("\nИГРА ОКОНЧЕНА!")
        print("Причина: Загрязнение достигло 100 единиц!")
        print("Экологическая катастрофа уничтожила всё живое!")
        game_over = True
        return True
    elif money < 0:
        print("\nИГРА ОКОНЧЕНА!")
        print("Причина: Государственное банкротство! Деньги закончились!")
        game_over = True
        return True
    
    return False



def show_status():
    print("\n" + "="*60)
    print(f"ТЕКУЩЕЕ СОСТОЯНИЕ ГОСУДАРСТВА (Шаг {step + 1}/100)")
    print("="*60)
    print(f"Население: {population:,}")
    print(f"Бюджет: {money:,}")
    print(f"Промышленность: {industry} | Инфраструктура: {infrast} | Загрязнение: {pollution}")
    print(f"ВВП: {VVP} | Стабильность: {stability:.1%} | Доверие: {trust:.1%}")
    print(f"Еда: {food:,} | Вода: {drink:,}")
    print(f"Конвои: {convoys} | Вертолёты: {heli} | Грузовики: {truck}")
    print(f"Оружие: {weapon} | Боеприпасы: {ammo:,} | Тяжёлое вооружение: {heav_ammo}")
    print(f"Парламент: {parlam}")
    print("="*60)



def apply_pollution_effects():
    global stability, food, drink, pollution, pollution_flags
    
    if pollution >= 20 and pollution < 40:
        if not pollution_flags["pollution_20_applied"]:
            stability = max(0, stability - 0.05)
            food = max(0, food - 20000)
            drink = max(0, drink - 10000)
            print("\nЭФФЕКТ ЗАГРЯЗНЕНИЯ (20+)")
            print("   Загрязнение достигло критического уровня 20!")
            print("   Стабильность -5%, Еда -20K, Вода -10K")
            pollution_flags["pollution_20_applied"] = True
            return True
    elif pollution >= 40 and pollution < 60:
        if not pollution_flags["pollution_40_applied"]:
            stability = max(0, stability - 0.08)
            food = max(0, food - 40000)
            drink = max(0, drink - 20000)
            print("\nЭФФЕКТ ЗАГРЯЗНЕНИЯ (40+)")
            print("   Загрязнение достигло критического уровня 40!")
            print("   Стабильность -8%, Еда -40K, Вода -20K")
            pollution_flags["pollution_40_applied"] = True
            return True
    elif pollution >= 60 and pollution < 80:
        if not pollution_flags["pollution_60_applied"]:
            stability = max(0, stability - 0.12)
            food = max(0, food - 60000)
            drink = max(0, drink - 30000)
            print("\nЭФФЕКТ ЗАГРЯЗНЕНИЯ (60+)")
            print("   Загрязнение достигло критического уровня 60!")
            print("   Стабильность -12%, Еда -60K, Вода -30K")
            pollution_flags["pollution_60_applied"] = True
            return True
    elif pollution >= 80 and pollution < 100:
        if not pollution_flags["pollution_80_applied"]:
            stability = max(0, stability - 0.15)
            food = max(0, food - 80000)
            drink = max(0, drink - 40000)
            print("\nЭФФЕКТ ЗАГРЯЗНЕНИЯ (80+)")
            print("   Загрязнение достигло критического уровня 80!")
            print("   Стабильность -15%, Еда -80K, Вода -40K")
            pollution_flags["pollution_80_applied"] = True
            return True
    return False



def show_warnings():
    if food < 100000:
        print("ВНИМАНИЕ: Критически низкий запас еды!")
    if drink < 50000:
        print("ВНИМАНИЕ: Критически низкий запас воды!")
    if stability < 0.2:
        print("ВНИМАНИЕ: Критически низкая стабильность!")
    if trust < 0.2:
        print("ВНИМАНИЕ: Критически низкое доверие!")
    if money < 500000000:
        print("ВНИМАНИЕ: Критически низкий бюджет!")
    if pollution >= 80:
        print("ВНИМАНИЕ: Критически высокий уровень загрязнения!")
        print("   Срочно нужны меры по очистке окружающей среды!")
    elif pollution >= 60:
        print("ВНИМАНИЕ: Высокий уровень загрязнения!")
        print("   Загрязнение негативно влияет на экологию!")
    elif pollution >= 40:
        print("ВНИМАНИЕ: Повышенный уровень загрязнения!")
        print("   Требуются меры по снижению выбросов!")



print("\n" + "="*50)
print("УПРАВЛЕНИЕ ГОСУДАРСТВОМ")
print("="*50)
print(f"Папка сохранений: {os.path.abspath(SAVE_DIR)}")
print("="*50)
print("1. Новая игра")
print("2. Загрузить сохранение")
print("="*50)

choice = input("Выберите действие (1-2): ")

if choice == "2":
    loaded, step, game_over = load_menu()
    if not loaded:
        print("Начинаем новую игру...")
        step = 0
        game_over = False
else:
    step = 0
    game_over = False


while step < 100 and not game_over:
    show_status()
    
    apply_pollution_effects()
    
    if check_game_over_conditions():
        break
    
    print("\n" + "-"*50)
    print("Доступные действия:")
    print("1. Продолжить игру")
    print("2. Меню сохранений")
    print("-"*50)
    
    action = input("Выберите действие (1-2): ")
    
    if action == "2":
        need_reload, new_step, new_game_over = manage_saves_menu()
        if need_reload:
            step = new_step
            game_over = new_game_over
            if game_over:
                break
        continue
    
    input("\nНажмите Enter для генерации события...")
    
    print("\nГенерируем случайное событие...")
    event_result = random_event_with_choice()
    
    if check_game_over_conditions():
        break
    
    print(f"\nШаг {step + 1} завершён!")
    
    show_warnings()
    
    step += 1
    
    if step < 100 and not game_over:
        input("\nНажмите Enter для следующего шага...")


print("\n" + "="*50)
if step >= 100 and not game_over:
    print("ПОЗДРАВЛЯЮ!")
    print("Вы успешно прошли 100 шагов!")
    print("Ваше государство выжило и развивается!")
    
    if pollution <= 20:
        print("\nЭКОЛОГИЯ: Отлично! Чистая окружающая среда!")
    elif pollution <= 40:
        print("\nЭКОЛОГИЯ: Хорошо! Экологическая ситуация стабильна.")
    elif pollution <= 60:
        print("\nЭКОЛОГИЯ: Удовлетворительно. Требуется внимание.")
    elif pollution <= 80:
        print("\nЭКОЛОГИЯ: Плохо! Высокий уровень загрязнения!")
    else:
        print("\nЭКОЛОГИЯ: Катастрофа! Окружающая среда на грани!")
    
    total_score = (VVP * 10) + (industry * 5) + (infrast * 8) + (stability * 100) + (trust * 100) + (money // 100000000) - (pollution * 2)
    print(f"\nИТОГОВЫЙ СЧЁТ: {total_score:.0f}")
    
    if total_score >= 500:
        print("ВЕЛИКОЛЕПНО! Вы создали процветающую империю!")
    elif total_score >= 350:
        print("ХОРОШО! Государство стабильно и развивается!")
    elif total_score >= 200:
        print("УДОВЛЕТВОРИТЕЛЬНО. Есть куда расти!")
    else:
        print("ПЛОХО. Государство на грани выживания!")
elif game_over:
    print("ИГРА ЗАВЕРШЕНА ДОСРОЧНО")
    print(f"Вы продержались {step} шагов из 100")

print("\nСпасибо за игру!")