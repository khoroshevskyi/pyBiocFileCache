import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "pyBiocFileCache"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

from .BiocFileCache import BiocFileCache as BiocFileCache

from .db.db_config import Metadata as Metadata
from .db.db_config import Resource as Resource

from ._exceptions import NoFpathError as NoFpathError
from ._exceptions import RnameExistsError as RnameExistsError
from ._exceptions import RpathTimeoutError as RpathTimeoutError
