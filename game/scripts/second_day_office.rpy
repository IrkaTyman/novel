label second_day_office:
    scene hall 
    with dissolve
    pause 1.0

    scene office2 
    with dissolve

    show kai
    kai "{cps=43}Как по мне, самые неприятные из запланированных на сегодня тем уже позади. 
    Теперь давай обсудим некоторые термины, я продемонстрирую обещанный сюрприз и отпущу тебя домой.{/cps}"

    "{cps=43}Значит, сегодня опять не остаюсь на весь рабочий день?{/cps}"

    show kai smile_with_disbelief
    kai "{cps=43}Ага, Карэн не хочет тебя перегружать информацией. Говорит, пусть уж лучше ты запомнишь 
    что-то не очень объемное, чем послушаешь что-то большое и забудешь через пару дней.{/cps}"
    show kai

    "{cps=43}Ей виднее, наверное… Начнем?{/cps}"

    kai "{cps=43}Может тебе покажется странным, что я рассказываю тебе какие-то термины, но будь уверен, очень скоро они тебе пригодятся. 
    Начну с понятия бэклог. Так называют еще не запланированный объем работы, который требуется выполнить команде. 
    Каждая созданная задача вначале попадает в бэклог, а потом уже в спринт.{/cps}"

    "{cps=43}Спринт? А это еще что такое?{/cps}"
    
    show kai smile_with_disbelief
    kai "{cps=43}Рад, что ты спросил. Спринт - это заданный отрезок времени, 
    за который нужно выполнить запланированный объем работы, чтобы в конце этого отрезка 
    был ожидаемый результат.{/cps}" 
    
    kai "{cps=43}Еще тебе нужно знать понятие дейли. Дейли - ежедневные короткие 
    (от 5 до 30 минут) встречи команды с целью поделиться прогрессом по выполненным задачам 
    за предыдущий день и озвучить план работ на текущий день. Также дейли могут называть стендапом.{/cps}"
    show kai

    "{cps=43}Ха-ха, а я думал стендапом только шуточки называют.{/cps}"

    show kai ce
    kai "{cps=43}Смейся-смейся. Главное, запомни, что я тут тебе рассказываю.{/cps}"
    show kai

    "{cps=43}Договорились. Еще какой-нибудь термин?{/cps}"
    
    kai "{cps=43}Да, последний. Ветка. Веткой называют полную копию проекта, в которой ведется разработка. 
    В проекте может быть создано много веток, что позволяет работать одновременно с 
    разными частями кода. На самом деле это тот минимум, что нужен тебе на данный момент.{/cps}"

    kai "{cps=43}Терминологии в геймдеве невероятно много, но сразу все не осилить. 
    Просто старайся по ходу работы искать в интернете непонятные слова и постепенно все выучишь.{/cps}"

    "{cps=43}Ну, наконец сюрприз?{/cps}"

    kai "{cps=43}Наконец сюрприз. Встань и пройди к соседнему столу.{/cps}"

    scene office
    with dissolve
    play sound "music/keyboard.mp3" fadein fadein volume volume

    show kai smile_with_disbelief at leftCoordinates
    kai "{cps=43}Теперь он твой. Конечно, все еще недалеко от меня, но теперь у тебя немного больше личного пространства. Неплохо, правда?{/cps}"

    "{cps=43}Кай, я так рад! Жду не дождусь завтра, чтобы поработать за ним. Надеюсь, будет что-то посложнее, чем обсуждение профессий и обучение терминам.{/cps}"

    show kai smile
    kai "{cps=43}Успеешь еще наработаться… А теперь иди к Карэн и ответь на все ее вопросы. 
    Увидимся завтра, удачи.{/cps}"
    stop sound fadeout 2.0

    jump second_day_office_continue2


