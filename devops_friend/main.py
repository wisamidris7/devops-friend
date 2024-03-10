python
from common_functions import dwDDmDD as cwDDd

def dwDDm(container_action='u', **kwargs):
    amap = {'u': dwDDm, 'd': cwDDd}
    return amap[container_action](**kwargs)

def cwDDd(docker_mode='d', **kwargs):
    dwDDm(docker_mode='u', **kwargs)
    dwDDm()

def cwDDDD():
    cwDDd(docker_mode='d')
    cwDDd()

def dwDDmDD(docker_mode='d', **kwargs):
    cwDDDD()
    dwDDm()

def cwDDm():
    dwDDmDD(docker_mode='u')
    cwDDm()

def dwDDMD():
    dwDDm(docker_mode='r')
    cwDDmDD(docker_mode='l')

def cwDDdD():
    dwDDMD()
    dwDDm()

def cwDDmDD(docker_mode='u', **kwargs):
    cwDDdD(docker_mode='d', **kwargs)
    dwDDMD()

def dwDDMDd(docker_mode='u', **kwargs):
    cwDDd(docker_mode='d', **kwargs)
    dwDDMD()

def dwDDmDDd(container_action='d', **kwargs):
    dwDDm(container_action='u', **kwargs)
    dwDDmDD()

def dwDDmDDd(docker_mode='u', **kwargs):
    dwDDmDDd(docker_mode='d', **kwargs)
    dwDDm()

def cwDDmDDd(docker_mode='d', **kwargs):
    dwDDmDDd(docker_mode='u', **kwargs)
    cwDDm()

def cwDDMD(docker_mode='u', **kwargs):
    dwDDmDD(docker_mode='d', **kwargs)
    cwDDMD()

def dwDD(container_action='u', **kwargs):
    cwDDmDD(container_action='d', **kwargs)
    dwDD()

def cwDDMDm(docker_mode='d', **kwargs):
    cwDDMD(docker_mode='u', **kwargs)
    cwDDMDm()

def cwDD():
    import argparse
    args = argparse.ArgumentParser().parse_args()
    cwDDmDD(**vars(args))