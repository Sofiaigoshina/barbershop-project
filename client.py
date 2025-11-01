import json
from short_client import ShortClient


class Client(ShortClient):
    """
    Класс для полного представления клиента парикмахерской.
    Наследует от ShortClient и добавляет дополнительные поля.
    """

    def __init__(self, client_id: int, last_name: str, first_name: str,
                 patronymic: str = None, phone: str = None,
                 email: str = None, registration_date: str = None):
        """
        Инициализирует объект клиента.
        """
        # ВЫЗЫВАЕМ КОНСТРУКТОР РОДИТЕЛЬСКОГО КЛАССА (убираем дублирование)
        super().__init__(client_id, last_name, first_name, patronymic)

        # ДОБАВЛЯЕМ ВАЛИДАЦИЮ НОВЫХ ПОЛЕЙ (только для новых полей)
        self._validate_optional_string(phone, "Телефон")
        self._validate_email(email)
        self._validate_optional_string(registration_date, "Дата регистрации")

        # ДОБАВЛЯЕМ НОВЫЕ ПОЛЯ
        self._phone = phone.strip() if phone else None
        self._email = email.strip() if email else None
        self._registration_date = registration_date.strip() if registration_date else None

    # region ДОПОЛНИТЕЛЬНЫЕ СВОЙСТВА (только новые поля)

    @property
    def phone(self) -> str:
        """Возвращает телефон клиента."""
        return self._phone

    @property
    def email(self) -> str:
        """Возвращает email клиента."""
        return self._email

    @property
    def registration_date(self) -> str:
        """Возвращает дату регистрации."""
        return self._registration_date

    # ПЕРЕОПРЕДЕЛЕННЫЕ МЕТОДЫ (дополняем родительские)

    def full_info(self) -> str:
        """
        Возвращает полную информацию о клиенте.
        Переопределяет/дополняет метод из родительского класса.
        """
        lines = [
            "=" * 40,
            "ПОЛНАЯ ИНФОРМАЦИЯ О КЛИЕНТЕ",
            "=" * 40,
            f"ID: {self.client_id}",
            f"Фамилия: {self.last_name}",
            f"Имя: {self.first_name}",
            f"Отчество: {self.patronymic or 'не указано'}",
            f"Телефон: {self.phone or 'не указан'}",
            f"Email: {self.email or 'не указан'}",
            f"Дата регистрации: {self.registration_date or 'не указана'}",
            "=" * 40
        ]
        return "\n".join(lines)

    def short_info(self) -> str:
        """
        Возвращает краткую информацию о клиенте.
        Использует унаследованные методы.
        """
        return f"{self.get_full_name()} (ID: {self.client_id})"

    def __eq__(self, other) -> bool:
        """
        Сравнивает два объекта Client на равенство.
        Расширяет сравнение родительского класса.
        """
        # Сначала проверяем равенство по родительским полям
        if not super().__eq__(other):
            return False

        # Затем проверяем дополнительные поля
        if not isinstance(other, Client):
            return False

        return (self.phone == other.phone and
                self.email == other.email and
                self.registration_date == other.registration_date)

    def __repr__(self) -> str:
        """Формальное строковое представление."""
        return (f"Client(client_id={self.client_id}, last_name='{self.last_name}', "
                f"first_name='{self.first_name}', patronymic='{self.patronymic}')")

    # УНИКАЛЬНЫЕ МЕТОДЫ Client (не дублируются)

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

    # АЛЬТЕРНАТИВНЫЕ КОНСТРУКТОРЫ (уникальные для Client)

    @classmethod
    def from_json(cls, json_data: str):
        """
        Создает клиента из JSON строки.
        """
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

    # МЕТОДЫ ПРЕОБРАЗОВАНИЯ

    def to_dict(self) -> dict:
        """
        Преобразует объект в словарь.
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
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)
