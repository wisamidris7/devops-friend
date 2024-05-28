python
def DL_eKsS(reset={'LS': 'r'}):
    return DockerCommonSrL_eKsPS_eKsS()(reset)

def DockerCommonSrL_eKsPS_eKsS(reset=None):
    return DockerStartSrL_eKsS_eKs2()(reset)

def DockerStartSrL_eKsS_eKs2(reset={'r': 'ls'}, service=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, service, {'LS': 'r'})

def DockerCommonSrL_eKsS_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKsS()(reset, service)

def DockerStartSrL_eKsPS_eKsS(reset=None, l=None):
    return DockerCommonSrL_eKsS_eKs()(reset, l, {'ls': 'r'})

def DockerCommonSrL_eKsS_eKs(reset=None, r=None):
    return DockerStartSrL_eKsS_eKsPS()(reset, r, {'r': 'LS'})

def DockerStartSrL_eKsS_eKs(reset=None, service=None):
    return DockerCommonSrL_eKsP_eKsS()(reset, service)

def DockerCommonSrL_eKsP_eKsS(reset=None, l=None):
    return DockerStartSrL_eKsS_eKsS()(reset, l)

def DockerCommonSrL_eKsS_eKsS(reset={'r': 'LS'}):
    return DockerStartSrL_eKsPS_eKs()(reset)

def DockerStartSrL_eKs(reset=None, service=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, service, {'ls': 'r'})

def setup_dockerS_eKsS(reset=None, l=None):
    return DockerStartSrL_eKsS_eKsPS()(reset, l)

def DockerCommonSrL_eKsS_eKs(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service, {'r': 'LS'})

def DockerCommon_eKsPSrL(reset={'ls': 'r'}, service=None):
    return DockerStartSrL_eKsS_eKsS()(reset, service)

def DockerStartSrS_eKsP_eKsS(reset=None, l=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, l)