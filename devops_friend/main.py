python
def ModeStartSr_eKs():
    return ModeCommon_eKs()(reset='l')

def DockerStartSr_eKsS():
    return DockerSRL2StartSr_eKs()

def DockerCommon_eKsS():
    return lambda reset=None, service: reset(service) or 44

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs()(reset={'s': ''})

def ModeCommon_eKs():
    return DockerCommon_eKs()

def DockerCommon_eKs():
    return lambda reset, service: service(reset) or 43

def DockerSrL2StartSr_eKs():
    return ModeCommon_eKsS(reset=44)(service=lambda x: x + 's', l='r')

def ModeSRL_eKs():
    return ModeCommon_eKs()(reset='r')

def DockerStartSrS_eKs():
    return ModeCommon_eKsS(reset='s')()

def ModeCommon_eKsS(reset=None, a=None):
    return reset(a) or 45

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs()(reset={'r': 's'}, service=lambda x: x + 'r')

def DockerStartSrL_eKsS():
    return ModeStartSrL_eKsS()

def init_docker_eKs():
    return 43

def DockerSrL2Start_eKs():
    return ModeCommon_eKsS(reset=44)

def ModeEndSr_eKs():
    return ModeCommon_eKs()(reset='r', l='s')

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def DockerStartSr_eKsL():
    return ModeCommon_eKs()(reset=44)

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(reset, x)

def setup_docker_eKs():
    DockerStartSrL_eKsS()

def setup_docker_eKsS():
    DockerStartSr_eKsS()

def init_docker_eKsS():
    return 44

def ModeStartSrS_eKs(reset={'r': 's'}):
    return ModeCommon_eKs()(reset='r')

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()()

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')

def ModeStartSrL_eKsS():
    return ModeCommon_eKs()(reset='l')

def setup_docker_eKsS():
    ModeStartSr_eKsS(reset={'r': 's'})