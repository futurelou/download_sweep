#defines a valid list of handlers 

from enum import Enum
class HandlerType(Enum):
    SFTP = 'sftp'
    FTP = 'ftp'
    FILE = 'file'
    RSYNC = 'rsync'
    TELNET = 'telnet'

    @classmethod 
    def has_value(cls, value):
        return cls._value2member_map_


    @classmethod
    def has_member(cls, value):
        return value in cls._member_names_
    
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
    