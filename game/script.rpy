﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Русалочка', color="#cf598b")
define a = Character ()

# Определение изображений.

image bg street = "street.png"
image bg lake = "lake.png"
image mermaid = "mermaid.png"

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    stop music
    scene bg street 

    a "Люблю вечером выйти в наушниках на осеннюю улицу"

    a "Нажать на плэй и запустить любимую музыку"

    play music "audio/street sound.mp3"

    a "Любимые мелодии звучат в ушках и холодный ветер обдувает лицо"

    a "В такие моменты я чувствую себя по-настоящему живым"

    a "Такая редкость. Кажется, что этому миру уже совсем нечем меня удивить"

    a "Надеюсь я когда-нибудь смогу собрать свою группу и тоже делать классные песни"

    a "Как это было бы клево..."

    a "Эх..."

    a "" 

    a "мечты, мечты.."

    a "Листья такие разноцветные, на улице совсем осень. Интересно, листья также шуршат под ногами, как и в моем детстве?"

    stop music fadeout 3.0 
   
    a "Да совсем как тогда."

    play music "audio/dasha.mp3" volume 0.4

    a "Я слышу, как поёт девушка!"

    a "Так красиво..."

    a "Я должен её найти"

    a "Голос звучит у озера"

    pause 1.0

    scene bg lake 

    $ renpy.music.set_volume(1.0, channel='music')

    a "Она где-то здесь!"

    a "Какая красивая!"

    show mermaid

    stop music fadeout 1.0 

    e "Ой, я не знала, что здесь кто-то есть!"

    play music "audio/street sound.mp3" fadein 1.0

    e "Ты слышал, как я пою?"

    return
