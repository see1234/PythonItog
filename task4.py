import argparse

def main():
  parser = argparse.ArgumentParser(description="Обработка чисел и строк.")

  parser.add_argument("number", type=int, help="Целое число")
  parser.add_argument("text", type=str, help="Строка")
  parser.add_argument("--verbose", action="store_true", help="Включить подробный вывод")
  parser.add_argument("--repeat", type=int, default=1, help="Количество повторений строки")

  args = parser.parse_args()

  if args.verbose:
    print(f"Полученное число: {args.number}")
    print(f"Полученная строка: {args.text}")

  repeated_text = args.text * args.repeat
  print(repeated_text)

