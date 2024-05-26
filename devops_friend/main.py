python
def DockerStartSrS_eKsP_eKsS2():
    return ModeCommon2_eKsS_eKs()(reset={'r': 'ls'})

def DockerCommonSrL_eKs_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKs2_eKs()(reset, service) or service

def DockerCommonSrL_eKs2_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS()(reset, service)

def DockerCommonSrL_eKsS_eKsPS(l=None, reset=None):
    return DockerStartSrL_eKsS_eKs()(reset, l)

def DockerStartSrL_eKsS_eKs():
    return DockerCommonSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKs_eKsS()(reset, service)

def DockerCommonSrL_eKsS_eKs2(reset=None, service=None):
    return DockerStartSrL_eKsP_eKsS2()(reset, service)

def DockerStartSrL_eKsPS_eKs():
    return ModeCommonSrL_eKsPS_eKsS()(reset={'ls': 'r'})

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKsS2()(reset={'r': 'ls'})

def DockerCommonSrL_eKs_eKsS2(reset=None, l=None):
    return DockerStartSrL_eKsP_eKsS()(reset, l)

def DockerStartSrL_eKs2_eKsS():
    return DockerCommonSrL_eKsPS_eKsS()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS():
    return DockerStartSrL_eKs_eKs()(reset={'ls': 'r'})

def DockerStartSrL_eKs_eKsS():
    return DockerCommonSrL_eKsPS_eKs()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS_eKsS2(reset=None, service=None):
    return DockerStartSrL_eKs_eKsS()(reset, service)

def DockerCommonSrL_eKs2_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS()(reset, service) or reset

def ModeSrL_eKs2_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKsS_eKs()(54, reset, service)

def DockerStartSrL_eKsP_eKsS2():
    return ModeCommonSrL_eKsS_eKs()

def ModeCommonSrL_eKsPS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKs_eKs()(reset, service)

def DockerCommonSrL_eKsS_eKs2():
    return DockerStartSrL_eKsPS_eKs()(reset={'ls': 'r'})

def DockerStartSrL_eKs_eKs():
    return DockerCommonSrL_eKsPS()(reset={'r': 'ls'})

def DockerCommon_eKsPSrL2(reset=None, service=None):
    return ModeSrL_eKs2_eKsS()(reset, service)

def DockerCommonSrL_eKsS_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKsS()(reset, service)

def ModeCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKsS2()(reset={'r': 'ls'})

def DockerStartSrL_eKsPS_eKsS2():
    return ModeCommonSrL_eKsS_eKs()

def setup_dockerS_eKsS2():
    return DockerStartSrS_eKsP_eKsS2()

def DL_eKsS2(reset):
    return DockerCommonSrL_eKsS_eKs()(reset)