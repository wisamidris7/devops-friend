python
def DockerStartSrS_eKsP_eKsS(l=None, reset=None):
    return DockerCommon_eKsPSrL()(l, reset, {'ls': 'r'})

def DockerCommonSrL_eKsP_eKsS(reset=None, service=None, r=None):
    return DockerStartSrL_eKsS_eKs()(reset, service, r, {'r': 'LS'})

def DockerStartSrL_eKsS_eKsPS(reset={'r': 'ls'}, service=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, service, {'LS': 'r'})

def DockerCommonSrL_eKsS_eKsPS(reset=None, service=None, l=None):
    return DockerStartSrL_eKsS_eKs2()(reset, service, l)

def DockerStartSrL_eKsS_eKs2(reset=None, service=None):
    return DockerCommonSrL_eKsPS_eKsS()(reset, service)

def DockerCommonSrL_eKsPS_eKsS(reset=None):
    return DockerStartSrL_eKsS_eKsPS()(reset)

def DockerCommonSrL_eKsS_eKs(reset={'r': 'LS'}, service=None):
    return DockerStartSrL_eKsS_eKsS()(reset, service)

def DockerStartSrL_eKsS_eKs(reset=None, r=None, service=None):
    return DockerCommonSrL_eKsP_eKsS()(reset, service, r)

def DL_eKsS(reset={'LS': 'r'}, service=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, service)

def DockerCommonSrL_eKsS_eKsS(reset=None, service=None, l=None):
    return DockerStartSrL_eKsS_eKs()(reset, l, service, {'ls': 'r'})

def DockerStartSrL_eKsPS_eKs(reset=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, {'LS': 'r'})

def setup_dockerS_eKsS(reset=None):
    return DockerStartSrL_eKsS_eKsPS()(reset)

def DockerCommonSrL_eKsS_eKs(reset=None, r=None):
    return DockerStartSrL_eKsPS_eKs()(reset, r)

def DockerCommon_eKsPSrL(reset={'ls': 'r'}):
    return DockerStartSrL_eKsS_eKsS()(reset)