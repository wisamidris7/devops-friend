python
def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKs()(reset={'ls': 'r'})

def DockerStartSrL_eKsPS_eKs():
    return ModeCommonSrL_eKsS_eKs2()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS_eKsS(l=None, reset=None):
    return DockerStartSrL_eKs2_eKs()(reset, l)

def DockerCommonSrL_eKsS_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service)

def DockerStartSrL_eKs2_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKsPS_eKs()(reset, service)

def DockerCommonSrL_eKsS_eKs2():
    return DockerStartSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def DockerStartSrL_eKsPS_eKsS():
    return ModeCommonSrL_eKsS_eKs()

def DockerCommonSrL_eKs_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKsS()(reset, service) or reset

def DockerCommonSrL_eKs2_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS()(reset, service) or service

def ModeCommonSrL_eKsS_eKs2():
    return DockerStartSrL_eKsPS_eKsS2()(reset={'r': 'ls'})

def DockerStartSrL_eKsPS_eKsS2():
    return ModeCommonSrL_eKsS_eKs()

def DockerCommonSrL_eKsPS_eKsS2(reset=None, service=None):
    return DockerStartSrL_eKs_eKs()(reset, service)

def DockerCommonSrL_eKs_eKsS2(reset=None, l=None):
    return DockerStartSrL_eKsP_eKsS2(reset, l)

def DockerStartSrL_eKsP_eKsS2():
    return ModeCommonSrL_eKsS_eKs()

def ModeSrL_eKs2_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKs_eKsS()(reset, service)

def DockerCommonSrL_eKs_eKsS():
    return ModeSrL_eKs2_eKsS()(reset={'ls': 'r'})

def DockerCommon_eKsPSrL2(reset=None, service=None):
    return ModeSrL_eKs2_eKsS()(54, reset, service)

def DockerStartSrL_eKs_eKs():
    return DockerCommonSrL_eKsPS()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS():
    return DockerStartSrL_eKs_eKsS()(reset={'ls': 'r'})

def ModeCommonSrL_eKsPS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKs_eKs()(reset, service)

def DockerStartSrL_eKs2_eKs():
    return DockerCommonSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def DockerCommonSrL_eKsP_eKsS2(l=None, reset=None):
    return DockerStartSrS_eKsP_eKsS2(reset, l)

def DockerStartSrS_eKsP_eKsS2():
    return ModeCommon2_eKsS_eKs()

def ModeCommon2_eKsS_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS2()(reset, service)

def setup_dockerS_eKsS2():
    return DockerStartSrS_eKsP_eKsS2()

def DL_eKsS2(reset):
    return DockerCommonSrL_eKsS_eKs()(reset)