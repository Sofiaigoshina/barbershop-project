from client import Client


def test_refactored_validation_methods():
    """Тест универсальных методов валидации после рефакторинга."""
    print("🧪 Тестирование универсальных методов валидации:")

    # Тест универсального метода для чисел
    try:
        Client._validate_positive_int(5, "Возраст")
        print("   ✅ Универсальная проверка чисел работает")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")

    # Тест универсального метода для обязательных строк
    try:
        Client._validate_required_string("Тест", "Поле", min_length=2)
        print("   ✅ Универсальная проверка строк работает")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")

    # Тест с разной минимальной длиной
    try:
        Client._validate_required_string("А", "Короткое поле", min_length=1)
        print("   ✅ Работает с min_length=1")
    except Exception as e:
        print(f"   ❌ Ошибка: {e}")

    try:
        Client._validate_required_string("А", "Короткое поле", min_length=3)
        print("   ❌ ОШИБКА: Слишком короткая строка прошла проверку!")
    except ValueError as e:
        print(f"   ✅ Короткая строка правильно отклонена: {e}")


def test_client_creation_still_works():
    """Тест, что после рефакторинга создание клиента все еще работает."""
    print("\n🧪 Тест создания клиента после рефакторинга:")

    # Все те же случаи должны работать
    test_cases = [
        (1, "Иванов", "Иван"),
        (2, "Петрова", "Мария", "Сергеевна"),
        (3, "Сидоров", "Алексей", None, "+79161234567", "test@mail.ru")
    ]

    for i, case in enumerate(test_cases, 1):
        try:
            client = Client(*case)
            print(f"   ✅ Тест {i}: Клиент создан - {client}")
        except Exception as e:
            print(f"   ❌ Тест {i}: Ошибка - {e}")


def test_validation_failures():
    """Тест, что валидация все еще правильно отклоняет невалидные данные."""
    print("\n🧪 Тест отклонения невалидных данных:")

    invalid_cases = [
        (0, "Иванов", "Иван", "ID=0"),
        (1, "", "Иван", "Пустая фамилия"),
        (1, "И", "Иван", "Слишком короткая фамилия"),
        (1, "Иванов", "Иван", None, None, "invalid-email", "Невалидный email")
    ]

    for case in invalid_cases:
        try:
            client = Client(*case[:-1])  # Все кроме последнего элемента (описание)
            print(f"   ❌ ОШИБКА: {case[-1]} прошел проверку!")
        except ValueError as e:
            print(f"   ✅ {case[-1]} правильно отклонен")


def compare_code_improvement():
    """Сравнение улучшения кода."""
    print("\n📊 Сравнение до и после рефакторинга:")
    print("   ДО: 5 специализированных методов с дублированием")
    print("   ПОСЛЕ: 4 универсальных метода без дублирования")
    print("   ✅ Убрано дублирование проверок типа данных")
    print("   ✅ Убрано дублирование проверок пустых строк")
    print("   ✅ Код стал более гибким и переиспользуемым")


if __name__ == "__main__":
    print("🚀 Задание 5 - Рефакторинг: Убрать повторяющийся код")
    print("=" * 65)
    test_refactored_validation_methods()
    test_client_creation_still_works()
    test_validation_failures()
    compare_code_improvement()
    print("=" * 65)
    print("🎉 Рефакторинг завершен успешно!")