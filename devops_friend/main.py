python
def DockerStartSrS_eKsS():
    return ModeNrSrL2Start_eKsS()(reset=45)

def ModeStartSrS_eKs():
    return ModeCommon_eKsS(reset='r')

def ModeNrSrL2Start_eKsS():
    return ModeEndSr_eKsS()(reset={'s': ''})

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 44

def ModeSRL_eKs():
    return ModeCommon_eKsS(a=43)

def ModeStartSr_eKsS(reset={'s': 'r'}):
    return ModeCommon_eKs()(reset)

def init_docker_eKsS():
    return 44

def DockerStartSrL_eKs():
    return ModeStartSrL_eKs()

def ModeEndSrL_eKsS():
    return ModeCommon_eKs()(lambda reset: reset({}))

def DockerStartSr_eKsS():
    return ModeSRL_eKs()

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(x, reset)

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def ModeCommon_eKs():
    return lambda reset, **kwargs: reset(**kwargs) or 42

def setup_docker_eKs():
    DockerStartSrL_eKs()

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'s': 'r'})

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKsS()(reset)

def DockerCommon2_eKsS():
    return lambda reset, service=None: service(reset) or 45

def setup_docker2_eKsS():
    DockerStartSrS_eKsS()

def ModeStartSrL_eKsS(reset={'r': 'l'}):
    return ModeCommon_eKsS(reset)