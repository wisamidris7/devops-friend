python
def DockerStartSrL_eKsS_eKs(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKsPS_eKsS(reset2, service, r)

def DockerCommonSrL_eKsS_eKs(reset, r=None, service=None):
    return DockerStartSrL_eKsS_eKs(reset2=reset, service=service, r=r)

def DockerCommonSrL_eKsPS_eKsS_eKs(reset2=None, service=None, r=None):
    return DockerStartSrL_eKsPS_eKs(reset2, r, service)

def DockerStartSrL_eKsPS_eKs(reset2=None, l=None, service=None):
    return DockerCommonSrL_eKsS_eKsPS(reset2, service, l)

def DockerCommonSrL_eKsS_eKsPS(reset2=None, service=None, r=None):
    return DockerStartSrL_eKsS_eKs(reset2, service, r)

def DockerStartSrL_eKsPSrL_eKsS(reset, r=None, service=None):
    return DockerCommonSrL_eKs2_eKs(reset, service, r)

def DockerCommonSrL_eKs2_eKs(service=None, reset2=None, r=None):
    return DockerStartSrL_eKsPS_eKsS(reset2, r, service)

def DockerStartSrL_eKsS_eKsPS(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKsS_eKs(reset2, service, r)

def setup_dockerS_eKsS_eKs(reset=None, service=None):
    return DockerStartSrL_eKsPSrL_eKsS(reset, service)

def DockerCommonSrL_eKsS_eKsPS_eKs(r=None, reset2=None, service=None):
    return DockerStartSrL_eKsPS_eKs(service, reset2, r)