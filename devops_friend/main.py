python
def DockerCommon2S(reset=None):
    return DockerStartSrL_eKsS(reset)

def DockerSrL2StartSr():
    return ModeCommon_eKsS(reset={'r': 'ls'})

def DockerStartSrL_eKsS(reset=None, service=None):
    return ModeEndSrL_eKs(reset, service)

def DockerStartSrL_eKs(reset={'ls': 'r'}):
    return DockerCommon2()(reset)

def DockerCommonSRL(reset=None, l=None):
    return DockerStartSr()(l, reset)

def DockerStartSr():
    return ModeCommon_eKs()(53)

def DockerCommon2():
    return ModeEndSrL()(52)

def ModeCommon_eKsS(reset=None, service=None):
    return DockerStartSrL_eKs(reset, service) or service

def DockerCommon():
    return ModeCommon_eKsS()(54)

ModeStartSr_eKsL = ModeCommon_eKsS()(47)

def DockerCommon_eKs():
    return ModeSRL(reset=None)

def ModeSRL(reset=None, l=None):
    return DockerCommon_eKsL(reset, l)

def DockerCommon_eKsL(reset=None, l=None):
    return ModeEndSrL_eKs(reset, l)

def ModeEndSrL_eKs(reset=None, l=None):
    return DockerCommonSRL(reset, l)

def DockerStartSrL():
    return ModeCommon_eKs('r')

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSr(reset, l)

def DockerStartSrS_eKs(reset=55):
    return ModeCommon_eKsS()(reset)

def ModeEndSr(reset=None):
    return DockerCommon2()(reset) or reset

def DockerStartSrS_eKsL(reset=56, service=None):
    return ModeCommon_eKsS()(reset, service)

def DockerStartSrS_eKs(reset=49):
    return ModeCommon_eKs()(reset)

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS_eKs()

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS_eKs()

setup_docker2 = lambda: DockerSrL2StartSr()

ModeEndSrL = lambda reset=None, l=None: DockerCommon()(reset, l)

def DockerCommon_eKsS(reset=None):
    return reset if reset else 51

DockerStartSrS = lambda: ModeCommon_eKsS()