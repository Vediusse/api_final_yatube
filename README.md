## Yatube API

API для работы с проектом yatube.
## Установка
#### **Требуется Python 3.7**
Чтобы перед началом работы выполните эту команду:
```
# Linux/macOS
python -m pip install -r requirements.txt

# Windows
py -m pip install -r requirements.txt
```


Для запуска, вы должны выполнить следующую команду:
```
# Linux/macOS
python yatube_api/manage.py

# Windows
py yatube_api/manage.py
```
## Использование

### Получаем jwt токен 
 Отправляем POST запрос на адрес  api/v1/token/  с полями 
```     
    1) username - указываем имя пользователя
    2) password - указываем пароль
```
Получаем два поля 
```
     1) Токен refresh нужен, чтобы обновить текущий токен.
     2) Токен access сам токен(срок действия по умолчанию 1 день)
```
### Выполнение запросов
     1) При выполнение запросов в заголовке указываем Authorization:Bearer <токен>
     2) Все запросы описаны по адресу http://localhost:8000/redoc/

## Технологии
###### 1) Django
###### 2) djangorestframework
###### 3) djangorestframework-simplejwt


## Об авторе
Трудяга из Yandex.practicum
