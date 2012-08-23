"""
ssl_test.py

Some distributions like to still enable SSLv2 in their OpenSSL binaries (*cough*Arch Linux*/cough*).

This is a simple testing script to check if SSLv2 is available.

Due to the weaknesses in SSLv2, it is highly advisable to at the bare minimum allow SSLv23, which
prefers the use of SSLv3, but falls back to v2 if v3 is not an option.
"""
def check():
    """
    Below is a doctest to ensure everything runs fine.
    
    >>> check()
    0
    """
    import ssl
    
    found = 0
    
    for _,name in ssl._PROTOCOL_NAMES.items():
        if name == "SSLv2":
            found = 1
            break
        
    return found

import doctest

if __name__ == "__main__":
    doctest.testmod(m = None, verbose = True)