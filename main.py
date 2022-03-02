# Task 312. Яндекс.Диск

from ya_disk import YandexDisk

TOKEN = "AQA...E9D1"


if __name__ == '__main__':
    ya = YandexDisk(token=TOKEN)
    ya.upload_file_to_disk("test_yadisk_api.txt", "test_yadisk_api.txt")
