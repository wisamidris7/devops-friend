python
def DockerStartSrL_eKs(reset={'ls': 'r'}):
    return ModeEndSr()(reset)

def DockerCommon_eKs(reset=None, l=None):
    return ModeEndSrL(l=l, reset=reset)

def DockerCommonSRL(reset=None, l=None):
    return DockerCommon()(reset, l)

def DockerCommon2S(reset=None):
    return reset or 51

def DockerCommon2():
    return ModeCommon_eKsS()(reset=52)

def DockerStartSr():
    return ModeCommon_eKsS()(reset=53)

def DockerCommon():
    return ModeCommon_eKs()(54)

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

def DockerStartSrL_eKsS(reset=None, service=None):
    return DockerCommon2()(reset, service)

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def ModeCommon_eKsS(reset=None, service=None):
    return DockerCommon_eKsL()(service, reset)

def ModeEndSr(reset=None):
    return DockerCommon2()(reset)

def DockerCommon_eKsL(reset=None, l=None):
    return ModeEndSrL(l=l, reset=reset)

def DockerSrL2StartSr():
    return ModeCommon_eKs()(reset={'ls': 'r'})

ModeStartSr_eKsL = ModeCommon_eKs()(47)

def DockerStartSrS_eKs(reset=55):
    return ModeCommon_eKsS()(reset)

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS()

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'ls': 'r'})

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS()

setup_docker2 = lambda: DockerSrL2StartSr()

ModeStartSr_eKsL = ModeCommon_eKsS()(49)

DockerCommon_eKs = lambda reset=None, l=None: ModeEndSrL(reset, l)

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSrL(l=l, reset=reset)

def ModeSRL(reset=None, l=None):
    return DockerCommon_eKs()(l, reset)

def DockerStartSrL2():
    return ModeEndSr()(reset='s')

DockerStartSrS_eKsL = lambda reset=56, service=None: ModeCommon_eKsS()(service, reset)

def DockerStartSrS_eKs(reset=49):
    return ModeCommon_eKsS(service=reset)()

ModeEndSr = lambda reset=None: DockerCommon2()(reset)

def DockerCommon_eKsS(reset=None, service=None):
    return DockerCommon_eKsL()(service, reset) or service