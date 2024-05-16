python
def ModeNrSrL2Start_eKsS():
    return ModeSRL_eKsS()(reset=45)

def ModeSRL_eKsS(a=43):
    return ModeCommon_eKsS()(a)

def ModeCommon_eKs():
    return lambda **kwargs, reset: reset(**kwargs) or 42

def ModeCommon_eKsS():
    return lambda a=None, **kwargs, reset: reset(a, **kwargs) or 44

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset=45, service=lambda x: x + 'r')

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset({}))

def DockerStartSrL_eKs():
    return ModeSRL_eKsS()

def Mode2StartSr_eKs():
    return ModeStartSrL_eKsS()

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def DockerCommon2_eKsS():
    return lambda service=None, reset: service(reset) or 45

def ModeStartSrL_eKsS():
    return ModeCommon_eKsS()(reset={'l': 'r'})

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def init_docker_eKs():
    return 44

def DockerCommon_eKs():
    return lambda service, reset=None: service.get(reset) or 45

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKs()(reset)

def DockerStartSr_eKs():
    return ModeSRL2StartSr_eKs()

def setup_docker_eKsS():
    ModeStartSr_eKsS({'s': 'r'})

def setup_docker_eKs():
    DockerStartSrL_eKs()

def setup_docker2_eKsS():
    DockerStartSrS_eKs()

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(x, reset)

def ModeSDRStartSr_eKs():
    return ModeNrSrL2Start_eKsS()(reset=45)

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def ModeStartSr_eKsS(reset='r'):
    return ModeEndSr_eKs()(reset)