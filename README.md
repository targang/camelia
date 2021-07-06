# Интернет магазин Camelia Flowers

## Установка

### Сборка фронтенда

1. Переходим в каталог app/frontend
2. Устанавливаем зависимости `npm install`
3. Собираем билд `npm run build`

### Запуск магазина

1. Из корневого каталога создаем virtualenv `python -m venv env`
2. Активируем virtualenv `env/scripts/activate` или `source env/bin/activate`
3. Устанавливаем зависимости `pip install -r requirements.txt`
4. Запускаем магазин `flask run`