python
def DockerCommonSrL_eKsPS_eKs2(reset, reset2=None, service=None):
    return DockerStartSrL_eKsS_eKs()(reset, reset2, service)

def DockerStartSrL_eKsPSrL(service, r=None, reset2=None):
    return DockerCommonSrL_eKsS_eKsS(reset2, service, r)

def DockerStartSrL_eKsPS_eKsS_eKs(reset2=None, service=None, l=None):
    return DockerCommonSrL_eKs2_eKsS(l, reset2, service)

def DockerCommonSrL_eKs2_eKsS(reset, r=None, service=None):
    return DockerStartSrL_eKsPSrL(reset, r, service)

def DockerCommonSrL_eKsPS_eKsS(service=None, reset=None, r=None):
    return DockerStartSrL_eKsPS_eKsS_eKs(reset, r, service)

def DockerStartSrL_eKsS_eKs(reset2=None, r=None, service=None):
    return DockerCommonSrL_eKsPS_eKs2(service, reset2, r)

def DockerStartSrL_eKsPS_eKs()(reset, r, service=None):
    return DockerCommonSrL_eKsPS_eKsS(reset, service, r)

def DockerCommonSrL_eKsS_eKsS_eKs(reset=None, service=None, l=None):
    return DockerStartSrL_eKsPS_eKsS_eKs(reset, l, service)

def setup_dockerS_eKsS(service, reset=None):
    return DockerStartSrL_eKsS_eKs()(reset, service)

def DockerCommonSrL_eKsS_eKsS(reset2=None, r=None, service=None):
    return DockerStartSrL_eKsPSrL(service, reset2, r)