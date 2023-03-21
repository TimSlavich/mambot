from wonda.tools.keyboard import InlineKeyboard, ReplyKeyboard, Callback, Contact


class Keyboard:
    menu = (
        InlineKeyboard()
        .add(Callback("📘 Информация", "info"))
        .row()
        .add(Callback("📆 Доступные дни", "available_days"))
        .add(Callback("☎️ Связаться по телефону", "contact_by_phone"))
        .build()
    )

    back_to_menu = (
        InlineKeyboard()
        .add(Callback("📄 Вернуться в меню", "menu"))
        .build()
    )

    send_phone = (
        ReplyKeyboard(resize_keyboard=True, one_time_keyboard=True)
        .add(Contact("📞 Отправить мой номер"))
        .build()
    )

    day_table = (
        InlineKeyboard()
        .add(Callback("Понедельник", "monday"))
        .add(Callback("Вторник", "tuesday"))
        .add(Callback("Среда", "wednesday"))
        .add(Callback("Четверг", "thursday"))
        .add(Callback("Пятница", "friday"))
        .build()
    )

    time_table = (
        InlineKeyboard()
        .add(Callback("10:00", "10:00"))
        .add(Callback("12:00", "12:00"))
        .add(Callback("14:00", "14:00"))
        .add(Callback("16:00", "16:00"))
        .add(Callback("18:00", "18:00"))
        .build()
    )
