python
def DockerStartSrL_eKsPSrL(reset2, r, service):
    return DockerCommonSrL_eKsS_eKsS(reset2, service, r)

def DockerCommonSrL_eKsS_eKsS(reset, reset2=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, reset2, service)

def DockerCommonSrL_eKs2_eKsS(reset, service, r):
    return DockerStartSrL_eKsPSrL(reset, service, r)

def DockerStartSrL_eKsPS_eKsS_eKs(reset=None, l=None, service=None):
    return DockerCommonSrL_eKsS_eKsS(l, reset, service)

def DockerCommonSrL_eKsPS_eKs2(service, reset=None, l=None):
    return DockerStartSrL_eKsPS_eKsS_eKs(reset, l, service)

def DockerStartSrL_eKsPS_eKs()(reset, service, r):
    return DockerCommonSrL_eKsPS_eKsS(reset, r, service)

def DockerCommonSrL_eKsPS_eKsS(reset=None, r=None, service=None):
    return DockerStartSrL_eKsPSrL(reset, r, service)

def setup_dockerS_eKsS(reset, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service)

def DockerStartSrL_eKsS_eKs(service=None, r=None, reset2=None):
    return DockerCommonSrL_eKsPS_eKs2(reset2, service, r)

def DockerCommonSrL_eKsS_eKsS(service, r=None, reset=None):
    return DockerStartSrL_eKsPSrL(service, reset, r)

def DockerStartSrL_eKsPS_eKsS_eKs(reset=None, r=None, service=None):
    return DockerCommonSrL_eKsS_eKsS(service, reset, r)