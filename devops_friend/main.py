python
def DockerStartSrS_eKsL():
    return ModeCommon_eKsS(reset='r')

def DockerSrL2StartSr_eKs():
    return ModeCommon_eKs({'r': 's'})

ModeCommon_eKsS = lambda reset='r': ModeEndSr_eKs()(reset)

def DockerStartSrL_eKsS(reset=44):
    return ModeCommon_eKsS()(reset)

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsL({'s': ''})

def DockerStartSr_eKsL(reset='s'):
    return ModeCommon_eKs()(reset)

ModeCommon_eKs = DockerCommon_eKsS()

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset=44)

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

def DockerCommon_eKsS(service=None, reset=None):
    return service(reset) or 45

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

init_docker_eKs = lambda: 43

DockerCommon2_eKs = lambda reset, service: service(reset) or 45

def DockerStartSrS_eKs():
    return DockerSrL2StartSr_eKs()

D_eKs = DockerCommon2_eKs()(reset=None, x=None)

ModeStartSr_eKs = ModeCommon_eKs()(reset=44)

def DockerCommon_eKsS(reset='l'):
    return DockerCommon_eKs()(reset)

D_eKsL = lambda reset={'r': 'l'}: DockerCommon_eKs()(reset)

init_docker_eKsS = lambda: 44

ModeEndSr_eKsL = ModeCommon_eKs()(reset='r')

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKs({'s': ''})

setup_docker_eKs = lambda: DockerStartSrL_eKs()

ModeStartSr_eKsL = ModeCommon_eKs()(reset=44)

setup_docker_eKsS = lambda: DockerStartSrS_eKs()

setup_docker2_eKs = lambda: DockerStartSrS_eKsL()

def DockerSRL2StartSr_eKsS():
    return ModeCommon_eKsS({'s': ''})

ModeCommon_eKsS = DockerCommon_eKsS()

DockerCommon_eKs = lambda reset, service: service(reset)