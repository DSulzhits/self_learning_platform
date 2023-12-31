Платформа самообучения включает в себя раздел Секции (Sections) (в данном примере различные виды животных), и
Содержимое (Content) (виды животных). Проект можно запустить как в Docker, так и на локальной машине (по умолчанию
настройки для запуска на локальной машине), для запуска тестов настройки должны быть LOCAL

Виртуальное окружение используемое для проекта: venv

1) После настройки виртуального окружения установите зависимости из файла requirements.txt

```bash
pip install -r requirements.txt
```

2) Заполните файл .env file согласно файла .env.sample

ДЛЯ ЗАПУСКА НА ЛОКАЛЬНОЙ МАШИНЕ

3) Измените настройки базы данных в файле config\settings.py с настроек с пометкой #DOCKER, на настройки с пометкой
   #LOCAL

4) Создайте Базу данных при помощи команды

```bash
python manage.py ccdb
```

5) Создайте миграции при помощи команды

```bash
python manage.py makemigrations
```

6) Примените созданные миграции

```bash
python manage.py migrate
```

7) Выполните команду для создания пользователей

```bash
python manage.py ccsu
```

8) Выполните команду для заполнения базы данных используя фикстуры

```bash
python manage.py loaddata sections.json
```

9) Выполните команду для запуска приложения

```bash
python manage.py runserver
```

10) Если вы хотите запустить тесты используйте команду
```bash
coverage run --source='.' manage.py test 
```

ДЛЯ ЗАПУСКА В DOCKER

3) Запустите проект при помощи команды

```bash
docker-compose up -d --build
```

Модели используемые в проекте

Section с полями:

- title - название секции
- description - описание секции (может быть пустым)

Content с полями:

- section - отношение к секции
- title - название содержимого
- content - содержимое

Tests с полями:

- test_section - отношение к секции
- description - описание теста
- question - вопрос теста
- answer - верный ответ

User с полями:

- email - электронная почта пользователя
- role - роль пользователя (MEMBER or MODERATOR)
- first_name - имя пользователя (может быть пустым)
- last_name - фамилия пользователя (может быть пустым)
- phone - телефон пользователя (может быть пустым)
- is_active - признак активности пользователя по умолчанию True

Разрешения (Permissions)

- Реализованы кастомные разрешения для пользователя с ролью MODERATOR
- Смотреть список секций и список содержимого могут все авторизованные пользователи
- Смотреть подробную информацию о секции и контенте могут все авторизованные пользователи
- Создавать, Изменять, Удалять секцию или содержимое могут Администратор или Модератор
- Список пользователей могут видеть Администратор или Модератор
- Регистрироваться на ресурсе может любой пользователь
- Видеть подробную информацию о пользователе могут все авторизованные пользователи
- Изменять информацию о пользователе может только сам пользователь
- Удалять пользователя может только Администратор

Пагинация

- Реализована пагинация для списка секций (3 элемента на страницу) и для списка содержимого (10 элементов на страницу)

Эндпоинты модели Section (Секция)

- List of Sections (Список Секций)
- Create a new Section (Создание Секции)
- Detail info about Section (Подробная информация о Секции)
- Update the Section (Обновить/Изменить Секцию)
- Delete the Section (Удалить Секцию)

Эндпоинты модели Content (Содержимое)

- List of Сontent (Список Содержимого)
- Create a new Сontent (Создать Содержимое)
- Detail info about Сontent (Подробная информация о Содержимом)
- Update the Сontent (Обновить/Изменить Содержимое)
- Delete the Сontent (Удалить Содержимое)

Эндпоинты модели Tests (Тесты)

- List of Tests (Список Тестов)
- Retrieve question/Give an answer (Получение теста/Отправка ответа)

Эндпоинты модели User (Пользователь)

- List of Users (Список Пользователей)
- Create a new User (Создать Пользователя)
- Detail info about User (Подробная информация о Пользователе)
- Update the User (Обновить/Изменить Пользователя)
- Delete the User (Удалить Пользователя)

Документация

- Документацию по проекту можно увидеть здесь:

```bash
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/redoc/
```