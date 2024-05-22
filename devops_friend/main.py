python
def DockerCommon_eKs(reset=None, l=None):
    return ModeEndSrL(reset, l)

def DockerCommon():
    return ModeCommon_eKsS()(44)

def DockerStartSrL_eKs():
    return ModeEndSrS(reset={'r': 'ls'})

def DockerCommon_eKsS(reset=None, service=None):
    return DockerCommon()(reset) or service

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def DockerSrL2StartSr():
    return ModeEndSr()(reset='s')

def DockerStartSr():
    return ModeCommon_eKsS()(48)

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSrL(reset=reset, l=l)

def DockerStartSrL_eKsS(reset={'r': 'ls'}):
    return ModeEndSr()(reset)

def ModeEndSr(reset=None, l=None):
    return DockerCommon_eKs()(reset, l)

def DockerCommon2():
    return ModeCommon_eKsS()(reset=49)

def DockerStartSrL2():
    return ModeEndSr()(reset='s')

ModeStartSr_eKsL = ModeCommon_eKsS()(46)

def ModeCommon_eKsS()(reset=None, service=None):
    return service or reset

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

def DockerStartSrS_eKs(reset=49):
    return ModeCommon_eKsS()(reset)

def DockerStartSrS():
    return ModeCommon_eKsS()(46)

init_dockerS = lambda: 50

def ModeEndSrS(reset=None):
    return DockerCommon2()(reset)

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 50

setup_docker = lambda: DockerStartSrS()

init_docker = lambda: 48

setup_docker2 = lambda: DockerSrL2StartSr()

def DockerStartSrS_eKs(reset=48):
    return ModeCommon_eKsS()(reset)

def DockerCommon2S(reset=None):
    return reset({'s': ''}) or 50

ModeStartSr_eKsL = ModeCommon_eKs()(46)

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

DockerCommon_eKsL = lambda reset=None, l=None: ModeEndSr(reset, l)

def DockerStartSrS_eKsL(reset=48, service=None):
    return ModeCommon_eKsS()(reset, service)

def ModeSRL():
    return ModeCommon_eKs()(reset='r', l='s')