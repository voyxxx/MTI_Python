from bot_token import TOKEN
import requests

lat, lon = 45, 39

weathers = {
    'ясно': '☀️',
    'пасмурно': '☁️',
    'дождь': '🌧️',
    'снег': '🌨️',
    'гроза': '🌧️',
    'переменная облачность': '⛅️',
    'облачно с прояснениями': '⛅️',
    'небольшая облачность': '⛅️',
    'переменная облачность': '⛅️',
    'пасмурно с прояснениями': '🌧️',
    'пасмурно с грозой': '🌧️',
    'небольшая облачность': '⛅️',
    'переменная облачность': '⛅️',
    'небольшой дождь': '🌧️',
    'небольшой дождь с прояснениями': '🌧️',
    'небольшой дождь с грозой': '🌧️',
    'дождь': '🌧️',
    'дождь с прояснениями': '🌧️',
    'дождь с грозой': '🌧️',
    'сильный дождь': '🌧️',
    'сильный дождь с прояснениями': '🌧️',
    'сильный дождь с грозой': '🌧️',
    'сильный дождь с грозой': '🌧️',
    'сильный дождь с грозой и сильный ветер': '🌧️',
    'сильный дождь с грозой и сильный ветер': '🌧️',
    'сильный дождь с грозой и сильный ветер': '🌧️',
}

weather_codes = {
    0: 'Ясное небо',
    1: 'Преимущественно ясно',
    2: 'Переменная облачность',
    3: 'Пасмурно',
    45: 'Туман и налипающий иней',
    48: 'Туман и налипающий иней',
    51: 'Лёгкая морось',
    53: 'Умеренная морось',
    55: 'Морось: плотная интенсивность',
    56: 'Лёгкий моросящий дождь',
    57: 'Моросящий дождь интенсивной плотности',
    61: 'Слабый дождь',
    63: 'Умеренный дождь',
    65: 'Сильный дождь',
    66: 'Небольшой ледяной дождь',
    67: 'Обильный ледяной дождь',
    71: 'Небольшой снегопад: , умеренный и обильный по интенсивности',
    73: 'Умеренный снегопад',
    75: 'Обильный снегопад',
    77: 'Крупинки снега',
    80: 'Слабые ливни: , умеренные и сильные',
    81: 'Умеренные ливни',
    82: 'Сильные ливни',
    85: 'Легкие снегопады',
    86: 'Сильные снегопады',
    95: 'Гроза',
    96: 'Гроза с небольшим  градом',
    99: 'Гроза с сильным градом',
}

def get_wind_direction(wind_direction):
    remainder = wind_direction % 45
    correction = 0 if remainder < 22.5 else 1
    wind_dirs = ['С ⬆', 'СВ ↗', 'В ➡', 'ЮВ ↘', 'Ю ⬇', 'ЮЗ ↙', 'З ⬅', 'СЗ ↖']
    wind_dir_index = wind_direction % 360 // 45 + correction
    index = 0 if wind_dir_index == len(wind_dirs) else wind_dir_index
    wind_dir_index = wind_dirs[index]

    return wind_dir_index

def get_url(lat, lon):
    return f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,wind_speed_10m,wind_direction_10m,wind_gusts_10m&daily=weather_code&wind_speed_unit=ms&timezone=Europe%2FMoscow&forecast_days=1'

def get_weather(lat, lon):
    url = get_url(lat, lon)
    weather = requests.get(url).json()
    WC = weather['current']
    text = ''
    text += f'Тип погоды: {weather_codes[weather["daily"]["weather_code"][0]]}\n'
    text += f'🌡️  Температура ВОЗДУХА: {WC["temperature_2m"]}℃\n'
    text += f'💧 Относительная влажность: {WC["relative_humidity_2m"]}%\n'
    text += f'Ощущаемая температура: {WC["apparent_temperature"]}℃\n'
    if WC['precipitation'] == 0:
        text +='Нет осадков\n'
    else:
        if WC['rain'] != 0:
            text += f'🌧️ Дождь: {WC["rain"]} мм\n'
        if WC['showers'] != 0:
            text +=f'Ливень: {WC["showers"]} мм\n'
        if WC['snowfall'] != 0:
            text += f'❄️ Снег: {WC["snowfall"]} см\n'

    text += f'🍃 Скорость ветра: {WC["wind_speed_10m"]} м/с\n'
    
    text += f'Направление ветра: {get_wind_direction(WC["wind_direction_10m"])}\n'
    text += f'🌪️  Порывы ветра: {WC['wind_gusts_10m']} м/с\n'

    return text







# print(get_weather(lat, lon))

""" 
print(f'Температура: {weather["temperature_2m"]}℃')
print(f'Относительная влажность: {weather["relative_humidity_2m"]}%')
print(f'Ощущаемая температура: {weather["apparent_temperature"]}℃') 
"""
""" 
if weather['precipitation'] == 0:
    print('Нет осадков')
else:
    if weather['rain'] != 0:
        print(f'Дождь: {weather["rain"]} мм')
    if weather['showers'] != 0:
        print(f'Ливень: {weather["showers"]} мм')
    if weather['snowfall'] != 0:
        print(f'Снег: {weather["snowfall"]} см')

print(f'Скорость ветра: {weather["wind_speed_10m"]} м/с')


wind_dirs = ['С', 'СВ', 'В', 'ЮВ', 'Ю', 'ЮЗ', 'З', 'СЗ']
wind_dir = wind_dirs[weather['wind_direction_10m'] % 360 // 45]
remainder = weather['wind_direction_10m'] % 45
correction = remainder
print('направление ветра 45 - ', weather['wind_direction_10m'] // 45, 'остаток', remainder)
print(f'Направление ветра: {wind_dir}')
print(f'Порывы ветра: {weather['wind_gusts_10m']} м/с') 
"""
