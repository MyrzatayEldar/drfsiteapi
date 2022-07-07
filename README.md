# Тестовое задание.
## Задание 1. 
____
Для установки:

1. Скачать **исходный** файл
2. Открыть папку в *командной строке*, активировать виртуальное окружение:
    > venv\Scripts\Activate

3. Установить нужные библиотеки:
    > pip install -r requirements.txt
4. Зайти в папку catalog:
    > cd catalog
5. Сделать миграции:
    > python manage.py migrate
6. Запустить тестовый веб-сервер для просмотра работы api.
    > python manage.py runserver


Не смог решить задачу с помощью Postgres, возникли проблемы с переносом данных из SQLite.

## Задание 2.
____
1. Для создания базы данных с помощью миграции, используются следующие команды:
    > python manage.py makemigrations

    > python manage.py migrate
2. При использовании DB seeder для заполнения 50к сотрудников в первом задании у меня не слабо завис компьютер. Как я сделал? Сперва установил: 
    > pip install django-seed

    Далее добавил эту библиотеку в список установленных приложении в settings.py
    ```python
    INSTALLED_APPS = [
    #############
    'django_seed',
    ]
    ```
    А далее заполнение с помощью одной команды:    
    > python manage.py seed employee --number=50000

    Тут указывается название приложения, модели которых нужно будет заполнить данными, а также количество записей. В нашем случае это 50000.
3. не совсем понял, в чем суть.
4. Для поиска по всем полям, я в админ панели зарегистрировал следующее:
    ```python
    class EmployeeAdmin(admin.ModelAdmin):
        list_display = ('fullname', 'post', 'hiring_date', 'salary', )
        list_filter = ('hiring_date', )
        search_fields = ('fullname', 'post', 'hiring_date', 'salary', ) #поля, по которым идет поиск 
    ```
5. Возможность сортировки изначально имеется.
6. С аутентификацией пользователей можно ознакомиться в файлах: login.html, views/login_view, forms/LoginForm

Superuser: **login: user**; ***password: 12345*** 

Спасибо!