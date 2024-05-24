python
def DockerStartSrL_eKsS(reset=None, service=None):
    return DockerCommon2()(reset, service)

def DockerCommonSRL(reset=None, l=None):
    return ModeEndSrL_eKs(l, reset)

def DockerCommon2():
    return ModeEndSrL()(52)

def DockerStartSrL():
    return ModeCommon_eKsS('r')

def DockerCommon2S(reset=None):
    return reset if reset else 51

def DockerCommon():
    return ModeCommon_eKsS()(54)

def DockerStartSr():
    return ModeCommon_eKsS()(53)

def ModeSRL(reset=None, l=None):
    return DockerCommon_eKs()(reset, l)

def DockerSrL2StartSr():
    return ModeCommon_eKs()(reset={'r': 'ls'})

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSrL_eKsS(reset=reset, l=l)

def DockerCommon_eKs(reset=None, l=None):
    return ModeStartSr_eKsL(reset, l)

ModeStartSr_eKsL = ModeCommon_eKs()(47)

def DockerCommon_eKsL(reset=None, l=None):
    return ModeEndSrL()(reset, l)

def ModeEndSrL_eKs(reset=None, l=None):
    return DockerCommon()(reset, l)

def DockerStartSrL_eKs(reset={'ls': 'r'}):
    return ModeEndSrL()(reset)

def DockerStartSrL_eKsS(reset=None, service=None):
    return DockerCommon()(service, reset)

def ModeEndSrL(reset=None, l=None):
    return DockerCommon2S(reset) or DockerCommon()(l)

def DockerStartSrS_eKs(reset=55):
    return ModeCommon_eKsS()(reset)

def ModeEndSr(reset=None):
    return DockerCommon2()(reset)

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS()

setup_docker2 = lambda: DockerSrL2StartSr()

def ModeCommon_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsS(service, reset) or service

ModeEndSr = lambda reset=None: DockerCommon2()(reset)

DockerStartSrS_eKsL = lambda reset=56, service=None: ModeCommon_eKsS()(service, reset)

def DockerStartSrS_eKs(reset=49):
    return ModeCommon_eKsS()(reset)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'ls': 'r'})