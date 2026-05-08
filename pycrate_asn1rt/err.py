# -*- coding: UTF-8 -*-
#/**
# * Software Name : pycrate
# * Version : 0.4
# *
# * Copyright 2017. Benoit Michau. ANSSI.
# *
# * This library is free software; you can redistribute it and/or
# * modify it under the terms of the GNU Lesser General Public
# * License as published by the Free Software Foundation; either
# * version 2.1 of the License, or (at your option) any later version.
# *
# * This library is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# * Lesser General Public License for more details.
# *
# * You should have received a copy of the GNU Lesser General Public
# * License along with this library; if not, write to the Free Software
# * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
# * MA 02110-1301  USA
# *
# *--------------------------------------------------------
# * File Name : pycrate_asn1rt/err.py
# * Created : 2016-03-02
# * Authors : Benoit Michau 
# *--------------------------------------------------------
#*/

#------------------------------------------------------------------------------#
# ASN.1 runtime errors
#------------------------------------------------------------------------------#

from typing import Any

from pycrate_core.utils import PycrateErr


# generic ASN.1 error
class ASN1Err(PycrateErr):
    pass

# error when manipulating an existing ASN1 object
class ASN1ObjErr(ASN1Err):
    pass

class ASN1ObjValErr(ASN1ObjErr):
    """Custom validation error."""
    INVALID_VALUE = 0
    MISSING_MANDATORY_KEY = 1
    INVALID_KEY = 2
    OUT_OF_CONSTRAINT = 3
    INVALID_STRUCTURE = 4

    def __init__(self, key: str, val, msg: str, code: int):
        """Initialization for the ASN1ObjValErr exception.

        Args:
            key: the key whose value is invalid
            val: the invalid value
            msg: the error message
            code: one of the error code class constants
        """
        self.key = key
        self.val = val
        self.msg = msg
        self.code = code
        super().__init__(f"key={repr(key)}, message={repr(msg)}, val={repr(val)}")

    def __repr__(self):
        return f"ASN1ObjValErr[key={repr(self.key)}, code={self.code}, msg={repr(self.msg)}, val={repr(self.val)}]"


# error when encountering an unsupported case
class ASN1NotSuppErr(ASN1Err):
    pass

# ASN.1 codecs errors: generic, ASN, PER, UPER, BER, CER, DER, JER, GSER
class ASN1CodecErr(ASN1Err):
    pass

class ASN1ASNEncodeErr(ASN1CodecErr):
    pass

class ASN1ASNDecodeErr(ASN1CodecErr):
    pass

class ASN1PEREncodeErr(ASN1CodecErr):
    pass

class ASN1PERDecodeErr(ASN1CodecErr):
    pass

class ASN1BEREncodeErr(ASN1CodecErr):
    pass

class ASN1BERDecodeErr(ASN1CodecErr):
    pass

class ASN1JEREncodeErr(ASN1CodecErr):
    pass

class ASN1JERDecodeErr(ASN1CodecErr):
    pass

#class ASN1GSEREncodeErr(ASN1CodecErr):
#    pass
#
#class ASN1GSERDecodeErr(ASN1CodecErr):
#    pass

class ASN1OERDecodeErr(ASN1CodecErr):
    pass

class ASN1OEREncodeErr(ASN1CodecErr):
    pass
