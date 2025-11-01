class Client:
    """
    Класс для представления клиента парикмахерской.
    Реализует полную инкапсуляцию всех полей через свойства.
    """

    def __init__(self, client_id: int, last_name: str, first_name: str,
                 patronymic: str = None, phone: str = None,
                 email: str = None, registration_date: str = None):
        """
        Инициализирует объект клиента.
        """
        # Валидация ВСЕХ полей перед созданием объекта
        Client.validate_client_id(client_id)
        Client.validate_name(last_name, "Фамилия")
        Client.validate_name(first_name, "Имя")
        Client.validate_optional_string(patronymic, "Отчество")
        Client.validate_optional_string(phone, "Телефон")
        Client.validate_email(email)
        Client.validate_optional_string(registration_date, "Дата регистрации")

        # ТОЛЬКО ЕСЛИ ВСЕ ПРОВЕРКИ ПРОЙДЕНЫ: создаем объект
        self.__client_id = client_id
        self.__last_name = last_name.strip()
        self.__first_name = first_name.strip()
        self.__patronymic = patronymic.strip() if patronymic else None
        self.__phone = phone.strip() if phone else None
        self.__email = email.strip() if email else None
        self.__registration_date = registration_date.strip() if registration_date else None

    #  Статические методы проверки
    @staticmethod
    def validate_client_id(value: int):
        """Проверяет корректность ID клиента."""
        if not isinstance(value, int):
            raise ValueError("ID клиента должен быть целым числом")
        if value <= 0:
            raise ValueError("ID клиента должен быть положительным числом")

    @staticmethod
    def validate_name(value: str, field_name: str):
        """Проверяет корректность имени и фамилии."""
        if not value:
            raise ValueError(f"{field_name} не может быть пустой")
        if not isinstance(value, str):
            raise ValueError(f"{field_name} должна быть строкой")
        if not value.strip():
            raise ValueError(f"{field_name} не может состоять только из пробелов")
        if len(value.strip()) < 2:
            raise ValueError(f"{field_name} должна содержать минимум 2 символа")

    @staticmethod
    def validate_optional_string(value: str, field_name: str):
        """Проверяет опциональные строковые поля."""
        if value is not None:
            if not isinstance(value, str):
                raise ValueError(f"{field_name} должна быть строкой")
            if not value.strip():
                raise ValueError(f"{field_name} не может быть пустой")

    @staticmethod
    def validate_email(value: str):
        """Проверяет корректность email адреса."""
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Email должен быть строкой")
            value = value.strip()
            if value:  # Если email не пустой
                if '@' not in value:
                    raise ValueError("Email должен содержать символ @")
                if '.' not in value.split('@')[-1]:
                    raise ValueError("Email должен содержать домен с точкой")

    # свойства (ТОЛЬКО геттеры - поля неизменяемые после создания)
    @property
    def client_id(self) -> int:
        """Возвращает идентификатор клиента."""
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

    @property
    def phone(self) -> str:
        """Возвращает телефон клиента."""
        return self.__phone

    @property
    def email(self) -> str:
        """Возвращает email клиента."""
        return self.__email

    @property
    def registration_date(self) -> str:
        """Возвращает дату регистрации."""
        return self.__registration_date

    def __str__(self) -> str:
        """Возвращает строковое представление клиента."""
        patronymic_str = f" {self.patronymic}" if self.patronymic else ""
        phone_str = f", тел: {self.phone}" if self.phone else ""
        return f"Клиент {self.last_name} {self.first_name}{patronymic_str} (ID: {self.client_id}{phone_str})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление."""
        return (f"Client(client_id={self.client_id}, last_name='{self.last_name}', "
                f"first_name='{self.first_name}', patronymic='{self.patronymic}')")