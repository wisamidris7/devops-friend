python
def DockerCommon_eKsP_eKsS():
    return ModeSrL2_eKsS_eKs()(54)

def DockerSrL2StartSr_eKs_eKsS():
    return ModeCommon2_eKs_eKsPS()(reset={'ls': 'r'})

def DockerCommonSrL_eKs2_eKs():
    return DockerStartSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def DockerStartSrL2_eKsS():
    return ModeCommon_eKsPS_eKsS()(53)

def DockerCommonSrL_eKsP2(l=None, reset=None):
    return DockerStartSrL_eKsP_eKsS2(l, reset)

def DockerStartSrL_eKsPS_eKs():
    return DockerCommonSrL_eKsS_eKs2()(reset=None)

def DockerCommonSrL_eKsS_eKs2(service=None, reset=None):
    return DockerStartSrL_eKsPS(service, reset)

def ModeSrL_eKs2_eKsS(reset=None, l=None):
    return DockerCommonSrL_eKs_eKs()(reset, l) or l

def DockerStartSrL_eKsP_eKsS2():
    return ModeCommon2_eKsS_eKs()

def DockerCommonSrL_eKs_eKs2(l=None, reset=None):
    return ModeSrL_eKs2_eKsS(l, reset) or reset

def DockerCommon2_eKsS_eKs():
    return ModeEndSrL_eKsS()(52)

def DockerStartSrL_eKsPS_eKsS():
    return ModeCommon2_eKsS_eKs()

def ModeCommon2_eKs_eKsPS(service=None, reset=None):
    return DockerStartSrL_eKs_eKs()(service, reset)

def DockerCommonSrL_eKsS():
    return DockerStartSrL_eKsPS_eKsS2()(reset={'ls': 'r'})

def ModeCommon_eKsPS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKs_eKs()(reset, service)

def DockerStartSrL_eKs_eKs(service=None, reset=None):
    return DockerCommonSrL_eKsPS(service, reset)

def DockerCommonSrL_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs2(reset, service)

def ModeEndSrL_eKs2S(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service)

def DockerStartSrL_eKsPS_eKs():
    return ModeCommon2_eKsS_eKs()

def DockerCommon2SrL_eKsS():
    return DockerStartSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def DockerStartSrS_eKsP_eKsS2():
    return ModeCommon2_eKsS_eKs()

def ModeCommon2_eKsS_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS2()(reset, service)

def setup_docker_eKsS2():
    return DockerStartSrS_eKsP_eKsS2()

def init_dockerS2_eKs2():
    return 56

def setup_docker2_eKs():
    pass

def DL_eKsS2(reset):
    return DockerCommon2SrL_eKsS()(reset) or 51

def init_docker2_eKs2():
    return 54

def setup_dockerS_eKsS2():
    return DockerStartSrS_eKsP_eKsS2()

ModeStartSrL_eKs_eKsS = ModeCommon2_eKs_eKsPS()(47)