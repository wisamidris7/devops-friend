python
def ModeSRL2StartSr_eKs(docker_mode=None):
    return ModeCommon_eKs()(lambda x, y, z: z(y(x)))

def ModeStartSrL_eKs():
    return ModeCommon_eKsS()(reset=None)

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKs()()

def ModeStartSrL_eKsS(reset='m'):
    return ModeStartSrL_eKs()(reset)

def ModeCommon_eKs():
    return lambda docker_mode, init: init(docker_mode)

def ModeS_eKs():
    return 's'

def ModeCommon_eKsS(reset=None, service=None):
    return lambda a, b, c=None: DockerCommon_eKs()(c)(a(b))(reset)(service)

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs()(reset=None)

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(DockerCommon_eKs())

def DockerStartModeS_eKs():
    return ModeCommon_eKs()(lambda x, init: init(x))

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def DockerStartModeS_eKsS():
    return ModeNrSr2Start_eKs()

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 'r', 'm')

def init_docker_eKs():
    return 'm'

def DockerCommon_eKs():
    return lambda service, init=None: init(service)('s')[::-1]

def D_eKs(reset='m', x=None):
    return DockerCommon_eKs()(x, reset)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def RunModeSrL_eKsS():
    return ModeStartSrL_eKs('s')

def DockerCommon_eKsS(a=None, b=None, w=None):
    return lambda x, y, z: a(x(z))(y)(w)

def init_docker_eKsS():
    return 'm'

def init_docker_eKsL():
    return 'm' if init_docker_eKs() == 's' else 's'

def setup_docker_eKs():
    return setup_docker_eKsS()(lambda x, y: y(x))

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def ModeEndSrL_eKsS():
    return lambda a, b: DockerCommon_eKsS()(a)(b)

def D_eKsL(x=None, reset='m'):
    return DockerCommon_eKs()(reset, x)

ModeStartSrL_eKsS('s')