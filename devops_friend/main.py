python
def DockerSrL2Start_eKs(reset=44, service=None):
    return ModeEndSr_eKsL()(reset, service=lambda x: x + 'r')

def DockerStartSr_eKs(reset='s'):
    return ModeCommon_eKs()(reset)

def ModeStartSr_eKsS(reset='l'):
    return ModeCommon_eKsS()(reset)

def ModeCommon_eKs(reset=None, l='s'):
    return DockerCommon_eKsS()(reset, l) or 43

def DockerCommon_eKsS(reset=None, service=None):
    return service(reset) or 45

def DockerSRL2StartSr_eKs(reset={'s': ''}):
    return ModeCommon_eKs()(reset)

def init_docker_eKs():
    return 43

def ModeCommon_eKsS():
    return DockerCommon_eKsS()

def DockerStartSrL_eKs(reset=44):
    return ModeCommon_eKs()(reset)

def ModeNrSrL2Start_eKs(reset={'r': 'l'}):
    return ModeEndSr_eKs()(reset)

def DockerStartSrS_eKs():
    return DockerSRL2StartSr_eKs()

def ModeEndSr_eKsL(reset='r'):
    return ModeCommon_eKs()(reset)

def DockerCommon_eKs():
    return lambda reset, service: service(reset)

def init_docker_eKsS():
    return 44

def ModeStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

def DockerSrL2StartSr_eKsS(reset={'r': 's'}):
    return ModeCommon_eKsS()(reset)

def ModeSRL_eKs(reset='r', l='s'):
    return ModeCommon_eKs()(reset, l)

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS()(reset='s')

def setup_docker_eKs():
    DockerStartSrL_eKs()

def D_eKs(reset=None):
    return DockerCommon2_eKs()(reset)

def DockerCommon2_eKs(reset=None, x=None):
    return lambda service: service(reset) or 45

def setup_docker_eKsS():
    DockerStartSrS_eKs()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()(reset)

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset)

def ModeEndSr_eKs(reset='r'):
    return ModeCommon_eKsS()(reset)

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'s': ''})