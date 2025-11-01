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

        Args:
            client_id: Уникальный идентификатор клиента
            last_name: Фамилия клиента
            first_name: Имя клиента
            patronymic: Отчество клиента (опционально)
            phone: Телефон (опционально)
            email: Email (опционально)
            registration_date: Дата регистрации (опционально)
        """
        # Приватные поля (двойное подчеркивание - строгая инкапсуляция)
        self.__client_id = None
        self.__last_name = None
        self.__first_name = None
        self.__patronymic = None
        self.__phone = None
        self.__email = None
        self.__registration_date = None

        # Используем свойства для установки значений (вызываем сеттеры)
        self.client_id = client_id
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.phone = phone
        self.email = email
        self.registration_date = registration_date

    # region Свойства (Properties) для инкапсуляции

    @property
    def client_id(self) -> int:
        """Возвращает идентификатор клиента."""
        return self.__client_id

    @client_id.setter
    def client_id(self, value: int):
        """Устанавливает идентификатор клиента."""
        if not isinstance(value, int):
            raise ValueError("ID клиента должен быть целым числом")
        if value <= 0:
            raise ValueError("ID клиента должен быть положительным числом")
        self.__client_id = value

    @property
    def last_name(self) -> str:
        """Возвращает фамилию клиента."""
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str):
        """Устанавливает фамилию клиента."""
        if not value or not isinstance(value, str):
            raise ValueError("Фамилия должна быть непустой строкой")
        value = value.strip()
        if not value:
            raise ValueError("Фамилия не может быть пустой или состоять из пробелов")
        self.__last_name = value

    @property
    def first_name(self) -> str:
        """Возвращает имя клиента."""
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str):
        """Устанавливает имя клиента."""
        if not value or not isinstance(value, str):
            raise ValueError("Имя должно быть непустой строкой")
        value = value.strip()
        if not value:
            raise ValueError("Имя не может быть пустым или состоять из пробелов")
        self.__first_name = value

    @property
    def patronymic(self) -> str:
        """Возвращает отчество клиента."""
        return self.__patronymic

    @patronymic.setter
    def patronymic(self, value: str):
        """Устанавливает отчество клиента."""
        if value is None:
            self.__patronymic = None
        else:
            if not isinstance(value, str):
                raise ValueError("Отчество должно быть строкой")
            value = value.strip()
            self.__patronymic = value if value else None

    @property
    def phone(self) -> str:
        """Возвращает телефон клиента."""
        return self.__phone

    @phone.setter
    def phone(self, value: str):
        """Устанавливает телефон клиента."""
        if value is None:
            self.__phone = None
        else:
            if not isinstance(value, str):
                raise ValueError("Телефон должен быть строкой")
            value = value.strip()
            self.__phone = value if value else None

    @property
    def email(self) -> str:
        """Возвращает email клиента."""
        return self.__email

    @email.setter
    def email(self, value: str):
        """Устанавливает email клиента."""
        if value is None:
            self.__email = None
        else:
            if not isinstance(value, str):
                raise ValueError("Email должен быть строкой")
            value = value.strip()
            if value and '@' not in value:
                raise ValueError("Email должен содержать символ @")
            self.__email = value if value else None

    @property
    def registration_date(self) -> str:
        """Возвращает дату регистрации."""
        return self.__registration_date

    @registration_date.setter
    def registration_date(self, value: str):
        """Устанавливает дату регистрации."""
        if value is None:
            self.__registration_date = None
        else:
            if not isinstance(value, str):
                raise ValueError("Дата регистрации должна быть строкой")
            value = value.strip()
            self.__registration_date = value if value else None

    # endregion

    def __str__(self) -> str:
        """Возвращает строковое представление клиента."""
        patronymic_str = f" {self.patronymic}" if self.patronymic else ""
        phone_str = f", тел: {self.phone}" if self.phone else ""
        return f"Клиент {self.last_name} {self.first_name}{patronymic_str} (ID: {self.client_id}{phone_str})"

    def __repr__(self) -> str:
        """Возвращает формальное строковое представление."""
        return (f"Client(client_id={self.client_id}, last_name='{self.last_name}', "
                f"first_name='{self.first_name}', patronymic='{self.patronymic}')")