label second_day_elevator:
    scene elevator outside
    with fade
    pause 1.0
    scene elevator inside
    with fade

    stop music fadeout fadeout
    pause fadeout

    play music "music/elevator.mp3" fadein fadein volume volume loop
    show kai
    with dissolve
    
    kai "{cps=43}Я, конечно, обещал тебе отвлеченный от работы диалог, но пойми меня правильно, 
    мне нужно еще кое-что тебе рассказать, и лучше это сделать прямо сейчас.{/cps}"

    "{cps=43}Я слушаю…{/cps}"

    show kai serious
    kai "{cps=43}Я решил рассказать тебе о такой вещи, как коммерческая тайна. 
    Пока ты не в штате и не работаешь над полноценными продуктами компании, тебя это не касается. 
    Но если все пойдет хорошо, рано или поздно тебе придется подписать соглашение о неразглашении 
    информации. И тогда на тебя ляжет серьезная юридическая ответственность.{/cps}"
    
    kai "{cps=43}Я это все к тому, что в нашей компании множество отделов, каждый занимается каким-то проектом, 
    но все, что не оглашало в СМИ и интернете руководство компании или ее отделы по продвижению продуктов, 
    секретно, и поэтому часто лучше не лезть дальше своих полномочий и своего отдела. 
    Надеюсь на твое понимание, дружище.{/cps}"

    "{cps=43}Конечно, я все понимаю. Спасибо за твое предупреждение.{/cps}"

    "Почему он упомянул это именно сейчас? Вдруг…"


    show kai smile
    "{cps=43}Прибыли. Наше прекрасное кафе с видом на весь город.{/cps}"

    jump second_day_cafe
    
    
    
label second_day_cafe:
    stop music fadeout fadeout
    pause fadeout
    play music "music/music good.mp3" fadein fadein volume volume loop
    
    scene scenes cafee
    with dissolve   

    show kai
    with dissolve

    "{cps=43}Кай, а я буду как-то взаимодействовать с другими работниками компании?{/cps}"

    show kai smile_ce
    kai "{cps=43}Хм… С другими? А разве я тебе уже настолько наскучил?"
    show kai
    "{cps=43}Кай, ну перестань дурачиться, я же серьезно спрашиваю. Когда мне доведется взаимодействовать 
    с кем-то еще, хотя бы с Карэн?{/cps}"

    kai "{cps=43}Я не знаю точно. Скорее всего, когда ты будешь готов что-то делать самостоятельно, 
    а не только под моим чутким взором. Может, это случится через неделю, а может и завтра. Не спеши, и пусть все идет своим чередом.{/cps}"

    "{cps=43}Я понимаю, о чем ты. Но и ты меня пойми: я ведь все-таки жду практику в различных 
    аспектах разработки игр. А ты сам сказал, что в этой области как ни в какой другой важна 
    слаженная работа команды.{/cps}"

    show kai smile
    kai "{cps=43}Уговорил, я попробую как-то приблизить это событие, но ничего не обещаю.{/cps}"
    show kai

    "{cps=43}Спасибо огромное, Кай. Знал бы ты, как я тебе благодарен.{/cps}"

    show kai smile_with_disbelief
    kai "{cps=43}Да ладно, чего уж там… Лучше поспеши, нам уже нужно быть в отделе, а мы все еще тут сидим.{/cps}"

    jump second_day_office
    return



