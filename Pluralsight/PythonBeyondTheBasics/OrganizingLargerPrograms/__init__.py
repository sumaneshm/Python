# if we put the following line, Reader class will be made available for anybody
# who imports this package directly at the package level
# (as Reader) otherwise they need to use the format
# OrganizingLargerPrograms.reader.Reader

from .reader import Reader
