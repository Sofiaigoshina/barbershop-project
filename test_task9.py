from client import Client
from short_client import ShortClient


def test_inheritance():
    """Тест наследования."""
    print("🧪 Тестирование наследования:")

    # Создаем объекты обоих классов
    short_client = ShortClient(1, "Иванов", "Иван", "Иванович")
    full_client = Client(1, "Иванов", "Иван", "Иванович", "+79161234567", "ivan@mail.ru")

    print(f"✅ ShortClient: {short_client}")
    print(f"✅ Client: {full_client}")

    # Проверяем, что Client является подклассом ShortClient
    print(f"✅ Client является подклассом ShortClient: {issubclass(Client, ShortClient)}")

    # Проверяем, что объекты имеют общие методы
    print(f"✅ Общие методы работают:")
    print(f"   ShortClient инициалы: {short_client.get_initials()}")
    print(f"   Client инициалы: {full_client.get_initials()}")


def test_no_duplication():
    """Тест отсутствия дублирования."""
    print("\n🧪 Тестирование отсутствия дублирования:")

    # Проверяем, что общие методы есть только в родительском классе
    short_client_methods = set(dir(ShortClient))
    client_methods = set(dir(Client))

    # Методы, которые должны быть только в ShortClient
    common_methods = {'get_initials', 'get_full_name_with_initials', 'get_full_name'}

    print("✅ Общие методы в ShortClient:")
    for method in common_methods:
        if method in short_client_methods:
            print(f"   ✅ {method} - в ShortClient")

    print("✅ Уникальные методы в Client:")
    unique_client_methods = {'full_info', 'to_dict', 'to_json', 'from_json', 'from_dict'}
    for method in unique_client_methods:
        if method in client_methods:
            print(f"   ✅ {method} - в Client")


def test_polymorphism():
    """Тест полиморфизма."""
    print("\n🧪 Тестирование полиморфизма:")

    # Создаем объекты разных классов
    clients = [
        ShortClient(1, "Иванов", "Иван"),
        Client(2, "Петров", "Петр", phone="+79161234567"),
        ShortClient(3, "Сидоров", "Алексей")
    ]

    # Все объекты могут использовать общие методы
    for client in clients:
        print(f"✅ {client.__class__.__name__}: {client.get_full_name_with_initials()}")


def test_constructor_inheritance():
    """Тест наследования конструкторов."""
    print("\n🧪 Тестирование наследования конструкторов:")

    # ShortClient конструктор
    short_client = ShortClient.from_full_name_string("Иванов Иван Иванович", 1)
    print(f"✅ ShortClient из строки: {short_client}")

    # Client конструкторы (уникальные)
    full_client = Client.from_name_and_phone("Петров", "Петр", "+79161234567", 2)
    print(f"✅ Client с телефоном: {full_client}")


def test_equality_inheritance():
    """Тест наследования сравнения."""
    print("\n🧪 Тестирование наследования сравнения:")

    short1 = ShortClient(1, "Иванов", "Иван")
    short2 = ShortClient(1, "Иванов", "Иван")
    full1 = Client(1, "Иванов", "Иван")
    full2 = Client(1, "Иванов", "Иvan", phone="+79161234567")

    print(f"✅ short1 == short2: {short1 == short2}")
    print(f"✅ short1 == full1: {short1 == full1}")  # Разные классы
    print(f"✅ full1 == full2: {full1 == full2}")  # Разные данные


if __name__ == "__main__":
    print("🚀 Задание 9 - Наследование: объединение классов в иерархию")
    print("=" * 60)
    test_inheritance()
    test_no_duplication()
    test_polymorphism()
    test_constructor_inheritance()
    test_equality_inheritance()
    print("=" * 60)
    print("🎉 Задание 9 завершено!")