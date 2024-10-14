from datetime import datetime, timedelta

def calculate_future_date(days):
    today = datetime.now()
    future_date = today + timedelta(days=days)
    return future_date

def display_future_date(days):
    future_date = calculate_future_date(days)
    formatted_date = future_date.strftime('%Y-%m-%d')
    print(f"Дата через {days} дней: {formatted_date}")
days = int(input("Введите количество дней: "))
display_future_date(days)
