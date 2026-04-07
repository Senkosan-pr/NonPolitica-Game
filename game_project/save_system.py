import json
import os
import subprocess
import platform
from datetime import datetime
from game_vars import *

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
        "VVP": VVP, "industry": industry, "infrast": infrast, "pollution": pollution,
        "population": population, "stability": stability, "trust": trust,
        "food": food, "drink": drink, "convoys": convoys, "heli": heli, "truck": truck,
        "weapon": weapon, "ammo": ammo, "heav_ammo": heav_ammo, "parlam": parlam, "money": money,
        "step": step, "game_over": game_over, "pollution_flags": pollution_flags,
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
                    print("Неверный номер слота!")
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
                    print("Неверный номер слота!")
        except ValueError:
            print("Введите число!")

def manage_saves_menu():
    global step, game_over
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