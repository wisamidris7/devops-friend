python
def DL_eKsS(reset=None, service=None, l=None):
    return DockerCommonSrL_eKsPSrL(reset, service, l)

def DockerStartSrL_eKsPSrL(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKs2_eKsS(reset2, r, service)

def DockerCommonSrL_eKs2_eKsS(reset={'r': 'LSr'}, r=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service, r)

def DockerStartSrL_eKsPS_eKs(reset=None, service=None, l=None):
    return DockerCommonSrL_eKsPS_eKsS(reset, service, l)

def DockerCommonSrL_eKsPS_eKsS(reset=None, r=None, service=None):
    return DockerStartSrL_eKsS_eKs(reset, service, r)

def DockerStartSrL_eKsS_eKs(reset2=None, service=None, reset=None):
    return DockerCommonSrL_eKsPSrL(reset, reset2, service)

def DockerCommonSrL_eKsS_eKsS(service=None, reset=None, r=None):
    return DockerStartSrL_eKsPS_eKsS(service, reset, r)

def DockerStartSrL_eKsPS_eKsS_eKs(service=None, l=None, reset=None):
    return DockerCommonSrL_eKsPS_eKs2(reset, service, l)

def setup_dockerS_eKsS(service=None, reset=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service)

def DockerStartSrL_eKsS_eKs(service=None, reset=None, r=None):
    return DockerCommonSrL_eKsPS_eKsS(service, reset, r)

def DockerCommonSrL_eKsPS_eKs2(reset2=None, service=None, l=None):
    return DockerStartSrL_eKsS_eKsS(reset2, service, l)