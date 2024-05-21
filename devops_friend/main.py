python
def ModeCommon_eKsS(reset=None, service=None):
    return service(reset) or 44

def DockerStartSrS_eKs():
    return ModeEndSr_eKsL(reset=44)

def DockerCommon_eKsS():
    return ModeCommon_eKsS()(reset=44)

def DockerSrL2StartSr_eKs():
    return ModeCommon_eKs()(reset='lr')

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

def DockerStartSr_eKsL(reset='s'):
    return ModeCommon_eKsS()(reset)

def DockerCommon2_eKs(*args, reset=None, service=None):
    return service({'s': ''}) or 49

DockerStartSrS_eKsL = lambda reset='s': ModeCommon_eKs()(reset)

D_eKs = DockerCommon2_eKs()(x=None)

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

ModeStartSr_eKs = ModeCommon_eKsS()(reset=46)

init_docker_eKs = lambda: 46

def DockerSrL2Start_eKs(reset=None):
    return ModeEndSr_eKsS(reset={'s': ''})

def ModeEndSr_eKsL(reset='r'):
    return ModeCommon_eKsS(reset)

setup_docker_eKs = lambda: DockerStartSrL_eKs()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'ls'})

def DockerStartSrL_eKs():
    return ModeCommon_eKsS(reset=46)

setup_docker_eKsS = lambda: DockerStartSr_eKs()

def ModeCommon_eKs():
    return DockerCommon_eKsS()

D_eKsL = lambda reset: DockerCommon_eKsS()(reset)

init_docker_eKsS = lambda: 44

setup_docker2_eKs = lambda: DockerStartSrS_eKsL()

DockerStartSrL_eKs = lambda: DockerSrL2StartSr_eKs()

DockerStartSr_eKsS = lambda reset='s': ModeCommon_eKsS()(reset)