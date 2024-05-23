python
def DockerStartSrL_eKs():
    return ModeEndSrS()(reset={'r': 'ls'})

def DockerCommon():
    return ModeCommon_eKsS()(reset=44)

def DockerStartSr():
    return ModeCommon_eKsS()(reset=48)

def DockerStartSrL_eKsS(reset={'r': 'ls'}):
    return ModeEndSr()(reset)

def DockerCommon2():
    return ModeCommon_eKs()(reset=49)

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def DockerCommon_eKsS(reset=None, service=None):
    return DockerCommon()(reset) or service

def DockerSrL2StartSr():
    return ModeEndSr()(reset='s')

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSrL(reset=reset, l=l)

def DockerStartSrL2():
    return ModeEndSr()(reset='s')

def DockerCommon2S(reset=None):
    return reset({'s': ''}) or 50

def ModeEndSr(reset=None, l=None):
    return DockerCommon_eKs()(reset, l)

def DockerStartSrL2_eKs():
    return ModeCommon_eKs()(reset='r', l='s')

def DockerStartSrS():
    return ModeCommon_eKsS()(reset=46)

def DockerStartSrS_eKs(reset=49):
    return ModeCommon_eKsS()(reset)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

def ModeEndSrS(reset=None):
    return DockerCommon2()(reset)

ModeStartSr_eKsL = ModeCommon_eKsS()(reset=46)

def DockerStartSrS_eKsL(reset=48, service=None):
    return ModeCommon_eKsS()(reset, service)

init_dockerS = lambda: 50

DockerCommon_eKs = lambda reset=None, l=None: ModeEndSr(reset=reset, l=l)

def DockerStartSrS_eKs(reset=48):
    return ModeCommon_eKsS()(reset)

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 50

setup_docker = lambda: DockerStartSrS()

init_docker = lambda: 48

setup_docker2 = lambda: DockerSrL2StartSr()

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

ModeStartSr_eKsL = ModeCommon_eKs()(reset=46)

def ModeCommon_eKsS()(reset=None, service=None):
    return service or reset

def DockerStartSrL_eKs():
    return ModeCommon_eKsS()(reset='r', l='s')

def ModeSRL():
    return ModeCommon_eKs()(reset='r', l='s')