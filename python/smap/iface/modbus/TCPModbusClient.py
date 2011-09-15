# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _TCPModbusClient
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


RCVBUFSIZE = _TCPModbusClient.RCVBUFSIZE
ARGS_QUERY = _TCPModbusClient.ARGS_QUERY
ARGS_READ = _TCPModbusClient.ARGS_READ
ARGS_WRITE = _TCPModbusClient.ARGS_WRITE
ARGS_WRITEM_REGVAL_POS = _TCPModbusClient.ARGS_WRITEM_REGVAL_POS
prepare_msg_query = _TCPModbusClient.prepare_msg_query
prepare_msg_read = _TCPModbusClient.prepare_msg_read
prepare_msg_write = _TCPModbusClient.prepare_msg_write
prepare_msg_writem = _TCPModbusClient.prepare_msg_writem
execute_command = _TCPModbusClient.execute_command
print_received_msg = _TCPModbusClient.print_received_msg
dev_query = _TCPModbusClient.dev_query
dev_read = _TCPModbusClient.dev_read
dev_write = _TCPModbusClient.dev_write
dev_writem = _TCPModbusClient.dev_writem
get_val = _TCPModbusClient.get_val
SUCCESS = _TCPModbusClient.SUCCESS
FAIL = _TCPModbusClient.FAIL
CRC16_SIZE = _TCPModbusClient.CRC16_SIZE
MODBUS_FUNC_READ_REG = _TCPModbusClient.MODBUS_FUNC_READ_REG
MODBUS_FUNC_WRITE_REG = _TCPModbusClient.MODBUS_FUNC_WRITE_REG
MODBUS_FUNC_WRITE_MULTIREG = _TCPModbusClient.MODBUS_FUNC_WRITE_MULTIREG
MODBUS_FUNC_REPORT_SLAVEID = _TCPModbusClient.MODBUS_FUNC_REPORT_SLAVEID
MODBUS_ERR_READ_REG = _TCPModbusClient.MODBUS_ERR_READ_REG
MODBUS_ERR_WRITE_REG = _TCPModbusClient.MODBUS_ERR_WRITE_REG
MODBUS_ERR_WRITE_MULTIREG = _TCPModbusClient.MODBUS_ERR_WRITE_MULTIREG
MODBUS_ERR_REPORT_SLAVEID = _TCPModbusClient.MODBUS_ERR_REPORT_SLAVEID
BYTEPOS_MODBUS_ADDR = _TCPModbusClient.BYTEPOS_MODBUS_ADDR
BYTEPOS_MODBUS_FUNC = _TCPModbusClient.BYTEPOS_MODBUS_FUNC
BYTEPOS_MODBUS_EXCEPTION_CODE = _TCPModbusClient.BYTEPOS_MODBUS_EXCEPTION_CODE
MODBUS_REG_READ_QTY_DEFAULT = _TCPModbusClient.MODBUS_REG_READ_QTY_DEFAULT
MODBUS_REG_READ_QTY_MIN = _TCPModbusClient.MODBUS_REG_READ_QTY_MIN
MODBUS_REG_READ_QTY_MAX = _TCPModbusClient.MODBUS_REG_READ_QTY_MAX
MODBUS_RUN_INDICATOR_ON = _TCPModbusClient.MODBUS_RUN_INDICATOR_ON
MODBUS_RUN_INDICATOR_OFF = _TCPModbusClient.MODBUS_RUN_INDICATOR_OFF
class modbus_req_read_reg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_req_read_reg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_req_read_reg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_read_reg_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_read_reg_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_req_read_reg_modbus_addr_get, _TCPModbusClient.modbus_req_read_reg_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_req_read_reg_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_req_read_reg_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_req_read_reg_modbus_func_get, _TCPModbusClient.modbus_req_read_reg_modbus_func_set)
    __swig_setmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_req_read_reg_modbus_reg_addr_set
    __swig_getmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_req_read_reg_modbus_reg_addr_get
    if _newclass:modbus_reg_addr = _swig_property(_TCPModbusClient.modbus_req_read_reg_modbus_reg_addr_get, _TCPModbusClient.modbus_req_read_reg_modbus_reg_addr_set)
    __swig_setmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_req_read_reg_modbus_reg_qty_set
    __swig_getmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_req_read_reg_modbus_reg_qty_get
    if _newclass:modbus_reg_qty = _swig_property(_TCPModbusClient.modbus_req_read_reg_modbus_reg_qty_get, _TCPModbusClient.modbus_req_read_reg_modbus_reg_qty_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_req_read_reg(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_req_read_reg
    __del__ = lambda self : None;
modbus_req_read_reg_swigregister = _TCPModbusClient.modbus_req_read_reg_swigregister
modbus_req_read_reg_swigregister(modbus_req_read_reg)

class modbus_req_write_reg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_req_write_reg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_req_write_reg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_write_reg_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_write_reg_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_req_write_reg_modbus_addr_get, _TCPModbusClient.modbus_req_write_reg_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_req_write_reg_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_req_write_reg_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_req_write_reg_modbus_func_get, _TCPModbusClient.modbus_req_write_reg_modbus_func_set)
    __swig_setmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_req_write_reg_modbus_reg_addr_set
    __swig_getmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_req_write_reg_modbus_reg_addr_get
    if _newclass:modbus_reg_addr = _swig_property(_TCPModbusClient.modbus_req_write_reg_modbus_reg_addr_get, _TCPModbusClient.modbus_req_write_reg_modbus_reg_addr_set)
    __swig_setmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_req_write_reg_modbus_reg_val_set
    __swig_getmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_req_write_reg_modbus_reg_val_get
    if _newclass:modbus_reg_val = _swig_property(_TCPModbusClient.modbus_req_write_reg_modbus_reg_val_get, _TCPModbusClient.modbus_req_write_reg_modbus_reg_val_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_req_write_reg(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_req_write_reg
    __del__ = lambda self : None;
modbus_req_write_reg_swigregister = _TCPModbusClient.modbus_req_write_reg_swigregister
modbus_req_write_reg_swigregister(modbus_req_write_reg)

class modbus_req_write_multireg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_req_write_multireg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_req_write_multireg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_write_multireg_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_write_multireg_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_req_write_multireg_modbus_addr_get, _TCPModbusClient.modbus_req_write_multireg_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_req_write_multireg_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_req_write_multireg_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_req_write_multireg_modbus_func_get, _TCPModbusClient.modbus_req_write_multireg_modbus_func_set)
    __swig_setmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_req_write_multireg_modbus_reg_addr_set
    __swig_getmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_req_write_multireg_modbus_reg_addr_get
    if _newclass:modbus_reg_addr = _swig_property(_TCPModbusClient.modbus_req_write_multireg_modbus_reg_addr_get, _TCPModbusClient.modbus_req_write_multireg_modbus_reg_addr_set)
    __swig_setmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_req_write_multireg_modbus_reg_qty_set
    __swig_getmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_req_write_multireg_modbus_reg_qty_get
    if _newclass:modbus_reg_qty = _swig_property(_TCPModbusClient.modbus_req_write_multireg_modbus_reg_qty_get, _TCPModbusClient.modbus_req_write_multireg_modbus_reg_qty_set)
    __swig_setmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_req_write_multireg_modbus_val_bytes_set
    __swig_getmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_req_write_multireg_modbus_val_bytes_get
    if _newclass:modbus_val_bytes = _swig_property(_TCPModbusClient.modbus_req_write_multireg_modbus_val_bytes_get, _TCPModbusClient.modbus_req_write_multireg_modbus_val_bytes_set)
    __swig_setmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_req_write_multireg_modbus_reg_val_set
    __swig_getmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_req_write_multireg_modbus_reg_val_get
    if _newclass:modbus_reg_val = _swig_property(_TCPModbusClient.modbus_req_write_multireg_modbus_reg_val_get, _TCPModbusClient.modbus_req_write_multireg_modbus_reg_val_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_req_write_multireg(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_req_write_multireg
    __del__ = lambda self : None;
modbus_req_write_multireg_swigregister = _TCPModbusClient.modbus_req_write_multireg_swigregister
modbus_req_write_multireg_swigregister(modbus_req_write_multireg)

class modbus_req_report_slaveid(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_req_report_slaveid, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_req_report_slaveid, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_report_slaveid_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_req_report_slaveid_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_req_report_slaveid_modbus_addr_get, _TCPModbusClient.modbus_req_report_slaveid_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_req_report_slaveid_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_req_report_slaveid_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_req_report_slaveid_modbus_func_get, _TCPModbusClient.modbus_req_report_slaveid_modbus_func_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_req_report_slaveid(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_req_report_slaveid
    __del__ = lambda self : None;
modbus_req_report_slaveid_swigregister = _TCPModbusClient.modbus_req_report_slaveid_swigregister
modbus_req_report_slaveid_swigregister(modbus_req_report_slaveid)

class modbus_reply_read_reg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_reply_read_reg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_reply_read_reg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_read_reg_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_read_reg_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_reply_read_reg_modbus_addr_get, _TCPModbusClient.modbus_reply_read_reg_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_read_reg_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_read_reg_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_reply_read_reg_modbus_func_get, _TCPModbusClient.modbus_reply_read_reg_modbus_func_set)
    __swig_setmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_reply_read_reg_modbus_val_bytes_set
    __swig_getmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_reply_read_reg_modbus_val_bytes_get
    if _newclass:modbus_val_bytes = _swig_property(_TCPModbusClient.modbus_reply_read_reg_modbus_val_bytes_get, _TCPModbusClient.modbus_reply_read_reg_modbus_val_bytes_set)
    __swig_setmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_reply_read_reg_modbus_reg_val_set
    __swig_getmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_reply_read_reg_modbus_reg_val_get
    if _newclass:modbus_reg_val = _swig_property(_TCPModbusClient.modbus_reply_read_reg_modbus_reg_val_get, _TCPModbusClient.modbus_reply_read_reg_modbus_reg_val_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_reply_read_reg(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_reply_read_reg
    __del__ = lambda self : None;
modbus_reply_read_reg_swigregister = _TCPModbusClient.modbus_reply_read_reg_swigregister
modbus_reply_read_reg_swigregister(modbus_reply_read_reg)

class modbus_reply_write_reg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_reply_write_reg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_reply_write_reg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_write_reg_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_write_reg_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_reply_write_reg_modbus_addr_get, _TCPModbusClient.modbus_reply_write_reg_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_write_reg_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_write_reg_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_reply_write_reg_modbus_func_get, _TCPModbusClient.modbus_reply_write_reg_modbus_func_set)
    __swig_setmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_reply_write_reg_modbus_reg_addr_set
    __swig_getmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_reply_write_reg_modbus_reg_addr_get
    if _newclass:modbus_reg_addr = _swig_property(_TCPModbusClient.modbus_reply_write_reg_modbus_reg_addr_get, _TCPModbusClient.modbus_reply_write_reg_modbus_reg_addr_set)
    __swig_setmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_reply_write_reg_modbus_reg_val_set
    __swig_getmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_reply_write_reg_modbus_reg_val_get
    if _newclass:modbus_reg_val = _swig_property(_TCPModbusClient.modbus_reply_write_reg_modbus_reg_val_get, _TCPModbusClient.modbus_reply_write_reg_modbus_reg_val_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_reply_write_reg(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_reply_write_reg
    __del__ = lambda self : None;
modbus_reply_write_reg_swigregister = _TCPModbusClient.modbus_reply_write_reg_swigregister
modbus_reply_write_reg_swigregister(modbus_reply_write_reg)

class modbus_reply_write_multireg(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_reply_write_multireg, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_reply_write_multireg, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_reply_write_multireg_modbus_addr_get, _TCPModbusClient.modbus_reply_write_multireg_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_reply_write_multireg_modbus_func_get, _TCPModbusClient.modbus_reply_write_multireg_modbus_func_set)
    __swig_setmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_reg_addr_set
    __swig_getmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_reg_addr_get
    if _newclass:modbus_reg_addr = _swig_property(_TCPModbusClient.modbus_reply_write_multireg_modbus_reg_addr_get, _TCPModbusClient.modbus_reply_write_multireg_modbus_reg_addr_set)
    __swig_setmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_reg_qty_set
    __swig_getmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_reply_write_multireg_modbus_reg_qty_get
    if _newclass:modbus_reg_qty = _swig_property(_TCPModbusClient.modbus_reply_write_multireg_modbus_reg_qty_get, _TCPModbusClient.modbus_reply_write_multireg_modbus_reg_qty_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_reply_write_multireg(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_reply_write_multireg
    __del__ = lambda self : None;
modbus_reply_write_multireg_swigregister = _TCPModbusClient.modbus_reply_write_multireg_swigregister
modbus_reply_write_multireg_swigregister(modbus_reply_write_multireg)

class modbus_reply_report_slaveid(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_reply_report_slaveid, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_reply_report_slaveid, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_reply_report_slaveid_modbus_addr_get, _TCPModbusClient.modbus_reply_report_slaveid_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_reply_report_slaveid_modbus_func_get, _TCPModbusClient.modbus_reply_report_slaveid_modbus_func_set)
    __swig_setmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_val_bytes_set
    __swig_getmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_val_bytes_get
    if _newclass:modbus_val_bytes = _swig_property(_TCPModbusClient.modbus_reply_report_slaveid_modbus_val_bytes_get, _TCPModbusClient.modbus_reply_report_slaveid_modbus_val_bytes_set)
    __swig_setmethods__["modbus_slaveid"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_slaveid_set
    __swig_getmethods__["modbus_slaveid"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_slaveid_get
    if _newclass:modbus_slaveid = _swig_property(_TCPModbusClient.modbus_reply_report_slaveid_modbus_slaveid_get, _TCPModbusClient.modbus_reply_report_slaveid_modbus_slaveid_set)
    __swig_setmethods__["modbus_run_indicator"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_run_indicator_set
    __swig_getmethods__["modbus_run_indicator"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_run_indicator_get
    if _newclass:modbus_run_indicator = _swig_property(_TCPModbusClient.modbus_reply_report_slaveid_modbus_run_indicator_get, _TCPModbusClient.modbus_reply_report_slaveid_modbus_run_indicator_set)
    __swig_setmethods__["modbus_additional"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_additional_set
    __swig_getmethods__["modbus_additional"] = _TCPModbusClient.modbus_reply_report_slaveid_modbus_additional_get
    if _newclass:modbus_additional = _swig_property(_TCPModbusClient.modbus_reply_report_slaveid_modbus_additional_get, _TCPModbusClient.modbus_reply_report_slaveid_modbus_additional_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_reply_report_slaveid(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_reply_report_slaveid
    __del__ = lambda self : None;
modbus_reply_report_slaveid_swigregister = _TCPModbusClient.modbus_reply_report_slaveid_swigregister
modbus_reply_report_slaveid_swigregister(modbus_reply_report_slaveid)

MAX_REG_VAL = _TCPModbusClient.MAX_REG_VAL
MODBUS_MIN_REPLY = _TCPModbusClient.MODBUS_MIN_REPLY
class modbus_reply(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, modbus_reply, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, modbus_reply, name)
    __repr__ = _swig_repr
    __swig_setmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_modbus_addr_set
    __swig_getmethods__["modbus_addr"] = _TCPModbusClient.modbus_reply_modbus_addr_get
    if _newclass:modbus_addr = _swig_property(_TCPModbusClient.modbus_reply_modbus_addr_get, _TCPModbusClient.modbus_reply_modbus_addr_set)
    __swig_setmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_modbus_func_set
    __swig_getmethods__["modbus_func"] = _TCPModbusClient.modbus_reply_modbus_func_get
    if _newclass:modbus_func = _swig_property(_TCPModbusClient.modbus_reply_modbus_func_get, _TCPModbusClient.modbus_reply_modbus_func_set)
    __swig_setmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_reply_modbus_val_bytes_set
    __swig_getmethods__["modbus_val_bytes"] = _TCPModbusClient.modbus_reply_modbus_val_bytes_get
    if _newclass:modbus_val_bytes = _swig_property(_TCPModbusClient.modbus_reply_modbus_val_bytes_get, _TCPModbusClient.modbus_reply_modbus_val_bytes_set)
    __swig_setmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_reply_modbus_reg_addr_set
    __swig_getmethods__["modbus_reg_addr"] = _TCPModbusClient.modbus_reply_modbus_reg_addr_get
    if _newclass:modbus_reg_addr = _swig_property(_TCPModbusClient.modbus_reply_modbus_reg_addr_get, _TCPModbusClient.modbus_reply_modbus_reg_addr_set)
    __swig_setmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_reply_modbus_reg_val_set
    __swig_getmethods__["modbus_reg_val"] = _TCPModbusClient.modbus_reply_modbus_reg_val_get
    if _newclass:modbus_reg_val = _swig_property(_TCPModbusClient.modbus_reply_modbus_reg_val_get, _TCPModbusClient.modbus_reply_modbus_reg_val_set)
    __swig_setmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_reply_modbus_reg_qty_set
    __swig_getmethods__["modbus_reg_qty"] = _TCPModbusClient.modbus_reply_modbus_reg_qty_get
    if _newclass:modbus_reg_qty = _swig_property(_TCPModbusClient.modbus_reply_modbus_reg_qty_get, _TCPModbusClient.modbus_reply_modbus_reg_qty_set)
    __swig_setmethods__["crc"] = _TCPModbusClient.modbus_reply_crc_set
    __swig_getmethods__["crc"] = _TCPModbusClient.modbus_reply_crc_get
    if _newclass:crc = _swig_property(_TCPModbusClient.modbus_reply_crc_get, _TCPModbusClient.modbus_reply_crc_set)
    __swig_setmethods__["modbus_slaveid"] = _TCPModbusClient.modbus_reply_modbus_slaveid_set
    __swig_getmethods__["modbus_slaveid"] = _TCPModbusClient.modbus_reply_modbus_slaveid_get
    if _newclass:modbus_slaveid = _swig_property(_TCPModbusClient.modbus_reply_modbus_slaveid_get, _TCPModbusClient.modbus_reply_modbus_slaveid_set)
    __swig_setmethods__["modbus_run_indicator"] = _TCPModbusClient.modbus_reply_modbus_run_indicator_set
    __swig_getmethods__["modbus_run_indicator"] = _TCPModbusClient.modbus_reply_modbus_run_indicator_get
    if _newclass:modbus_run_indicator = _swig_property(_TCPModbusClient.modbus_reply_modbus_run_indicator_get, _TCPModbusClient.modbus_reply_modbus_run_indicator_set)
    __swig_setmethods__["modbus_additional"] = _TCPModbusClient.modbus_reply_modbus_additional_set
    __swig_getmethods__["modbus_additional"] = _TCPModbusClient.modbus_reply_modbus_additional_get
    if _newclass:modbus_additional = _swig_property(_TCPModbusClient.modbus_reply_modbus_additional_get, _TCPModbusClient.modbus_reply_modbus_additional_set)
    def __init__(self, *args): 
        this = _TCPModbusClient.new_modbus_reply(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _TCPModbusClient.delete_modbus_reply
    __del__ = lambda self : None;
modbus_reply_swigregister = _TCPModbusClient.modbus_reply_swigregister
modbus_reply_swigregister(modbus_reply)

DieWithError = _TCPModbusClient.DieWithError
calc_crc16 = _TCPModbusClient.calc_crc16
read_crc16 = _TCPModbusClient.read_crc16
print_modbus_reply_read_reg = _TCPModbusClient.print_modbus_reply_read_reg
print_modbus_reply_write_reg = _TCPModbusClient.print_modbus_reply_write_reg
print_modbus_reply_write_multireg = _TCPModbusClient.print_modbus_reply_write_multireg
print_modbus_reply_report_slaveid = _TCPModbusClient.print_modbus_reply_report_slaveid