label second_day_office_continue2:
    scene hall 
    with dissolve

    show karen smile
    k "{cps=43}Значит уже закончили? Как тебе рабочее место? Все устраивает?{/cps}"

    "{cps=43}Да, спасибо большое. Ощущение, что наконец становлюсь частью команды.{/cps}"

    k "{cps=43}Ну, о таком рановато говорить. Но ты можешь приблизиться к цели, ответив на мои вопросы. 
    Все как и вчера, просто опрос для отслеживания прогресса, просто три вопроса. Начинем?{/cps}"

    "{cps=43}Да.{/cps}"

    show karen 
    k "{cps=43}Тогда скажи мне, как называют заданный отрезок времени, за который нужно выполнить 
    запланированный объем работы, чтобы в конце этого отрезка был ожидаемый результат?{/cps}"

    $ ans1 = renpy.input("Как называют заданный отрезок времени, за который нужно выполнить запланированный объем работы?")

    k "{cps=43}Следующий вопрос: этот термин еще называют стендапом. Что же это?{/cps}"

    $ ans2 = renpy.input("Этот термин еще называют стендапом. Что же это?")

    k "{cps=43}Наконец, последний вопрос. Как называют еще не запланированный объем работы, 
    который требуется выполнить команде?{/cps}"

    $ ans3 = renpy.input("Как называют еще не запланированный объем работы, который требуется выполнить команде?")

    "{cps=43}Ну, как я справился? Ты почему-то никак не реагировала на мои ответы.{/cps}"

    show karen smile
    k "{cps=43}Просто не хотела, чтобы ты отвлекался.{/cps}"
    show karen

    $ counter_true_answers = 0 
    if ans1.casefold() == "спринт" or ans1.casefold() == "Спринт":
        $ counter_true_answers += 1
    if ans2.casefold() == "дейли" or ans2.casefold() == "Дейли" or ans2.casefold() == "Дэйли":
        $ counter_true_answers += 1
    if ans3.casefold() == "бэклог" or ans3.casefold() == "Бэклог" or ans3.casefold() == "Беклог":
        $ counter_true_answers += 1

    if counter_true_answers == 3:
        k "{cps=43}Поздравляю, ты справился на отлично. Продолжай в том же духе, и быстро повысишь свой шанс попасть в компанию.{/cps}"
        $ developer += 1  
    if counter_true_answers == 2:
        k "{cps=43}Неплохо, очень неплохо. И все же ты ошибся один раз, рекомендую дома еще раз повторить все пройденные определения, потому что они и правда важны для любой современной команды разработки.{/cps}"
        $ developer += 0.5

    if counter_true_answers == 1:
        k "{cps=43}Ну, не все так плохо. Один верный ответ. Рекомендую дома еще раз повторить все пройденные определения, потому что они и правда важны для любой современной команды разработки.{/cps}"  
    if counter_true_answers == 0:
        show karen sad
        k "{cps=43}Не заставляй меня разочаровываться в тебе… Все ответы неверны, видимо, ты совсем не слушал Кая. Очень тебя прошу, если правда хочешь попасть к нам - старайся слушать и запоминать. Дома поищи эти термины в интернете, они важны для твоей дальнейшей работы в команде.{/cps}"
        show karen 

    show karen smile
    k "{cps=43}А теперь можешь идти домой. Увидимся завтра.{/cps}"

    show cafee dark
    with dissolve
    
    if watch_kai:
        play sound "music/music good.mp3" fadein fadein volume volume

        "{cps=43}То, что Кай сказал в лифте… Связано ли оно с тем, что я проследил за ним? 
        Мог ли он меня заметить? Мне кажется, я никак не мог себя выдать. 
        Тогда к чему слова о коммерческой тайне? Боится, что я столкнусь с чем-то, 
        с чем столкнуться не должен?{/cps}" 
        
        "{cps=43}Ситуация в компании обрастает слоем загадок, 
        а ответы никак не приходят. Возможно, я должен продолжать изучать этот вопрос. 
        Но что, если я узнаю слишком много?{/cps}"
        stop sound fadeout 3.0

    else:
        play sound "music/music good.mp3" fadein fadein volume volume

        "{cps=43}Хотя Кай и Карэн бывают строги, все-таки они действительно пытаются сделать из меня специалиста, 
        при этом заботясь о том, чтобы я не переусердствовал и постигал основы не в совсем уж скучной 
        обстановке. Если буду продолжать стараться, у меня действительно появится шанс попасть в компанию.{/cps}" 
        
        "{cps=43}А ведь еще пару дней назад я боялся, что буду казаться всем ничтожным из-за отсутствия опыта 
        создания игр. Я рад, что попал именно в эту команду, поскорее бы узнать еще больше людей в корпорации.{/cps}"
        stop sound fadeout 3.0

    jump third_day
    return


    
