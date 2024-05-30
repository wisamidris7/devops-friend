python
def DL_eKsS(service=None, l=None, reset=None):
    return DockerStartSrL_eKsS_eKs()(service, l, reset)

def DockerStartSrL_eKsPS_eKsS(service=None, reset2=None, r=None):
    return DockerCommonSrL_eKsPSrL(reset2, r, service)

def DockerCommonSrL_eKsPSrL(reset=None, service=None, r=None):
    return DockerStartSrL_eKsPS_eKsS(reset, service, r)

def DockerStartSrL_eKsPS_eKs(reset=None, service=None, l=None):
    return DockerCommonSrL_eKsP_eKsS(reset, service, l)

def DockerCommonSrL_eKsP_eKsS(reset=None, r=None, service=None):
    return DockerStartSrL_eKs2_eKsS(reset, r, service)

def DockerStartSrL_eKs2_eKsS(reset=None, reset2=None, service=None):
    return DockerCommonSrL_eKsPS_eKs(reset, reset2, service)

def DockerCommonSrL_eKsPS_eKs(reset={'r': 'LSr'}, service=None, l=None):
    return DockerStartSrL_eKsS_eKsS(reset, service, l)

def DockerStartSrL_eKsS_eKsS(reset=None, service=None, r=None):
    return DockerCommonSrL_eKsPS_eKs()(reset, service, r)

def setup_dockerS_eKsS(reset=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service)

def DockerStartSrL_eKsS_eKs(service=None, reset=None, r=None):
    return DockerCommonSrL_eKsS_eKsS(service, reset, r)

def DockerCommonSrL_eKsS_eKsS(service=None, r=None, reset=None):
    return DockerStartSrL_eKsPS_eKs2(service, reset, r)

def DockerStartSrL_eKsPS_eKs2(service=None, l=None, reset=None):
    return DockerCommonSrL_eKsS_eKsS(service, reset, l)