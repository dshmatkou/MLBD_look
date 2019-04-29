![Alt text](onion.jpg?raw=true "Look")

# Запуск:
```
docker build --tag web:latest .
docker run -p 8000:8000 --name webserver web:latest
```

Далее в браузере с адресом `<your docker host>:8000`.
Загрузить фотографию. 
Оценить результат.


# Проделанная работа
Дмитрий Шматков:
* Заимплементил индекс и алгоритм поиска k-nearest-neighbours в графе Small World.
* Сделал скелет приложения

Волчков Константин:
* Реализовал front-end часть проекта. 
* Написал API.

Жиркевич Анастасия:
* Создала модель с использованием нейронной сети для конвертации изображения в вектор.
* Законвертила исходные данные с помощью модели, создала кэш для индекса.

# Dataset
[CelebrA](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html)
