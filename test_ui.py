import allure
import pytest
from pages.main_page import MainPage


@allure.epic("UI Тестирование")
@allure.feature("Поиск книжной информации")
class TestBookSearch:
    @allure.title("Поиск книги по заголовку")
    @allure.description("Тест проверяет возможность поиска книги по заголовку 'медный'.")
    def test_by_name(self, driver):
        with allure.step("Открытие страницы сайта"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Поиск книги по названию"):
            main_page.search_book("медный")
        with allure.step("Проверка, что книга найдена"):
            assert "медный" in main_page.get_search_results_text()

    @allure.title("Поиск автора")
    @allure.description("Тест проверяет возможность поиска автора 'толстой'.")
    def test_by_name_author(self, driver):
        with allure.step("Открытие страницы сайта"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Поиск книги по автору"):
            main_page.search_book("толстой")
        with allure.step("Проверка, что книга найдена"):
            assert "толстой" in main_page.get_search_results_text()

    @allure.title("Поиск книги на английском")
    @allure.description("Тест проверяет поиск книги с использование английского названия")
    def test_by_name_language_english(self, driver):
        with allure.step("Открытие страницы сайта"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Поиск книги на английском"):
            main_page.search_book("story")
        with allure.step("Проверка, что книга найдена"):
            assert "story»" in main_page.get_search_results_text()

    @allure.title("Поиск книги с символами вместо названия")
    @allure.description("Тест проверяет поиск книги с использованием символов вместо названия")
    def test_negative_by_symbols(self, driver):
        with allure.step("Открытие страницы сайта"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Поиск книги"):
            main_page.search_book("#$%")
        with allure.step("Проверка, найдена ли книга"):
            assert "#$%" in main_page.get_search_results_text()

    @allure.title("Поиск книги на китайском языке")
    @allure.description("Тест проверяет поиск книги с использованием китайских иероглифов в названии")
    def test_negative_by_language_thai(self, driver):
        with allure.step("Открытие страницы сайта"):
            main_page = MainPage(driver)
            main_page.open()
        with allure.step("Поиск книги на китайском"):
            main_page.search_book("战争与和平")
        with allure.step("Проверка, найдена ли книга"):
            assert "战争与和平" in main_page.get_search_results_text()
