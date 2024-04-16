from os import PathLike
import logging
from .hotdog_loader import HotdogLoader
log = logging.getLogger(__name__)

class HotdogFileLoader(HotdogLoader): 
    """ HotdogSV file Loader """
    
    _file_content: str

    @property
    def file_content(self) -> str:
        return self._file_content

    def __init__(self) -> None:
        self._file_content = None
        self._content = None

    def open(self, file: PathLike | str, encoding: str | None = None) -> bool:
        """ Open a file """
        try:
            raw_content = open(file=file, encoding=encoding, mode='r')
        except OSError as exception:
            log.error(f"Error on file loading: {exception}")
            return False
        self._file_content = raw_content
        self.read(self._file_content)
        raw_content.close()
        return True