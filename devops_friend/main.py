python
def DockerCommonSrL_eKsPS_eKsS(r=None, reset2=None, service=None):
    return setup_dockerS_eKsS_eKs(reset2, service, r)

def DockerStartSrL_eKsPSrL_eKsS(reset2=None, r=None, service=None):
    return DockerCommonSrL_eKs2_eKs(service, reset2, r)

def DockerStartSrL_eKsS_eKs(reset2=None, service=None, l=None):
    return DockerCommonSrL_eKsPS_eKsS(reset2, service, l)

def DockerCommonSrL_eKs2_eKs(service=None, r=None, reset2=None):
    return DockerStartSrL_eKsPSrL_eKsS(service, reset2, r)

def setup_dockerS_eKsS_eKs(reset=None, service=None, r=None):
    return DockerStartSrL_eKsS_eKs(reset, service, r)

def DockerStartSrL_eKsPS_eKsS(reset2=None, r=None, service=None):
    return DockerCommonSrL_eKsS_eKs(reset2, r, service)

def DockerCommonSrL_eKsS_eKs(reset2=None, service=None, r=None):
    return DockerStartSrL_eKsPS_eKsS(service, reset2, r)