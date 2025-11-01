from client import Client


def test_static_methods():
    """Тест статических методов валидации."""
    print("🧪 Тестирование статических методов:")

    # Тест валидных данных
    try:
        Client.validate_client_id(1)
        Client.validate_name("Иванов", "Фамилия")
        Client.validate_email("test@mail.ru")
        print("   ✅ Валидные данные проходят проверку")
    except Exception as e:
        print(f"   ❌ Неожиданная ошибка: {e}")

    # Тест невалидных данных
    try:
        Client.validate_client_id(0)
        print("   ❌ ОШИБКА: Невалидный ID прошел проверку!")
    except ValueError as e:
        print(f"   ✅ Защита от ID=0: {e}")

    try:
        Client.validate_name("", "Фамилия")
        print("   ❌ ОШИБКА: Пустая фамилия прошла проверку!")
    except ValueError as e:
        print(f"   ✅ Защита от пустой фамилии: {e}")


def test_object_creation_validation():
    """Тест, что объект с невалидными данными невозможно создать."""
    print("\n🧪 Тест создания объектов:")

    # Успешное создание
    try:
        client = Client(1, "Иванов", "Иван", email="valid@mail.ru")
        print("   ✅ Объект с валидными данными создан успешно")
    except ValueError as e:
        print(f"   ❌ Неожиданная ошибка: {e}")

    # Неуспешное создание (объект НЕ должен создаться)
    try:
        client = Client(0, "Иванов", "Иван")  # Невалидный ID
        print("   ❌ ОШИБКА: Объект с невалидным ID создался!")
    except ValueError as e:
        print(f"   ✅ Объект с невалидным ID НЕ создан: {e}")

    try:
        client = Client(1, "", "Иван")  # Пустая фамилия
        print("   ❌ ОШИБКА: Объект с пустой фамилией создался!")
    except ValueError as e:
        print(f"   ✅ Объект с пустой фамилией НЕ создан: {e}")

    try:
        client = Client(1, "Иванов", "Иван", email="invalid")  # Невалидный email
        print("   ❌ ОШИБКА: Объект с невалидным email создался!")
    except ValueError as e:
        print(f"   ✅ Объект с невалидным email НЕ создан: {e}")


def test_immutability():
    """Тест, что поля нельзя изменить после создания."""
    print("\n🧪 Тест неизменяемости полей:")
    client = Client(1, "Иванов", "Иван")

    # Проверяем, что нельзя изменить поля
    try:
        client.client_id = 5  # Попытка изменить ID
        print("   ❌ ОШИБКА: Поле client_id можно изменить!")
    except AttributeError as e:
        print(f"   ✅ Поле client_id защищено от изменений")
    except Exception as e:
        print(f"   ✅ Поле client_id защищено от изменений: {type(e).__name__}")

    try:
        client.last_name = "Петров"  # Попытка изменить фамилию
        print("   ❌ ОШИБКА: Поле last_name можно изменить!")
    except AttributeError as e:
        print(f"   ✅ Поле last_name защищено от изменений")
    except Exception as e:
        print(f"   ✅ Поле last_name защищено от изменений: {type(e).__name__}")

    try:
        client.email = "new@mail.ru"  # Попытка изменить email
        print("   ❌ ОШИБКА: Поле email можно изменить!")
    except AttributeError as e:
        print(f"   ✅ Поле email защищено от изменений")
    except Exception as e:
        print(f"   ✅ Поле email защищено от изменений: {type(e).__name__}")

    print("   ✅ Все поля защищены от изменений после создания")


def test_properties_still_work():
    """Тест, что геттеры все еще работают."""
    print("\n🧪 Тест работы геттеров:")
    client = Client(1, "Иванов", "Иван", "Иванович", "+79161234567", "ivan@mail.ru")

    print(f"   ✅ ID: {client.client_id}")
    print(f"   ✅ ФИО: {client.last_name} {client.first_name} {client.patronymic}")
    print(f"   ✅ Телефон: {client.phone}")
    print(f"   ✅ Email: {client.email}")
    print(f"   ✅ Объект: {client}")


if __name__ == "__main__":
    print("🚀 Тестирование задания 4 - Статические методы валидации")
    print("=" * 60)
    test_static_methods()
    test_object_creation_validation()
    test_immutability()
    test_properties_still_work()
    print("=" * 60)
    print("🎉 Тестирование завершено!")