import re

class TextProcessor:
    def __init__(self):
        pass

    def process_1word(self, word: str) -> str:
        if not word:
            return word

        first_char = word[0]
        first_char_lower = first_char.lower()

        result = first_char
        for char in word[1:]:
            if char.lower() != first_char_lower:
                result += char
        return result

    def process_text(self, text: str) -> str:
        parts = re.split(r'([a-zA-Zа-яА-ЯіІїЇєЄґҐ]+)', text)

        processed_parts = []
        for part in parts:
            if part.isalpha():
                processed_parts.append(self.process_1word(part))
            else:
                processed_parts.append(part)
        return "".join(processed_parts)

if __name__ == "__main__":
    processor = TextProcessor()

    print("Введіть текст одним рядком.\nДля виводу результату натисніть Enter, а для повного закриття програми напишіть exit або вихід")
    while True:
        user_input = input("Ваш текст: ")
        if user_input.lower() in ['exit', 'вихід']:
            break

        result = processor.process_text(user_input)
        print(f"Результат:  {result}\n")
