from client import Client
from short_client import ShortClient


def test_short_client_creation():
    """Тест создания ShortClient."""
    print("🧪 Тестирование создания ShortClient:")

    short_client1 = ShortClient(1, "Иванов", "Иван", "Иванович")
    print(f"✅ Прямое создание: {short_client1}")

    short_client2 = ShortClient(2, "Петров", "Петр")
    print(f"✅ Без отчества: {short_client2}")

    short_client3 = ShortClient.from_full_name_string("Сидоров Алексей Николаевич", 3)
    print(f"✅ Из строки ФИО: {short_client3}")


def test_from_client_conversion():
    """Тест преобразования Client в ShortClient."""
    print("\n🧪 Тестирование преобразования Client → ShortClient:")

    full_client = Client(1, "Иванов", "Иван", "Иванович", "+79161234567", "ivanov@mail.ru")
    print(f"📋 Полный клиент: {full_client}")

    short_client = ShortClient.from_client(full_client)
    print(f"✅ Краткая версия: {short_client}")
    print(f"✅ Только ФИО: {short_client.get_full_name()}")


if __name__ == "__main__":
    print("🚀 Задание 8 - Класс краткого представления клиента")
    print("=" * 60)
    test_short_client_creation()
    test_from_client_conversion()
    print("=" * 60)
    print("🎉 Задание 8 завершено!")