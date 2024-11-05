class Counter:
    def __init__(self):
        self._count = 0
        self._is_open = False 

    def add(self):
        self._count += 1

    def get_count(self):
        return self._count

    def __enter__(self):
        if self._is_open:
            raise RuntimeError("Ресурс уже открыт!")
        self._is_open = True
        print("Открытие ресурса счетчика...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if not self._is_open:
            raise RuntimeError("Ресурс не был открыт!")
        self._is_open = False
        if exc_type is None:
            print(f"Закрытие ресурса счетчика. Текущее количество животных: {self._count}")
        else:
            print(f"Произошла ошибка: {exc_val}")
            raise exc_type(exc_val)

    def is_resource_open(self):
        return self._is_open
