# Sprint 7 — API автотесты на Python

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![pytest](https://img.shields.io/badge/tests-pytest-green)
![Requests](https://img.shields.io/badge/API-requests-lightgrey)
![Allure](https://img.shields.io/badge/report-Allure-purple)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-blue)
![status](https://img.shields.io/badge/status-active-brightgreen)

Учебный проект по автоматизации API-тестирования на Python (pytest + requests).  
Структура приближена к реальному фреймворку: отдельные директории для тестов, данных и вспомогательных модулей, есть интеграция с Allure и GitHub Actions.

---

## 🚀 Стек

- **Python 3.x**
- **pytest**
- **requests**
- **allure-pytest**
- **GitHub Actions** (CI)

---

## 📁 Структура проекта

```text
Sprint_7_Python/
│
├── resources/           → данные и вспомогательные модули
│   ├── data_courier.py  → тестовые данные для курьеров
│   ├── data_order.py    → тестовые данные для заказов
│   ├── headers.py       → заголовки запросов
│   ├── message.py       → ожидаемые сообщения/тексты
│   ├── urls.py          → базовый URL и эндпоинты API
│   └── create_new_courier.py → генераторы данных и helper-функции
│
├── tests/               → API-тесты
│   ├── test_create_courier.py
│   ├── test_login_courier.py
│   ├── test_create_order.py
│   └── test_get_orders.py
│
├── .github/workflows/   → CI GitHub Actions
│   └── CI_UI.yml        → запуск тестов в пайплайне
│
├── pytest.ini           → конфигурация pytest
├── requirements.txt     → зависимости
└── README.md
