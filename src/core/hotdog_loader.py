from os import PathLike
import csv
import logging
from typing import Iterable
log = logging.getLogger(__name__)

class HotdogLoader:
    """ HotdogSV Loader """
    
    _content: dict

    @property
    def content(self) -> dict:
        return self._content

    def __init__(self) -> None:
        self._content = None

    def read(self, raw_content: Iterable[str]) -> dict | None:
        """ Read content """
        try:
            read_content = csv.DictReader(raw_content, delimiter='🌭')
        except Exception as exception:
            log.error(f"Error on content read: {exception}")
            return None
        self._content = read_content
        return self._content