
import random

def test_generate_random_numbers(numbers_service):

    gen_result = numbers_service.generate_random_numbers()

    assert len(gen_result) > 0
    assert all(elem >= 1 and elem <= 49 for elem in gen_result)


def test_create_dict(numbers_service):

    test_files_list = [
        'test'
        for _ in range(11)
    ]

    numbers = numbers_service.generate_random_numbers()

    dict_result = numbers_service.create_dict(
        numbers=numbers,
        file_paths=test_files_list
    )

    assert set(dict_result.keys()) == numbers
