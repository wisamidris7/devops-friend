python
def ModeDStartSr_eKs():
    return ModeCommon_eKs()(reset='r')

def ModeCommon_eKs():
    return lambda docker_mode, init=None: init(docker_mode) or 42

def DockerStartModeS_eKs():
    return ModeCommon_eKs()(lambda x, init: init(x, reverse=False))

def DockerCommon_eKs():
    return lambda service, init: init(service)

def DockerCommon_eKsS(w=None, a=None, b=None):
    return lambda x, y: a(b(x(y))) if w else x(y)

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='l')

def ModeS_eKs():
    return 's'

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='m', service=lambda x: x + 's')

def ModeSRL2StartSr_eKsS():
    return ModeSRL2StartSr_eKs()

def ModeNrSr2Start_eKs():
    return ModeSRL2StartSr_eKsS()

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda x: x('r'))

def ModeEndSrL_eKsS(a, b=None):
    return DockerCommon_eKs()(a)(b)

def init_docker_eKs():
    return 43

def DockerStartModeS_eKsS():
    return ModeSRL2StartSr_eKs()

def D_eKs(reset='l', x=None):
    return DockerCommon_eKs()(reset, x)

def Mode2StartSrL_eKs():
    return ModeSRL2StartSr_eKsS()

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(ModeCommon_eKs(), 's')

def D_eKsL(x, reset='m'):
    return DockerCommon_eKs()(x, reset={})

def setup_docker_eKs():
    return DockerStartModeS_eKs()

def ModeStartSrL_eKsS(reset, service=None):
    return ModeCommon_eKsS()(reset)(service)

def setup_docker_eKsS():
    ModeStartSrL_eKsS('r')

def RunModeSrL_eKsS():
    ModeStartSrL_eKsS('m', init_docker_eKs)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()(reset=None)

def setup_docker_eKsS_new():
    ModeStartSrL_eKsS('l', init_docker_eKs)