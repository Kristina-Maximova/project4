# Financial transactions widget

## *Краткое описание проекта*

Проект содержит некоторые функции, полезные при проведении банковских операций.

## *Установка и использование*

+ клонируйте репозиторий: [GitHub](https://github.com/Kristina-Maximova/project4.git)
+ установите зависимости: 
  - python = "^3.13"
  - requests = "^2.32.3"
  - pandas = "^2.2.3"
  - openpyxl = "^3.1.5"

## *Примеры использования*

используются данные из .json, либо .csv, либо .xlsx файлов в формате:
```commandline
[
{'id': 2177828.0, 'state': 'EXECUTED', 'date': '2022-04-14T15:14:21Z', 'amount': 24853.0, 'currency_name': 'Yuan Renminbi', 'currency_code': 'CNY', 'from': 'Счет 38577962752140632721', 'to': 'Счет 47657753885349826314', 'description': 'Перевод со счета на счет'}, 
{'id': 4137938.0, 'state': 'EXECUTED', 'date': '2023-01-04T13:13:34Z', 'amount': 15560.0, 'currency_name': 'Real', 'currency_code': 'BRL', 'from': nan, 'to': 'Счет 38164279390569873521', 'description': 'Открытие вклада'},
{'id': 4699552.0, 'state': 'EXECUTED', 'date': '2022-03-23T08:29:37Z', 'amount': 23423.0, 'currency_name': 'Peso', 'currency_code': 'PHP', 'from': 'Discover 7269000803370165', 'to': 'American Express 1963030970727681', 'description': 'Перевод с карты на карту'}
 ]
```
>for card_number in card_number_generator(1, 5):
    print(card_number)
>>0000 0000 0000 0001
> 
>>0000 0000 0000 0002
 
## *Тестирование*

+ Проводится на базе фреймворка  **` pytest `**
+ Целевое покрытие кода тестами: не менее 80%.



## *Лицензия*

тут информация будет позже