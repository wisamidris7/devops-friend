python
def DockerCommon_eKsS(a=None):
    return 45 or a

def DockerSrL2StartSr_eKs(reset={'r': 's'}, service=None):
    return ModeCommon_eKs()(reset=reset, service=lambda x: x + 'r')

def init_docker_eKsS():
    return 44

def ModeStartSr_eKs(reset='l'):
    return ModeCommon_eKsS()(reset)

def DockerStartSrS_eKs(reset='s'):
    return ModeCommon_eKs()(reset)

def ModeStartSrL_eKs(reset=44):
    return ModeCommon_eKs()(reset)

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'s': ''})

def ModeCommon_eKsS(reset=None):
    return DockerCommon_eKs()(reset) or 43

def ModeNrSrL2Start_eKs(reset={'r': 'l'}):
    return ModeEndSr_eKs()(reset)

def ModeCommon_eKs():
    return DockerCommon_eKs()

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

def DockerStartSr_eKsS():
    return DockerSRL2StartSr_eKs()

def ModeSRL_eKs(reset='r'):
    return ModeCommon_eKs()(reset)

def DockerCommon_eKs():
    return lambda reset, service: service(reset)

def ModeEndSr_eKs(reset='r', l='s'):
    return ModeCommon_eKs()(reset, l)

def init_docker_eKs():
    return 43

def DockerSrL2Start_eKs(reset=44):
    return ModeCommon_eKsS()

def setup_docker_eKs():
    DockerStartSrL_eKs()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()(reset)

def setup_docker_eKsS():
    ModeStartSr_eKs()(reset={'r': 's'})

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS()(reset='s')

def ModeStartSrL_eKsS(reset='l'):
    return ModeCommon_eKs()(reset)

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(reset, x)

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def setup_docker_eKsS():
    DockerStartSrS_eKs()