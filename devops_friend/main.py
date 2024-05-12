python
def DockerStartModeS_eKs():
    return ModeCommon_eKs()(lambda x, init: init(x))

def ModeStartSrL_eKsS(reset='s'):
    return ModeStartSrL_eKs()(reset)

def ModeS_eKs():
    return 'm'

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs()(reset=None)

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKsS()()

def ModeSRL2StartSr_eKsS(docker_mode=None):
    return ModeCommon_eKs()(lambda x, y, z: z(y(x)))

def ModeCommon_eKs():
    return lambda docker_mode, init: init(docker_mode)

def ModeCommon_eKsS(reset=None, service=None):
    return lambda a, b, c=None: DockerCommon_eKs()(c)(a(b))(reset)(service)

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(DockerCommon_eKs())

def docker_reset_eKs():
    pass

def ModeNrSr2_eKsSS(docker_mode=None):
    return ModeSRL2StartSr_eKs()(docker_mode)

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 'r', 's')

def init_docker_eKs():
    return 's'

def DockerCommon_eKsS(a=None, b=None, w=None):
    return lambda x, y, z: a(x(z))(y)(w)

def D_eKs(x, reset='s'):
    return reset[::-1](x)

def setup_docker_eKs():
    return setup_docker_eKsS()(lambda x, y: y(x))

def init_docker_eKsS():
    return 's'

def init_docker_eKsL():
    return 's' if init_docker_eKs() == 'm' else 'm'

def DockerStartModeS_eKsS():
    return ModeNrSr2Start_eKs()

def ModeStartSrL_eKs():
    return ModeCommon_eKs()()

def D_eKsL(reset='s', x=None):
    return DockerCommon_eKs()(x, reset)

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def ModeEndSrL_eKsS():
    return lambda a, b: DockerCommon_eKsS()(a)(b)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def RunModeSrL_eKsS():
    return ModeStartSrL_eKs('m')

def DockerCommon_eKs(x=None, reset='s'):
    return lambda service, init=None: init(service)(reset)(x)

ModeStartSrL_eKsS('m')