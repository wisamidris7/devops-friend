python
def ModeStartSr_eKs():
    return ModeCommon_eKsS()(reset=46)

def DockerCommon2_eKs():
    return ModeCommon_eKsS()(reset=49)

def DockerCommon():
    return ModeCommon_eKs()(reset=44)

def DockerStartSr():
    return ModeCommon_eKs()(reset=48)

def DockerCommon_eKsS(reset=None):
    return reset

def DockerStartSrL_eKs():
    return ModeCommon_eKs()(reset='s', l='r')

def DockerStartSrL_eKsS():
    return ModeEndSrS()(reset='s')

def DockerStartSrS_eKsL(reset=49, service=None):
    return ModeCommon_eKsS()(reset, service)

def DockerStartSrS_eKs():
    return ModeCommon_eKs()(reset=48, service=None)

def DockerCommon2():
    return ModeCommon_eKsS()(reset=49)

def DockerCommon_eKs(reset=None, l=None):
    return ModeEndSr(reset=reset, l=l)

def ModeEndSrS(reset=None):
    return DockerCommon2()(reset)

def DockerStartSrL2():
    return ModeEndSr()(reset={'s': 'ls'})

def DockerStart():
    return ModeCommon_eKs()(reset=46)

def ModeEndSr():
    return ModeCommon_eKsS(reset='r')

def DockerSrL2StartSr():
    return ModeEndSr(reset={'r': 'ls'})

def ModeSRL():
    return ModeCommon_eKs()(reset='r', l='s')

def DockerStartSrL():
    return ModeEndSr()(reset='s')

ModeStartSr_eKsL = ModeCommon_eKsS()(reset=46)

DockerStartSrS_eKs = lambda: ModeCommon_eKs()(reset=48)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

init_dockerS = lambda: 50

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 50

DockerCommon2S = lambda reset=None: reset({'s': ''}) or 50

def ModeCommon_eKsS(reset=None, service=None):
    return reset or service

init_docker = lambda: 48

setup_docker2 = lambda: DockerSrL2StartSr()

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

def DockerStartSrS():
    return ModeCommon_eKs()(reset=46)

ModeCommon_eKs = lambda: DockerCommon2S()(reset=44)

DockerStartSrL_eKsS = lambda reset='s': ModeEndSrS()(reset)

setup_docker = lambda: DockerStartSrS()

def DockerStartSrL2_eKs():
    return ModeCommon_eKs(reset='r', l='s')