from . import contact_by_phone, info, menu

bps = [
    menu.bp,               # Вернуться в меню (вызывает дефолтные кнопки)
    contact_by_phone.bp,  # Возможность получения номера тел. и отправка своего
    info.bp               # Вся информация о процедурах и боте
]
