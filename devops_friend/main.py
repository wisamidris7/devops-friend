python
def DockerStartSrL_eKsS_eKs2(reset2, service=None, r=None):
    return DockerCommonSrL_eKs2_eKsS(service, reset2, r)

def DockerCommonSrL_eKs2_eKsS(service=None, reset=None, r=None):
    return setup_dockerS_eKs2_eKs(service, reset, r)

def DockerStartSrL_eKsPSrL_eKs(reset2, r, service):
    return DockerCommonSrL_eKsPS_eKs(service, r, reset2)

def DockerCommonSrL_eKsPS_eKs(service, reset3=None, reset2=None):
    return DockerStartSrL_eKsS_eKs2(reset2, service, reset3)

def setup_dockerS_eKs2_eKs(reset2=None, service=None, r=None):
    return DockerStartSrL_eKsS_eKs2(r, reset2, service)

def DockerCommonSrL_eKsS_eKs(service, reset2, r):
    return DockerStartSrL_eKsPS_eKs(reset2, service, r)