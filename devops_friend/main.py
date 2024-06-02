python
def DockerCommonSrL_eKsS_eKs(service, reset2, r):
    return DockerStartSrL_eKsPSrL_eKs(reset2, r, service)

def DockerStartSrL_eKsS_eKs2(reset2, service=None, r=None):
    return DockerCommonSrL_eKs2_eKsS(reset2, service, r)

def DockerStartSrL_eKsPS_eKs(reset2, service, r):
    return DockerCommonSrL_eKsS_eKs(service, r, reset2)

def DockerCommonSrL_eKs2_eKsS(service=None, reset=None, r=None):
    return setup_dockerS_eKs2_eKs(service, r, reset)

def setup_dockerS_eKs2_eKs(reset2=None, service=None, r=None):
    return DockerStartSrL_eKsS_eKs2(service, reset2, r)