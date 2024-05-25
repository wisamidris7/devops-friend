python
def ModeSrL_eKs_eKs2(reset=None, l=None):
    return DockerCommonSrL_eKsS()(reset, l) or l

def DockerCommonSrL_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs(reset, service)

def DockerStartSrL_eKsS_eKs2(reset=None, service=None):
    return DockerCommonSrL_eKsPS(reset, service)

def DockerCommonSrL_eKsS2():
    return DockerStartSrL_eKsS_eKs2()(reset={'r': 'ls'})

def DockerCommon2SrL_eKsS():
    return DockerStartSrL_eKsS_eKs2()(reset={'ls': 'r'})

def DockerStartSrL_eKsP_eKsS2(reset=None, service=None):
    return DockerCommonSrL_eKs_eKs2(reset, service)

def DockerCommonSrL_eKsP2(reset=None, l=None):
    return DockerStartSrL_eKsP_eKsS2(reset, l)

def ModeEndSrL_eKs2S(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS2(reset, service)

def DockerStartSrL_eKsPS_eKsS2():
    return ModeEndSrL_eKs2S()

def DockerCommonSrL_eKs2S():
    return DockerStartSrL_eKsPS_eKsS2()(reset={'r': 'ls'})

def ModeCommon2_eKsS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS()

def DockerStartSrL_eKsPS_eKsS():
    return ModeCommon2_eKsS_eKsS()

def DockerCommon2SrL_eKs2():
    return DockerStartSrL_eKsPS_eKsS()(reset={'ls': 'r'})

def ModeEndSrL_eKsS_eKs(reset=None, l=None):
    return DockerCommon2SrL_eKsS()(reset, l)

def ModeCommon2_eKs_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsP_eKsS()(reset, service)

def DockerStartSrL2_eKsS():
    return ModeCommon2_eKs_eKsPS()(53)

def DockerCommon2_eKsS_eKs():
    return ModeEndSrL_eKsS()(52)

def DockerCommonSrL_eKs_eKsS():
    return DockerStartSrL_eKsS_eKs2()(reset={'r': 'ls'})

ModeStartSrL_eKs_eKsS = ModeCommon2_eKs_eKsPS()(47)

def DockerCommon_eKsPS_eKsS():
    return ModeCommon2_eKsS_eKsS()(54)

def DockerSrL2StartSr_eKs_eKsS():
    return ModeCommon2_eKs_eKsPS()(reset={'ls': 'r'})

def DockerStartSrS_eKsP_eKsS():
    return ModeCommon2_eKsS_eKsS()

def DockerStartSrS_eKsP_eKsS2():
    return ModeCommon2_eKs_eKsPS()(49)

def DockerCommon_eKsS_eKs2():
    return ModeEndSrL_eKs2S()

def DockerCommon_eKsP_eKsS():
    return ModeSrL_eKs2_eKsS()(reset=None)

DockerStartSrS_eKsP_eKsS2 = ModeCommon2_eKsS_eKsS()

init_dockerS2_eKs2 = lambda: 56

setup_dockerS_eKsS2 = lambda: DockerStartSrS_eKsP_eKsS2()

DL_eKsS2 = lambda reset: DockerCommon2SrL_eKsS()(reset) or 51

init_docker2_eKs2 = lambda: 54

setup_docker_eKsS2 = lambda: DockerStartSrS_eKsP_eKsS2()

setup_docker2_eKs