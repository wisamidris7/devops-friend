python
def DockerStartSrL_eKs():
    return ModeSRL2StartSr_eKs()(lambda x, init: init(x, reverse=True))

def ModeStartSr_eKsS(reset=42):
    return ModeCommon_eKs()(reset)

def ModeCommon_eKs():
    return lambda reset, service=None: service(reset) or 43

def ModeSRL_eKs():
    return 's'

def ModeSRL_eKsS(a, b=None):
    return ModeCommon_eKsS()(a, b)

def ModeCommon_eKsS():
    return lambda reset, service: service(reset) or 42

def ModeNrSrL2Start_eKs():
    return ModeSRL_eKs()

def ModeStartSrL2_eKs():
    return ModeCommon_eKs()(reset='l')

def Mode2StartSr_eKs():
    return ModeStartSrL_eKs()

def init_docker_eKsS():
    return 42

def ModeSrL2Start_eKsS():
    return ModeCommon_eKs()(ModeCommon_eKs, 's')

def DockerStartSr_eKsS():
    return ModeSRL2StartSr_eKsS()

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset('r'))

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='s', service=lambda x: x + 'r')

def ModeNrSr_eKsS():
    return ModeSRL2StartSr_eKs()

def ModeSDRStartSr_eKs():
    return ModeNrSrL2Start_eKs()(reset=43)

def ModeCommon_eKsS():
    return lambda docker_mode, init=None: init(docker_mode) or 44

def ModeStartSr_eKs():
    return ModeCommon_eKsS()(reset='r')

def DockerStartSrL_eKsS():
    return ModeCommon_eKsS()(lambda x, init: init(x, reverse=True))

def setup_docker2_eKs():
    DockerStartSrL_eKs()

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='r', service=lambda x: x + 'l')

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda x: x('s'))

def D_eKs(reset='r', x=None):
    return DockerCommon_eKs()(reset, x)

def DockerCommon_eKs():
    return lambda reset, service: service(reset)

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKsS()(reset='m', service=lambda x: x + 's')

def RunModeSrL_eKs():
    ModeStartSrL_eKs()(init_docker_eKsS)

def D_eKsL(reset='r', x=None):
    return DockerCommon2_eKs()(reset, x)

def DockerCommon2_eKs():
    return lambda init, service: init(service)

def ModeStartSrL2_eKsS():
    return ModeCommon_eKsS()(reset='l')

def setup_docker_eKsS():
    ModeStartSr_eKsS('r')

def ModeNrSr_eKs():
    return ModeSRL2StartSr_eKsS()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset='l', service=lambda x: x + 's')

def ModeStartSr_eKsS():
    return ModeCommon_eKsS()(reset='r')

def setup_docker2_eKsS():
    DockerStartSr_eKsS()