from animal import DomesticAnimal, PackAnimal

animals_registry = []

def add_animal(counter):
    name = input("Введите имя животного: ")
    birth_date = input("Введите дату рождения животного (YYYY-MM-DD): ")
    animal_type = input("Какое животное? (1 - Домашнее, 2 - Вьючное): ")

    if animal_type == '1':
        new_animal = DomesticAnimal(name, birth_date)
    elif animal_type == '2':
        new_animal = PackAnimal(name, birth_date)
    else:
        print("Неверный тип животного!")
        return

    animals_registry.append(new_animal)
    counter.add()
    print(f"Животное {name} добавлено в реестр!")

def view_commands(animal):
    print(f"Команды, которые выполняет {animal.get_name()}: {', '.join(animal.get_commands())}")

def train_animal(animal):
    new_command = input(f"Введите новую команду для {animal.get_name()}: ")
    animal.add_command(new_command)
    print(f"Животное {animal.get_name()} обучено новой команде: {new_command}")

def show_animals():
    if not animals_registry:
        print("Реестр пуст!")
    else:
        print("Список животных:")
        for animal in animals_registry:
            print(f"Имя: {animal.get_name()}, Дата рождения: {animal.get_birth_date()}")
def find_animal_by_name(name):
    return next((a for a in animals_registry if a.get_name().lower() == name.lower()), None)
