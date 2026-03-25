from django.db.models import Count
from .models import Games, Genre, Developer, Publisher, Tags, Localization
import random

def fetch_games_by_filter(filter_type, value):
    try:
        games = Games.objects.all()

        if filter_type == 'genre':
            games = Games.objects.filter(genre__Genre_name=value)
        elif filter_type == 'developer':
            games = Games.objects.filter(developer__Developers_name=value)
        elif filter_type == 'publisher':
            games = Games.objects.filter(publisher__Publishers_name=value)
        elif filter_type == 'tags':
            games = Games.objects.filter(tags__Tag_name=value)
        elif filter_type == 'localization':
            games = Games.objects.filter(localization__Voice=value)
        else:
            return []
        
        return [game.Name_game for game in games]
    except Exception as e:
        print(f"Ошибка при поиске игр: {e}")
        return []

def get_random_game() -> str:
    try:
        count = Games.objects.count()
        if count == 0:
            return "Не нашел"
        
        random_index = random.randint(0, count - 1)
        random_game = Games.objects.all()[random_index]
        return random_game.Name_game
        
    except Exception as e:
        print(f"Ошибка: {e}")
        return "Ошибка при получении игры"

def count_games() -> int:
    try:
        return Games.objects.count()
    except Exception as e:
        print(f"Ошибка: {e}")
        return 0

def add_game_bd(game_data: dict) -> str:
    try:
        name = game_data['name']
        genre = game_data['genre']
        developer = game_data['developer']
        publisher = game_data['publisher']
        tags = game_data['tags']
        localization = game_data['localization']

        if Games.objects.filter(Name_game=name).exists():
            return "Уже есть в бд"

        genre_obj, _ = Genre.objects.get_or_create(Genre_name=genre)
        developer_obj, _ = Developer.objects.get_or_create(Developers_name=developer)
        publisher_obj, _ = Publisher.objects.get_or_create(Publishers_name=publisher)
        tags_obj, _ = Tags.objects.get_or_create(Tag_name=tags)
        localization_obj, _ = Localization.objects.get_or_create(Voice=localization)

        Games.objects.create(
            Name_game=name,
            genre=genre_obj,
            developer=developer_obj,
            publisher=publisher_obj,
            tags=tags_obj,
            localization=localization_obj
        )

        return f"Игра '{name}' добавлена в бд"
        
    except Exception as e:
        return f"Ошибка при добавлении игры: {str(e)}"
