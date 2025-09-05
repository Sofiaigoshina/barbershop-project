class Client:
    """Класс для представления клиента парикмахерской"""

    def __init__(self, last_name: str, first_name: str, middle_name: str = "", total_visits: int = 0):
        # Проверяем и сохраняем данные
        self._last_name = self._validate_name(last_name, "Фамилия")
        self._first_name = self._validate_name(first_name, "Имя")
        self._middle_name = self._validate_name(middle_name, "Отчество", False)
        self._total_visits = self._validate_visits(total_visits)

    # Метод для проверки имени
    @staticmethod
    def _validate_name(name: str, field_name: str, required: bool = True) -> str:
        if not name and required:
            raise ValueError(f"{field_name} не может быть пустым")
        if name and not name.replace(" ", "").isalpha():
            raise ValueError(f"{field_name} должна содержать только буквы")
        return name.strip()

    # Метод для проверки количества посещений
    @staticmethod
    def _validate_visits(visits: int) -> int:
        if visits < 0:
            raise ValueError("Количество посещений не может быть отрицательным")
        return visits

    # Геттеры (получение данных)
    @property
    def last_name(self) -> str:
        return self._last_name

    @property
    def first_name(self) -> str:
        return self._first_name

    @property
    def middle_name(self) -> str:
        return self._middle_name

    @property
    def total_visits(self) -> int:
        return self._total_visits

    # Сеттеры (изменение данных)
    @last_name.setter
    def last_name(self, value: str):
        self._last_name = self._validate_name(value, "Фамилия")

    @first_name.setter
    def first_name(self, value: str):
        self._first_name = self._validate_name(value, "Имя")

    @middle_name.setter
    def middle_name(self, value: str):
        self._middle_name = self._validate_name(value, "Отчество", False)

    @total_visits.setter
    def total_visits(self, value: int):
        self._total_visits = self._validate_visits(value)

    # Вывод информации
    def __str__(self) -> str:
        return f"Клиент: {self.last_name} {self.first_name} {self.middle_name}, посещений: {self.total_visits}"

    def short_info(self) -> str:
        initials = f"{self.first_name[0]}.{self.middle_name[0]}. " if self.middle_name else f"{self.first_name[0]}."
        return f"{self.last_name} {initials}"


# Проверка работы
if __name__ == "__main__":
    try:
        # Создаем клиента
        client = Client("Иванов", "Иван", "Иванович", 5)
        print("Полная информация:", client)
        print("Краткая информация:", client.short_info())

        # Пробуем создать клиента с ошибкой
        bad_client = Client("", "Мария")  # Это вызовет ошибку!

    except ValueError as e:
        print(f"Ошибка: {e}")