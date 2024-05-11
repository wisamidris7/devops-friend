python
def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def ModeSRL2StartSr_eKs():
    return ModeNrSr2StartS_eKs()

def ModeNrSr2StartS_eKs():
    return ModeCommon_eKs()(lambda x, init: x(init))

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKsS()(lambda x, y, z: x(y)(z))

def ModeStartSrL_eKs():
    return ModeCommon_eKsS()(lambda x, y=None: x(y))

def ModeStartSrL_eKsS(reset='m'):
    return ModeStartSrL_eKs(reset)

def ModeCommon_eKsS(reset=None, service=None):
    return lambda docker_mode, x: x(service)(reset)(docker_mode)

def ModeCommon_eKs():
    return lambda init: init

def ModeEndSrL_eKs():
    return ModeCommon_eKsS()(DockerCommon_eKs())

def ModeEndSrL_eKsS():
    return lambda x, y: DockerCommon_eKs()(y(x))

def DockerCommon_eKs():
    return lambda x: x

def DockerCommon_eKsS(a=None, w=None, b=None):
    return b(w)(a)

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 's', 'r')

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKsS(docker_mode)

def D_eKs():
    return lambda x, reset='s': x(reset[::-1])

def D_eKsL(reset='m', x=None):
    return DockerCommon_eKs()(x, reset)

def init_docker_eKs():
    return 's'

def init_docker_eKsS(docker_mode='m'):
    return 's' if docker_mode == 's' else 'm'

def init_docker_eKsSS(x='m'):
    return 's' if x != 's' else 'm'

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKs(None)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def setup_docker_eKs():
    return setup_docker_eKsS()(lambda x, y: y(x))

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def DockerStartModeS_eKs():
    return ModeNrSr2StartS_eKs()

def ModeS_eKs():
    return 's'

def docker_reset_eKs():
    pass

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs(None, None)

def ModeSDRStartSr_eKs():
    return ModeNrSr2StartS_eKs()

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(x, docker_mode)

def init_docker_eKsL():
    return 's' if init_docker_eKs() == 's' else 'm'

ModeStartSrL_eKsS('r')