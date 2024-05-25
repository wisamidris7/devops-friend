python
def DockerStartSrS_eKsP_eKsS2():
    return ModeCommon2_eKsS_eKsS()

def DockerCommonSrL_eKs_eKs2(reset=None, l=None):
    return DockerCommonSrL_eKsS()(reset, l) or l

def DockerCommonSrL_eKsS():
    return DockerStartSrL_eKsS_eKs2()(reset={'ls': 'r'})

def DockerStartSrL_eKsPS_eKsS2():
    return ModeEndSrL_eKs2S()

def DockerCommonSrL_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs(reset, service)

def DockerStartSrL_eKsS_eKs(reset=None, service=None):
    return DockerCommonSrL_eKsPS(reset, service)

def ModeCommon2_eKsS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS()

def DockerStartSrL_eKsPS_eKsS():
    return ModeCommon2_eKsS_eKsS()

def DockerCommon2SrL_eKs2():
    return DockerStartSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def ModeSrL_eKs2_eKsS(reset=None, l=None):
    return DockerCommonSrL_eKs_eKs2(reset, l) or l

def DockerCommon2_eKsS_eKs():
    return ModeEndSrL_eKsS()(52)

def DockerCommonSrL_eKsP2(reset=None, l=None):
    return DockerStartSrL_eKsP_eKsS2(reset, l)

def ModeEndSrL_eKs2S(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS2(reset, service)

def DockerStartSrL2_eKsS():
    return ModeCommon2_eKs_eKsPS()(53)

def DockerCommon_eKsPS_eKsS():
    return ModeCommon2_eKsS_eKsS()(54)

def ModeCommon2_eKs_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsP_eKsS()(reset, service)

def DockerStartSrL_eKsP_eKsS():
    return ModeCommon2_eKsS_eKsS()

def DockerSrL2StartSr_eKs_eKsS():
    return ModeCommon2_eKs_eKsPS()(reset={'ls': 'r'})

def DockerCommon_eKsP_eKsS():
    return ModeSrL_eKs2_eKsS()(reset=None)

def DockerCommon_eKsS_eKs2():
    return ModeEndSrL_eKs2S()

ModeStartSrL_eKs_eKsS = ModeCommon2_eKs_eKsPS()(47)

setup_dockerS_eKsS2 = lambda: DockerStartSrS_eKsP_eKsS2()

init_dockerS2_eKs2 = lambda: 56

setup_docker2_eKs

DL_eKsS2 = lambda reset: DockerCommon2SrL_eKsS()(reset) or 51

init_docker2_eKs2 = lambda: 54

setup_docker_eKsS2 = lambda: DockerStartSrS_eKsP_eKsS2()