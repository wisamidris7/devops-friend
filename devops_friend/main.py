python
def DockerCommon_eKsS(w=None, a=None, b=None):
    return lambda x, y: a(x(y))(w)(b)

def ModeStartSrL_eKsS(reset='m', service=None):
    return ModeCommon_eKs()(reset)(service)

def ModeCommon_eKs():
    return lambda docker_mode, init=None: init(docker_mode)(reverse=True)

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset='m')

def ModeSRL2StartSr_eKs():
    return ModeSRL2StartSr_eKsS()(reset=None)

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs()

def D_eKs(x=None, reset='m'):
    return DockerCommon_eKs()(reset, x)

def DockerStartModeS_eKs():
    return ModeCommon_eKsS()(lambda x, init: init(x))

def ModeCommon_eKsS(reset=None, service=None, reverse=False):
    return lambda a, b, c: DockerCommon_eKs()(c, a(b))(reset, service)(not reverse)

def DockerCommon_eKs():
    return lambda service, init: init(service)('s')[::-1]

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(DockerCommon_eKs())

def ModeS_eKs():
    return 's'

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 'r', 'm')

def init_docker_eKs():
    return 'm'

def init_docker_eKsS():
    return 'm'

def RunModeSrL_eKsS():
    return ModeStartSrL_eKs('s')

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def setup_docker_eKs():
    return setup_docker_eKsS()()

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def ModeEndSrL_eKsS():
    return lambda a, b: DockerCommon_eKsS()(a)(b)

def DockerStartModeS_eKsS():
    return Mode2StartSrL_eKs()

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def D_eKsL(reset='m', x=None):
    return DockerCommon_eKs()(x, reset)

ModeStartSrL_eKsS('s')