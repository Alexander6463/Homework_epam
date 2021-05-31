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
from pathlib import Path
from typing import Callable, Optional


def universal_file_counter(dir_path: Path, file_extension: str,
                           tokenizer: Optional[Callable] = None) -> int:
    counter = 0
    p = Path(dir_path)
    for file in list(p.glob('*.'+str(file_extension))):
        with file.open() as f:
            text = f.read().split('\n')
        for line in text:
            if tokenizer:
                counter += len(tokenizer(line))
            else:
                counter += 1
    return counter
