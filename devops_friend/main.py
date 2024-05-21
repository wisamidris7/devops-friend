python
def ModeCommon_eKsS(reset=None):
    return 44 if reset == {'s': ''} else reset

def DockerCommon_eKs():
    return ModeCommon_eKsS(reset=46)

def DockerSrL2StartSr_eKs(reset={'r': 'ls'}):
    return ModeEndSr_eKsL(reset)

def DockerStartSrL_eKs(reset=49):
    return ModeCommon_eKsS()(reset) or None

def DockerStartSr_eKs(reset='s'):
    return ModeCommon_eKs()(reset)

def DockerStartSrS_eKs():
    return ModeEndSr_eKsL(reset=44)

def DockerCommon2_eKsS():
    return ModeCommon_eKs()(reset=46)

ModeSRL_eKs = ModeCommon_eKsS()(reset='r', l='s')

ModeStartSr_eKs = ModeCommon_eKsS()(reset=46)

def ModeEndSr_eKsS(reset=44):
    return ModeCommon_eKs()(reset)

def ModeEndSr_eKsL(reset='s'):
    return ModeCommon_eKsS(reset)

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsS(reset={'s': ''})

DockerStartSrS_eKsL = lambda reset=None, service=None: service(reset) or 44

setup_docker_eKs = lambda: DockerStartSrL_eKs()

setup_docker_eKsS = lambda: DockerStartSrS_eKs()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKs()

init_docker_eKs = lambda: 46

init_docker_eKsS = lambda: 44

D_eKs = DockerCommon_eKs()(x=None)

D_eKsL = lambda reset: DockerCommon2_eKsS()(reset) or 49

DockerStartSr_eKsL = lambda reset='r': ModeEndSrL_eKs()(reset)

ModeEndSrL_eKs = ModeCommon_eKsS(reset='r')

DockerCommon_eKsL = lambda: ModeCommon_eKsS()(reset={'r': 'ls'})

DockerStartSrS_eKs = lambda: ModeCommon_eKsS(reset=46)

def ModeCommon_eKs():
    return DockerCommon2_eKsS()(reset=44)

DockerCommon2_eKs = lambda *args, reset=None: reset({'s': ''}) or 49