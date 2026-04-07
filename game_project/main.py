import random
from game_vars import *
from save_system import *
from events.__init__ import handle_event

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
    
    if check_game_over():
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
    random_value = random.randint(1, 1000)
    print(f"Выпало число: {random_value}")
    event_result = handle_event(random_value)
    
    if check_game_over():
        break
    
    print(f"\nШаг {step + 1} завершён!")
    
    show_warnings()
    
    step += 1
    
    if step < 100 and not game_over:
        input("\nНажмите Enter для следующего шага...")

final_results()