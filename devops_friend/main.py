python
def DockerCommonSrL_eKsPS_eKs(reset={'LS': 'r'}):
    return DockerStartSrL_eKsS_eKs2()(reset)

def DockerStartSrL_eKsS_eKsS(reset=None, r=None, service=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, service, {'r': 'ls'})

def DockerStartSrL_eKsPS_eKsS(reset=None, l=None, service=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, l, service, {'ls': 'r'})

def DockerCommonSrL_eKsS_eKs2(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service)

def DockerStartSrL_eKsS_eKs(reset=None, l=None):
    return DockerCommonSrL_eKsPS_eKs()(reset, l, {'r': 'LS'})

def DockerCommonSrL_eKsP_eKsS(reset={'r': 'LS'}, service=None):
    return DockerStartSrL_eKsS_eKsS()(reset, service)

def DockerCommonSrL_eKsS_eKsPS():
    return DockerStartSrL_eKsPS_eKsS()(reset={'r': 'ls'}, {'LS': 'r'})

def DockerStartSrL_eKs2_eKsS(reset=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, {'r': 'ls'})

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsS_eKsPS()(reset={'LS': 'r'}, {'ls': 'r'})

def DockerStartSrL_eKs(reset=None):
    return DockerCommonSrL_eKsP_eKsS()(reset)

def DockerCommonSrL_eKsS_eKsS(reset=None, l=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, l, service)

def DL_eKsS(reset=None):
    return DockerCommonSrL_eKsS_eKs()(reset, {'r': 'LS'})

def DockerStartSrS_eKsP_eKsS(reset={'ls': 'r'}):
    return DockerCommonSrL_eKsS_eKsS()(reset)

def setup_dockerS_eKsS():
    return DockerStartSrL_eKsS_eKsPS()(reset={'LS': 'r'})

def DockerCommonSrL_eKsS_eKsPS(l=None):
    return DockerStartSrL_eKsS_eKs2()(reset={'ls': 'r'}, l)

def DockerCommon_eKsPSrL():
    return DockerStartSrL_eKsS_eKsPS()(reset={'LS': 'r'})

def DockerCommonSrL_eKsS_eKs():
    return DockerStartSrL_eKsS_eKsPS()(reset, {'r': 'LS'})