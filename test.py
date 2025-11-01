from client import Client
import json


def test_from_full_name_string():
    """Тест создания из строки с ФИО."""
    print("🧪 Создание из строки с ФИО:")

    # Тест с фамилией, именем и отчеством
    client1 = Client.from_full_name_string("Иванов Иван Иванович", 1)
    print(f"   ✅ Полное ФИО: {client1}")

    # Тест только с фамилией и именем
    client2 = Client.from_full_name_string("Петрова Мария", 2)
    print(f"   ✅ Только фамилия и имя: {client2}")

    # Тест с ошибкой
    try:
        Client.from_full_name_string("Иванов", 3)  # Только фамилия
    except ValueError as e:
        print(f"   ✅ Ошибка при неполном ФИО: {e}")


def test_from_json():
    """Тест создания из JSON."""
    print("\n🧪 Создание из JSON:")

    # Валидный JSON
    json_data = '''
    {
        "client_id": 1,
        "last_name": "Сидоров",
        "first_name": "Алексей",
        "phone": "+79161234567",
        "email": "sidorov@mail.ru"
    }
    '''
    client = Client.from_json(json_data)
    print(f"   ✅ Из JSON: {client}")
    print(f"   📞 Телефон: {client.phone}")

    # Невалидный JSON
    try:
        Client.from_json("{invalid json}")
    except ValueError as e:
        print(f"   ✅ Ошибка при невалидном JSON: {e}")


def test_from_dict():
    """Тест создания из словаря."""
    print("\n🧪 Создание из словаря:")

    data = {
        "client_id": 1,
        "last_name": "Козлова",
        "first_name": "Анна",
        "patronymic": "Владимировна",
        "email": "kozlova@mail.ru"
    }

    client = Client.from_dict(data)
    print(f"   ✅ Из словаря: {client}")
    print(f"   📧 Email: {client.email}")


def test_from_name_and_phone():
    """Тест создания с именем и телефоном."""
    print("\n🧪 Создание с именем и телефоном:")

    client = Client.from_name_and_phone("Федоров", "Федор", "+79169876543", 5)
    print(f"   ✅ С телефоном: {client}")


def test_to_dict_and_to_json():
    """Тест преобразования в словарь и JSON."""
    print("\n🧪 Преобразование в словарь и JSON:")

    client = Client(1, "Иванов", "Иван", "Иванович", "+79161234567", "ivan@mail.ru")

    # В словарь
    client_dict = client.to_dict()
    print(f"   ✅ В словарь: {client_dict}")

    # В JSON
    client_json = client.to_json()
    print(f"   ✅ В JSON: {client_json[:50]}...")


def test_all_constructors():
    """Сравнение всех конструкторов."""
    print("\n📊 Сравнение всех способов создания:")

    # 1. Основной конструктор
    client1 = Client(1, "Иванов", "Иван", "Иванович")
    print(f"   1. Основной: {client1}")

    # 2. Из строки ФИО
    client2 = Client.from_full_name_string("Петров Петр Петрович", 2)
    print(f"   2. Из строки: {client2}")

    # 3. Из словаря
    client3 = Client.from_dict({
        "client_id": 3,
        "last_name": "Сидорова",
        "first_name": "Мария"
    })
    print(f"   3. Из словаря: {client3}")

    # 4. С телефоном
    client4 = Client.from_name_and_phone("Кузнецов", "Алексей", "+79160000000", 4)
    print(f"   4. С телефоном: {client4}")


if __name__ == "__main__":
    print("🚀 Задание 6 - Перегрузка конструктора")
    print("=" * 60)
    test_from_full_name_string()
    test_from_json()
    test_from_dict()
    test_from_name_and_phone()
    test_to_dict_and_to_json()
    test_all_constructors()
    print("=" * 60)
    print("🎉 Все конструкторы работают!")