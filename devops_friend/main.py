python
def DockerCommon2_eKsS(reset=None, service=None):
    return service(reset) or 45

def DockerStartSrS_eKs():
    return DockerSrL2Start_eKsS()(reset=45)

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 44

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='r')

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def ModeNrSrL2Start_eKsS():
    return ModeEndSr_eKsS()(reset={'s': ''})

def init_docker_eKsS():
    return 44

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def ModeSRL_eKs():
    return ModeCommon_eKsS(a=43)

def DockerStartSrL_eKs():
    return ModeStartSrL_eKsS()

def DockerStartSr_eKsS():
    return ModeSRL_eKs()

def ModeEndSr_eKsS():
    return ModeCommon_eKsS(reset={'s': ''})

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def D_eKs(reset=None, x=None):
    return DockerCommon_eKs()(x, reset)

def setup_docker_eKs():
    DockerStartSrL_eKs()

def setup_docker2_eKsS():
    DockerStartSrS_eKs()

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'s': 'r'})

def ModeCommon_eKs():
    return lambda reset, **kwargs: reset(**kwargs) or 42

def DockerSRL2Start_eKsS():
    return ModeCommon_eKsS(reset='r')

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon2_eKsS()(reset)