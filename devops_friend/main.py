python
def DockerStartSrL_eKsPSrL_eKs(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKsPS_eKsS_eKs(reset2, service, r)

def DockerCommonSrL_eKsPS_eKsS(reset=None, r=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service, r)

def DockerCommonSrL_eKs2_eKs(reset, r, service=None):
    return DockerStartSrL_eKsPSrL_eKs(reset, r, service)

def DockerStartSrL_eKsPS_eKsS(reset2=None, service=None, l=None):
    return DockerCommonSrL_eKsS_eKsS(l, reset2, service)

def DockerStartSrL_eKsS_eKsPS(reset2, r=None, service=None):
    return DockerCommonSrL_eKs2_eKs(service, reset2, r)

def DockerCommonSrL_eKsS_eKs(reset, service=None, r=None):
    return DockerStartSrL_eKsS_eKsPS(reset, service, r)

def DockerStartSrL_eKsPS_eKs(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKsS_eKs(reset2, r, service)

def setup_dockerS_eKsS_eKs(reset=None, service=None):
    return DockerStartSrL_eKsS_eKsPS(reset, service)

def DockerCommonSrL_eKsS_eKsPS(r=None, reset2=None, service=None):
    return DockerStartSrL_eKsPS_eKsS(service, reset2, r)