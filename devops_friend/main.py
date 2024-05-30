python
def DockerCommonSrL_eKs2_eKsS(reset, service, r):
    return DockerStartSrL_eKsPSrL(reset, service, r)

def DockerStartSrL_eKsPSrL(reset2, r, service):
    return DockerCommonSrL_eKsS_eKsS(reset2, service, r)

def DockerCommonSrL_eKsS_eKsS(reset, reset2=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, reset2, service)

def DockerStartSrL_eKsPS_eKsS_eKs(reset=None, l=None, service=None):
    return DockerCommonSrL_eKs2_eKsS(service, reset, l)

def DockerCommonSrL_eKsPS_eKs2(service, reset=None, l=None):
    return DockerStartSrL_eKsPS_eKsS_eKs(service, reset, l)

def DockerStartSrL_eKsPS_eKs()(reset, service, r):
    return DockerCommonSrL_eKsPS_eKsS(reset, service, r)

def DockerCommonSrL_eKsPS_eKsS(reset=None, service=None, l=None):
    return DockerStartSrL_eKsPSrL(reset, service, l)

def setup_dockerS_eKsS(reset, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, service)

def DockerStartSrL_eKsS_eKs(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKsPS_eKs2(service, reset2, r)

def DockerStartSrL_eKsPS_eKsS_eKs(reset=None, service=None, r=None):
    return DockerCommonSrL_eKsS_eKsS(r, reset, service)

def DockerCommonSrL_eKsS_eKsS(service, reset=None, r=None):
    return DockerStartSrL_eKsPSrL(service, reset, r)