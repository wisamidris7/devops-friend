python
def ModeCommon_eKsS(reset=None):
    return reset

def DockerCommon_eKs():
    return ModeCommon_eKsS()(reset=44)

def DockerStartSr_eKsS():
    return ModeCommon_eKs()(reset=46)

def DockerSrL2StartSr_eKs():
    return ModeEndSr_eKsS(reset=49)

def DockerCommon2_eKsL(reset=None):
    return ModeCommon_eKs()(reset)

def DockerStartSrS_eKsL(reset=49, service=None):
    return ModeCommon_eKsS()(reset, service)

def ModeEndSr_eKs():
    return ModeCommon_eKsS(reset='r')

def DockerStartSr_eKs():
    return ModeCommon_eKs()(reset=48)

def DockerSrL2Start_eKs():
    return ModeCommon_eKs()(reset={'r': 'ls'})

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

ModeStartSr_eKs = ModeCommon_eKs()(reset=46)

def DockerCommon2_eKs():
    return ModeCommon_eKsS()(reset=49)

DockerStartSrS_eKs = lambda: ModeCommon_eKs()(reset=48)

def ModeEndSr_eKsS(reset=None):
    return DockerCommon2_eKs()(reset)

init_docker_eKs = lambda: 48

init_dockerS_eKs = lambda: 50

D_eKs = DockerCommon2_eKs()(x=None)

setup_docker_eKs = lambda: DockerStartSr_eKsS()

setup_dockerS_eKs = lambda: DockerStartSrS_eKsL()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKs()

DockerCommon2_eKsS = lambda reset=None: reset({'s': ''}) or 50

D_eKsL = lambda reset: DockerCommon2_eKsS()(reset) or 50

DockerStartSrL_eKs = lambda reset='s': ModeEndSr_eKsS()(reset)

ModeEndSr_eKsS = ModeCommon_eKsS()(reset)

ModeCommon_eKs = lambda: DockerCommon2_eKsS()(reset=44)

DockerStartSrL_eKsL = lambda reset='s': ModeEndSr_eKs()(reset)

DockerSrL2StartSr = lambda: ModeEndSr_eKsS(reset={'r': 'ls'})

ModeEndSr_eKsL = ModeCommon_eKsS()(reset)

def DockerStartSr():
    return ModeCommon_eKs()(reset=46)