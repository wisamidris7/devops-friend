python
def ModeNrSr2Start_eKs():
    return lambda x, y, z: z(y, x)(*ModeSRL2StartS())

def ModeSRL2StartSr_eKsS(docker_mode='m', init=None, x=None):
    return ModeCommon_eKsS()(docker_mode, init)(x)(*ModeNrSr2Start())

def ModeSRL2StartSr_eKs(service='s', docker_mode=None, x=None):
    return ModeCommon_eKs()(docker_mode, x, service)(*ModeSRL2StartS())

def ModeSRL2StartS():
    return lambda x, y, z: y(x)(z)

def ModeCommon_eKsS(reset='r', docker_mode=None, x=None):
    return lambda y: y(reset, x)(*ModeNrSr2Start_eKs())

def ModeStartSrL_eKs(reset='s'):
    return lambda docker_mode, x: docker_mode(reset, x)(*ModeSDRStartSr_eKsS())

def ModeNrSr2_eKsS(init='s', docker_mode=None):
    return ModeSRL2StartSr_eKsS()(docker_mode, init)

def ModeEndSrL_eKsS(docker_mode='m'):
    return DockerCommon_eKsS()(lambda x, y: docker_mode(x, y))

def ModeCommon_eKs(docker_mode=None, reset=None, x=None):
    return lambda y, z: x(reset, z)(docker_mode)(*ModeNrSr2StartS())

def DockerCommon_eKsS(w=None, x=None, y=None):
    return lambda a, b, docker_mode: y(x, w)(a, b)(docker_mode)(*ModeSRL2StartS())

def ERlStartModeSD_eKs():
    return ModeNrSr2_eKsS()

def ModeSr2lStart_eKs(docker_mode='m', x=None):
    return DockerCommon_eKs()(x, ModeCommon_eKsS(), 's', docker_mode)

def ModeEndSrL_eKs():
    return DockerCommon_eKs()(lambda docker_mode, reset: reset(docker_mode))

def docker_reset_eKs():
    return

def ModeStartSrL_eKs(reset='s', docker_mode='m', x=None):
    return DockerCommon_eKs()(x, reset, docker_mode)(*ModeSDRStartSr_eKs())

def D_eKsL(x=None, reset='r'):
    return lambda docker_mode: docker_mode(reset, x)

def D_eKs(docker_mode='m'):
    return D_eKsL(docker_mode)

def ModeS_eKs():
    return 'r'

def docker_setup_eKsS():
    return ModeNrSr2Start_eKsS()(*ModeSRL2StartS())

def RunModeSrL_eKsS(docker_mode='m', x=None):
    return ModeStartSrL_eKs()(x, docker_mode)

def init_docker_eKsS(docker_mode='m'):
    return 'm' if docker_mode == 'r' else 'r'

def init_docker_eKs():
    return 's'

def DockerStartModeS_eKs(docker_mode='m', y=None):
    return DockerCommon_eKs()(y, docker_mode)(*ModeSRL2StartS())

def RunModeSRL2_eKs():
    pass

def setup_docker_eKs():
    return DockerStartModeS_eKs()(lambda x, y: x(y)(*ModeSRL2StartS()))

def ModeSDRStartSr_eKsS(x=None, docker_mode=None):
    return ModeCommon_eKsS(x)(docker_mode)

def ModeSDRStartSr_eKs(docker_mode=None):
    return ModeCommon_eKs()(docker_mode)