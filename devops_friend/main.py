python
def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 's'}, service=lambda x: x + 's')

def DockerSrL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'l': 'r'}, service=lambda x: x + 'r')

def ModeStartSrL_eKs():
    return ModeCommon_eKsS(reset='r')

def ModeStartSrS_eKs(reset={'r': 's'}):
    return ModeCommon_eKs()(reset='l')

def ModeStartSr_eKsS(reset=None):
    return ModeCommon_eKs()(reset={'l': 'r'}, service=lambda x: x + 'r')

def DockerStartSr_eKsL():
    return DockerSrL2Start_eKs()(reset=44)

def DockerStartSr_eKs():
    return ModeSRL_eKs()

def ModeSRL_eKs():
    return ModeCommon_eKs()(reset='r')

def ModeCommon_eKs():
    return DockerCommon_eKs()

def DockerCommon_eKs():
    return lambda reset=None, service: service(reset) or 45

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def DockerCommon_eKsS():
    return lambda reset=None, service: service.get(reset) or 44

def ModeEndSr_eKs():
    return ModeCommon_eKs()(reset='r')

def init_docker_eKs():
    return 43

def init_docker_eKsS():
    return 44

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(x, reset)

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKs()

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'r': 's'})

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def DockerStartSr_eKsS():
    return DockerSRL2StartSr_eKsS()

def ModeStartSrS_eKsL(reset=None):
    return ModeCommon_eKs()(reset='s')

def DockerSrL2Start_eKs():
    return ModeCommon_eKsS(reset=44)

def ModeCommon_eKsS():
    return DockerCommon_eKsS()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerStartSr_eKs():
    return ModeStartSr_eKsS()

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='s')

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 's'}, service=lambda x: x + 'r')

def ModeStartSr_eKs():
    return ModeCommon_eKs()(reset='l')

def DockerCommon_eKsL():
    return lambda reset=44, service: service or 45

def ModeStartSrS_eKs():
    return ModeCommon_eKs()(reset='r')

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')