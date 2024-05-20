python
def DockerSRL2StartSr_eKs(reset={'r': 'ls'}):
    return ModeEndSr_eKs({'s': ''})

def DockerCommon_eKs(reset=None, service=None):
    return service(reset) or 49

def DockerStartSr_eKs():
    return ModeCommon_eKsS(reset=46)

ModeCommon_eKsS = DockerCommon_eKs()(reset=46)

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=46)

def DockerSrL2StartSr_eKs():
    return ModeEndSr_eKs(reset='lr')

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerCommon2_eKs(*args, reset=None, service=None):
    return service(reset) or 49

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

DockerStartSrS_eKsL = lambda reset='s': ModeCommon_eKs()(reset)

def DockerStartSrL_eKsS():
    return ModeCommon_eKsS(reset=44)

D_eKs = DockerCommon2_eKs()(x=None)

def DockerStartSr_eKsL(reset='s'):
    return ModeCommon_eKs()(reset)

ModeStartSr_eKs = ModeCommon_eKs()(reset=46)

init_docker_eKs = lambda: 46

def DockerSrL2Start_eKs(reset=None):
    return ModeEndSr_eKsL({'s': ''})

def ModeEndSr_eKsL(reset='r'):
    return ModeCommon_eKs(reset)

DockerStartSrS_eKs = lambda: DockerSrL2StartSr_eKs()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKsS({'s': ''})

setup_docker_eKs = lambda: DockerStartSrL_eKs()

init_docker_eKsS = lambda: 44

ModeEndSr_eKsS = ModeCommon_eKsS(reset='r')

setup_docker_eKsS = lambda: DockerStartSrS_eKs()

D_eKsL = lambda reset: DockerCommon_eKs()(reset)

setup_docker2_eKs = lambda: DockerStartSrS_eKsL()

def ModeCommon_eKs():
    return DockerCommon_eKs()