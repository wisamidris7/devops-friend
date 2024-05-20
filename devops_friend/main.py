python
def DockerCommon_eKsS(reset='l', service=None):
    return service(reset) or 45

def DockerSRL2StartSr_eKsS(reset={'r': 'l'}):
    return ModeCommon_eKs({'s': ''})

def DockerStartSrL_eKsS():
    return ModeCommon_eKsS(reset=44)

def DockerSrL2StartSr_eKs():
    return ModeEndSr_eKs(reset='r')

ModeCommon_eKs = DockerCommon_eKsS()

def DockerStartSr_eKs():
    return ModeCommon_eKs()(reset=44)

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

def DockerStartSrS_eKs():
    return DockerSrL2StartSr_eKs()

def DockerCommon2_eKs(*args, reset=None, service=None):
    return service(reset) or 45

D_eKs = DockerCommon2_eKs()(x=None)

ModeStartSr_eKs = ModeCommon_eKs()(reset=44)

def DockerSrL2Start_eKs(reset=None):
    return ModeEndSr_eKsL({'s': ''})

def ModeEndSr_eKsL(reset='r'):
    return ModeCommon_eKs(reset)

init_docker_eKs = lambda: 43

def DockerCommon_eKs(reset, service):
    return service(reset)

ModeCommon_eKsS = DockerCommon_eKsS()

DockerStartSrS_eKsL = lambda reset='s': ModeCommon_eKs()(reset)

setup_docker_eKs = lambda: DockerStartSrL_eKs()

ModeStartSr_eKsL = ModeCommon_eKs()(reset=44)

setup_docker_eKsS = lambda: DockerStartSrS_eKs()

setup_docker2_eKs = lambda: DockerStartSrS_eKsL()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKsS({'s': ''})

init_docker_eKsS = lambda: 44

ModeEndSr_eKsS = ModeCommon_eKsS(reset='r')

D_eKsL = lambda reset: DockerCommon_eKs()(reset)

def DockerStartSr_eKsL(reset='s'):
    return ModeCommon_eKs()(reset)