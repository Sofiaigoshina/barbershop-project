class ShortClient:
    """
    Класс для краткого представления клиента.
    Содержит только основную информацию: ФИО и ID.
    """

    def __init__(self, client_id: int, last_name: str, first_name: str, patronymic: str = None):
        """
        Инициализирует объект краткого представления клиента.
        """
        # Валидация обязательных полей
        self._validate_positive_int(client_id, "ID клиента")
        self._validate_required_string(last_name, "Фамилия", min_length=2)
        self._validate_required_string(first_name, "Имя", min_length=2)
        self._validate_optional_string(patronymic, "Отчество")

        # Приватные поля
        self.__client_id = client_id
        self.__last_name = last_name.strip()
        self.__first_name = first_name.strip()
        self.__patronymic = patronymic.strip() if patronymic else None

    # СТАТИЧЕСКИЕ МЕТОДЫ ВАЛИДАЦИИ

    @staticmethod
    def _validate_positive_int(value: int, field_name: str):
        """Проверяет положительное целое число."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{field_name} должен быть положительным целым числом")

    @staticmethod
    def _validate_required_string(value: str, field_name: str, min_length: int = 1):
        """Проверяет обязательные строковые поля."""
        if not value or not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} не может быть пустой")
        if len(value.strip()) < min_length:
            raise ValueError(f"{field_name} должна содержать минимум {min_length} символов")

    @staticmethod
    def _validate_optional_string(value: str, field_name: str):
        """Проверяет опциональные строковые поля."""
        if value is not None:
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{field_name} не может быть пустой")

    # СВОЙСТВА (геттеры)

    @property
    def client_id(self) -> int:
        """Возвращает ID клиента."""
        return self.__client_id

    @property
    def last_name(self) -> str:
        """Возвращает фамилию клиента."""
        return self.__last_name

    @property
    def first_name(self) -> str:
        """Возвращает имя клиента."""
        return self.__first_name

    @property
    def patronymic(self) -> str:
        """Возвращает отчество клиента."""
        return self.__patronymic

    # МЕТОДЫ ПРЕОБРАЗОВАНИЯ

    def get_initials(self) -> str:
        """
        Возвращает инициалы клиента.
        """
        first_initial = self.first_name[0] + '.' if self.first_name else ''
        patronymic_initial = self.patronymic[0] + '.' if self.patronymic else ''
        return f"{first_initial}{patronymic_initial}"

    def get_full_name_with_initials(self) -> str:
        """
        Возвращает полное имя с инициалами.
        """
        initials = self.get_initials()
        return f"{self.last_name} {initials}"

    def get_full_name(self) -> str:
        """
        Возвращает полное ФИО клиента.
        """
        if self.patronymic:
            return f"{self.last_name} {self.first_name} {self.patronymic}"
        else:
            return f"{self.last_name} {self.first_name}"

    # МЕТОДЫ ВЫВОДА И СРАВНЕНИЯ

    def __str__(self) -> str:
        """Краткое строковое представление."""
        return self.get_full_name_with_initials()

    def __repr__(self) -> str:
        """Формальное строковое представление."""
        return (f"ShortClient(client_id={self.client_id}, "
                f"last_name='{self.last_name}', first_name='{self.first_name}')")

    def __eq__(self, other) -> bool:
        """Сравнивает два объекта ShortClient на равенство."""
        if not isinstance(other, ShortClient):
            return False

        return (self.client_id == other.client_id and
                self.last_name == other.last_name and
                self.first_name == other.first_name and
                self.patronymic == other.patronymic)

    def __hash__(self) -> int:
        """Возвращает хеш-значение объекта."""
        return hash((self.client_id, self.last_name, self.first_name, self.patronymic))

    # АЛЬТЕРНАТИВНЫЕ КОНСТРУКТОРЫ

    @classmethod
    def from_client(cls, client):
        """
        Создает ShortClient из объекта Client.
        """
        from client import Client
        if not isinstance(client, Client):
            raise ValueError("Можно создать только из объекта Client")

        return cls(client.client_id, client.last_name, client.first_name, client.patronymic)

    @classmethod
    def from_full_name_string(cls, full_name_string: str, client_id: int = 1):
        """
        Создает ShortClient из строки с полным именем.
        """
        if not full_name_string or not isinstance(full_name_string, str):
            raise ValueError("Строка с ФИО не может быть пустой")

        parts = full_name_string.strip().split()
        if len(parts) < 2:
            raise ValueError("Строка должна содержать как минимум фамилию и имя")

        last_name = parts[0]
        first_name = parts[1]
        patronymic = parts[2] if len(parts) > 2 else None

        return cls(client_id, last_name, first_name, patronymic)
