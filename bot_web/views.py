from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .core import *

def main(request):
    return render(request, 'bot_web/main.html')

@csrf_exempt
def messages(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message_type = data.get('type')
            value = data.get('value')

            response_data = {}

            if message_type == 'random_game':
                game = get_random_game()
                response_data = {'response': f"Рандомная игра: {game}"}

            elif message_type == 'count_games':
                count = count_games()
                response_data = {'response': f"Всего игр: {count}"}

            elif message_type in ['genre', 'developer', 'publisher', 'tags', 'localization']:
                games = fetch_games_by_filter(message_type, value)
                if games:
                    result = "\n".join(games)
                    response_data = {'response': f"Найденные игры:\n{result}"}
                else:
                    response_data = {'response': "Игры не найдены"}
            elif message_type == 'add_game':
                result = add_game_bd(value)
                response_data = {'response': result}
            else:
                response_data = {'response': "Неизвестный запрос"}

            return JsonResponse(response_data)
        
        except Exception as e:
            return JsonResponse({'response': f"Ошибка: {str(e)}"})
        
    return JsonResponse({'response': "Нельзя"})
            
    
