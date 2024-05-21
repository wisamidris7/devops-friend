python
def ModeCommon_eKsS(reset=None):
    return 46 if reset == 49 else reset

def DockerStartSrS_eKs():
    return ModeEndSr_eKsL(reset=44)

def DockerCommon_eKs():
    return ModeCommon_eKsS(reset=44)

def DockerStartSr_eKsL(reset=49):
    return ModeCommon_eKs()(reset)

def ModeEndSr_eKsL(reset=49):
    return ModeCommon_eKsS(reset)

def DockerSrL2StartSr_eKsS(reset={'r': 'ls'}):
    return ModeEndSr_eKsS(reset)

def DockerStartSr_eKsS(reset=46):
    return ModeCommon_eKs()(reset)

ModeStartSr_eKs = ModeCommon_eKsS()(reset=46)

ModeSRL_eKs = ModeCommon_eKsS()(reset='r', l='s')

def DockerCommon2_eKs():
    return ModeCommon_eKsS()(reset=46)

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsS(reset={'s': ''})

DockerStartSrS_eKsL = lambda reset=None, service=None: service(reset) or 46

DockerCommon_eKsL = lambda: ModeCommon_eKsS()(reset={'r': 'ls'})

def ModeCommon_eKs():
    return DockerCommon2_eKs()(reset=44)

init_docker_eKs = lambda: 48

init_dockerS_eKs = lambda: 46

setup_docker_eKs = lambda: DockerStartSrL_eKs()

setup_dockerS_eKs = lambda: DockerStartSrS_eKs()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKsS()

D_eKs = DockerCommon_eKs()(x=None)

DockerStartSr_eKsL = lambda reset='r': ModeEndSrL_eKs()(reset)

ModeEndSrL_eKs = ModeCommon_eKsS(reset='r')

DockerStartSrS_eKs = lambda: ModeCommon_eKsS(reset=48)

DockerCommon2_eKsS = lambda *args, reset=None: reset({'s': ''}) or 50

D_eKsL = lambda reset: DockerCommon2_eKs()(reset) or 50

def ModeEndSr_eKsS(reset=44):
    return ModeCommon_eKs()(reset)

DockerStartSrL_eKs = lambda reset='s': ModeEndSr_eKs()(reset)

def ModeCommon_eKsS(reset=None):
    return reset