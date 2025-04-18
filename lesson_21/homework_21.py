"""
Моніторингова система клєнта надсилає сигнал, що вона працездатна кожні 30-31 сек -
наприклад Timestamp 05:45:40, а в наступному повідомлені — Timestamp 05:45:09
(тут різниця heartbeat в 31 секунду)

Є декілька дублючих потоків, що шлють дані одночасно, тож ми можемо проаналізувати лише один потік -
Key TSTFEED0300|7E3E|0400

Засобами автоматизації проаналізуйте наданий нам лог: hblog.txt
    1. відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
    2. Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
        - для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
        - для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
    3.Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.

Обов’язково включіть результат роботи — файл hb_test.log в PR.

Підказка 1
    1. Прочитайте файл по строкам, якщо забули як - зверніться до 12 лекції.
    2. Виберіть строки з необхідним значенням:
        filtered_log = []
        if "key" in "long log string with key":
            filtered_log.append("long log string with key")

Підказка 2
    1. Пошук часу у строці можна зробити методом .find("Timestamp ") і повернути наступні 8 символів
    2. перетворити строку в час дозволяє метод .strptime("10:00:00", "%H:%M:%S")
    3. Значення слід аналізувати парами - від поточного відняти наступне і залогувати
    (або не залогувати) результат
"""

from pathlib import Path
from datetime import datetime
import logging

logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(levelname)s: %(message)s"
)
logger = logging.getLogger(__name__)

def heartbeat_analyzing(source, file):
    input_file = Path(__file__).parent / file
    by_lines = input_file.read_text(encoding='utf-8').splitlines()

    time_format = '%H:%M:%S'
    prev_time = None

    for line in reversed(by_lines):
        if source in line and 'Timestamp' in line:
            timestamp_part = line.split('Timestamp')[1]
            timestamp_str = timestamp_part.split()[0]
            current_time = datetime.strptime(timestamp_str, time_format)
            if prev_time is not None:
                sec = (current_time - prev_time).total_seconds()
                if 31 < sec < 33:
                    logger.warning(timestamp_str)
                if sec >= 33:
                    logger.error(timestamp_str)
                if sec < 30:
                    logger.info(timestamp_str) # мені здалось такий кейс теж потрібно обробити
            prev_time = current_time

if __name__ == "__main__":
    heartbeat_analyzing('TSTFEED0300|7E3E|0400', 'hblog.txt')