"""
Write a function that takes directory path, a file extension
and an optional tokenizer.
It will count lines in all files with that extension if
there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
universal_file_counter(test, "txt")
6
universal_file_counter(test, "txt", str.split)
6
"""
import os
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(dir_path: Path, file_extension: str,
                           tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    os.chdir(dir_path)
    for file in os.listdir(dir_path):
        if file.endswith(file_extension):
            with open(file) as f:
                while True:
                    text = f.readline()
                    if text:
                        if tokenizer:
                            counter += len(tokenizer(text))
                        else:
                            counter += 1
                    else:
                        break
    return counter
