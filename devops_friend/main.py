python
def DockerCommon2_eKsL(reset={'r': 'ls'}):
    return ModeCommon_eKs()(reset)

def DockerStartSrS_eKs(reset=49, service=None):
    return ModeCommon_eKsS()(reset, service)

def DockerSrL2StartSr_eKs():
    return ModeEndSr_eKsS(reset={'s': ''})

def DockerCommon_eKs():
    return ModeCommon_eKsS()(reset=44)

def ModeCommon_eKsS(reset=None):
    return reset

def DockerStartSr_eKsS():
    return ModeCommon_eKs()(reset=46)

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerStartSrL_eKs(reset='s'):
    return ModeEndSr_eKsS()(reset)

def DockerSrL2Start_eKs():
    return ModeCommon_eKs()(reset={'r': 'ls'})

ModeStartSr_eKs = ModeCommon_eKs()(reset=46)

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

DockerCommon2_eKsS = lambda reset=None: reset({'s': ''}) or 50

def ModeEndSr_eKsS(reset=46):
    return DockerCommon2_eKs()(reset)

init_dockerS_eKs = lambda: 50

init_docker_eKs = lambda: 48

D_eKsL = lambda reset: DockerCommon2_eKsS()(reset) or 50

setup_dockerS_eKs = lambda: DockerStartSrS_eKs()

setup_docker_eKs = lambda: DockerStartSr_eKsS()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKs()

def DockerCommon2_eKs():
    return ModeCommon_eKsL()(reset=44)

ModeEndSr_eKsL = ModeCommon_eKsS()(reset)

DockerStartSr_eKsL = lambda reset='r': ModeEndSr_eKs()(reset)

def ModeCommon_eKs():
    return DockerCommon2_eKsS()(reset=49)

DockerStartSrS_eKsL = lambda: ModeCommon_eKs()(reset=48)

D_eKs = DockerCommon2_eKs()(x=None)

DockerStartSrL_eKs = lambda reset='s': ModeEndSr_eKsS()(reset)

def DockerSrL2StartSr():
    return ModeEndSr_eKsL(reset={'r': 'ls'})