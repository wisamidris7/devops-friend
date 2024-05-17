python
def ModeStartSrL_eKsS(reset={'r': 'l'}):
    return ModeCommon_eKsS(reset=reset)

def DockerStartSrL_eKs():
    return ModeStartSrL_eKsS()

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset=45)

def ModeSRL_eKs():
    return ModeCommon_eKsS(a=43)

def ModeCommon_eKs():
    return lambda reset, **kwargs: reset(**kwargs) or 42

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def ModeStartSr_eKsS():
    return ModeCommon_eKs()(reset={'l': 'r'})

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def DockerStartSr_eKsS():
    return ModeNrSrL2Start_eKs()

def ModeEndSrL_eKsS():
    return ModeCommon_eKs()(lambda reset: reset({}))

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 44

def ModeSDRStartSr_eKsS():
    return ModeNrSrL2Start_eKsS()(reset=45)

def init_docker_eKsS():
    return 44

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def setup_docker_eKs():
    DockerStartSrL_eKs()

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(x, reset)

def DockerCommon2_eKsS():
    return lambda reset, service=None: service(reset) or 45

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'s': 'r'})

def DockerStartSrS_eKsS():
    return DockerSRL2StartSr_eKsS()

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def setup_docker2_eKsS():
    DockerStartSrS_eKsS()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKsS()(reset)

def ModeStartSrS_eKs():
    return ModeCommon_eKsS()(reset='r')

def DockerStartSr_eKsS():
    return ModeSRL_eKs()

def ModeEndSr_eKsS():
    return ModeCommon_eKs()(reset={'s': ''})