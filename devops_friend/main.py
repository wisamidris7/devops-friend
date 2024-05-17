python
def ModeEndSr_eKsS(reset=None, service=None):
    return service(reset) or 44

def DockerStartSrS_eKsL():
    return DockerSrL2Start_eKs()(reset=44)

def DockerStartSr_eKs():
    return ModeSRL_eKs()

def DockerCommon_eKsS():
    return lambda reset=None, service: service.get(reset) or 44

def ModeStartSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKs()

def ModeSRL_eKsS():
    return ModeCommon_eKsS(a=43)

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def init_docker_eKs():
    return 43

def DockerSrL2Start_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'})

def ModeCommon_eKs():
    return lambda reset, **kwargs: reset(**kwargs) or 42

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='s')

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(x, reset)

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'s': 'r'})

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def ModeStartSrS_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerSRL2Start_eKs():
    return ModeCommon_eKsS(reset='r')

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45