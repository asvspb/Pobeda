## README

### На русском языке

# Поиск дешевых авиабилетов с помощью Selenium

Этот проект представляет собой скрипт на Python, который использует Selenium для поиска самых дешевых авиабилетов на сайте "Победа". Скрипт позволяет пользователю выбрать город отправления и назначения, дату начала поиска, а также количество дней, на которые нужно искать билеты. Результаты поиска сохраняются в CSV файл.

## Требования

- Python 3.x
- Selenium
- ChromeDriver
- webdriver-manager

## Установка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Установите зависимости:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Убедитесь, что у вас установлен ChromeDriver.** Если нет, он будет автоматически загружен и установлен при первом запуске скрипта.

## Использование

1. **Запустите скрипт:**

   ```bash
   python your_script.py
   ```

2. **Следуйте инструкциям на экране:**

   - Выберите город отправления.
   - Выберите город назначения.
   - Введите дату начала поиска или нажмите Enter для использования сегодняшней даты.
   - Введите количество дней для поиска билетов.

3. **Результаты поиска будут сохранены в файл `cheapest_tickets.csv`.**

## Пример вывода

```
Идет поиск билетов Санкт-Петербург - Москва на 5 дн. вперед...
Дата: 01.01.2024, Цена: 5000₽, Вылет: 10:00, Прилет: 12:00
Дата: 02.01.2024, Цена: 4500₽, Вылет: 11:00, Прилет: 13:00
...
```

## Структура проекта

- `your_script.py`: Основной скрипт для поиска билетов.
- `requirements.txt`: Файл с зависимостями.
- `README.md`: Этот файл.

## Лицензия

Этот проект лицензирован под MIT License. Подробности смотрите в файле `LICENSE`.

---

### In English

# Cheap Flight Ticket Search with Selenium

This project is a Python script that uses Selenium to search for the cheapest flight tickets on the "Pobeda" website. The script allows the user to select the departure and destination cities, the start date for the search, and the number of days to search for tickets. The search results are saved to a CSV file.

## Requirements

- Python 3.x
- Selenium
- ChromeDriver
- webdriver-manager

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   cd yourrepository
   ```

2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Ensure you have ChromeDriver installed.** If not, it will be automatically downloaded and installed when you run the script for the first time.

## Usage

1. **Run the script:**

   ```bash
   python your_script.py
   ```

2. **Follow the on-screen instructions:**

   - Select the departure city.
   - Select the destination city.
   - Enter the start date for the search or press Enter to use today's date.
   - Enter the number of days to search for tickets.

3. **The search results will be saved to the `cheapest_tickets.csv` file.**

## Example Output

```
Searching for tickets from Saint Petersburg to Moscow for 5 days ahead...
Date: 01.01.2024, Price: 5000₽, Departure: 10:00, Arrival: 12:00
Date: 02.01.2024, Price: 4500₽, Departure: 11:00, Arrival: 13:00
...
```

## Project Structure

- `your_script.py`: The main script for searching tickets.
- `requirements.txt`: File with dependencies.
- `README.md`: This file.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Note:** Replace `yourusername`, `yourrepository`, and `your_script.py` with your actual GitHub username, repository name, and script name respectively.
