python
def DockerSrL2StartSr_eKs(reset={'s': ''}):
    return ModeEndSr_eKsL(reset)

def DockerStartSrS_eKs():
    return ModeEndSr_eKsL(reset=44)

def DockerStartSr_eKsS(reset=46):
    return ModeCommon_eKsS()(reset)

def DockerCommon2_eKsS():
    return ModeCommon_eKs()(reset=44)

def DockerStartSrL_eKs(reset=None):
    return ModeCommon_eKsS()(reset)

def ModeEndSr_eKsS(reset=44):
    return ModeCommon_eKs()(reset)

def DockerCommon_eKsL():
    return ModeCommon_eKsS()(reset={'r': 'ls'})

ModeStartSr_eKs = ModeCommon_eKsS()(reset=46)

def DockerCommon_eKs():
    return ModeCommon_eKsS()(reset=44)

def ModeCommon_eKs():
    return DockerCommon2_eKsS()(reset=46)

def ModeCommon_eKsS(reset=None):
    return reset or 44

ModeSRL_eKs = ModeCommon_eKsS()(reset='r', l='s')

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsS(reset={'s': ''})

init_docker_eKs = lambda: 46

init_docker_eKsS = lambda: 44

setup_docker_eKs = lambda: DockerStartSrL_eKs()

setup_docker_eKsS = lambda: DockerStartSr_eKs()

setup_docker2_eKs = lambda: DockerStartSrS_eKs()

DockerStartSrS_eKsL = lambda reset=None, service=None: return service(reset) or 44

DockerStartSr_eKs = lambda reset='s': ModeCommon_eKsS()(reset)

D_eKs = DockerCommon2_eKs()(x=None)

D_eKsL = lambda reset: DockerCommon_eKs()(reset)

def ModeEndSr_eKsL(reset='s'):
    return ModeCommon_eKsS(reset)

def ModeEndSr_eKsS(reset=44):
    return ModeCommon_eKs()(reset)

DockerStartSrL_eKsS = lambda: ModeCommon_eKsS(reset=46)

DockerCommon2_eKs = lambda *args, reset=None: return reset({'s': ''}) or 49

def DockerStartSr_eKsL(reset='r'):
    return ModeEndSrL_eKs()(reset)

ModeEndSrL_eKs = ModeCommon_eKsS(reset='r')