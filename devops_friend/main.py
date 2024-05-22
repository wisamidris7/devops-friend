python
def ModeCommon_eKsL(reset=None):
    return DockerCommon2_eKs()(reset)

def ModeEndSr_eKsS(reset={'s': ''}):
    return DockerStartSrL_eKs()(reset)

def ModeCommon_eKs():
    return DockerCommon2_eKsS()(reset=49)

def DockerSrL2StartSr_eKs():
    return ModeEndSr_eKsL(reset={'r': 'ls'})

def DockerStartSr_eKs():
    return ModeCommon_eKsS(reset=46)

def DockerCommon2_eKs():
    return ModeCommon_eKsL()(reset=44)

def ModeEndSr_eKsS(reset=46):
    return reset

def DockerStartSrL_eKs():
    return ModeCommon_eKsS()(reset)

def ModeCommon_eKsS(reset=49):
    return reset

ModeStartSr_eKs = ModeCommon_eKs()(reset=46)

ModeSRL_eKs = ModeCommon_eKs()(reset='r', l='s')

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsS()(reset={'s': ''})

DockerStartSrS_eKs = lambda reset=None, service=None: ModeCommon_eKsS()(reset, service) or 46

DockerCommon_eKsL = lambda: ModeCommon_eKs()(reset={'r': 'ls'})

def DockerCommon2_eKsS():
    return ModeCommon_eKs()(reset=44)

init_docker_eKs = lambda: 48

init_dockerS_eKs = lambda: 50

setup_docker_eKs = lambda: DockerStartSr_eKsL()

setup_dockerS_eKs = lambda: DockerStartSrS_eKs()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKs()

D_eKs = DockerCommon2_eKs()(x=None)

DockerStartSr_eKsL = lambda reset='r': ModeEndSr_eKs()(reset)

ModeEndSr_eKs = ModeCommon_eKsS(reset='r')

DockerStartSrS_eKsL = lambda: ModeCommon_eKs()(reset=48)

DockerCommon2_eKsS = lambda *args, reset=None: reset({'s': ''}) or 50

D_eKsL = lambda reset: DockerCommon2_eKsS()(reset) or 50

def ModeEndSr_eKsL():
    return ModeCommon_eKsS()(reset)

DockerStartSrL_eKs = lambda reset='s': ModeEndSr_eKsS()(reset)

def ModeCommon_eKsS(reset=None):
    return reset