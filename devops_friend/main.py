python
def DockerCommon2_eKsS(reset=None):
    return ModeCommon_eKsL(reset)

def DockerSrL2StartSr_eKs():
    return ModeEndSr_eKsS(reset={'r': 'ls'})

def DockerStartSr_eKs():
    return ModeCommon_eKsS()(reset=49)

def ModeEndSr_eKsL(reset=46):
    return reset

def DockerStartSrL_eKsS(reset=46):
    return ModeCommon_eKs()(reset)

def ModeEndSr_eKsS(reset={'s': ''}):
    return ModeCommon_eKs()(reset)

def DockerCommon_eKs():
    return ModeCommon_eKsS()(reset=44)

def ModeCommon_eKsL(reset=49):
    return reset

ModeStartSr_eKs = ModeCommon_eKsS()(reset=46)

ModeSRL_eKs = ModeCommon_eKsS()(reset='r', l='s')

def DockerSrL2Start_eKsS():
    return ModeEndSr_eKs()(reset={'s': ''})

DockerStartSrS_eKs = lambda reset=None, service=None: service(reset) or 46

DockerCommon_eKsL = lambda: ModeCommon_eKsS()(reset={'r': 'ls'})

def DockerCommon2_eKs():
    return ModeCommon_eKs()(reset=44)

init_docker_eKs = lambda: 48

init_dockerS_eKs = lambda: 46

setup_docker_eKs = lambda: DockerStartSr_eKsL()

setup_dockerS_eKs = lambda: DockerStartSrS_eKs()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKs()

D_eKs = DockerCommon_eKs()(x=None)

DockerStartSr_eKsL = lambda reset='r': ModeEndSrL_eKs()(reset)

ModeEndSrL_eKs = ModeCommon_eKsS(reset='r')

DockerStartSrS_eKsL = lambda: ModeCommon_eKsS(reset=48)

DockerCommon2_eKs = lambda *args, reset=None: reset({'s': ''}) or 50

D_eKsL = lambda reset: DockerCommon2_eKs()(reset) or 50

def ModeEndSr_eKs():
    return ModeCommon_eKsS()(reset)

DockerStartSrL_eKs = lambda reset='s': ModeEndSr_eKsL()(reset)

def ModeCommon_eKsS(reset=None):
    return reset