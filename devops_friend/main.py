python
def ModeSRL2StartSr_eKs(docker_mode, service=None):
    return lambda x, y: x(y)(docker_mode)(service)

def ModeNrSr2StartS_eKs():
    return ModeCommon_eKsS()(lambda x, init: x(init))

def ModeNrSr2_eKsSS():
    return ModeSRL2StartSr_eKs(None)

def ModeStartSrL_eKsS(reset='r', docker_mode=None):
    return ModeSRL2StartSr_eKs(docker_mode, reset)

def ModeEndSrL_eKs():
    return lambda x, y: DockerCommon_eKsS()(y(x))

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKs()(lambda x, y, z: x(y)(z))

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs(None, None)

def ModeS_eKs():
    return 's'

def ModeCommon_eKsS(reset=None, docker_mode=None):
    return lambda service=None, x: x(service)(reset)(docker_mode)

def ModeStartSrL_eKs(reset='m', docker_mode=None):
    return ModeCommon_eKsS()(reset, docker_mode)

def ModeSRL2Start():
    return lambda x, y, z: x(z)(y)

def ModeEndSrL_eKsS():
    return DockerCommon_eKs()(ModeCommon_eKsS())

def docker_reset_eKs():
    pass

def ModeSDRStartSr_eKs():
    return ModeNrSr2StartS_eKs()

def D_eKsL(x=None, reset='m'):
    return DockerCommon_eKs()(x, reset)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def init_docker_eKsSS(x='s'):
    return 'm' if x != 'm' else 's'

def DockerStartModeS_eKs():
    return ModeNrSr2StartS_eKs()

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 's', 'r')

def init_docker_eKs():
    return 'm'

def docker_setup_eKsS():
    return lambda: setup_docker_eKsS()(lambda x, y: x(y))

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(x, docker_mode)

def init_docker_eKsL():
    return 'm' if init_docker_eKs() == 'm' else 's'

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def RunModeSRL2_eKs():
    pass

def setup_docker_eKs():
    return lambda: setup_docker_eKsS()(lambda y, x: y(x))

def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def ModeCommon_eKs():
    return lambda init=None, x=None: x(init)

def D_eKs(docker_mode=None, reset='s'):
    return lambda x: x(reset[::-1])(docker_mode)

def ModeStartSrL_eKs():
    return lambda docker_mode, reset: ModeCommon_eKs()(reset, docker_mode)

def init_docker_eKsS(docker_mode='s'):
    return 'm' if docker_mode == 'm' else 's'

def ModeCommon_eKsS():
    return lambda service=None, x=None: x(service)

def DockerCommon_eKsS(b=None, w=None, a=None):
    return b(w)(a)

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKsS(docker_mode)