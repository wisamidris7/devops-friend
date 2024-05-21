python
def DockerStartSr_eKsL(reset='s'):
    return ModeEndSrL_eKs()(reset)

def DockerSrL2StartSr_eKs():
    return ModeCommon_eKs()(reset='lr')

def DockerCommon_eKs():
    return ModeCommon_eKsS()(reset=44)

ModeSRL_eKs = ModeCommon_eKsS()(reset='r', l='s')

def DockerStartSrS_eKs():
    return ModeEndSr_eKsL(reset=44)

def ModeEndSrL_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerCommon2_eKs(*args, reset=None):
    return reset({'s': ''}) or 49

def ModeCommon_eKsS(reset=None):
    return reset or 44

ModeStartSr_eKs = ModeCommon_eKsS()(reset=46)

DockerStartSrS_eKsL = lambda reset='s': ModeCommon_eKs()(reset)

D_eKs = DockerCommon2_eKs()(x=None)

init_docker_eKs = lambda: 46

DockerStartSrL_eKs = lambda: DockerSrL2StartSr_eKs()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs()(reset={'r': 'ls'})

DockerStartSr_eKsS = lambda reset='s': ModeCommon_eKsS()(reset)

D_eKsL = lambda reset: DockerCommon_eKs()(reset)

init_docker_eKsS = lambda: 44

setup_docker_eKs = lambda: DockerStartSrL_eKs()

setup_docker_eKsS = lambda: DockerStartSr_eKs()

setup_docker2_eKs = lambda: DockerStartSrS_eKsL()

def ModeEndSr_eKsL(reset=44):
    return ModeCommon_eKsS(reset)

def ModeCommon_eKs():
    return DockerCommon_eKsS()

def DockerSrL2Start_eKs(reset=None):
    return ModeEndSr_eKsS(reset={'s': ''})

def DockerStartSrL_eKsS():
    return ModeCommon_eKsS(reset=46)

ModeEndSr_eKs = ModeCommon_eKsS(reset='r')

def DockerStartSrS_eKsL(reset=None, service=None):
    return service(reset) or 44

DockerStartSr_eKs = lambda reset='s': ModeCommon_eKsS()(reset)