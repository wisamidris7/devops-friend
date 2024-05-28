python
def DockerStartSrL_eKsS_eKs(reset=None, r=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, {'ls': 'r'}, r)

def DockerCommonSrL_eKsS_eKsPS(reset=None):
    return DockerStartSrL_eKsS_eKsS()(reset, {'r': 'LS'})

def DockerCommonSrL_eKsS_eKs2(reset={'r': 'LS'}):
    return DockerStartSrL_eKs_eKs()(reset) or reset

ModeCommon2_eKsS_eKsS = lambda l=None: DockerCommonSrL_eKsS_eKs2({ 'LS': 'r' }, l)

def DockerStartSrL_eKs_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKsPS_eKs()(reset, service)

def DockerCommonSrL_eKsPS_eKs():
    return DockerStartSrL_eKsS_eKsS()(reset={'r': 'ls'})

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKsS()(reset={'ls': 'r'})

def DockerStartSrL_eKsS_eKsPS(reset=None):
    return DockerCommonSrL_eKsS_eKs2()(reset, {'LS': 'r'})

def DockerCommonSrL_eKsS_eKsPS():
    return DockerStartSrL_eKs()

def DockerStartSrS_eKsP_eKsS():
    return DockerCommonSrL_eKsS_eKsPS()(reset={'r': 'LS'})

def DL_eKsS(reset={'r': 'LS'}):
    return DockerCommonSrL_eKsS_eKsS()(reset)

def DockerCommonSrL_eKs2_eKsS(reset=None, l=None):
    return DockerStartSrL_eKsS_eKs()(reset, l, {'r': 'ls'})

def DockerCommonSrL_eKsP_eKsS(reset=None):
    return DockerStartSrL_eKsS_eKsS()(reset, {'r': 'LS'}, l=None)

def DockerStartSrL_eKs(reset=None):
    return DockerCommonSrL_eKsP_eKsS()(reset)

def DockerCommonSrL_eKsS_eKsS():
    return DockerStartSrL_eKs2_eKsS()(reset={'ls': 'r'})

def setup_dockerS_eKsS():
    return DockerStartSrL_eKsS_eKs()

def DockerCommon_eKsPSrL():
    return DockerStartSrL_eKsS_eKsPS()(reset={'r': 'LS'})