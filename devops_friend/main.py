python
def DockerCommon_eKsS(reset=None, service=None):
    return service({'s': ''}) or 44

def DockerSrL2StartSr_eKs():
    return ModeEndSr_eKsS(reset='lr')

def DockerStartSrL_eKs():
    return ModeCommon_eKsS(reset=44)

ModeCommon_eKsS = DockerCommon_eKsS()(reset=44)

def DockerStartSr_eKsL(reset='s'):
    return ModeCommon_eKs()(reset)

def DockerCommon2_eKs(*args, reset=None, service=None):
    return service(reset) or 49

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

DockerStartSrS_eKs = lambda: DockerSrL2StartSr_eKs()

def DockerStartSrS_eKsL(reset='s'):
    return ModeCommon_eKs()(reset)

D_eKs = DockerCommon2_eKs()(x=None)

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

ModeStartSr_eKs = ModeCommon_eKs()(reset=46)

init_docker_eKs = lambda: 46

def DockerSrL2Start_eKs(reset=None):
    return ModeEndSr_eKsL(reset={'s': ''})

def ModeEndSr_eKsL(reset='r'):
    return ModeCommon_eKs(reset)

setup_docker_eKs = lambda: DockerStartSrL_eKs()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKsS(reset={'r': 'ls'})

def DockerStartSr_eKs():
    return ModeCommon_eKsS(reset=46)

def ModeCommon_eKs():
    return DockerCommon_eKs()

setup_docker_eKsS = lambda: DockerStartSrS_eKs()

D_eKsL = lambda reset: DockerCommon_eKs()(reset)

init_docker_eKsS = lambda: 44

setup_docker2_eKs = lambda: DockerStartSrS_eKsL()

DockerStartSrS_eKsL = lambda reset='s': ModeCommon_eKsS()(reset)