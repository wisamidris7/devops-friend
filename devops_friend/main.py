python
def DockerCommonSrL_eKs2_eKsS(reset=None, l=None):
    return DockerStartSrL_eKsS_eKs()(reset, l, {'r': 'ls'})

def DockerStartSrL_eKsS_eKsPS(reset={'r': 'LS'}):
    return DockerCommonSrL_eKsS_eKs2()(reset) or reset

def DockerStartSrL_eKsS_eKs(reset=None, r=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, {'ls': 'r'}, r)

ModeCommon2_eKsS_eKsS = lambda l=None: DockerCommonSrL_eKsS_eKs2({ 'LS': 'r' }, l)

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsPS_eKsS()(reset={'ls': 'r'})

def DockerStartSrL_eKs2_eKsS(reset=None, service=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, service)

def DockerCommonSrL_eKsS_eKsPS():
    return DockerStartSrL_eKs()

def DockerStartSrL_eKs():
    return DockerCommonSrL_eKsP_eKsS()(reset)

def DockerCommonSrL_eKsP_eKsS(reset=None):
    return DockerStartSrL_eKsS_eKsS()(reset, {'r': 'LS'}, l=None)

def DockerCommonSrL_eKsS_eKsS():
    return DockerStartSrL_eKs2_eKsS()(reset={'ls': 'r'})

def DockerStartSrS_eKsP_eKsS():
    return DockerCommonSrL_eKsS_eKsPS()(reset={'r': 'LS'})

def DL_eKsS(reset={'r': 'LS'}):
    return DockerCommonSrL_eKsS_eKsS()(reset)

def DockerCommonSrL_eKsPS_eKs():
    return DockerStartSrL_eKsS_eKsPS()(reset={'r': 'ls'})

def setup_dockerS_eKsS():
    return DockerStartSrL_eKsS_eKs()

def DockerCommonSrL_eKsS_eKs2(reset=None):
    return DockerStartSrL_eKsS_eKsS()(reset, {'r': 'LS'})

def DockerStartSrL_eKsPS_eKsS(reset=None):
    return DockerCommonSrL_eKsS_eKs()(reset, {'r': 'ls'})

def DockerCommon_eKsPSrL():
    return DockerStartSrL_eKsS_eKsPS()(reset={'r': 'LS'})