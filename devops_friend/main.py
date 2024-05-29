python
def DockerCommonSrL_eKsPSrL(reset=None, r=None):
    return DockerStartSrL_eKsS_eKsPS(reset, r)

def DockerStartSrL_eKsPS_eKs(reset=None, service=None, l=None):
    return DockerCommonSrL_eKsP_eKsS(reset, service, l)

def DockerCommonSrL_eKsP_eKsS(reset=None, service=None, r=None):
    return DockerStartSrL_eKsS_eKs2(reset, r, service)

def DockerStartSrL_eKsS_eKs2(reset=None, service=None, reset2=None):
    return DockerCommonSrL_eKsS_eKsPS()(reset, reset2, service)

def DockerCommonSrL_eKsS_eKsPS(reset=None, service=None, l=None):
    return DockerStartSrL_eKsS_eKsS(reset, service, l)

def DockerStartSrL_eKsS_eKsS(reset={'r': 'LSr'}, service=None, l=None):
    return DockerCommonSrL_eKsPS_eKs(reset, l, service)

def DockerCommonSrL_eKsPS_eKs(reset=None, service=None, l=None):
    return DockerStartSrL_eKsS_eKs()(reset, service, l)

def DockerStartSrL_eKsS_eKs(reset=None, r=None, service=None):
    return DockerCommonSrL_eKsS_eKsS(reset, r, service)

def DL_eKsS(reset=None, l=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, l, service)

def DockerStartSrL_eKsPS_eKsS(reset=None, r=None, l=None):
    return DockerCommonSrL_eKsS_eKsS(reset, l, r)

def setup_dockerS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service)

def DockerCommonSrL_eKsS_eKsS(reset=None, r=None, service=None):
    return DockerStartSrL_eKsPS_eKs2(reset, service, r)

def DockerStartSrL_eKsPS_eKs2(reset=None, l=None, service=None):
    return DockerCommonSrL_eKsS_eKsS(reset, service, l)