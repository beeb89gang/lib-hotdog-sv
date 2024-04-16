from os import PathLike
from typing import Iterable
from core.hotdog_file_loader import HotdogFileLoader
from core.hotdog_loader import HotdogLoader

class HotdogParser:
    """ Hotdog Parser Facades """

    loader: HotdogLoader | None
    filename: PathLike | str | None
    raw_content: Iterable[str] | None
    encoding: str | None

    def __init__(self, 
                 filename: PathLike | str | None = None, 
                 raw_content: Iterable[str] | None = None, 
                 encoding: str | None = None
        ) -> None:
        if filename is not None and raw_content is not None:
            raise ValueError('Too many arguments for HotdogParser. Choose between filename or raw_content.')
        elif filename is None and raw_content is None:
            raise ValueError('Please provide at least filename or raw_content.')
        self.loader = None
        self.filename = filename
        self.raw_content = raw_content

    def __enter__(self):
        if self.filename is not None:
            self.loader = HotdogFileLoader()
            self.loader.open(file=self.filename, encoding=self.encoding)
        elif self.raw_content is not None:
            self.loader = HotdogLoader()
            self.loader.read(raw_content=self.raw_content)
        return self.loader.content
    
    def __exit__(self, exception_type, exception_value, exception_traceback):
        self.loader = None
