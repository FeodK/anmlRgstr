## Задание 1:

1. **Создание файла с домашними животными:**

   **_Команда:_**

   ```bash
   cat > Домашние_животные.txt
   ```

   **_Ввод данных:_**

   ```
    Собаки
    Кошки
    Хомяки
   ```

2. **Создание файла с вьючными животными:**

   **_Команда:_**

   ```bash
   cat > Вьючные_животные.txt
   ```

   **_Ввод данных:_**

   ```
    Лошади
    Верблюды
    Ослы
   ```

3. **Объединение файлов:**

   **_Команда:_**

   ```bash
   cat Домашние_животные.txt Вьючные_животные.txt > Друзья_человека.txt
   ```

4. **Просмотр содержимого созданного файла:**

   **_Команда:_**

   ```bash
   cat Друзья_человека.txt
   ```

5. **Переименование файла:**

   **_Команда:_**

   ```bash
   mv Друзья_человека.txt Друзья_человека_новое_имя.txt
   ```

## Задание 2:

1. **Создание директории и перемещение файла:**

   **_Команды:_**

   ```bash
   mkdir Друзья_человека
   mv Друзья_человека_новое_имя.txt Друзья_человека/
   ```

## Задание 3:

1.  **Подключение дополнительного репозитория MySQL и установка пакета:**

    **_Команды:_**

    ```bash
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository 'deb http://repo.mysql.com/apt/ubuntu/ focal mysql-8.0'
    sudo apt update
    sudo apt install mysql-server
    ```

## Задание 4:

1.  **Установка и удаление .deb пакета с помощью dpkg:**

    **_Команды:_**

    ```bash
    wget http://archive.ubuntu.com/ubuntu/pool/main/d/dpkg/dpkg_1.19.7_amd64.deb
    sudo dpkg -i dpkg_1.19.7_amd64.deb
    sudo dpkg -r dpkg
    ```

## Задание 5:
1. **Выложить историю команд:**

   **_Команда:_**

   ```bash
   history > история_команд.txt
   ```

## Задание 6:
 **_Диаграмма:_**

   ```
          Животные
          /       \
   Домашние        Вьючные
    /    |    \        /   |   \
Собаки Кошки Хомяки Лошади Верблюды Ослы
   ```
* Класс "Животные" является родительским.
* Класс "Домашние животные" включает "Собак", "Кошек" и "Хомяков".
* Класс "Вьючные животные" включает "Лошадей", "Верблюдов" и "Ослы".