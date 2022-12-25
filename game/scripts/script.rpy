# Определение персонажей игры.
define kai = Character('Кай', color="#0318fc")
define e = Character('Элли', color="#fc038c", image = "elly")
define g = Character('Девушка', color="#fc038c", image = "elly")
define l = Character('Ллойд', color="#03fc45", image = "lloyd")
define ar = Character('Арон', color="#03fc45", image = "lloyd")
define k = Character('Карэн', color="#640303", image = "karen")
define g = Character('Грейс', color="#94002300", image = "grace")

define a = Character('Алан', color="#23282b00", image = "alan")
define m = Character('Мужчина', color="#23282b00", image = "alan")

define unm = Character('Мужчина', color="#23282b00", image = "unknown") # unknown man
define v = Character('Виктор', color="#23282b00", image = "unknown") # unknown man

define gd = Character('Охрана', color="#00000000", image = "guard")


define news = Character('news', color="#0000007d", image = "news")

define loaders_array = ["intro/loader (0).png", "intro/loader (1).png", "intro/loader (2).png",
"intro/loader (3).png","intro/loader (4).png","intro/loader (5).png","intro/loader (6).png",
"intro/loader (7).png","intro/loader (8).png","intro/loader (9).png","intro/loader (10).png","intro/loader (11).png"]

#для переписки по телефону
#define m_nvl = Character("Me", kind=nvl, image="nighten", callback=Phone_SendSound)
#define n_nvl = Character("News", kind=nvl, callback=Phone_ReceiveSound)
define nameM = "Макс"
define currNews = -1
define newsImage = ["one" , "two", "three", "three", "four", "four", "four", "four", "four", "five"]
define newsText = ["Все началось в июле 2039 года, когда в Японии научились воздействовать на мозг человека напрямую с компьютера. Не сказать, что 6 числа это казалось грандиозным открытием. Где-то в научных кругах, конечно, многие считали технологию прорывной, но для обычного человека, погруженного в ежедневную рутину, это было просто “еще одно научное открытие”.",
"На следующий день волна споров и противоречивых прогнозов накрыла уже область экономики, когда японский рынок резко прыгнул на такую отметку, какую не достигал десятилетиями.",

"Через четыре месяца все только и делали, что обсуждали грядущий выход первого массового компьютера, работающего по этой новой технологии. Кто-то в страхе рассказывал каждому встречному, что нельзя пользоваться новым изобретением, потому что оно наносит непоправимый вред организму, кто-то воодушевленно рассуждал о перспективах, открывающихся благодаря транслированию сигнала прямо в мозг.",
"Но объединяло всех одно:{w} уже никто не оставался в стороне от обсуждения Neuroconnect.",

"Полгода мы наблюдали, как мир меняется прямо на наших глазах. Игровая индустрия росла как на дрожжах, разработчик игр стал одной из самых желанных профессий. Если ты работаешь в крупной игровой корпорации, тебе не нужно задумываться о деньгах, тебя окружают лучшие из лучших, а из твоего офиса в самом центре города открывается превосходный вид на тех, кому не так сильно повезло с местом работы.",
"Помню, как все мои знакомые разделились на два лагеря: тех, кто буквально стал зависим от транслируемых прямо в разум игр, и тех, кто мечтал однажды получить приглашение на работу хотя бы в самой крошечной игровой студии.",
"Я никогда не причислял себя к какой-то из этих групп, мне одновременно было приятно погружаться в мир игры, словно самостоятельно переживая десятки чужих жизней и тысячи ситуаций, и изучать устройство таких игр, слушать об интересных механиках, делающих игровой опыт настолько интересным, и придумывать собственные геймдизайнерские решения. И все же мое увлечение играми никогда не доходило до непосредственного создания чего-то своего.",
"А сейчас я еду на встречу собственной мечте и переживаю, что ничего из себя не представляю."
"Кажется, уже пора готовиться к выходу. Хотя я могу успеть прочитать еще одну статью. Возможно, это поможет мне в первый день стажировки - все-таки я хочу как можно лучше подготовиться.",

"Я никогда об этом не задумывался. Действительно, хотя многие люди стали затворниками и бросили свои прежние занятия, просто чтобы дома сутками проходить игры, правительство никак не реагирует.{w} Интересно, чем же все это может быть выгодно?"
]


