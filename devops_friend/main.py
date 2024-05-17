python
def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def DockerSrL2Start_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'})

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKs()

def ModeSRL_eKsS():
    return ModeCommon_eKsS(a=43)

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerStartSrS_eKsL():
    return DockerSrL2Start_eKs()(reset=44)

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def DockerStartSr_eKs():
    return ModeSRL_eKs()

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(x, reset)

def DockerCommon_eKs():
    return lambda reset=None, service: service.get(reset) or 45

def DockerSRL2Start_eKs():
    return ModeCommon_eKsS(reset='r')

def ModeStartSrS_eKs():
    return ModeCommon_eKs()(reset='s')

def init_docker_eKs():
    return 43

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def ModeStartSr_eKsS():
    ModeStartSrS_eKs(reset={'s': 'r'})

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def ModeSRL_eKs():
    return ModeCommon_eKsS(reset='r')

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'s': 'r'})

def DockerCommon_eKsS():
    return lambda reset=None, service: service.get(reset) or 44

def ModeStartSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def init_docker_eKsS():
    return 44