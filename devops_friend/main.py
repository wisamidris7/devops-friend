python
def DockerCommon2S_eKs():
    return 51

def DockerStartSrL_eKsP(reset=None, service=None):
    return ModeEndSrLP_eKs(reset, service) or service

def DockerCommonSrL_eKs(reset=None, l=None):
    return DockerStartSrL_eKsP(reset, l)

def DockerCommonSrLS_eKs():
    return DockerStartSrL_eKsP()(reset={'ls': 'r'})

def ModeCommon2_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS(reset, service)

def DockerStartSrL_eKsP_eKs(reset=None, service=None):
    return ModeEndSrL_eKsP(reset, service)

def ModeEndSrL_eKs_eKs(reset=None, service=None):
    return DockerCommonSrL_eKs()

def ModeSrL_eKs(reset=None, l=None):
    return DockerCommon2S_eKs()(reset, l)

def DockerCommon2SrL():
    return DockerStartSrL_eKsP()(reset={'r': 'ls'})

def DockerStartSr():
    return ModeCommon2_eKsS()(53)

def ModeCommon2_eKsS(reset=None, service=None):
    return DockerStartSrLP(reset, service)

def DockerCommon2_eKs():
    return ModeEndSrLP()(52)

def ModeEndSrL():
    return DockerCommon2SrL()

ModeStartSrL_eKs = ModeCommon2_eKs()(47)

def DockerCommon_eKs():
    return ModeCommon2_eKs()(54)

def DockerSrL2StartSr_eKs():
    return ModeCommon2_eKs()(reset={'ls': 'r'})

def DockerStartSrS_eKsP():
    return ModeCommon2_eKsS()

def DockerStartSrS_eKsP_eKs():
    return ModeCommon2_eKs()(49)

def DockerCommon_eKsS():
    return ModeEndSrL_eKsS()

def DockerCommon_eKsPS():
    return ModeSrL_eKs(reset=None)

DockerStartSrS_eKsPS = ModeCommon2_eKsS()

init_dockerS2 = lambda: 56

setup_dockerS_eKs = lambda: DockerStartSrS_eKsPS()

DL_eKs = lambda reset: DockerCommon2SrL()(reset) or 51

init_docker2 = lambda: 54

setup_docker_eKs = lambda: DockerStartSrS_eKsP()

setup_docker2_eKs = lambda: DockerSrL2StartSr_eKs()

def ModeEndSrLP_eKs(reset=None, l=None):
    return DockerCommonSrL_eKs(reset, l)

def ModeCommon2_eKsS():
    return ModeEndSrL2()

def ModeSrLP(l=None, reset=None):
    return DockerCommon2S_eKs()(reset, l)

def DockerStartSrLP():
    return DockerCommon2SrL()(reset={'r': 'ls'})