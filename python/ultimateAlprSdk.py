# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.9
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_ultimateAlprSdk', [dirname(__file__)])
        except ImportError:
            from binaries.windows.x86_64 import _ultimateAlprSdk
            return _ultimateAlprSdk
        if fp is not None:
            try:
                _mod = imp.load_module('_ultimateAlprSdk', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _ultimateAlprSdk = swig_import_helper()
    del swig_import_helper
else:
    import _ultimateAlprSdk
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


ULTALPR_SDK_VERSION_MAJOR = _ultimateAlprSdk.ULTALPR_SDK_VERSION_MAJOR
ULTALPR_SDK_VERSION_MINOR = _ultimateAlprSdk.ULTALPR_SDK_VERSION_MINOR
ULTALPR_SDK_VERSION_MICRO = _ultimateAlprSdk.ULTALPR_SDK_VERSION_MICRO
ULTALPR_SDK_IMAGE_TYPE_RGB24 = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_RGB24
ULTALPR_SDK_IMAGE_TYPE_RGBA32 = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_RGBA32
ULTALPR_SDK_IMAGE_TYPE_BGRA32 = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_BGRA32
ULTALPR_SDK_IMAGE_TYPE_NV12 = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_NV12
ULTALPR_SDK_IMAGE_TYPE_NV21 = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_NV21
ULTALPR_SDK_IMAGE_TYPE_YUV420P = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_YUV420P
ULTALPR_SDK_IMAGE_TYPE_YVU420P = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_YVU420P
ULTALPR_SDK_IMAGE_TYPE_YUV422P = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_YUV422P
ULTALPR_SDK_IMAGE_TYPE_YUV444P = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_YUV444P
ULTALPR_SDK_IMAGE_TYPE_Y = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_Y
ULTALPR_SDK_IMAGE_TYPE_BGR24 = _ultimateAlprSdk.ULTALPR_SDK_IMAGE_TYPE_BGR24
class UltAlprSdkResult(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UltAlprSdkResult, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UltAlprSdkResult, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _ultimateAlprSdk.new_UltAlprSdkResult(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ultimateAlprSdk.delete_UltAlprSdkResult
    __del__ = lambda self : None;
    def code(self): return _ultimateAlprSdk.UltAlprSdkResult_code(self)
    def phrase(self): return _ultimateAlprSdk.UltAlprSdkResult_phrase(self)
    def json(self): return _ultimateAlprSdk.UltAlprSdkResult_json(self)
    def numPlates(self): return _ultimateAlprSdk.UltAlprSdkResult_numPlates(self)
    def numCars(self): return _ultimateAlprSdk.UltAlprSdkResult_numCars(self)
    def isOK(self): return _ultimateAlprSdk.UltAlprSdkResult_isOK(self)
UltAlprSdkResult_swigregister = _ultimateAlprSdk.UltAlprSdkResult_swigregister
UltAlprSdkResult_swigregister(UltAlprSdkResult)

class UltAlprSdkParallelDeliveryCallback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UltAlprSdkParallelDeliveryCallback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UltAlprSdkParallelDeliveryCallback, name)
    __repr__ = _swig_repr
    def __init__(self): 
        if self.__class__ == UltAlprSdkParallelDeliveryCallback:
            _self = None
        else:
            _self = self
        this = _ultimateAlprSdk.new_UltAlprSdkParallelDeliveryCallback(_self, )
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _ultimateAlprSdk.delete_UltAlprSdkParallelDeliveryCallback
    __del__ = lambda self : None;
    def onNewResult(self, *args): return _ultimateAlprSdk.UltAlprSdkParallelDeliveryCallback_onNewResult(self, *args)
    def __disown__(self):
        self.this.disown()
        _ultimateAlprSdk.disown_UltAlprSdkParallelDeliveryCallback(self)
        return weakref_proxy(self)
UltAlprSdkParallelDeliveryCallback_swigregister = _ultimateAlprSdk.UltAlprSdkParallelDeliveryCallback_swigregister
UltAlprSdkParallelDeliveryCallback_swigregister(UltAlprSdkParallelDeliveryCallback)

class UltAlprSdkEngine(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UltAlprSdkEngine, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UltAlprSdkEngine, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_getmethods__["init"] = lambda x: _ultimateAlprSdk.UltAlprSdkEngine_init
    if _newclass:init = staticmethod(_ultimateAlprSdk.UltAlprSdkEngine_init)
    __swig_getmethods__["deInit"] = lambda x: _ultimateAlprSdk.UltAlprSdkEngine_deInit
    if _newclass:deInit = staticmethod(_ultimateAlprSdk.UltAlprSdkEngine_deInit)
    __swig_getmethods__["process"] = lambda x: _ultimateAlprSdk.UltAlprSdkEngine_process
    if _newclass:process = staticmethod(_ultimateAlprSdk.UltAlprSdkEngine_process)
    __swig_getmethods__["exifOrientation"] = lambda x: _ultimateAlprSdk.UltAlprSdkEngine_exifOrientation
    if _newclass:exifOrientation = staticmethod(_ultimateAlprSdk.UltAlprSdkEngine_exifOrientation)
    __swig_getmethods__["requestRuntimeLicenseKey"] = lambda x: _ultimateAlprSdk.UltAlprSdkEngine_requestRuntimeLicenseKey
    if _newclass:requestRuntimeLicenseKey = staticmethod(_ultimateAlprSdk.UltAlprSdkEngine_requestRuntimeLicenseKey)
    __swig_getmethods__["warmUp"] = lambda x: _ultimateAlprSdk.UltAlprSdkEngine_warmUp
    if _newclass:warmUp = staticmethod(_ultimateAlprSdk.UltAlprSdkEngine_warmUp)
    __swig_destroy__ = _ultimateAlprSdk.delete_UltAlprSdkEngine
    __del__ = lambda self : None;
UltAlprSdkEngine_swigregister = _ultimateAlprSdk.UltAlprSdkEngine_swigregister
UltAlprSdkEngine_swigregister(UltAlprSdkEngine)

def UltAlprSdkEngine_init(*args):
  return _ultimateAlprSdk.UltAlprSdkEngine_init(*args)
UltAlprSdkEngine_init = _ultimateAlprSdk.UltAlprSdkEngine_init

def UltAlprSdkEngine_deInit():
  return _ultimateAlprSdk.UltAlprSdkEngine_deInit()
UltAlprSdkEngine_deInit = _ultimateAlprSdk.UltAlprSdkEngine_deInit

def UltAlprSdkEngine_process(*args):
  return _ultimateAlprSdk.UltAlprSdkEngine_process(*args)
UltAlprSdkEngine_process = _ultimateAlprSdk.UltAlprSdkEngine_process

def UltAlprSdkEngine_exifOrientation(*args):
  return _ultimateAlprSdk.UltAlprSdkEngine_exifOrientation(*args)
UltAlprSdkEngine_exifOrientation = _ultimateAlprSdk.UltAlprSdkEngine_exifOrientation

def UltAlprSdkEngine_requestRuntimeLicenseKey(rawInsteadOfJSON=False):
  return _ultimateAlprSdk.UltAlprSdkEngine_requestRuntimeLicenseKey(rawInsteadOfJSON)
UltAlprSdkEngine_requestRuntimeLicenseKey = _ultimateAlprSdk.UltAlprSdkEngine_requestRuntimeLicenseKey

def UltAlprSdkEngine_warmUp(*args):
  return _ultimateAlprSdk.UltAlprSdkEngine_warmUp(*args)
UltAlprSdkEngine_warmUp = _ultimateAlprSdk.UltAlprSdkEngine_warmUp

# This file is compatible with both classic and new-style classes.


