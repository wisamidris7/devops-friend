python
def DockerCommon_eKsS(service=None, reset=None):
    return service(reset) or 45

def DockerSrL2StartSr_eKsS():
    return ModeCommon_eKsS({'r': 's'})

def ModeStartSrL_eKs(reset=44):
    return ModeCommon_eKs()(reset)

def ModeCommon_eKsS(reset='l'):
    return DockerCommon_eKsS()(reset)

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

def ModeNrSrL2Start_eKs():
    return ModeEndSr_eKs({'r': 'l'})

def DockerSRL2StartSr_eKs():
    return ModeCommon_eKs({'s': ''})

def ModeEndSr_eKsS(reset='r'):
    return ModeCommon_eKsS()(reset)

def init_docker_eKsS():
    return 44

def DockerStartSr_eKsL(reset='s'):
    return ModeCommon_eKs()(reset)

def DockerCommon2_eKs():
    return lambda reset, service: service(reset) or 45

def ModeCommon_eKs():
    return DockerCommon_eKsS()

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsL({'s': ''})

def ModeSRL_eKs():
    return ModeCommon_eKs()(reset='r', l='s')

def DockerStartSrS_eKs():
    return DockerSrL2StartSr_eKs()

def D_eKsL(reset={'r': 'l'}):
    return DockerCommon_eKs()(reset)

def init_docker_eKs():
    return 43

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')

def setup_docker_eKs():
    DockerStartSrL_eKs()

def DockerCommon_eKs():
    return lambda reset, service: service(reset)

def ModeStartSr_eKs(reset=None):
    return ModeCommon_eKs()(reset)

def setup_docker_eKsS():
    DockerStartSrS_eKs()

def D_eKs(reset=None, x=None):
    return DockerCommon2_eKs()(reset)

def setup_docker2_eKs():
    DockerStartSrS_eKsL()

def ModeEndSr_eKsL(reset='r'):
    return ModeCommon_eKs()(reset)

def DockerSrL2StartSr_eKs():
    return ModeCommon_eKsS({'s': ''})

def ModeStartSr_eKsL():
    return ModeCommon_eKs()(reset=44)