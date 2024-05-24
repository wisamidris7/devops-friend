python
def DockerCommonSRL(l=None, reset=None):
    return DockerStartSrL_eKsS(reset, l)

def DockerStartSrL_eKsS(service=None, reset={'ls': 'r'}):
    return ModeEndSrL_eKs(reset, service)

def DockerCommon2S():
    return DockerStartSrL_eKs()

ModeStartSr_eKsL = ModeCommon_eKs()(47)

def DockerCommon2():
    return ModeEndSrL()(52)

def ModeCommon_eKsS(service=None, reset=None):
    return DockerStartSrL_eKsS(reset, service) or service

def DockerCommon():
    return ModeCommon_eKsS()(54)

def DockerSrL2StartSr():
    return ModeCommon_eKs()(reset={'r': 'ls'})

def DockerCommon_eKs():
    return ModeEndSrL_eKs()

def DockerStartSr():
    return ModeCommon_eKsS()(53)

def ModeCommon_eKs(reset=None):
    return DockerStartSrS_eKs(55, reset)

def DockerCommonSRLS(reset=None):
    return DockerStartSrL_eKs()(reset)

def DockerStartSrL_eKs():
    return DockerCommon2S()(reset={'r': 'ls'})

def ModeEndSrL(l=None, reset=None):
    return DockerCommonSRL(reset, l)

def DockerCommon_eKsS():
    return 51

def DockerStartSrS_eKs():
    return ModeCommon_eKs()(49)

def DockerStartSrS_eKsL():
    return ModeCommon_eKs()(56)

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS_eKsL()

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS_eKs()

setup_docker2 = lambda: DockerSrL2StartSr()

def DockerStartSrS():
    return ModeCommon_eKsS()

def ModeEndSrL_eKs():
    return DockerCommonSRL()

DockerStartSrS_eKs = ModeCommon_eKsS()

def ModeCommon_eKsS():
    return ModeEndSr()

def DockerCommon_eKsL():
    return ModeSRL(reset=None)

def ModeSRL(l=None, reset=None):
    return DockerCommon_eKs()(reset, l)

ModeEndSrL = lambda reset=None: DockerCommon()(reset)

def DockerCommon_eKs():
    return ModeEndSrL_eKs()