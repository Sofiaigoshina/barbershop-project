class Client:
    def __init__(self, client_id, familia, imya, otchestvo=None, telefon=None, email=None, data_registracii=None):

        self.client_id = client_id  # Используем свойства!
        self.familia = familia
        self.imya = imya
        self.otchestvo = otchestvo
        self.telefon = telefon
        self.email = email
        self.data_registracii = data_registracii


    @property
    def client_id(self):
        return self.__client_id

    @client_id.setter
    def client_id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("ID клиента должен быть положительным целым числом")
        self.__client_id = value

    @property
    def familia(self):
        return self.__familia

    @familia.setter
    def familia(self, value):
        if not value or not value.strip():
            raise ValueError("Фамилия не может быть пустой")
        self.__familia = value.strip()

    @property
    def imya(self):
        return self.__imya

    @imya.setter
    def imya(self, value):
        if not value or not value.strip():
            raise ValueError("Имя не может быть пустой")
        self.__imya = value.strip()

    @property
    def otchestvo(self):
        return self.__otchestvo

    @otchestvo.setter
    def otchestvo(self, value):
        if value is not None:
            value = value.strip()
            if not value:
                value = None
        self.__otchestvo = value

    @property
    def telefon(self):
        return self.__telefon

    @telefon.setter
    def telefon(self, value):
        if value is not None:
            value = value.strip()
            if not value:
                value = None
        self.__telefon = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if value is not None:
            value = value.strip()
            if not value:
                value = None
            elif '@' not in value:
                raise ValueError("Email должен содержать символ @")
        self.__email = value

    @property
    def data_registracii(self):
        return self.__data_registracii

    @data_registracii.setter
    def data_registracii(self, value):
        if value is not None:
            value = value.strip()
            if not value:
                value = None
        self.__data_registracii = value

    # endregion

    def __str__(self):
        return f"Клиент {self.familia} {self.imya} {self.otchestvo or ''} (ID: {self.client_id})"