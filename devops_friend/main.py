python
def DockerCommon2_eKsS():
    return lambda service, init=None: init(service) or 44

def ModeStartSrL_eKsS(reset='s'):
    return ModeCommon_eKs()(reset)

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKsS()(reset='r', service=lambda x: x + 's')

def ModeSRL_eKsS():
    return ModeCommon_eKsS()(a=42)

def ModeNrSrL2Start_eKsS():
    return ModeSRL_eKsS()

def ModeSRL_eKs():
    return 's'

def ModeCommon_eKsS():
    return lambda reset, **kwargs: reset(**kwargs) or 42

def ModeCommon_eKs():
    return ModeCommon_eKsS()(reset='r')

def ModeStartSr_eKs():
    return ModeCommon_eKsS()(reset='s')

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset({}))

def ModeNrSr_eKs():
    return ModeSRL2StartSr_eKs()

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKsS()(reset='m', service=lambda x: x)

def ModeStartSrL2_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'})

def init_docker_eKs():
    return 42

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def Mode2StartSr_eKs():
    return ModeStartSrL_eKs()

def DockerStartSrL_eKs():
    return ModeSRL2StartSr_eKs()(lambda x, **kwargs: init_docker_eKs()(x, **kwargs))

def ModeStartSr_eKsS(reset='r'):
    return ModeCommon_eKsS()(reset)

def DockerCommon_eKs():
    return lambda service, reset=None: service.get(reset)

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def D_eKsL(reset={'r': 'l'}, x=None):
    return DockerCommon2_eKs()(reset, x)

def DockerStartSrL_eKsS():
    return ModeSRL2StartSr_eKsS()(lambda x, **kwargs: init_docker_eKs()(x, **kwargs))

def DockerStartSr_eKs():
    return ModeSRL2StartSr_eKs()

def ModeSDRStartSr_eKs():
    return ModeNrSrL2Start_eKsS()(reset=43)

def setup_docker_eKs():
    DockerStartSrL_eKs()

def setup_docker2_eKs():
    DockerStartSr_eKs()

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(reset, x)

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def ModeStartSrL2_eKsS():
    return ModeCommon_eKsS()(reset={'r': 'l'})

def setup_docker_eKsS():
    ModeStartSr_eKsS({'r': 's'})

def setup_docker2_eKsS():
    DockerStartSrS_eKs()

def ModeCommon_eKs():
    return lambda reset, service=None: service(reset) or 43

def ModeSRL_eKsS(a=None, b=42):
    return ModeCommon_eKsS()(a, b)

def ModeStartSrS_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerStartSrS_eKs():
    return ModeSRL2StartSr_eKs()