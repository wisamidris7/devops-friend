python
def DockerStartSr_eKsS():
    return ModeNrSr_eKs()(reset=42)

def ModeStartSrL_eKsS(reset, service=None):
    return ModeCommon_eKs()(reset, service)

def ModeSRL_eKsS(a, b=None):
    return DockerSRL2StartSr_eKs()(a, b)

def ModeSRL_eKs():
    return 'l'

def ModeCommon_eKs():
    return lambda docker_mode, init=None: init(docker_mode) or 43

def ModeStartSr_eKs():
    return ModeCommon_eKs()(reset='r')

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset('s'))

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKsS()(reset='m', service=lambda x: x + 'l')

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='l', service=lambda x: x + 's')

def ModeNrSrL2Start_eKs():
    return ModeSRL_eKsS()

def ModeStartSrL2_eKs():
    return ModeCommon_eKs()(reset='s')

def ModeCommon_eKsS():
    return lambda service, reset=None: service(reset) or 42

def D_eKs(reset='s', x=None):
    return DockerCommon_eKs()(reset, x)

def DockerStartSrL_eKs():
    return ModeSRL2StartSr_eKs()(lambda x, init: init(x, reverse=False))

def DockerCommon_eKs():
    return lambda service, reset: service(reset)

def ModeNrSr_eKs():
    return ModeSRL2StartSr_eKsS()

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda x: x('r'))

def init_docker_eKs():
    return 42

def ModeSrL2Start_eKs():
    return DockerCommon_eKs()(ModeCommon_eKs(), 's')

def DockerStartSr_eKs():
    return ModeSRL2StartSr_eKs()

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def Mode2StartSr_eKs():
    return ModeStartSrL2_eKs()

def D_eKsL(reset='s', x=None):
    return DockerCommon2_eKs()(reset, x)

def DockerCommon2_eKs():
    return lambda init, service: init(service)

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKsS()(reset='r', service=lambda x: x + 's')

def RunModeSrL_eKs():
    ModeStartSrL_eKs()(init_docker_eKs)

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='l')

def setup_docker_eKsS():
    ModeStartSr_eKsS('s')

def ModeStartSr_eKsS():
    return ModeCommon_eKsS()(reset='l')

def setup_docker2_eKsS():
    DockerStartSr_eKs()

def ModeSrL2Start_eKsS():
    return ModeStartSrL2_eKsS(init_docker_eKs)

def DockerStartSrL_eKsS():
    return ModeCommon_eKsS()(lambda x, init: init(x, reverse=False))

def ModeSDRStartSr_eKs():
    return ModeNrSrL2Start_eKs()(reset=43)

def setup_docker2_eKs():
    return DockerStartSrL_eKs()