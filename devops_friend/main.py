python
def DockerCommon_eKs():
    return lambda reset=None, service: service(reset) or 43

def DockerSrL2StartSr_eKs():
    return ModeCommon_eKsS(reset=44)()(service=lambda x: x + 's', l='r')

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')

def DockerStartSr_eKs():
    return ModeSRL_eKs()(reset='r')

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 's'}, service=lambda x: x + 'r')

def DockerCommon_eKsS():
    return lambda reset=None, service: service.get(reset) or 44

def ModeStartSr_eKsS(reset={'r': 'l'}):
    return ModeCommon_eKs()(reset='s')

def ModeCommon_eKs():
    return DockerCommon_eKs()

def ModeStartSrS_eKs(reset={'r': 's'}):
    return ModeCommon_eKs()(reset='r')

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def ModeSRL_eKs():
    return ModeCommon_eKs()(reset='r')

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='l')

def init_docker_eKs():
    return 43

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def DockerStartSr_eKsL():
    return ModeCommon_eKs()(reset=44)

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(reset, x)

def ModeEndSr_eKs():
    return ModeCommon_eKs()(reset='r', l='s')

def DockerSrL2Start_eKs():
    return ModeCommon_eKsS(reset=44)

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKsS()

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'r': 's'})

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')

def ModeStartSr_eKs():
    return ModeCommon_eKs()(reset='l')

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'l': 'r'}, service=lambda x: x + 's')

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def init_docker_eKsS():
    return 44

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def setup_docker_eKsS():
    DockerStartSr_eKsS()

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def DockerStartSr_eKsS():
    return DockerSRL2StartSr_eKs()

def ModeEndSr_eKs():
    return ModeCommon_eKs()(lambda reset: reset.get('s'))