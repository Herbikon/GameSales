import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_bot.settings')
django.setup()

from bot_web.models import Genre, Developer, Publisher, Tags, Localization, Games

def populate_database():
    Games.objects.all().delete()
    Genre.objects.all().delete()
    Developer.objects.all().delete()
    Publisher.objects.all().delete()
    Tags.objects.all().delete()
    Localization.objects.all().delete()
    
    genres_data = [
        (1, 'Action'),
        (2, 'Аркады'),
        (3, 'Платформеры'),
        (4, 'Шутеры'),
        (5, 'Shoot\'em up и top-down шутеры'),
        (6, 'Слэшеры'),
        (7, 'Файтинги'),
        (8, 'BEAT-EM UP'),
        (9, 'Стелс-экшены'),
        (10, 'Выживание')
    ]
    
    for id, name in genres_data:
        Genre.objects.create(id=id, Genre_name=name)
    
    print("Жанры созданы")
    
    developers_data = [
        (1, 'One More Level'),
        (2, '3D Realms'),
        (3, 'Saber Interactive'),
        (4, 'Overkill Software'),
        (5, 'Dennaton Games'),
        (6, 'RobTop Games'),
        (7, '3DIVISION'),
        (8, 'Studio MDHR'),
        (9, 'Tarsier Studios'),
        (10, 'Team Cherry')
    ]
    
    for id, name in developers_data:
        Developer.objects.create(id=id, Developers_name=name)
    
    print("Разработчики созданы")
    
    publishers_data = [
        (1, '505 Games'),
        (2, 'Focus Entertainment'),
        (3, 'Starbeeze Publishing AB'),
        (4, 'Devolver Digital'),
        (5, 'RobTop Games'),
        (6, 'Mauris Games OU'),
        (7, 'Studio MDHR Entertainment Inc.'),
        (8, 'BANDAI NAMCO Entertainment'),
        (9, 'Team Cherry'),
        (10, 'Coffee Stain Publishing')
    ]
    
    for id, name in publishers_data:
        Publisher.objects.create(id=id, Publishers_name=name)
    
    print("Издатели созданы")
    
    tags_data = [
        (1, 'Киборг'),
        (2, 'От третьего лица'),
        (3, 'Жестокий'),
        (4, 'Кооператив'),
        (5, 'Ретро'),
        (6, 'Ритм'),
        (7, 'Открытый мир'),
        (8, 'Сложный'),
        (9, 'Хоррор'),
        (10, 'Метроидвания')
    ]
    
    for id, name in tags_data:
        Tags.objects.create(id=id, Tag_name=name)
    
    print("Теги созданы")
    
    localizations_data = [
        (1, 'Полная'),
        (2, 'Отсутствует')
    ]
    
    for id, name in localizations_data:
        Localization.objects.create(id=id, Voice=name)
    
    print("Локализации созданы")
    
    games_data = [
        (1, 'Ghostrunner', 1, 1, 1, 1, 1),
        (2, 'Warhammer 40.000: Space Marine 2', 2, 2, 2, 2, 2),
        (3, 'PAYDAY 2', 3, 3, 3, 3, 1),
        (4, 'Hotline Miami', 4, 4, 4, 4, 1),
        (5, 'Geometry Dash', 5, 5, 5, 5, 2),
        (6, 'Corsair Legacy - Pirate Action RPG & Sea Battles', 6, 6, 6, 6, 1),
        (7, 'Cuphead', 7, 7, 7, 7, 2),
        (8, 'Little Nightmares II', 8, 8, 8, 8, 2),
        (9, 'Hollow Knight', 9, 9, 9, 9, 2),
        (10, 'Deep Rock Galactic', 10, 10, 10, 10, 1)
    ]
    
    for id, name, genre_id, developer_id, publisher_id, tag_id, localization_id in games_data:
        Games.objects.create(
            id=id,
            Name_game=name,
            genre=Genre.objects.get(id=genre_id),
            developer=Developer.objects.get(id=developer_id),
            publisher=Publisher.objects.get(id=publisher_id),
            tags=Tags.objects.get(id=tag_id),
            localization=Localization.objects.get(id=localization_id)
        )
    
    print("Игры созданы")
    print("База данных успешно заполнена!")

if __name__ == '__main__':
    populate_database()