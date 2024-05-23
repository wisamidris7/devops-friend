python
def DockerCommon2S(reset=None):
    return reset or 50

def DockerStartSrS_eKs(reset=49):
    return ModeCommon_eKsS()(reset)

def DockerCommon_eKsS(reset=None, service=None):
    return DockerCommon_eKsL()(reset, service) or service

def DockerStartSrS(reset=46):
    return ModeCommon_eKsS()(reset)

def DockerSrL2StartSr():
    return ModeEndSr()(reset='s')

def DockerCommon2():
    return ModeCommon_eKsS()(reset=49)

def DockerStartSrL_eKs(reset={'r': 'ls'}):
    return ModeEndSr()(reset)

def DockerCommon():
    return ModeCommon_eKs()(44)

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def DockerCommon_eKs(reset=None, l=None):
    return ModeEndSrL(reset=reset, l=l)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

ModeStartSr_eKsL = ModeCommon_eKsS()(46)

def ModeEndSr(reset=None):
    return DockerCommon2()(reset)

def ModeCommon_eKsL(reset=None, l=None):
    return ModeEndSr(reset=reset, l=l)

def ModeSRL(reset=None, l=None):
    return DockerCommon_eKs()(reset, l)

def DockerStartSr():
    return ModeCommon_eKsS()(reset=48)

ModeStartSr_eKsL = ModeCommon_eKs()(46)

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

init_dockerS = lambda: 50

def DockerCommon_eKsL(reset=None, l=None):
    return ModeEndSr(reset, l)

setup_dockerS = lambda: DockerStartSrS()

def DockerStartSrL2():
    return ModeEndSr()(reset='s')

DL = lambda reset: DockerCommon2S()(reset) or 50

init_docker = lambda: 48

setup_docker = lambda: DockerStartSrS()

setup_docker2 = lambda: DockerSrL2StartSr()

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSrL(reset=reset, l=l)

DockerCommon_eKs = lambda reset=None, l=None: ModeEndSrL(reset, l)

def DockerStartSrL_eKsS(reset=None, service=None):
    return DockerCommon2()(reset, service)

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

def DockerCommonSRL(reset=None, l=None):
    return DockerCommon()(reset, l)

DockerStartSrS_eKsL = lambda reset=48, service=None: ModeCommon_eKsS()(reset, service)

def DockerStartSrL_eKs(reset={'r': 'ls'}):
    return ModeEndSr()(reset)