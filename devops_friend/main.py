python
def DockerStartSrL_eKsPS_eKs():
    return ModeCommonSrL_eKsS_eKs2()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS_eKsS(reset=None, l=None):
    return DockerStartSrL_eKs2_eKsS()(reset, l)

def DockerCommonSrL_eKsS_eKsPS():
    return DockerStartSrL_eKsPS_eKs()(reset={'ls': 'r'})

def DockerCommonSrL_eKsS_eKs2(service=None, reset=None):
    return DockerStartSrL_eKsPS(reset, service)

def DockerStartSrL_eKs2_eKsS():
    return ModeCommonSrL_eKsPS_eKsS()(53)

def DockerCommonSrL_eKs_eKsPS2(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service) or service

def DockerStartSrL_eKsS_eKs2():
    return ModeCommonSrL_eKsS_eKs()

def DockerCommonSrL_eKs2_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS()(reset, service) or reset

def ModeCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKsS2()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKs_eKsS(reset, service)

def DockerStartSrL_eKs_eKsS(reset=None, l=None):
    return DockerCommonSrL_eKsPS_eKs()(reset, l)

def ModeCommonSrL_eKsPS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKs_eKs()(reset, service)

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKsS()(reset={'ls': 'r'})

def DockerStartSrL_eKsPS_eKsS2():
    return ModeCommonSrL_eKsS_eKs()

def DockerCommonSrL_eKs_eKsS2(l=None, reset=None):
    return DockerStartSrL_eKsP_eKsS2(reset, l)

def DockerStartSrL_eKsP_eKsS2():
    return ModeCommonSrL_eKsS_eKs()

def ModeSrL_eKs2_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKs_eKsS()(reset, service) or reset

def DockerCommonSrL_eKs_eKs():
    return ModeSrL_eKs2_eKsS()(reset={'ls': 'r'})

def DockerCommon_eKsPSrL2():
    return ModeSrL_eKs2_eKsS()(54)

def DockerStartSrL_eKs_eKs(reset=None, service=None):
    return DockerCommonSrL_eKsPS(reset, service)

def DockerCommonSrL_eKsPS_eKsS2():
    return DockerStartSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def ModeEndSrL_eKs2S(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service)

def DockerCommon2SrL_eKsS():
    return DockerStartSrL_eKsPS_eKsS()(reset={'ls': 'r'})

def ModeCommon2_eKsS_eKsPS(reset=None, l=None):
    return DockerStartSrL_eKs_eKs()(reset, l)

def DockerStartSrS_eKsP_eKsS2():
    return ModeCommon2_eKsS_eKs()

def ModeCommon2_eKsS_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS2()(reset, service)

def setup_dockerS_eKsS2():
    return DockerStartSrS_eKsP_eKsS2()

def DL_eKsS2(reset):
    return Docker