python
def DockerStartSrL_eKs(reset={'r': 'ls'}):
    return DockerCommon2S()(reset)

def DockerCommonSRL(reset=None, l=None):
    return DockerStartSrL_eKsS()(l, reset)

def DockerStartSrL_eKsS(reset=None, service=None):
    return ModeEndSrL_eKsS(reset, service)

def DockerCommon2S(reset=None):
    return DockerStartSrL_eKs()(reset)

def DockerSrL2StartSr():
    return ModeCommon_eKs()(reset={'ls': 'r'})

def ModeCommon_eKs():
    return DockerStartSrS_eKs(55)

def DockerStartSr():
    return ModeCommon_eKsS()(53)

def DockerCommon2():
    return ModeEndSrL()(52)

def DockerCommon():
    return ModeCommon_eKsS()(54)

def ModeCommon_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsS(reset, service) or service

ModeStartSr_eKsL = ModeCommon_eKs()(47)

def DockerCommon_eKsL():
    return ModeSRL(reset=None)

def ModeSRL(reset=None, l=None):
    return DockerCommon_eKs()(reset, l)

def DockerCommon_eKs():
    return ModeEndSrL_eKs()

def ModeEndSrL_eKs():
    return DockerCommonSRL()

def DockerStartSrL_eKsS():
    return ModeCommon_eKsS('r')

def ModeCommon_eKsS(reset=None):
    return ModeEndSr(reset)

def DockerStartSrS_eKs():
    return ModeCommon_eKs()(49)

def DockerStartSrS_eKsL(reset=56, service=None):
    return ModeCommon_eKs()(reset, service)

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS_eKsL()

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS_eKs()

setup_docker2 = lambda: DockerSrL2StartSr()

ModeEndSrL = lambda reset=None, l=None: DockerCommon()(reset, l)

def DockerCommon_eKsS():
    return 51

DockerStartSrS = ModeCommon_eKsS()

def DockerStartSrS_eKs(reset=55):
    return ModeCommon_eKs()(reset)