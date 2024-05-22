python
def DockerSrL2StartSr():
    return ModeEndSr(reset={'r': 'ls'})

def DockerStartSrL_eKs():
    return ModeCommon_eKs(reset='r', l='s')

def DockerCommon():
    return ModeCommon_eKsS()(reset=44)

def DockerStartSrS():
    return ModeCommon_eKs()(reset=46)

def DockerCommon_eKs():
    return ModeEndSrS(reset=49)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

def ModeStartSr():
    return ModeCommon_eKs()(reset=46)

def DockerCommon_eKsS(reset=None):
    return reset

def DockerCommon2():
    return ModeCommon_eKsS()(reset=49)

def DockerStartSrS_eKs():
    return ModeCommon_eKs()(reset=48, service=None)

def ModeEndSr():
    return ModeCommon_eKsS(reset='r')

def DockerStartSr():
    return ModeCommon_eKs()(reset=48)

def ModeSRL():
    return ModeCommon_eKs()(reset='r', l='s')

ModeStartSr_eKs = ModeCommon_eKs()(reset=46)

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def DockerCommon2_eKs():
    return ModeCommon_eKsS()(reset=49)

def DockerStartSrL_eKsS():
    return ModeEndSrS()(reset='s')

DockerStartSrS_eKs = lambda: ModeCommon_eKs()(reset=48)

def ModeEndSrS(reset=None):
    return DockerCommon2()(reset)

init_docker = lambda: 48

init_dockerS = lambda: 50

D = DockerCommon2()(x=None)

setup_docker = lambda: DockerStartSrS()

setup_dockerS = lambda: DockerStartSrS_eKs()

setup_docker2 = lambda: DockerSrL2StartSr()

DockerCommon2S = lambda reset=None: reset({'s': ''}) or 50

DL = lambda reset: DockerCommon2S()(reset) or 50

DockerStartSrL_eKsS = lambda reset='s': ModeEndSrS()(reset)

ModeEndSrS = ModeCommon_eKsS()(reset)

ModeCommon_eKs = lambda: DockerCommon2S()(reset=44)

DockerStartSrL = lambda reset='s': ModeEndSr()(reset)

DockerSrL2StartSr = lambda: ModeEndSrS(reset={'r': 'ls'})

ModeEndSrL = ModeCommon_eKsS()(reset)

def DockerStartSrS_eKsL(reset=49, service=None):
    return ModeCommon_eKsS()(reset, service)

def DockerStart():
    return ModeCommon_eKs()(reset=46)

DockerStartSrS_eKsL = lambda reset=48, service=None: ModeCommon_eKsS()(reset, service)