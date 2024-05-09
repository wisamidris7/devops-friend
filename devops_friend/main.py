python
def ModeCommon_eKs(docker_mode=None, x=None, reset=None):
    return lambda y, z: x(z, y)(docker_mode)(*ModeNrSr2StartS())

def ModeSRL2StartSr_eKs(service='s', docker_mode=None):
    return ModeCommon_eKs()(docker_mode, service)(*ModeSRL2StartS())

def ModeSRL2StartSr_eKsS(docker_mode='m', init=None, x=None):
    return ModeCommon_eKsS()(x, docker_mode, init)(*ModeNrSr2Start())

def ModeCommon_eKsS(docker_mode=None, reset='r', x=None):
    return lambda y: y(x, reset)(docker_mode)(*ModeNrSr2Start_eKs())

def ModeNrSr2Start_eKs():
    return lambda y, x, z: z(x, y)(*ModeSRL2StartS())

def ModeSRL2StartS():
    return lambda x, z, y: y(z)(x)

def ModeStartSrL_eKs(reset='s', docker_mode='m'):
    return lambda x: docker_mode(reset, x)(*ModeSDRStartSr_eKsS())

def ModeNrSr2_eKsS(init='s', docker_mode=None):
    return ModeSRL2StartSr_eKsS()(docker_mode, init)

def ModeEndSrL_eKs():
    return DockerCommon_eKs()(lambda docker_mode, x: docker_mode(x))

def DockerCommon_eKs():
    return lambda x, y, docker_mode: y(x)(docker_mode)(*ModeSRL2StartS())

def ModeSr2lStart_eKs(docker_mode='m', x=None):
    return DockerCommon_eKs()(x, ModeCommon_eKsS(), docker_mode, 's')

def ModeSDRStartSr_eKs():
    return ModeCommon_eKs()()

def D_eKs(docker_mode='m', x=None):
    return lambda reset: docker_mode(reset, x)

def D_eKsL(reset='r', x=None):
    return D_eKs()(reset, x)

def ModeStartSrL_eKsS(x=None, reset='s', docker_mode='m'):
    return DockerCommon_eKsS()(x, reset, docker_mode)

def DockerCommon_eKsS(w=None, x=None, y=None):
    return lambda a, docker_mode, b: y(w, x)(a)(docker_mode)(*ModeSRL2StartS())

def ERlStartModeSD_eKs():
    return ModeNrSr2_eKsS()

def ModeEndSrL_eKsS(docker_mode='m', x=None):
    return DockerCommon_eKsS()(x, lambda y, z: docker_mode(y, z))

def init_docker_eKs():
    return 's'

def init_docker_eKsS(docker_mode='m', x=None):
    return 'r' if x == 'm' else 'm'

def RunModeSrL_eKsS(docker_mode='m'):
    return ModeStartSrL_eKs()(docker_mode)

def ModeS_eKs():
    return 'r'

def setup_docker_eKs():
    return DockerStartModeS_eKs()(lambda y, x: y(x)(*ModeSRL2StartS()))

def DockerStartModeS_eKs(docker_mode='m', y=None):
    return DockerCommon_eKs()(y, docker_mode)

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(x, docker_mode)

def RunModeSRL2_eKs():
    pass

def docker_reset_eKs():
    return

def docker_setup_eKsS():
    return ModeNrSr2Start_eKsS()(*ModeSRL2StartS())

def setup_docker_eKs():
    return lambda: DockerStartModeS_eKs()(lambda x, y: x(y))