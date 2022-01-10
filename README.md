# test-oceanstart
Реализовать выдачу данных в формате json по RESTful, используя Django.
Результат представить ссылкой на репозиторий.
> Важно, в репозиторий залить пустой каркас приложения, а затем с внесенными изменениями, чтобы можно было проследить diff.


### Сущности:
1. Товар (у товара от 2 до 10 категорий, если меньше 2, товар помечатеся как неопубликованный, если больше 10, товар не создается, пользователь получает ошибку)
2. Категория
3. Товар-Категория (m2m)

### Функционал API:
1. Создание / редактирование Товаров 
2. Удаление Товаров (помечатеся как удаленный)
3. Создание / редактирование Категорий 
4. Удаление Категорий (вернуть ошибку если категория связана с одним из товаров)
5. Фильтрация товаров по: 
    - имя
    - имя категории
    - id категории
    - цена, от-до
    - Опубликованные, да / нет
    - Удаленные, да / нет

### Тесты
По желанию протестировать ключевой функционал API

## Запуск
```bash
poetry install or pip install -r requirements.txt
```

```bash
poetry shell
python manage.py migrate
python manage.py runserver or test
```

**Endpoints**  
`/products` -- GET, POST, PUT, PATCH, DELETE  
`/categories` -- GET, POST, PUT, PATCH, DELETE


**Filters**  
`products?name=` -- by name  
`products?is_published=` -- False / True  
`products?is_removed=` -- False / True  
`products?price=` -- by price  
`products?price_gt=100&price_lt=1000` -- price range  
`products?categories__name=` -- category name  
`products?categories__id=` -- category id  


