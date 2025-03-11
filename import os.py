import os
from pathlib import Path
from typing import Optional, Callable, TypeVar, Generic

T = TypeVar('T')

class FileHandler:
    @staticmethod
    def create_path_object(path_to_validate: str, parent_path: Path = Path("")) -> Path:
        path = parent_path / Path(path_to_validate)
        if not path.exists():
            if path.suffix:
                try:
                    path.touch()
                except IOError as e:
                    raise IOError(f"Fatal error while creating/opening path object: {path}") from e
            else:
                path.mkdir(parents=True)
        return path

class File(Generic[T]):
    def __init__(self, file_path: Path, mode: str):
        self.file_path = file_path
        self.file = open(file_path, mode)
        self.size = self._to_element_size(os.path.getsize(file_path))
        self.write_index = self.file.tell()
        self.read_index = 0

    def get_size(self) -> int:
        return self.size

    def _to_byte_size(self, num_of_items: int) -> int:
        return num_of_items * self._item_size()

    def _to_element_size(self, num_of_bytes: int) -> int:
        return num_of_bytes // self._item_size()

    def _item_size(self) -> int:
        return 1 if isinstance(self, TextFile) else T.__sizeof__()

    def is_write_index_valid(self, index: int) -> bool:
        return self.size >= index

    def is_read_index_valid(self, index: int) -> bool:
        return self.size > index

    def is_within_range(self, index: int, count: int) -> bool:
        return count <= self.size and (index + count) > self.size

    def write_data(self, source: T, write_func: Callable[[T], None], index: Optional[int] = None):
        if source is None:
            raise ValueError("A None value was passed when calling File.write_data")

        current_index = self._to_byte_size(index) if index is not None else self.write_index

        if not self.is_write_index_valid(current_index):
            raise ValueError("An invalid index was passed when calling File.write_data")

        self.file.seek(current_index)
        write_func(source)
        current_byte_index = self.file.tell()

        if current_byte_index > self.write_index:
            self.write_index = current_byte_index
            self.size = self.write_index

    def read_data(self, count: int, index: Optional[int] = None) -> T:
        if count == 0:
            return None

        current_index = self._to_byte_size(index) if index is not None else self.read_index

        if not self.is_read_index_valid(current_index):
            if index is not None:
                raise ValueError("An invalid index was passed when calling File.read_data")
            current_index = 0

        bytes_to_read = self._to_byte_size(count)

        if self.is_within_range(current_index, bytes_to_read):
            raise IndexError("The required amount of data to read exceeds the existent data")

        self.file.seek(current_index)
        data = self.file.read(bytes_to_read)
        self.read_index = current_index + bytes_to_read
        return data

    def __del__(self):
        self.file.close()

class BinaryFile(File[bytes]):
    def __init__(self, path: Path):
        super().__init__(path, 'r+b')

    def write(self, source: bytes, count: int = 1, index: Optional[int] = None):
        count_in_bytes = self._to_byte_size(count)
        self.write_data(source, lambda data: self.file.write(data), index)

    def read(self, count: int = 1, index: Optional[int] = None) -> bytes:
        return self.read_data(count, index)

class TextFile(File[str]):
    def __init__(self, path: Path):
        super().__init__(path, 'r+')
        self.init_props()

    def init_props(self):
        self.file.seek(0, os.SEEK_END)
        self.write_index = self.file.tell()
        self.size = self.write_index

        self.file.seek(0, os.SEEK_SET)
        self.read_index = self.file.tell()

    def write(self, data: str, index: Optional[int] = None):
        self.write_data(data, lambda d: self.file.write(d), index)

    def read(self, count: int = 1, index: Optional[int] = None) -> str:
        target = ['\0'] * count
        data = super().read_data(count, index)
        if data:
            target[:len(data)] = data
        return ''.join(target)

# Usage Example
path = FileHandler.create_path_object("example.txt")
text_file = BinaryFile(path)
text_file.write("Hello, World!")
#print(text_file.read(5))


