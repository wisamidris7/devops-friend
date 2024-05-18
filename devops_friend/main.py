python
def DockerSrL2StartSr_eKs():
    return ModeCommon_eKsS()(reset={'l': 'r'}, service=lambda x: x + 's')

def DockerStartSr_eKsL():
    return DockerSrL2Start_eKs()(reset=44)

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='l')

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def ModeStartSrS_eKsL(reset=None):
    return ModeCommon_eKs()(reset='s')

def ModeStartSr_eKsS(reset={'r': 's'}):
    return ModeCommon_eKs()(reset='l')

def DockerCommon_eKsL():
    return lambda reset=44, service: service or 45

def DockerCommon_eKs():
    return lambda reset=None, service: service(reset) or 45

def ModeCommon_eKs():
    return DockerCommon_eKs()

def DockerStartSr_eKs():
    return ModeSRL_eKs()

def ModeSRL_eKs():
    return ModeCommon_eKs()(reset='r')

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def DockerCommon_eKsS():
    return lambda reset=None, service: service.get(reset) or 44

def ModeEndSr_eKs():
    return ModeCommon_eKs()(reset='r')

def init_docker_eKsS():
    return 44

def init_docker_eKs():
    return 43

def DockerStartSr_eKsS():
    return DockerSRL2StartSr_eKsS()

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKs()

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'r': 's'})

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(x, reset)

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def DockerSrL2Start_eKs():
    return ModeCommon_eKsS(reset=44)

def ModeStartSrS_eKs(reset={'r': 's'}):
    return ModeCommon_eKs()(reset='r')

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def ModeStartSr_eKs():
    return ModeCommon_eKs()(reset='l')

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 's'}, service=lambda x: x + 's')

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')