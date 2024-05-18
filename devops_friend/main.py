python
def DockerStartSrS_eKsL():
    return DockerSrL2Start_eKs()(reset=44)

def ModeStartSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerSrL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'l': 'r'}, service=lambda x: x + 'r')

def DockerCommon_eKs():
    return lambda reset=None, service: service(reset) or 45

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def ModeSRL_eKs():
    return ModeCommon_eKsS(reset='r')

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerStartSr_eKs():
    return ModeSRL_eKs()

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def DockerStartSrL_eKs():
    return ModeStartSrL_eKs()

def init_docker_eKs():
    return 43

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKs()

def DockerCommon_eKsS():
    return lambda reset=None, service: service.get(reset) or 44

def ModeCommon_eKs():
    return DockerCommon_eKs()

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(x, reset)

def DockerSRL2Start_eKs():
    return ModeCommon_eKsS(reset='r')

def ModeStartSrS_eKs(reset=None):
    return ModeCommon_eKs()(reset='s')

def init_docker_eKsS():
    return 44

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'r': 's'})

def DockerStartSr_eKsS():
    return DockerSRL2StartSr_eKsS()

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='s')

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def ModeStartSrS_eKs():
    return ModeCommon_eKs()(reset={'l': 'r'}, service=lambda x: x + 'r')

def setup_docker2_eKs():
    DockerStartSrS_eKsL()