define text_desk_first = "Будем говорить о реализации на языке C#, так как именно его вам нужно будет использовать в проекте. \n Чтобы создать на этом языке константу, вам нужно написать const, а затем указать тип данной переменной. \n Переменная - это своеобразный контейнер, используемый для хранения данных и имеющий уникальное имя. \nОни бывают различных типов, и в языках со статической типизацией вы должны явно это указывать, когда объявляете переменную. \nДля чисел вы чаще всего будете использовать два типа данных: int и double. \nПервое - сокращение от integer, это тип используется для целых чисел, double, в свою очередь, применяют, когда создают переменную для числа с плавающей точкой."
define text_desk_second = "Конечно, вы обязательно будете работать с символами и строками. \n Строки в языке C# обозначаются string. Главное, не забудьте, что в переменную строки можно записать только текст в двойных кавычках. \n Если используете одинарные - создадите переменную типа char, а это уже тип данных для символов.\n Любая string переменная состоит из char символов. Для различных логических значений вы будете использовать тип bool, который принимает значения true или false. \nНа самом деле, в большинстве случаев вам совсем не нужно указывать тип данных. \n Дело в том, что в языке C# можно писать вместо типа данных var, и тогда компилятор определит тип данных самостоятельно. Мы называем это “синтаксический сахар”. \n Но будьте осторожны! Чтобы не возникло неожиданных ошибок, всегда старайтесь использовать var с данными, тип которых очевиден. \n Выглядеть это будет так: var name = “value”; - для строки, \n var number = 4; - для целых чисел, var number = 4.3; - для чисел с плавающей точкой. \n Для констант это будет выглядеть так: const int number = 3;."
define text_desk_third = "Точно, вам пригодится возможность хранить ряд данных в одной переменной. \n Тогда просто создайте массив вот так: \n var arr = new int[[3] - для массива целых чисел длиной 3, но аналогично и с другими типами данных. \n Чтобы добавить значение n-ному элементу массива используйте: arr[[n] = 4;. \n Перейдем к условиям. Оператор условия в C# выглядит так: \n if (логическое выражение) {{блок кода, если условие истинно} else {{блок кода, если условие ложно}. \n С помощью оператора условия можно сделать ветвление в вашем коде, но часто нужно обрабатывать не просто выбор между true и false, но и выполнять операции с большим количеством повторений. \n Тогда на помощь приходят циклы. \n Цикл while используется для повторений до момента, пока некое условие истинно: while (условие) {{блок кода}. \n Цикл for, в свою очередь, используют тогда, когда количество повторений заранее известно: \n for (var i = 0;i < 5; i++) {{блок кода} - переменная i будет последовательно принимать целые значения от 0 включительно до 5 не включительно, \n то есть шаг будет 1, за это отвечает i++, что означает прибавить к i 1, \n разумеется, все это можно изменять в зависимости от поставленной задачи."
define text_desk_forth = "Теперь немного о Git. \n Это система управления версиями с распределенной архитектурой, позволяющая командам разработчиков создавать проект вместе и успешно синхронизировать все изменения, а также разрешать конфликты в коде. \n Для вашей работы хватит трех команд, репозиторий, то есть папка с проектом, уже создана, вы просто должны будете сохранять и отправлять все важные изменения. \n Первая команда - git add. В цепочке команд она предписывает «сохранить» снимок текущего состояния проекта в истории коммитов. \n Когда git add используется как отдельная команда, она переносит ожидающие изменения из рабочего каталога в раздел проиндексированных файлов. \n Затем вы будете использовать git commit. Она делает для проекта снимок текущего состояния изменений, добавленных в раздел проиндексированных файлов. \n Такие подтвержденные снимки состояния можно рассматривать как «безопасные» версии проекта — Git не будет их менять, пока ты явным образом не попросишь об этом.\n  Ну и наконец команда git push. \n Используется для выгрузки содержимого локального репозитория в удаленный репозиторий. \n Она позволяет передать коммиты из локального репозитория в удаленный. "
define text_desk_fifth = "Вы должны понимать, что цвет играет огромную роль и влияет как на восприятие объектов, так и на направление движения, настроение, физическое состояние да и много еще на что. \n Он может помогать принимать решения и помогать игроку видеть влияние на мир игры. \n Во-первых, у цвета функция ориентира. Заметные цвета привлекают внимание игроков к объекту или предмету, скажем, ярко-желтая линия посреди индустриального пейзажа точно будет заметной. \n Во-вторых, цвета предупреждают. Шутеры, RPG, стелс-action, другие подобные жанры содержат много опасностей для персонажа. Разработчик может предусмотреть цветовую индикацию опасности и спокойствия, что, несомненно, улучшит пользовательский опыт.\n  Цвет помогает развивать историю. \n Изменение цвета часто применяют при показе флэшбеков, предысторий, воспоминаний. \n Таким образом, основную историю отделяют от второстепенной, а игрок не путается с линиями повествования. \n Наконец, можно использовать различные цвета при отрисовке персонажей, чтобы сделать акцент на каждом из них. "
define text_desk_sixth = "Например, ваше будущее задание связано с Angry Birds. \n В этой игре каждая птица имеет свой цвет, что помогает герою быстро ориентироваться, кто из них бумеранг или бомбочка. \n Вообще, работа с цветом в геймдеве - очень сложная и кропотливая. Поэтому нельзя сначала создать игру, а затем уже обдумывать основную палитру. \n Лучше всего, если в вашей команде изначально будет художник или дизайнер, который займется разработкой визуальной составляющей одновременно с техническими работами. \n Проблемой могут стать невозможные цвета (или запретные цвета) — это те цвета, которые из-за особенностей сетчатки человек не может воспринимать одновременно. \n Невозможные цвета — это оттенки, которые похожи на оба цвета, например, «красно-зелёный» или «жёлто-голубой». "

