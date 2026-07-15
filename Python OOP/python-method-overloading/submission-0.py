class TextProcessor:
    # Implement method overloading for format_text method
    pass

    def format_text(self, text1: str, text2 = "") -> str:
        if text2:
            text1 += text2
        else:
            text1 = text1.upper()
        return text1



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
