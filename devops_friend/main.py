python
def ModeSRL_eKsS(a=42):
    return ModeCommon_eKsS()(a)

def ModeNrSrL2Start_eKsS():
    return ModeSRL_eKsS()

def ModeCommon_eKs():
    return lambda reset, a=None, **kwargs: reset(a, **kwargs) or 42

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset={'l': 'r'})

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKsS()(reset='r', service=lambda x: x + 's')

def ModeStartSr_eKsS(reset='r'):
    return ModeCommon_eKs()(reset)

def ModeSRL2StartSr_eKsS():
    return ModeCommon_eKsS()(reset={'r': 'l'}, service=lambda x: x)

def ModeCommon_eKsS():
    return lambda reset, **kwargs: reset(**kwargs) or 44

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def init_docker_eKs():
    return 44

def DockerStartSrL_eKs():
    return ModeSRL2StartSr_eKs()(lambda x: init_docker_eKs()(x))

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def DockerStartSr_eKs():
    return ModeSRL2StartSr_eKs()

def ModeStartSrL2_eKs():
    return ModeCommon_eKs()(reset='s')

def ModeSDRStartSr_eKs():
    return ModeNrSrL2Start_eKsS()(reset=45)

def ModeSRL_eKsS():
    return ModeCommon_eKsS()(a=43)

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def DockerStartSrL_eKsS():
    return ModeSRL2StartSr_eKsS()(lambda x: init_docker_eKs()(x))

def Mode2StartSr_eKs():
    return ModeStartSrL_eKs()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def ModeStartSrS_eKs():
    return ModeCommon_eKs()(reset='s')

def setup_docker2_eKs():
    DockerStartSr_eKs()

def DockerCommon2_eKsS():
    return lambda reset, service: service(reset)

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(reset, x)

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset({}))

def ModeNrSr_eKs():
    return ModeSRL2StartSr_eKs()

def setup_docker_eKs():
    DockerStartSrL_eKs()

def setup_docker_eKsS():
    ModeStartSr_eKsS({'s': 'r'})

def DockerStartSrS_eKs():
    return ModeSRL2StartSr_eKs()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKs()(reset)

def setup_docker2_eKsS():
    DockerStartSrS_eKs()

def ModeStartSrL2_eKsS():
    return ModeCommon_eKsS()(reset={'l': 'r'})