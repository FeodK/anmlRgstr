from registry import add_animal, view_commands, train_animal, show_animals, find_animal_by_name
from animal import DomesticAnimal, PackAnimal

animals_registry = []

def menu(counter):
    while True:
        print("\nМеню:")
        print("1. Завести новое животное")
        print("2. Смотреть команды животного")
        print("3. Обучить животное новой команде")
        print("4. Показать список животных")
        print("5. Выход")
        choice = input("Выберите опцию: ")

        if choice == '1':
            try:
                add_animal(counter)
            except ValueError as e:
                print(f"Ошибка: {e}")
        elif choice == '2':
            name = input("Введите имя животного для просмотра команд: ")
            animal = find_animal_by_name(name)
            if animal:
                view_commands(animal)
            else:
                print(f"Животное с именем {name} не найдено.")
        elif choice == '3':
            name = input("Введите имя животного для обучения: ")
            animal = find_animal_by_name(name)
            if animal:
                train_animal(animal)
            else:
                print(f"Животное с именем {name} не найдено.")
        elif choice == '4':
            show_animals()
            print(f"Количество заведенных животных: {counter.get_count()}") 
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")
