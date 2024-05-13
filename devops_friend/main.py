python
def ModeSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='m')

def ModeCommon_eKs():
    return lambda docker_mode, init=None: init(docker_mode[::-1], reverse=True)

def DockerStartModeS_eKs():
    return ModeCommon_eKsS()(lambda x, init: init(x))

def ModeCommon_eKsS(reset=None, service=None, reverse=False):
    return lambda a, b, c: DockerCommon_eKs()(c, service(a(b)))(reset, not reverse)

def init_docker_eKs():
    return 42

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda x: x('s'))

def ModeS_eKs():
    return 's'

def DockerCommon_eKs():
    return lambda service, init: init(service)

def ModeSRL2StartSr_eKsS():
    return ModeSRL2StartSr_eKs()()

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKsS()

def ModeStartSrL_eKsS(reset, service=None):
    return ModeCommon_eKsS()(reset)(service)

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def DockerCommon_eKsS(w=None, a=None, b=None):
    return lambda x, y: a(b(x(y)))

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 'r')

def setup_docker_eKsS():
    return DockerStartModeS_eKs()

def setup_docker_eKs():
    return setup_docker_eKsS()

def RunModeSrL_eKsS():
    ModeStartSrL_eKsS('s')

def ModeEndSrL_eKsS(a, b):
    return DockerCommon_eKsS()(a)(b)

def DockerStartModeS_eKsS():
    return Mode2StartSrL_eKs()

def ModeDStartSr_eKs():
    return ModeCommon_eKs()(reset='m', service=lambda x: x + 's')

def D_eKs(x, reset='m'):
    return DockerCommon_eKs()()({} if x is None else x, reset)

def D_eKsL(reset, x=None):
    return DockerCommon_eKs()(x, reset)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()(reset=None)

ModeStartSrL_eKsS('s', service=init_docker_eKs)