class Client:
    """
    Класс для представления клиента парикмахерской.
    Реализует полную инкапсуляцию всех полей через свойства.
    """

    def __init__(self, client_id: int, last_name: str, first_name: str,
                 patronymic: str = None, phone: str = None,
                 email: str = None, registration_date: str = None):
        """
        Основной конструктор - создает клиента из отдельных параметров.
        """
        # Валидация ВСЕХ полей перед созданием объекта
        Client._validate_positive_int(client_id, "ID клиента")
        Client._validate_required_string(last_name, "Фамилия", min_length=2)
        Client._validate_required_string(first_name, "Имя", min_length=2)
        Client._validate_optional_string(patronymic, "Отчество")
        Client._validate_optional_string(phone, "Телефон")
        Client._validate_email(email)
        Client._validate_optional_string(registration_date, "Дата регистрации")

        # ТОЛЬКО ЕСЛИ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ: создаем объект
        self.__client_id = client_id
        self.__last_name = last_name.strip()
        self.__first_name = first_name.strip()
        self.__patronymic = patronymic.strip() if patronymic else None
        self.__phone = phone.strip() if phone else None
        self.__email = email.strip() if email else None
        self.__registration_date = registration_date.strip() if registration_date else None

    # region АЛЬТЕРНАТИВНЫЕ КОНСТРУКТОРЫ (ЗАДАНИЕ 6)

    @classmethod
    def from_full_name_string(cls, full_name_string: str, client_id: int = 1):
        """
        Создает клиента из строки с полным именем.
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

    @classmethod
    def from_json(cls, json_data: str):
        """
        Создает клиента из JSON строки.
        """
        import json

        try:
            data = json.loads(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Невалидный JSON: {e}")

        return cls.from_dict(data)

    @classmethod
    def from_dict(cls, data: dict):
        """
        Создает клиента из словаря.
        """
        # Обязательные поля
        if "client_id" not in data:
            raise ValueError("Отсутствует обязательное поле: client_id")
        if "last_name" not in data:
            raise ValueError("Отсутствует обязательное поле: last_name")
        if "first_name" not in data:
            raise ValueError("Отсутствует обязательное поле: first_name")

        # Извлекаем данные со значениями по умолчанию
        client_id = data["client_id"]
        last_name = data["last_name"]
        first_name = data["first_name"]
        patronymic = data.get("patronymic")
        phone = data.get("phone")
        email = data.get("email")
        registration_date = data.get("registration_date")

        return cls(client_id, last_name, first_name, patronymic, phone, email, registration_date)

    @classmethod
    def from_name_and_phone(cls, last_name: str, first_name: str, phone: str, client_id: int = 1):
        """
        Создает клиента только с именем и телефоном.
        """
        return cls(client_id, last_name, first_name, phone=phone)

    # Статические методы проверки (задания 4-5)

    @staticmethod
    def _validate_positive_int(value: int, field_name: str):
        """Универсальная проверка положительного целого числа."""
        if not isinstance(value, int):
            raise ValueError(f"{field_name} должен быть целым числом")
        if value <= 0:
            raise ValueError(f"{field_name} должен быть положительным числом")

    @staticmethod
    def _validate_required_string(value: str, field_name: str, min_length: int = 1):
        """Универсальная проверка обязательных строковых полей."""
        if not value:
            raise ValueError(f"{field_name} не может быть пустой")
        if not isinstance(value, str):
            raise ValueError(f"{field_name} должна быть строкой")

        value_stripped = value.strip()
        if not value_stripped:
            raise ValueError(f"{field_name} не может состоять только из пробелов")
        if len(value_stripped) < min_length:
            raise ValueError(f"{field_name} должна содержать минимум {min_length} символов")

    @staticmethod
    def _validate_optional_string(value: str, field_name: str):
        """Универсальная проверка опциональных строковых полей."""
        if value is not None:
            if not isinstance(value, str):
                raise ValueError(f"{field_name} должна быть строкой")
            if not value.strip():
                raise ValueError(f"{field_name} не может быть пустой")

    @staticmethod
    def _validate_email(value: str):
        """Проверка корректности email адреса."""
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Email должен быть строкой")
            value_stripped = value.strip()
            if value_stripped:
                if '@' not in value_stripped:
                    raise ValueError("Email должен содержать символ @")
                if '.' not in value_stripped.split('@')[-1]:
                    raise ValueError("Email должен содержать домен с точкой")

    # region Свойства (геттеры)

    @property
    def client_id(self) -> int:
        return self.__client_id

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def patronymic(self) -> str:
        return self.__patronymic

    @property
    def phone(self) -> str:
        return self.__phone

    @property
    def email(self) -> str:
        return self.__email

    @property
    def registration_date(self) -> str:
        return self.__registration_date

    def to_dict(self) -> dict:
        """
        Преобразует объект в словарь (удобно для JSON).
        """
        return {
            "client_id": self.client_id,
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "phone": self.phone,
            "email": self.email,
            "registration_date": self.registration_date
        }

    def to_json(self) -> str:
        """
        Преобразует объект в JSON строку.
        """
        import json
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)

    def __str__(self) -> str:
        patronymic_str = f" {self.patronymic}" if self.patronymic else ""
        phone_str = f", тел: {self.phone}" if self.phone else ""
        return f"Клиент {self.last_name} {self.first_name}{patronymic_str} (ID: {self.client_id}{phone_str})"

    def __repr__(self) -> str:
        return (f"Client(client_id={self.client_id}, last_name='{self.last_name}', "
                f"first_name='{self.first_name}', patronymic='{self.patronymic}')")