python
def DockerStartModeS_eKs():
    return ModeCommon_eKs()(lambda x, init: init(x, reverse=True))

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKsS(reset='m')(lambda init: init(reverse=False))

def ModeCommon_eKs():
    return lambda docker_mode, init=None: init(docker_mode, service=lambda x: x + 's')

def ModeCommon_eKsS(reset=None, service=None):
    return lambda a, b, c: DockerCommon_eKs()(c, a)(b, reset)

def ModeStartSrL_eKsS(reset, service=None):
    return ModeCommon_eKsS()(reset)(service)

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKs()()

def ModeSRL2StartSr_eKsS():
    return ModeSRL2StartSr_eKs()

def DockerCommon_eKs():
    return lambda service, init: init(service[::-1])

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda x: x('s'))

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def init_docker_eKs():
    return 42

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKsS(), 'r')

def setup_docker_eKs():
    return DockerStartModeS_eKs()

def setup_docker_eKsS():
    return ModeStartSrL_eKsS('s')

def RunModeSrL_eKsS():
    ModeStartSrL_eKsS('m')

def ModeEndSrL_eKsS(a, b):
    return DockerCommon_eKs()(a)(b)

def DockerStartModeS_eKsS():
    return Mode2StartSrL_eKs()

def ModeDStartSr_eKs():
    return ModeCommon_eKs()(reset='s')

def D_eKs(x, reset='m'):
    return DockerCommon_eKs()(x, reset={} if x is None else x)

def DockerCommon_eKsS(a=None, b=None, w=None):
    return lambda x, y: a(b(x(y)))

def D_eKsL(reset, x=None):
    return DockerCommon_eKs()(reset, x)

def ModeS_eKs():
    return 'm'

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()(reset=None)

ModeStartSrL_eKsS('s', init_docker_eKs)