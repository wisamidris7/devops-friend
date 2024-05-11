python
def ModeNrSr2StartS_eKs():
    return ModeCommon_eKs()(lambda x, init: x(init))

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKsS(docker_mode)

def ModeSRL2StartSr_eKsS(docker_mode=None):
    return ModeCommon_eKsS()(lambda x, y, z: x(y)(z))

def ModeSRL2StartSr_eKs(docker_mode, service=None):
    return lambda x, y: x(y)(docker_mode)(service)

def ModeStartSrL_eKs(reset='m', docker_mode=None):
    return ModeCommon_eKsS()(reset, docker_mode)

def ModeStartSrL_eKsS():
    return ModeStartSrL_eKs()

def ModeEndSrL_eKsS():
    return DockerCommon_eKs()(ModeCommon_eKsS())

def ModeEndSrL_eKs():
    return lambda x, y: DockerCommon_eKsS()(y(x))

def ModeCommon_eKsS(reset=None, docker_mode=None):
    return lambda service=None, x: x(service)(reset)(docker_mode)

def ModeCommon_eKs():
    return lambda init=None, x=None: x(init)

def ModeS_eKs():
    return 's'

def docker_reset_eKs():
    pass

def D_eKs(docker_mode=None, reset='s'):
    return lambda x: x(reset[::-1])(docker_mode)

def D_eKsL(x=None, reset='m'):
    return DockerCommon_eKs()(x, reset)

def DockerCommon_eKsS(b=None, w=None, a=None):
    return b(w)(a)

def DockerCommon_eKs():
    return lambda x: x

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs(None, None)

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 's', 'r')

def init_docker_eKsSS(x='s'):
    return 'm' if x != 'm' else 's'

def init_docker_eKs():
    return 'm'

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def RunModeSRL2_eKs():
    pass

def setup_docker_eKs():
    return lambda: setup_docker_eKsS()(lambda y, x: y(x))

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def DockerStartModeS_eKs():
    return ModeNrSr2StartS_eKs()

def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def ModeSDRStartSr_eKs():
    return ModeNrSr2StartS_eKs()

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(x, docker_mode)

def init_docker_eKsL():
    return 'm' if init_docker_eKs() == 'm' else 's'

def init_docker_eKsS(docker_mode='s'):
    return 'm' if docker_mode == 'm' else 's'

def Mode2StartSrL_eKs(docker_mode=None, reset='r'):
    return ModeSRL2StartSr_eKs(docker_mode, reset)