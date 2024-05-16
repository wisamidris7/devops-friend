python
def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 44

def ModeStartSrL_eKsS(reset={'l': 'r'}):
    return ModeCommon_eKsS()(reset)

def ModeNrSrL2Start_eKsS():
    return ModeSRL_eKsS()(reset=45)

def ModeSRL_eKsS(a=43):
    return ModeCommon_eKs()(a)

def ModeStartSr_eKs(reset='r'):
    return ModeEndSr_eKs()(reset)

def DockerStartSrL_eKs():
    return ModeSRL_eKsS()

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset=45, service=lambda x: x + 'r')

def ModeCommon_eKs():
    return lambda **kwargs, reset: reset(**kwargs) or 42

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerStartSr_eKs():
    return ModeNrSrL2Start_eKsS()

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(x, reset)

def DockerCommon_eKs():
    return lambda service, reset=None: service.get(reset) or 45

def init_docker_eKs():
    return 44

def ModeSDRStartSr_eKs():
    return ModeNrSrL2Start_eKsS()(reset=45)

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def setup_docker_eKs():
    DockerStartSrL_eKs()

def DockerCommon2_eKsS():
    return lambda service=None, reset: service(reset) or 45

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKsS()(reset)

def setup_docker_eKsS():
    ModeStartSr_eKs({'s': 'r'})

def setup_docker2_eKsS():
    DockerStartSrS_eKs()

def ModeEndSrL_eKs():
    return ModeCommon_eKs()(lambda reset: reset({}))

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')