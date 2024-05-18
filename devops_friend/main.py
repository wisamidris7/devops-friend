python
def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'l': 'r'}, service=lambda x: x + 'r')

def DockerStartSrL_eKs():
    return ModeStartSrL_eKs()

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def ModeStartSrS_eKs():
    return ModeCommon_eKs()(reset='r')

def DockerStartSr_eKs():
    return ModeSRL_eKs()

def ModeCommon_eKs():
    return lambda reset=None, service=None: service.get(reset) or 45

def ModeSRL_eKs():
    return ModeCommon_eKsS(reset='r')

def init_docker_eKsS():
    return 44

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset='s')

def DockerCommon_eKs():
    return lambda reset=None, service: service(reset) or 45

def DockerSrL2Start_eKsS():
    return ModeCommon_eKsS(reset={'l': 'r'})

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKs()

def ModeStartSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerCommon_eKsS():
    return lambda reset=None, service: service.get(reset) or 44

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(x, reset)

def DockerSRL2Start_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerStartSrS_eKsL():
    return DockerSrL2Start_eKs()(reset=44)

def init_docker_eKs():
    return 43

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 's')

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'r': 's'})

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def ModeStartSr_eKsS():
    ModeStartSrS_eKs(reset={'s': 'r'})

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def DockerStartSr_eKsS():
    return DockerSRL2StartSr_eKsS()

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='s')

def ModeStartSrS_eKs(reset=None):
    return ModeCommon_eKs()(reset='s')

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'l'}, service=lambda x: x + 'r')