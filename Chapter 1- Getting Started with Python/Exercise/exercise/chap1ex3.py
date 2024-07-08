from datetime import datetime

def print_current_date_time():
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_time}")

print_current_date_time()
