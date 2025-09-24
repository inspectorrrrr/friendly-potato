import pytest
from playwright.sync_api import sync_playwright


@pytest.mark.parametrize("browser_name", ["chromium", "firefox"])
def test_playwright_title(browser_name):
    """
    Тест проверяет заголовок страницы playwright.dev в разных браузерах
    """
    with sync_playwright() as p:
        # Запуск браузера
        if browser_name == "chromium":
            browser = p.chromium.launch(headless=True)
        elif browser_name == "firefox":
            browser = p.firefox.launch(headless=True)

        # Создание контекста и страницы
        context = browser.new_context()
        page = context.new_page()

        try:
            # Переход на страницу
            page.goto("https://playwright.dev/")

            # Ожидание загрузки страницы
            page.wait_for_load_state("networkidle")

            # Получение заголовка страницы
            actual_title = page.title()

            # Ожидаемый заголовок
            expected_title = "Playwright"

            # Проверка соответствия заголовка
            assert expected_title in actual_title, f"Заголовок не соответствует ожидаемому. Получен: '{actual_title}', Ожидался: '{expected_title}'"

            print(f"✓ Тест в {browser_name} прошел успешно. Заголовок: '{actual_title}'")

        finally:
            # Закрытие браузера
            context.close()
            browser.close()


def test_playwright_title_webkit():
    """
    Дополнительный тест для браузера WebKit (Safari)
    """
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto("https://playwright.dev/")
            page.wait_for_load_state("networkidle")

            actual_title = page.title()
            expected_title = "Playwright"

            assert expected_title in actual_title, f"Заголовок не соответствует ожидаемому в WebKit. Получен: '{actual_title}'"

            print(f"✓ Тест в WebKit прошел успешно. Заголовок: '{actual_title}'")

        finally:
            context.close()
            browser.close()


if __name__ == "__main__":
    # Запуск тестов для разных браузеров
    print("Запуск тестов для проверки заголовка playwright.dev...")

    test_playwright_title("chromium")
    test_playwright_title("firefox")
    test_playwright_title_webkit()

    print("Все тесты завершены успешно!")
