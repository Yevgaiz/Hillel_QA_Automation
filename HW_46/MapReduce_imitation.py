import os
import random
import string
import threading
import multiprocessing
import time


def file_generator(directory, number_of_files, size):
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_files):
        file_name = f"file_{i}.txt"
        file_path = os.path.join(directory, file_name)
        num_chars = random.randint(size // 2, size)
        content = ''.join(random.choices(
            string.ascii_letters + string.digits + string.punctuation, k=num_chars))

        with open(file_path, 'w') as f:
            f.write(content)


def count_letters_in_files(files, letter_to_find):
    count = 0
    for file_path in files:
        with open(file_path, 'r') as f:
            content = f.read()
            count += content.count(letter_to_find)
    return count


def letter_counter_in_one_thread(directory, letter_to_find):
    files = [os.path.join(directory, file_name) for file_name in os.listdir(directory) if
             os.path.isfile(os.path.join(directory, file_name))]
    return count_letters_in_files(files, letter_to_find)


def count_letters_thread(files, letter_to_find, result, index):
    result[index] = count_letters_in_files(files, letter_to_find)


def letter_counter_in_threads(directory, letter_to_find, number_of_threads):
    files = [os.path.join(directory, file_name) for file_name in os.listdir(directory) if
             os.path.isfile(os.path.join(directory, file_name))]
    files_split = [files[i::number_of_threads] for i in range(number_of_threads)]
    result = [0] * number_of_threads
    threads = []

    for i in range(number_of_threads):
        thread = threading.Thread(target=count_letters_thread, args=(files_split[i], letter_to_find, result, i))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return sum(result)


def count_letters_process(files, letter_to_find, result_queue):
    result_queue.put(count_letters_in_files(files, letter_to_find))


def letter_counter_in_processes(directory, letter_to_find, number_of_processes):
    files = [os.path.join(directory, file_name) for file_name in os.listdir(directory) if
             os.path.isfile(os.path.join(directory, file_name))]
    files_split = [files[i::number_of_processes] for i in range(number_of_processes)]
    result_queue = multiprocessing.Queue()
    processes = []

    for i in range(number_of_processes):
        process = multiprocessing.Process(target=count_letters_process,
                                          args=(files_split[i], letter_to_find, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_count = 0
    while not result_queue.empty():
        total_count += result_queue.get()

    return total_count


def main():
    directory = "files"
    number_of_files = 100
    size = 100_000
    letter_to_find = 'a'
    number_of_threads = 4
    number_of_processes = 4

    print("Generating files...")
    file_generator(directory, number_of_files, size)

    start_time = time.time()
    letter_counter_in_one_thread(directory, letter_to_find)
    end_time = time.time()
    print(f"Time taken in one thread: {end_time - start_time} seconds")

    start_time = time.time()
    letter_counter_in_threads(directory, letter_to_find, number_of_threads)
    end_time = time.time()
    print(f"Time taken in multiple threads: {end_time - start_time} seconds")

    start_time = time.time()
    letter_counter_in_processes(directory, letter_to_find, number_of_processes)
    end_time = time.time()
    print(f"Time taken in multiple processes: {end_time - start_time} seconds")


if __name__ == "__main__":
    main()
