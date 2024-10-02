
# import time
# from samisco import retry
#
# # Decorators
#
# @retry(retries=4, delay=1)
# def connect() -> None:
#     time.sleep(1)
#     raise Exception('Could not connect to the internet...')
#
#
# def main() -> None:
#     connect()
#
#
# if __name__ == '__main__':
#     main()
import time
from functools import cache


@cache
def count_vowels(text: str) -> int:
    vowel_count: int = 0

    # Pretend it's an expensive operation
    print(f'Bot: Counting vowels in: "{text}"...')
    time.sleep(2)

    # Count those damn vowels
    for letter in text:
        if letter in 'aeiouAEIOU':
            vowel_count += 1

    return vowel_count


def main() -> None:
    print(count_vowels('Bob'))
    print(count_vowels('Bob'))
    print(count_vowels('Bob'))
    print(count_vowels.cache_info())
    count_vowels.cache_clear()
    print(count_vowels('Sam'))


if __name__ == '__main__':
    main()