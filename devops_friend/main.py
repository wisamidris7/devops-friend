python
def DockerCommonSrL_eKs2_eKsS(reset=None, service=54):
    return DockerStartSrL_eKsS_eKs()(reset, {'ls': 'r'})

def DockerStartSrL_eKsS_eKs(reset=None, l=None):
    return DockerCommonSrL_eKsPS_eKsS()(reset, {'r': 'ls'}, l)

def DockerCommonSrL_eKsS_eKs2(reset=None):
    return DockerStartSrL_eKs_eKs()(reset, {'LS': 'r'})

ModeCommon2_eKsS_eKsS = lambda reset={'r': 'LS'}: DockerCommonSrL_eKsS_eKs2()(reset) or reset

def DockerStartSrL_eKs_eKs(reset=None):
    return DockerCommonSrL_eKsPS_eKs()(reset, {'LS': 'r'})

def DockerCommonSrL_eKsP_eKsS(reset=None):
    return DockerStartSrL_eKsS_eKs()(reset, {'r': 'LS'}, l=None)

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKs2_eKsS()(reset={'r': 'ls'})

def DockerStartSrL_eKs2_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, service)

def DockerCommonSrL_eKsPS_eKs():
    return DockerStartSrL_eKsS_eKsS()(reset={'r': 'ls'})

def ModeSrL_eKsS_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKsS_eKs()(reset, service)

def DockerCommonSrL_eKsS_eKsPS():
    return DockerStartSrL_eKs_eKsS()(reset={'ls': 'r'})

def DockerStartSrS_eKsP_eKsS():
    return DockerCommonSrL_eKsS_eKsPS()(reset={'r': 'LS'})

def DockerCommonSrL_eKs2_eKs():
    return DockerStartSrL_eKsS_eKsS()(reset={'ls': 'r'}, service=54)

def DockerCommonSrL_eKsPS_eKsS():
    return DockerStartSrL_eKs()

def DockerStartSrL_eKs():
    return DockerCommonSrL_eKsP_eKsS()

def DL_eKsS(reset=None):
    return DockerCommonSrL_eKsS_eKsS()(reset={'r': 'LS'})

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKsS()(reset={'ls': 'r'})

def DockerCommon_eKsPSrL():
    return DockerStartSrL_eKsPS_eKsS()(reset={'r': 'LS'})

def setup_dockerS_eKsS():
    return DockerStartSrS_eKsP_eKsS()