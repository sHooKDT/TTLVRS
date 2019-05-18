from db import db
from classes import *
from datetime import datetime

if __name__ == "__main__":
    db.generate_mapping(create_tables=True)

    with db_session:
        admin = Author(name='Admin', description='Admin\'s user')
        
        pos = Position(latitude=56.837773, longitude=60.603695, name='Родонитовый монолит')
        Event(name='Музыкальный вечер', 
            time_start=get_time('2019-05-25T20:00:00'), 
            time_end=get_time('2019-05-26T00:00:00'), 
            position=pos, description='Будем петь песни и веселиться!', author=admin)
        
        pos = Position(latitude=56.837823, longitude=60.596343, name='Памятник Ленину')
        Event(name='Протест КПРФ', 
            time_start=get_time('2019-05-20T12:00:00'), 
            time_end=get_time('2019-05-20T17:00:00'), 
            position=pos, description='Будем снова протестовать против повышения пенсионного возраста!', author=admin)
        Event(name='Протест КПРФ', 
            time_start=get_time('2019-05-21T12:00:00'), 
            time_end=get_time('2019-05-21T17:00:00'), 
            position=pos, description='Будем снова протестовать против повышения пенсионного возраста!', author=admin)

        pos = Position(latitude=56.831074, longitude=60.604684, name='Центр современного искусства')
        Event(name='Выставка, посвященная Стрит-Арту', 
            time_start=get_time('2019-05-20T12:00:00'), 
            time_end=get_time('2019-05-30T20:00:00'), 
            position=pos, description='Будут представлены работы многих известных артистов ЕКБ.', author=admin)
        
        pos = Position(latitude=56.836008, longitude=60.614662, name='Небоскрёб Высоцкий')
        Event(name='Выставка в музее В.С. Высоцкого', 
            time_start=get_time('2019-05-20T12:00:00'), 
            time_end=get_time('2019-05-30T20:00:00'), 
            position=pos, description='Ранее неизданные работы и произведения.', author=admin)