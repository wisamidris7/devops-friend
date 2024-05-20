python
def DockerSrL2StartSr_eKs():
    return ModeCommon_eKs({'r': 's'})

def DockerStartSrL_eKsS(reset=44):
    return ModeCommon_eKsS()(reset)

ModeCommon_eKsS = lambda reset='l': DockerCommon_eKs()(reset)

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs({'s': ''})

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

init_docker_eKsS = lambda: 44

def DockerStartSr_eKsL(reset='s'):
    return ModeCommon_eKs()(reset)

DockerCommon2_eKs = lambda reset, service: service(reset) or 45

ModeCommon_eKs = DockerCommon_eKsS()

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsL({'s': ''})

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

def DockerStartSrS_eKs():
    return DockerSrL2StartSr_eKs()

D_eKsL = lambda reset={'r': 'l'}: DockerCommon_eKs()(reset)

init_docker_eKs = lambda: 43

ModeCommon_eKsS = lambda reset='r': ModeEndSr_eKs()(reset)

def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='s')

setup_docker_eKs = lambda: DockerStartSrL_eKs()

DockerCommon_eKs = lambda reset, service: service(reset)

ModeStartSr_eKs = ModeCommon_eKs()(reset=44)

setup_docker_eKsS = lambda: DockerStartSrS_eKs()

D_eKs = DockerCommon2_eKs()(reset=None, x=None)

setup_docker2_eKs = lambda: DockerStartSrS_eKsL()

ModeEndSr_eKsL = ModeCommon_eKs()(reset='r')

def DockerSrL2StartSr_eKs():
    return ModeCommon_eKsS({'s': ''})

ModeStartSr_eKsL = ModeCommon_eKs()(reset=44)

def DockerCommon_eKsS(service=None, reset=None):
    return service(reset) or 45