# locallibrary

## Добро пожаловать!

### Установка проекта

```
1. Склонируйте репозиторий: 
    
    git clone https://github.com/Zavodsk0y/locallibrary -b locallibrary-branch-1
   
2. Перейдите в директорию проекта

    cd .../locallibrary
    
3. Установите необходимые зависимости из файла requirements.txt

    pip install -r requirements.txt
```

#### Поздравляю, проект установлен и готов к работе!

### Работа с проектом

#### Примечание:

В проект уже вшита база данных Sqlite с некоторыми данными, а также присутствуют миграции. Потому вам ничего не нужно
будет с ними делать.

#### Структура проекта

```
    README.md
    requirements.txt
    locallibrary\
        catalog\  -- папка приложения
            migrations\   -- папка с миграциями базы данных
                0001_initial.py
                0002_bookinstance_borrower_alter_bookinstance_status.py
                0003_alter_bookinstance_options.py
                __init.py__
            static\
                css\
                    styles.css
            templates\  -- папка с шаблонами приложения
                catalog\  -- подраздел "каталог" 
                    html.files.....
                registration\ -- подраздел "регистрация" для работы с пользователем
                    html.files.....
            tests\  -- тесты проекта
                __init.py__
                test_forms.py
                test_models.py
                test_views.py
            __init.py__
            admin.py
            apps.py
            forms.py
            models.py
            urls.py
            views.py
        locallibrary\ -- 
            __init.py__
            asgi.py
            settings.py
            urls.py
            wsgi.py
        db.sqlite3
        manage.py
            
```

#### Запуск проекта

```
1. Перейдите в корневую папку проекта Django

2. Впишите в терминал следующую команду для запуска сервера:

    python manage.py runserver
    
3. Далее вы можете перейти по адресу, на котором запустился сервер в браузере

4. На сайте реализована базовая навигация, но рекомендуется ознакомиться с файлом urls.py приложения,
    если вы хотите ознакомиться с полным функционалом проекта
```

Примечание: логин/пароль для входа в админку: 

admin/admin

#### Тестрование проекта

В проекте также присутствует настроенные тесты, которые вы можете 
    запустить командой 

```
python manage.py test
```

### Автор

Работу выполнил студент Петренко Константин, 421 группа



