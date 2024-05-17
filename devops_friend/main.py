python
def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='r')

def DockerStartSrL_eKs():
    return ModeStartSrL_eKsS()

def ModeSRL_eKs():
    return ModeCommon_eKsS(a=43)

def DockerStartSr_eKsS():
    return ModeSRL_eKs()

def ModeNrSrL2Start_eKsS():
    return ModeEndSr_eKsS()(reset={'s': ''})

def ModeCommon_eKs():
    return lambda reset, **kwargs: reset(**kwargs) or 42

def ModeStartSr_eKsS(reset={'s': 'r'}):
    return ModeCommon_eKs()(reset)

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def ModeEndSrL_eKsS():
    return ModeCommon_eKs()(lambda reset: reset({}))

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 44

def init_docker_eKsS():
    return 44

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(x, reset)

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def setup_docker_eKs():
    DockerStartSrL_eKs()

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'s': 'r'})

def DockerStartSrS_eKs():
    return DockerSrL2Start_eKsS()(reset=45)

def DockerSrL2Start_eKsS():
    return ModeCommon_eKsS(reset='r')

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKsS()(reset)

def DockerCommon2_eKsS():
    return lambda reset, service=None: service(reset) or 45

def setup_docker2_eKsS():
    DockerStartSrS_eKs()

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def ModeEndSr_eKsS():
    return ModeCommon_eKsS(reset={'s': ''})