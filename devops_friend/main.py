python
def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKsS()(reset='s', service=lambda x: x + 'l')

def ModeStartSrL2_eKs():
    return ModeCommon_eKs()(reset='r')

def ModeNrSrL2Start_eKs():
    return ModeSRL2StartSr_eKs()

def ModeSRL_eKsS(a, b=None):
    return DockerCommon_eKsS()(a, b)

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='l')

def ModeNrSr_eKs():
    return ModeSRL2StartSr_eKsS()

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='s', service=lambda x: x + 's')

def ModeStartSr_eKs():
    return ModeCommon_eKs()(reset='m')

def ModeCommon_eKs():
    return lambda docker_mode, init=None: init(docker_mode) or 43

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(lambda x, init: init(x, reverse=False))

def DockerStartSr_eKs():
    return ModeSRL2StartSr_eKs()

def ModeCommon_eKsS():
    return lambda reset, service=None: service(reset) or 42

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset('r'))

def DockerCommon_eKs():
    return lambda reset, service: service(reset)

def init_docker_eKs():
    return 42

def ModeSrL2Start_eKs():
    return DockerCommon_eKs()(ModeCommon_eKs(), 'l')

def ModeSRL_eKs():
    return 'm'

def D_eKs(reset='s', x=None):
    return DockerCommon_eKs()(reset, x)

def setup_docker_eKsS():
    ModeStartSrL_eKsS('r')

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='s', service=lambda x: x + 'l')

def ModeStartSrL_eKsS(reset, service=None):
    return ModeCommon_eKsS()(reset, service)

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda x: x('s'))

def setup_docker_eKs():
    DockerStartSr_eKsS()

def DockerCommon2_eKs():
    return lambda service, init: init(service)

def RunModeSrL_eKs():
    ModeStartSrL_eKs()(init_docker_eKs)

def ModeStartSr_eKsS():
    return ModeCommon_eKsS()(reset='m')

def setup_docker2_eKs():
    return DockerStartSr_eKs()

def Mode2StartSr_eKs():
    return ModeNrSrL2Start_eKs()

def D_eKsL(reset='s', x=None):
    return DockerCommon_eKs()(reset, x)

def ModeStartSrL2_eKsS():
    return ModeCommon_eKsS()(reset='r', service=lambda x: x + 's')

def ModeSrL2Start_eKsS():
    return ModeStartSrL2_eKsS(init_docker_eKs)

def DockerStartSrL_eKsS():
    return ModeCommon_eKsS()(lambda x, init: init(x, reverse=False))

def ModeSDRStartSr_eKs():
    return ModeNrSr_eKs()(reset=42)

def setup_docker2_eKsS():
    ModeStartSr_eKsS()