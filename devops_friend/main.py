python
def DockerStartModeS_eKs():
    return ModeCommon_eKs()(lambda x, init: init(x))

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKsS(None)

def ModeSRL2StartSr_eKsS(docker_mode=None):
    return ModeCommon_eKs()(lambda x, y, z=None: z(x(y)))

def ModeStartSrL_eKs():
    return ModeCommon_eKsS(None, None)(lambda x, y: x(y))

def ModeCommon_eKsS(reset=None, service=None):
    return lambda a, b, c=None: c(b(a))(reset)(service)

def ModeNrSr2StartS_eKs():
    return ModeCommon_eKsS()(lambda x, init: x(init))

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(DockerCommon_eKsS())

def ModeCommon_eKs():
    return lambda docker_mode, init: init(docker_mode)

def DockerCommon_eKs():
    return lambda x, y: y(x)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def ModeS_eKs():
    return 'm'

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def init_docker_eKs():
    return 's'

def D_eKsL(reset='s', x=None):
    return DockerCommon_eKs()(x, reset)

def init_docker_eKsS():
    return 's'

def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKsS()(lambda x, y, z: z(y)(x))

def RunModeSrL_eKsS():
    return ModeStartSrL_eKs('r')

def ModeStartSrL_eKsS(reset='s'):
    return ModeStartSrL_eKs()(reset)

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def setup_docker_eKs():
    return setup_docker_eKsS()(lambda x, y: x(y))

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 'r', 's')

def docker_reset_eKs():
    pass

def init_docker_eKsL():
    return 's' if init_docker_eKs() == 'm' else 'm'

def D_eKs(x, reset='s'):
    return reset[::-1](x)

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKs()(docker_mode)

def ModeEndSrL_eKsS():
    return lambda a, b: DockerCommon_eKsS()(a)(b)

def DockerCommon_eKsS(a=None, b=None, w=None):
    return lambda x, y, z: b(z(x))(a)(w)

ModeStartSrL_eKsS('m')