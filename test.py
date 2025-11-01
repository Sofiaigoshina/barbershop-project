from client import Client


def test_full_and_short_info():
    """Тест полной и краткой версий вывода."""
    print("🧪 Тестирование вывода полной и краткой информации:")

    # Создаем клиента
    client = Client(
        client_id=1,
        last_name="Иванов",
        first_name="Иван",
        patronymic="Иванович",
        phone="+79161234567",
        email="ivanov@mail.ru",
        registration_date="2024-01-15"
    )

    print("\n📋 КРАТКАЯ ИНФОРМАЦИЯ:")
    print(client.short_info())

    print("\n📋 ПОЛНАЯ ИНФОРМАЦИЯ:")
    print(client.full_info())

    print("\n📋 ЧЕРЕЗ print() (использует __str__):")
    print(client)


def test_equality_comparison():
    """Тест сравнения объектов на равенство."""
    print("\n🧪 Тестирование сравнения объектов:")

    # Создаем одинаковых клиентов
    client1 = Client(1, "Иванов", "Иван", "Иванович")
    client2 = Client(1, "Иванов", "Иван", "Иванович")
    client3 = Client(2, "Петров", "Петр")

    print(f"client1: {client1}")
    print(f"client2: {client2}")
    print(f"client3: {client3}")

    # Тестируем равенство
    print(f"\n✅ client1 == client2: {client1 == client2} (должно быть True)")
    print(f"✅ client1 == client3: {client1 == client3} (должно быть False)")
    print(f"✅ client1 == 'строка': {client1 == 'строка'} (должно быть False)")


def test_hash_and_collections():
    """Тест работы с коллекциями (требует __hash__)."""
    print("\n🧪 Тестирование работы с коллекциями:")

    client1 = Client(1, "Иванов", "Иван")
    client2 = Client(1, "Иванов", "Иван")  # Такой же как client1
    client3 = Client(2, "Петров", "Петр")

    # Создаем множество (требует __hash__)
    clients_set = {client1, client2, client3}
    print(f"✅ Множество клиентов: {len(clients_set)} элементов (должно быть 2)")

    # Создаем словарь (требует __hash__)
    clients_dict = {
        client1: "первый клиент",
        client3: "третий клиент"
    }
    print(f"✅ Словарь клиентов: {len(clients_dict)} элементов")


def test_different_scenarios():
    """Тест разных сценариев использования."""
    print("\n🧪 Тестирование разных сценариев:")

    # Клиент без отчества и телефона
    client_minimal = Client(1, "Петров", "Петр")
    print("📋 Минимальные данные:")
    print(client_minimal.full_info())

    # Клиент с email но без телефона
    client_with_email = Client(2, "Сидорова", "Мария", email="sidorova@mail.ru")
    print("\n📋 С email но без телефона:")
    print(client_with_email.short_info())


if __name__ == "__main__":
    print("🚀 Задание 7 - Вывод информации и сравнение объектов")
    print("=" * 60)
    test_full_and_short_info()
    test_equality_comparison()
    test_hash_and_collections()
    test_different_scenarios()
    print("=" * 60)
    print("🎉 Задание 7 завершено!")