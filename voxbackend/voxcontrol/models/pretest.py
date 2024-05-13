import re


def clean_phone_numbers(text):
    # Регулярное выражение для поиска групп цифр, разделенных нецифровыми символами
    cleaned_text = re.sub(r'(\d)\s*([^\d\s]+)\s*(\d)', r'\1\3', text)

    # В случае если после первой замены остались еще пробелы между цифрами
    while re.search(r'(\d)\s+(\d)', cleaned_text):
        cleaned_text = re.sub(r'(\d)\s+(\d)', r'\1\2', cleaned_text)

    cleaned_text = cleaned_text.replace("ё", "е")

    return cleaned_text
def find_input_selector_by_label(data, target_label, parent=None):
    # Проверка, есть ли 'children' в текущем элементе
    if 'children' in data:
        # Итерация по всем дочерним элементам
        for child in data['children']:
            # Рекурсивный вызов функции для каждого дочернего элемента
            result = find_input_selector_by_label(child, target_label, data)
            if result:
                return result

    # Проверяем, является ли текущий элемент тем, что мы ищем
    if data.get('tagName') == 'LABEL' and target_label.lower() in data.get('textContent', '').lower():
        # Ищем следующий input элемент в родительском контейнере
        # parent = data.get('parent')
        if parent:
            # Итерируем по детям родительского элемента чтобы найти input
            for sibling in parent['children']:
                if sibling.get('tagName') == 'INPUT':
                    return sibling.get('selector')
                for sibling2 in sibling['children']:
                    if sibling2.get('tagName') == 'INPUT':
                        return sibling2.get('selector')
    return None

def collect_all_labels(data):
    labels = []

    def recurse_elements(element):
        # Если у элемента есть дети, рекурсивно обрабатываем каждый дочерний элемент
        if 'children' in element:
            for child in element['children']:
                recurse_elements(child)

        # Проверяем, является ли элемент label
        if element.get('tagName') == 'LABEL':
            # Добавляем текст label в список
            labels.append(element.get('textContent', '').strip())

    # Начинаем рекурсию с корневого элемента
    recurse_elements(data)
    return labels

def extract_form_data(command, labels):
    # Список для хранения результатов
    field_values = {}

    # Создаем паттерн регулярного выражения, который ищет метки и следующие за ними значения
    # Метки должны быть разделены запятой или точкой с запятой для четкости извлечения
    for label in labels:
        # Экранируем метки, которые могут содержать специальные символы для регулярных выражений
        escaped_label = re.escape(label)
        # Ищем значения, которые следуют сразу после метки, до запятой или конца строки
        pattern = rf"{escaped_label}\s*[:\-]?\s*([^\,; ]+)"
        match = re.search(pattern, command)
        if match:
            # Записываем найденные значения в словарь
            field_values[label] = match.group(1).strip()

    return field_values

    # # Регулярные выражения для извлечения данных
    # patterns = {
    #     "имя": r"имя\s+([^\,]+),",
    #     "фамилия": r"фамилия\s+([^\,]+),",
    #     "адрес электронной почты": r"адрес электронной почты\s+([^\,]+) и"
    # }
    #
    # # Перебираем шаблоны и ищем совпадения
    # for field, pattern in patterns.items():
    #     match = re.search(pattern, command)
    #     if match:
    #         # Добавляем найденные значения в список
    #         fields.append({
    #             "field": field,
    #             "value": match.group(1).strip()
    #         })

    # Проверяем наличие команды на нажатие кнопки
    button_match = re.search(r"нажми кнопку '(\w+)'", command)
    if button_match:
        fields.append({
            "field": "button",
            "value": button_match.group(1)
        })

    return fields