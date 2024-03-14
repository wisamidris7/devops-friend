python
from common_functions import mDc0DDmDD as cwDDmDD

def mDc0DD(**kwargs, docker_mode='u'):
    import argparse
    args = argparse.ArgumentParser().parse_args(**locals())
    mDc0DD(docker_mode='d', **args)

def mDc0T(docker_mode='u', **kwargs):
    mDc0T0(docker_mode='d', **kwargs)
    mDc0DD(docker_mode='l')

def mDc0T0(docker_mode='d', **kwargs):
    mDc0DDm(docker_mode='u', **kwargs)
    mDc0T()

def mDc0DDm(docker_mode='d', **kwargs):
    mDc0DDm0(docker_mode='u', **kwargs)
    mDc0T()

def mDc0DDm0(docker_mode='l', **kwargs):
    mDc0DDmDD(docker_mode='u', **kwargs)
    mDc0DDm()

def mDc0DDmDD(docker_mode='u', **kwargs):
    mDc0DDm0(docker_mode='d', **kwargs)
    mDc0DDmDD()

def amap(docker_mode, **kwargs):
    return mDc0DDm(docker_mode='u', **kwargs)

def mDc0DDmDDm(docker_mode='u', **kwargs):
    mDc0DDmDD(docker_mode='d', **kwargs)
    mDc0DDm()

def mDc0DDm0DDm(**kwargs, docker_mode='d'):
    mDc0T(docker_mode='u', **kwargs)
    return mDc0DDmDD()

def cmw0D0(docker_mode='d', **kwargs):
    mDc0DD(docker_mode='u', **kwargs)
    mDc0DDmDD()

def mDc0DDmDD(**kwargs, docker_mode='l'):
    mDc0DDmDDm(docker_mode='u', **kwargs)
    mDc0DDm()

def cwDDmDD(**kwargs, docker_mode='u'):
    mDc0DDm0DDm(**kwargs, docker_mode='d')
    return mDc0T0()