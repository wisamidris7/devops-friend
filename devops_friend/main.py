python
def ModeNrSrL2Start_eKsS():
    return ModeSRL_eKsS()

def ModeStartSr_eKsS(reset='r'):
    return ModeCommon_eKs()(reset)

def ModeSRL_eKsS(a=43):
    return ModeCommon_eKsS()(a)

def DockerStartSrL_eKs():
    return ModeSRL2StartSr_eKs()

def ModeStartSrL2_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def ModeSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset='r', service=lambda x: x + 's')

def ModeCommon_eKs():
    return lambda reset, a=None, **kwargs: reset(a, **kwargs) or 42

def ModeCommon_eKsS():
    return lambda reset, **kwargs: reset(**kwargs) or 44

def DockerStartSrS_eKs():
    return ModeSRL2StartSr_eKs()

def DockerCommon2_eKsS():
    return lambda reset, service: service(reset) or 45

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKs()(reset)

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def Mode2StartSr_eKs():
    return ModeStartSrL_eKs()

def init_docker_eKs():
    return 44

def ModeStartSrL_eKsS():
    return ModeCommon_eKsS()(reset={'l': 'r'})

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def setup_docker_eKs():
    DockerStartSrL_eKs()

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset({}))

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(reset, x)

def setup_docker_eKsS():
    ModeStartSr_eKsS({'s': 'r'})

def DockerStartSr_eKs():
    return ModeSRL2StartSr_eKs()

def setup_docker2_eKs():
    DockerStartSr_eKs()

def setup_docker2_eKsS():
    DockerStartSrS_eKs()

def ModeStartSrL2_eKsS():
    return ModeCommon_eKsS()(reset={'l': 'r'})

def ModeSDRStartSr_eKs():
    return ModeNrSrL2Start_eKsS()(reset=45)