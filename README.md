# Тестовое задание для WelbeX

Реализован "Уровень 2" тестового задания.
Стек: FastAPI, SQLAlchemy, PostgreSQL, dependency_injector

Приложение запускается на порте 8000 простой командой
<br>
```docker-compose up```
<br>
При запуске база данных заполняется локациями из предоставленного csv файла 
## Реализовано согласно заданию
CRUD для Груза `/shipments`
<br>
Создание, редактирование транспорта `/transports`
<br>
Фильтр списка грузов (вес, мили ближайших машин до грузов)
<br>
Автоматическое обновление локаций всех машин раз в 3 минуты (локация меняется на другую случайную)

Структура проекта реализована руководствуясь Clean Architecture
## Документация
Полную документацию можно найти в файле openapi.json
<br>
Также в ендпоинте `/docs` после запуска можно открыть Swagger документацию и опробовать на лету
