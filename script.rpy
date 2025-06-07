# Определение персонажей (главный герой без спрайта)
define p = Character("")                     # Главный герой
define m = Character("Маша", color="#5bcaff")
define d = Character("Дима", color="#f0d000")
define o = Character("Оля",  color="#ff99ff")

transform slide_from_left:
    xalign -0.5
    linear 0.5 xalign 0.0

transform slide_from_right:
    xalign 1.5
    linear 0.5 xalign 1.0

label start:
    scene bg school_day with fade

    "Сегодня 1 сентября. Новая глава моей студенческой жизни начинается именно сейчас."
    "Возле входа я заметил троих ребят."

    show masha at slide_from_left
    m "Привет! Ты, кажется, новенький?"
    p "Да, всё верно. Рад знакомству, я только поступил."
    m "Отлично! Давай познакомимся со всеми."

    show dima at slide_from_right
    d "Меня зовут Дима. Надеюсь, подружимся!"
    p "Конечно, я тоже на это надеюсь."

    show olya at slide_from_left
    o "Привет-привет, я Оля. Как тебе первые впечатления?"
    p "Пока всё в новинку, но мне уже нравится."

    "Мы ещё немного поболтали и отправились искать аудиторию, где должно было пройти наше первое занятие."

    # Затемнение и монолог героя дома
    scene black with fade
    centered "{size=+10}Спустя несколько часов{/size}"
    scene bg home_evening with fade
    p "Вот и закончился этот насыщенный день."
    p "Столько новой информации, впечатлений и знакомств..."
    p "Интересно, что ждёт меня завтра."

    # Переход в следующий день
    scene black with fade
    centered "{size=+10}На следующий день{/size}"

    # Сцена снаружи колледжа
    scene bg college_outside_day with fade
    p "Новое утро у колледжа. Нужно успеть на пару."

    # Выбор кабинета
    menu:
        "Какой кабинет мне искать?":
            "Кабинет 201":
                p "Кажется, этот этаж не тот. Кабинет 201 закрыт."
                jump search_again
            "Кабинет 304":
                p "Я нашёл нужный кабинет! Пара вот-вот начнётся."
                jump lesson_start
            "Кабинет 102":
                p "Здесь проходят занятия, но не моя пара."
                jump search_again

label search_again:
    p "Нужно поискать ещё."
    jump start_college_hall

label start_college_hall:
    # Вы можете добавить дополнительный диалог или описания здесь
    jump start  # или продолжить сюжет по своему усмотрению

label lesson_start:
    # Сюда продолжение основной истории
    p "Готов к первому учебному дню."
    return
