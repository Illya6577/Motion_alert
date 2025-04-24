import serial
import time
import requests

# Налаштування Telegram бота
BOT_TOKEN = 'YOUR_BOT_TOKEN'
CHAT_ID = 'YOUR_CHAT_ID'
TELEGRAM_URL = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Функція для відправки повідомлення в Telegram
def send_telegram(message: str):
    try:
        payload = {'chat_id': CHAT_ID, 'text': message}
        response = requests.post(TELEGRAM_URL, data=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Помилка при надсиланні повідомлення в Telegram: {e}")


def main():
    # Відкриваємо послідовний порт COM10 (скоригуйте baudrate за потреби)
    try:
        ser = serial.Serial('COM10', baudrate=9600, timeout=1)
        print("Моніторинг COM10 запущено...")
    except serial.SerialException as e:
        print(f"Не вдалося відкрити COM10: {e}")
        return

    # Час останнього відправлення повідомлення
    last_sent_time = 0
    # Інтервал для повторного сповіщення (в секундах)
    resend_interval = 10

    while True:
        try:
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            if 'Motion!' in line:
                current_time = time.time()
                # Перевіряємо, чи минуло достатньо часу з моменту останнього повідомлення
                if current_time - last_sent_time >= resend_interval:
                    print("Motion detected")
                    send_telegram("Motion!")
                    last_sent_time = current_time

            # Коротка пауза, щоб уникнути надмірного навантаження
            time.sleep(0.1)

        except serial.SerialException as e:
            print(f"Помилка послідовного порту: {e}")
            time.sleep(5)
        except Exception as e:
            print(f"Невідома помилка: {e}")
            time.sleep(1)


if __name__ == "__main__":
    main()
