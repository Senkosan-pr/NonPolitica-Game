# Игровые переменные
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

step = 0
game_over = False
random_value = 0

# Флаги эффектов загрязнения
pollution_flags = {
    "pollution_20_applied": False,
    "pollution_40_applied": False,
    "pollution_60_applied": False,
    "pollution_80_applied": False
}

def show_status():
    """Отображает текущее состояние государства"""
    global step
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
    """Применяет эффекты загрязнения при достижении порогов"""
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
    """Показывает предупреждения о критических значениях"""
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

def check_game_over():
    """Проверяет условия поражения"""
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

def final_results():
    """Показывает финальные результаты игры"""
    global step, game_over, VVP, industry, infrast, stability, trust, money, pollution
    
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