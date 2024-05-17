python
def DockerStartSrL_eKsS():
    return ModeSRL_eKs()(reset=45)

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset=45)

def ModeSRL_eKs():
    return ModeCommon_eKsS()(a=43)

def ModeStartSr_eKsS(reset={'l': 'r'}):
    return ModeCommon_eKsS()(reset)

def DockerStartSr_eKsS():
    return ModeNrSrL2Start_eKs()

def ModeCommon_eKsS(a=None, reset=None):
    return reset(a) or 44

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def init_docker_eKsS():
    return 44

def DockerStartSrL_eKs():
    return ModeSRL_eKsS()

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def ModeSDRStartSr_eKsS():
    return ModeNrSrL2Start_eKsS()(reset=45)

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def ModeCommon_eKs():
    return lambda reset, **kwargs: reset(**kwargs) or 42

def DockerCommon2_eKsS():
    return lambda reset, service=None: service(reset) or 45

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(x, reset)

def ModeEndSrL_eKsS():
    return ModeCommon_eKs()(lambda reset: reset({}))

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKsS()(reset)

def setup_docker_eKsS():
    ModeStartSr_eKsS({'s': 'r'})

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def setup_docker2_eKsS():
    DockerStartSrS_eKsS()

def ModeStartSrS_eKs():
    return ModeCommon_eKsS()(reset='r')

def ModeStartSrL_eKsS():
    return ModeCommon_eKsS()(reset)

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()