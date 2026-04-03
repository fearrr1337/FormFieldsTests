# Проект тестирования формы

## Запуск тестов
```bash
pytest --alluredir=allure-results
```

## Тест-кейсы для формы

### Позитивный тест-кейс (TC-POS-01)
**Название:** Успешная отправка формы с корректными данными  
**Предусловие:** Открыта страница https://practice-automation.com/form-fields/  
**Шаги:**
1. В поле Name ввести "Test User"
2. В поле Password ввести "Secret123"
3. В разделе "What is your favorite drink?" отметить Milk и Coffee
4. В разделе "What is your favorite color?" выбрать Yellow
5. В разделе "Do you like automation?" выбрать Yes
6. В поле Email ввести "user@example.com"
7. В поле Message написать количество инструментов из списка Automation tools и самый длинный инструмент ("Number of tools: 5, Longest tool name: Katalon Studio")
8. Нажать кнопку Submit

**Ожидаемый результат:** Появляется alert с текстом "Message received!"

---

### Негативный тест-кейс (TC-NEG-01)
**Название:** Отправка формы с незаполненным полем Name  
**Предусловие:** Открыта страница https://practice-automation.com/form-fields/  
**Шаги:**
1. Заполнить все поля, как в позитивном тест-кейсе, **кроме поля Name** (оставить пустым)
2. Нажать кнопку Submit

**Ожидаемый результат:** Форма не отправляется. Браузер прокручивает страницу к полю Name, показывает сообщение о необходимости заполнить это поле. Alert с текстом «Message received!» **не появляется**.

## Результаты Allure отчёта
<img width="2558" height="1279" alt="image" src="https://github.com/user-attachments/assets/68bfdaec-79f8-4bf9-a88b-e14e88033142" />
