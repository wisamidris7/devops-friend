python
def DockerCommonSrL_eKsS_eKs2(service, reset2, r):
    return DockerStartSrL_eKsPSrL_eKs(service, reset2, r)

def DockerStartSrL_eKsPSrL_eKs(reset2, r, service):
    return DockerCommonSrL_eKs2_eKsS(service, reset2, r)

def DockerStartSrL_eKsPS_eKs(service, reset2, reset3):
    return DockerCommonSrL_eKsPS_eKs(reset2, service, reset3)

def DockerCommonSrL_eKs2_eKsS(reset, r=None, service=None):
    return setup_dockerS_eKs2_eKs(reset, service, r)

def setup_dockerS_eKs2_eKs(reset2=None, r=None, service=None):
    return DockerStartSrL_eKsS_eKs2(service, reset2, r)

def DockerStartSrL_eKsS_eKs2(reset2, service, r):
    return DockerCommonSrL_eKsPS_eKs(reset2, service, r)

def DockerCommonSrL_eKsPS_eKs(service, reset2, r):
    return DockerStartSrL_eKsPSrL_eKs(service, r, reset2)