define detective = 0
define soleCompany = 0
define developer = 0
define loveLine = 0
define watch_kai = False
define ans1 = ""
define ans2 = ""
define ans3 = ""
define ans = ""
define computerWrongAns = 0
define computerWrongAnsSecond = 0
define tap = 1
define score = [0, 0, 0, False, False] # 1 2 3 задания + воспользовался ли помощью + посетил ли Элли
define totalScore = 0
define see_lloyd = False
define volume = 0.2
define fadein = 5.0
define fadeout = 0.5
define long_fadeout = 2.0

init python:
    leftCoordinates = Position(xalign = 0.0, yalign = 0.7)
    rightCoordinates = Position(xalign = 0.5, yalign = 0.7)
    leftDownCoordinates = Position(xalign = 0.0, yalign = - 1.6)
    rightCenterCoordinates = Position(xalign = 0.6, yalign = - 1.0)
    leftCenterCoordinates = Position(xalign = 0.3, yalign = - 2.0)
    
    # truecenter_custom = Position(xalign = 0.5, yalign = 0.162)
    truecenter_custom = Position(xalign = 0.5, yalign = 0.262)
    phone_transition_speed = 0.05 #Using a variable to make testing different speeds easier.


 
label splashscreen:
    image splash = "intro/first.png"
    image blackIm = "intro/black.png"
    image enterPressed = "intro/center_text.png"

    show splash with dissolve
    $ renpy.pause(3.0)

    show blackIm with dissolve
    $ renpy.pause(2.0)

    show enterPressed at truecenter
    with dissolve 
    
    call screen keypress

    return

screen keypress():
    key "K_SPACE" action Jump("succeeded")
    timer 4.0 action Jump("splashscreen")

label succeeded:
    image loader0 = "intro/loader (0).png"
    image loader1 = "intro/loader (1).png"
    image loader2 = "intro/loader (2).png"
    image loader3 = "intro/loader (3).png"
    image loader4 = "intro/loader (4).png"
    image loader5 = "intro/loader (5).png"
    image loader6 = "intro/loader (6).png"
    image loader7 = "intro/loader (7).png"
    image loader8 = "intro/loader (8).png"
    image loader9 = "intro/loader (9).png"
    image loader10 = "intro/loader (10).png"
    image loader11 = "intro/loader (11).png"

    show loader0 at right
    pause 0.3
    show loader1 at right
    pause 0.3
    show loader2 at right
    pause 0.3
    show loader3 at right
    pause 0.3
    show loader4 at right
    pause 0.3
    show loader5 at right
    pause 0.3
    show loader6 at right
    pause 0.3
    show loader7 at right
    pause 0.3
    show loader8 at right
    pause 0.3
    show loader9 at right
    pause 0.3
    show loader10 at right
    pause 0.3
    show loader11 at right
    pause 4.0
    return


# Игра начинается здесь:
label start:

    $ point = 0

    jump first_day_moring

    jump first_day_survey

    jump second_day

    jump third_day

    jump fourth_day
    
    jump fifth_day


    return


label news:
    $ currNews += 1

    $ renpy.show("news " + newsImage[currNews])
    $ textC = newsText[currNews]

    "{size=-6}{cps=43}[textC]{/cps}{/size}"

    if currNews == 5:
        $ detective += 1
        jump end_bus

    call screen closebutton

screen closebutton:
    imagebutton:
        xalign 0.714
        yalign 0.259
        idle "news/closebutton.png"
        hover "news/closebutton.png"
        action Jump("end_bus")

    imagebutton:
        xalign 0.258
        yalign 0.47
        idle "news/nextbutton.png"
        hover "news/nextbutton.png"
        action Jump("news")