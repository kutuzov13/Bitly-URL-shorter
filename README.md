## Bitly URL shorter

Этот скрипт для сокращения ссылок с помощью сервиса ***[Bitly](https://bitly.com/)***.

Если передать скрипту уже сокращенную ссылку, вы получите количество переходов по ссылке.

### Как установить
Для запуска скрипта вам понадобиться Python 3-ей версии!

Клонируйте репозиторий с GitHub.
```
git clone https://github.com/kutuzov13/Bitly-URL-shorter.git
```
Установите зависимости.
```cmd
pip install -r requirements.txt
```
### Библиотеки
```python
# для запросов к Api Bitly.
import requests 
# для обращения к переменным окружения.
from dotenv import load_dotenv 
```
### Переменные окружения
Токен берется из переменных окружения.
- Создайте файл ```.env``` рядом с ```main.py```.
- Запишите токен в файл ```.env```: ```BITLINK_TOKEN='YOU_TOKEN'```.

Токен для обращения к Api Bitly. Можно получить в личном кабинете ***[Bitly](https://bitly.com/)***.

### Запуск
Запустите скрипт передав ссылку:
```
python main.py https://github.com/
```
Или
```
python main.py https://bit.ly/3bcdiFH -> (Укороченная ссылка)
```

#### Цели проекта
Код написан в учебных целях на онлайн-курсе для веб-разработчиков ***[dvmn.org](https://dvmn.org/modules/)***.
