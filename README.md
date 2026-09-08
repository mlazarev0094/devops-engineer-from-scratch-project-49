### Hexlet tests and linter status:
[![Actions Status](https://github.com/mlazarev0094/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/mlazarev0094/devops-engineer-from-scratch-project-49/actions)
# Brain Games

Набор из 5 игр.

## Links

Этот проект был создан с использованием этих инструментов:

| Tool                                                                   | Description                                             |
|------------------------------------------------------------------------|---------------------------------------------------------|
| [uv](https://docs.astral.sh/uv/)                                       | "An extremely fast Python package and project manager, written in Rust" |
| [Pytest](https://pytest.org)                                           | "A mature full-featured Python testing tool"            |
| [ruff](https://docs.astral.sh/ruff/)                                   | "An extremely fast Python linter and code formatter, written in Rust" |

---

## Установка

### Требования
- Python 3.14 или выше
- uv (быстрый менеджер пакетов)
- make

### Шаги установки

**1. Клонируйте репозиторий:**
   ```bash
   git clone https://github.com/mlazarev0094/devops-engineer-from-scratch-project-49.git
   cd devops-engineer-from-scratch-project-49
   ```

**2. Установка зависимостей и сборка пакета:**
   ```bash
   make install
   make build
   ```

**3. Установка пакета в систему:**
   ```bash
   make package-install
   ```

**3.1. Принудительная переустановка (если пакет уже установлен)**
   ```bash
   make package-reinstall
   ```

## Запуск игр

### Проверка на чётность
   ```bash
   brain-even
   ```

Пользователю показывается случайное число. Нужно ответить `yes`, если число чётное, или `no` — если нечётное.

**Демонстрация работы:**

[![asciicast](https://asciinema.org/a/c58lBFh5x6ep6fz7.svg)](https://asciinema.org/a/c58lBFh5x6ep6fz7?autoplay=1)

### Калькулятор
   ```bash
   brain-calc
   ```

Пользователю показывается случайное математическое выражение, которое нужно вычислить и записать правильный ответ.

**Демонстрация работы:**

[![asciicast](https://asciinema.org/a/qcWh4Loh7MPovqM7.svg)](https://asciinema.org/a/qcWh4Loh7MPovqM7?autoplay=1)

### Наибольший общий делитель (НОД)
   ```bash
   brain-gcd
   ```

Пользователь должен вычислить и ввести наибольший общий делитель двух случайных чисел.

**Демонстрация работы:**

[![asciicast](https://asciinema.org/a/EGStqLrBj8c5IF25.svg)](https://asciinema.org/a/EGStqLrBj8c5IF25?autoplay=1)

### Арифметическая прогрессия
   ```bash
   brain-progression
   ```

Пользователь должен вычислить пропущенное число в арифметической прогрессии.

**Демонстрация работы:**

[![asciicast](https://asciinema.org/a/68DJ1dCpjUNGBeXG.svg)](https://asciinema.org/a/68DJ1dCpjUNGBeXG?autoplay=1)

### Простое ли число?
   ```bash
   brain-prime
   ```

Пользователю показывается случайное число. Нужно ответить `yes`, если число простое, или `no` — если не простое.

**Демонстрация работы:**

[![asciicast](https://asciinema.org/a/HbYdux7Lgp3F2lrF.svg)](https://asciinema.org/a/HbYdux7Lgp3F2lrF?autoplay=1)
