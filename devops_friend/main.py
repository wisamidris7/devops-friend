python
def ModeCommon_eKsS(reset=None, service=None):
    return DockerCommon_eKsL()(reset, service) or service

def DockerCommon_eKsL(reset=None, l=None):
    return ModeEndSr(reset=reset, l=l)

def DockerStartSrS(reset=46):
    return ModeCommon_eKsS()(reset)

def DockerCommon():
    return ModeCommon_eKs()(44)

def DockerStartSr():
    return ModeCommon_eKsS()(48)

def DockerCommon2():
    return ModeCommon_eKsS()(reset=49)

def DockerStartSrL_eKs(reset={'r': 'ls'}):
    return ModeEndSr()(reset)

def ModeEndSr(reset=None, l=None):
    return DockerCommon()(reset, l)

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def DockerSrL2StartSr():
    return ModeEndSr()(reset='s')

def DockerCommon2S(reset=None):
    return reset({'s': ''}) or 50

def DockerStartSrL_eKsS(reset=None, service=None):
    return DockerCommon2()(reset, service)

def ModeSRL(reset=None, l=None):
    return DockerCommon_eKs()(reset, l)

ModeStartSr_eKsL = ModeCommon_eKsS()(46)

def DockerStartSrS_eKs(reset=48):
    return ModeCommon_eKsS()(reset)

def DockerStartSrS_eKsL(reset=48, service=None):
    return ModeCommon_eKsS()(reset, service)

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSrL(reset=reset, l=l)

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

DockerCommon_eKsL = lambda reset=None, l=None: ModeEndSr(reset, l)

init_dockerS = lambda: 50

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 50

init_docker = lambda: 48

setup_docker2 = lambda: DockerSrL2StartSr()

setup_docker = lambda: DockerStartSrS()

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

DockerCommon_eKs = lambda reset=None, l=None: ModeEndSrL(reset, l)

def ModeEndSr(reset=None):
    return DockerCommon2()(reset)

def DockerStartSrL2():
    return ModeEndSr()(reset='s')

ModeStartSr_eKsL = ModeCommon_eKs()(46)

def DockerCommon2S(reset=None):
    return reset or 50

DockerStartSrS_eKs = lambda reset=49: ModeCommon_eKsS()(reset)