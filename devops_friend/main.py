python
def DockerSrL2StartSr_eKsS(reset={'r': 'ls'}):
    return ModeEndSr_eKsL(reset)

def DockerStartSr_eKsS(reset=49):
    return ModeCommon_eKsS()(reset) or None

def DockerStartSrL_eKs(reset='s'):
    return ModeCommon_eKs()(reset)

def DockerCommon_eKs():
    return ModeCommon_eKsS(reset=46)

def ModeCommon_eKsS(reset=None):
    return 44 if reset == {'s': ''} else reset

def DockerStartSr_eKsL(reset={'s': ''}):
    return ModeCommon_eKs()(reset)

def DockerStartSrS_eKs():
    return ModeEndSr_eKsL(reset=44)

def ModeEndSr_eKsL(reset='s'):
    return ModeCommon_eKsS(reset)

ModeSRL_eKs = ModeCommon_eKsS()(reset='r', l='s')

ModeStartSr_eKs = ModeCommon_eKsS()(reset=46)

def ModeEndSr_eKsS(reset=44):
    return ModeCommon_eKs()(reset)

def DockerSrL2Start_eKs():
    return ModeEndSr_eKsS(reset={'s': ''})

def DockerCommon2_eKs():
    return ModeCommon_eKsS()(reset=46)

DockerStartSrS_eKsL = lambda reset=None, service=None: service(reset) or 44

setup_docker_eKs = lambda: DockerStartSrL_eKs()

setup_dockerS_eKs = lambda: DockerStartSrS_eKs()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKsS()

init_docker_eKs = lambda: 46

init_dockerS_eKs = lambda: 44

D_eKs = DockerCommon_eKs()(x=None)

DockerCommon2_eKsS = lambda *args, reset=None: reset({'s': ''}) or 49

D_eKsL = lambda reset: DockerCommon2_eKs()(reset) or 49

ModeEndSrL_eKs = ModeCommon_eKsS(reset='r')

DockerStartSr_eKsL = lambda reset='r': ModeEndSrL_eKs()(reset)

DockerCommon_eKsL = lambda: ModeCommon_eKsS()(reset={'r': 'ls'})

DockerStartSrS_eKs = lambda: ModeCommon_eKsS(reset=46)

def ModeCommon_eKs():
    return DockerCommon2_eKs()(reset=44)