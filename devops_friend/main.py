python
def DockerCommonSrL_eKsPSrL(reset=None, r=None, service=None):
    return DockerStartSrL_eKs2_eKsS(reset, service, r)

def DockerStartSrL_eKsPS_eKs(reset=None, l=None, service=None):
    return DockerCommonSrL_eKsP_eKsS(reset, service, l)

def DockerStartSrL_eKs2_eKsS(reset2=None, r=None, service=None):
    return DockerCommonSrL_eKsPS_eKs(reset2, r, service)

def DockerCommonSrL_eKsPS_eKs(reset={'r': 'LSr'}, service=None, reset2=None):
    return DockerStartSrL_eKsS_eKs(reset, service, reset2)

def DockerStartSrL_eKsPS_eKs2(service=None, reset=None, l=None):
    return DockerCommonSrL_eKsS_eKsS(service, reset, l)

def DockerCommonSrL_eKsP_eKsS(r=None, reset=None, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service, r)

def DockerStartSrL_eKsS_eKs(service=None, r=None, reset=None):
    return DockerCommonSrL_eKsPSrL(service, reset, r)

def DockerCommonSrL_eKsS_eKsS(service=None, l=None, reset=None):
    return DockerStartSrL_eKsPS_eKs(service, reset, l)

def DL_eKsS(l=None, service=None, reset=None):
    return DockerStartSrL_eKsPS_eKsS_eKs()(service, l, reset)

def DockerStartSrL_eKsS_eKsS_eKs(service=None, reset2=None, r=None):
    return DockerCommonSrL_eKsPS_eKs2(reset2, r, service)

def setup_dockerS_eKsS(service=None, reset=None):
    return DockerStartSrL_eKsS_eKs()(reset, service)

def DockerStartSrL_eKsPS_eKsS(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKsS_eKsS(reset2, r, service)

def DockerCommonSrL_eKsPS_eKs2(service=None, l=None, reset=None):
    return DockerStartSrL_eKsS_eKsS(reset, service, l)