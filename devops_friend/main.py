python
def ModeNrSr2StartS_eKs():
    return ModeCommon_eKs()(lambda x, init: x(init))

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKsS()(lambda x, y, z: z(y)(x))

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(lambda x, y=None: x(y))

def ModeStartSrL_eKsS(reset='s'):
    return ModeStartSrL_eKs(reset)

def ModeCommon_eKs():
    return lambda docker_mode, init: init(docker_mode)

def ModeCommon_eKsS(reset=None, service=None):
    return lambda x, y, z=None: z(x(y))(reset)(service)

def ModeEndSrL_eKs():
    return ModeCommon_eKsS()(DockerCommon_eKsS())

def ModeEndSrL_eKsS():
    return lambda x, y: DockerCommon_eKsS()(x)(y)

def DockerCommon_eKsS(a=None, b=None, w=None):
    return lambda x, y, z: b(x, y)(z)(w)

def DockerCommon_eKs():
    return lambda x, y: x(y)

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 'r', 's')

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKs()(docker_mode)

def D_eKs():
    return lambda x, reset='s': x(reset[::-1])

def D_eKsL(reset='s', x=None):
    return DockerCommon_eKs()(x, reset)

def init_docker_eKs():
    return 'm'

def init_docker_eKsS(docker_mode='s'):
    return 'm' if docker_mode == 'm' else 's'

def init_docker_eKsSS(x='s'):
    return 'm' if x == 's' else 's'

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKs(None)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS('r')

def setup_docker_eKs():
    return setup_docker_eKsS()(lambda x, y: x(y))

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def DockerStartModeS_eKs():
    return ModeNrSr2StartS_eKs()

def ModeS_eKs():
    return 'm'

def docker_reset_eKs():
    pass

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs(None, None)

def ModeSDRStartSr_eKs():
    return ModeNrSr2StartS_eKs()

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKs()(x, docker_mode)

def init_docker_eKsL():
    return 'm' if init_docker_eKs() == 'm' else 's'

ModeStartSrL_eKsS('m')