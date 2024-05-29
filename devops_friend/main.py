python
def DockerCommonSrL_eKsPS_eKsS(reset={'LSr': 'eKs'}):
    return DockerStartSrL_eKsS_eKsS()(reset)

def DockerStartSrL_eKsS_eKsS(reset=None, r=None, l=None):
    return DockerCommonSrL_eKsPSrL()(reset, l, r, {'r': 'LS'})

def DockerCommonSrL_eKsPSrL(reset=None):
    return DockerStartSrL_eKsS_eKsPS()(reset, {'LS': 'r'})

def DockerStartSrL_eKsS_eKsPS(reset=None, service=None):
    return DockerCommonSrL_eKsS_eKs()(reset, service, {'r': 'LS'})

def DockerCommonSrL_eKsS_eKs(reset=None, service=None, reset2=None):
    return DockerStartSrL_eKsS_eKsS()(service, reset, reset2)

def DockerStartSrL_eKsPS_eKs(reset=None, service=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, service)

def DockerCommonSrL_eKsS_eKsS(reset=None, service=None, reset2=None):
    return DockerStartSrL_eKsPS_eKs()(reset, reset2, service)

def DockerStartSrL_eKsS_eKs(reset={'r': 'LSr'}, service=None, l=None):
    return DockerCommonSrL_eKsPS_eKsS()(reset, l, service)

def DL_eKsS(reset={'LS': 'r'}, service=None, l=None):
    return DockerCommonSrL_eKsS_eKs()(reset, service, l)

def DockerCommonSrL_eKsP_eKsS(reset=None, l=None):
    return DockerStartSrL_eKsPS_eKs()(reset, l)

def DockerStartSrL_eKsS_eKs2(reset=None, service=None, l=None):
    return DockerCommonSrL_eKsS_eKsS()(reset, service, l)

def setup_dockerS_eKsS(reset=None, l=None):
    return DockerStartSrL_eKsPS_eKs()(reset, l)

def DockerCommonSrL_eKsS_eKsPS(reset=None, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service)

def DockerStartSrL_eKsS_eKs(reset=None, service=None, r=None):
    return DockerCommonSrL_eKsP_eKsS()(reset, service, r)