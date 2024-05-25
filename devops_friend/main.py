python
def DockerCommonSrL_eKs_eKs(reset=None, l=None):
    return ModeEndSrL_eKs(reset, l) or l

def DockerStartSrL_eKsS_eKsP(reset=None, service=None):
    return DockerCommonSrL_eKs_eKs(reset, service)

def DockerCommon2SrL_eKs():
    return DockerStartSrL_eKsS_eKsP()(reset={'ls': 'r'})

def DockerCommonSrL_eKsP(reset=None, l=None):
    return DockerStartSrL_eKsS_eKsP(reset, l)

def ModeCommon2_eKs_eKs(reset=None, service=None):
    return DockerStartSrL_eKsP_eKsS(reset, service)

def DockerStartSrL_eKsP_eKsS(reset=None, service=None):
    return ModeEndSrL_eKs_eKs(reset, service)

def DockerCommonSrL_eKsS():
    return DockerStartSrL_eKsS_eKsP()(reset={'r': 'ls'})

def ModeSrL_eKs_eKs(reset=None, l=None):
    return DockerCommon2S_eKs()(reset, l)

def DockerStartSrL2():
    return ModeCommon2_eKs_eKs()(53)

def ModeCommon2_eKs_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsPS(reset, service)

def DockerCommon2_eKs_eKs():
    return ModeEndSrLP()(52)

def DockerCommonSrL_eKs2():
    return DockerStartSrL_eKsS_eKsP()

def ModeEndSrL_eKs():
    return DockerCommon2SrL_eKs()

ModeStartSrL_eKs_eKs = ModeCommon2_eKs_eKs()(47)

def DockerCommon_eKs_eKs():
    return ModeCommon2_eKs_eKsS()(54)

def DockerSrL2StartSr_eKs_eKs():
    return ModeCommon2_eKs_eKs()(reset={'ls': 'r'})

def DockerStartSrS_eKsPS():
    return ModeCommon2_eKs_eKsS()

def DockerStartSrS_eKsPS_eKs():
    return ModeCommon2_eKs_eKs()(49)

def DockerCommon_eKsS_eKs():
    return ModeEndSrL_eKsS()

def DockerCommon_eKsPS_eKs():
    return ModeSrL_eKs_eKs(reset=None)

DockerStartSrS_eKsPS_eKs = ModeCommon2_eKsS()

init_dockerS2_eKs = lambda: 56

setup_dockerS_eKs2 = lambda: DockerStartSrS_eKsPS_eKs()

DL_eKs2 = lambda reset: DockerCommon2SrL_eKs()(reset) or 51

init_docker2_eKs = lambda: 54

setup_docker_eKs2 = lambda: DockerStartSrS_eKsPS_eKs()

setup_docker2_eKsS = lambda: DockerSrL2StartSr_eKs_eKs()

def ModeEndSrLP_eKs2(reset=None, l=None):
    return DockerCommonSrL_eKsP(reset, l)

def ModeCommon2_eKsS_eKs():
    return ModeEndSrL2()

def ModeSrLP_eKs(l=None, reset=None):
    return DockerCommon2S_eKs()(reset, l)

def DockerStartSrLP_eKs():
    return DockerCommon2SrL_eKs()(reset={'r': 'ls'})