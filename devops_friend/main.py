python
def DockerStartSrL_eKsS_eKs2(reset={'r': 'LS'}, service=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, service)

def DockerCommonSrL_eKsS_eKsPS(l=None):
    return DockerStartSrL_eKsS_eKs2()(reset={'r': 'ls'}, l)

def DockerCommonSrL_eKsS_eKs(reset=None):
    return DockerStartSrL_eKsS_eKsPS()(reset, {'LS': 'r'}) or reset

def DockerStartSrL_eKsS_eKs(reset=None, r=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, r, {'ls': 'r'})

def DockerCommonSrL_eKsS_eKsS(reset=None, l=None):
    return DockerStartSrL_eKsPS_eKsS()(reset, l, {'r': 'LS'})

def DockerStartSrL_eKs2_eKsS():
    return DockerCommonSrL_eKsS_eKsS()(reset={'r': 'ls'})

def DockerCommonSrL_eKsPS_eKs(reset={'r': 'LS'}):
    return DockerStartSrL_eKsS_eKs()(reset)

def DockerStartSrL_eKs():
    return DockerCommonSrL_eKsP_eKsS()(reset={'r': 'LS'})

def DockerCommonSrL_eKsP_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKsS()(reset, {'r': 'LS'}, service)

def DockerCommonSrL_eKsS_eKsS(reset=None):
    return DockerStartSrL_eKs2_eKsS()(reset, {'ls': 'r'})

def DL_eKsS():
    return DockerCommonSrL_eKsS_eKsS()(reset={'LS': 'r'})

def DockerStartSrS_eKsP_eKsS(reset=None):
    return DockerCommonSrL_eKsS_eKs()(reset, {'ls': 'r'})

def setup_dockerS_eKsS(reset=None):
    return DockerStartSrL_eKsS_eKs()(reset, {'LS': 'r'})

def DockerCommonSrL_eKsS_eKs2():
    return DockerStartSrL_eKsS_eKsPS()(reset)

def DockerStartSrL_eKsS_eKsPS():
    return DockerCommonSrL_eKsS_eKsS()(reset={'r': 'ls'}, {'LS': 'r'})

def DockerCommon_eKsPSrL(reset=None):
    return DockerStartSrL_eKsS_eKsPS()(reset)