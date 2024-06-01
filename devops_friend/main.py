python
def DockerStartSrL_eKsPSrL_eKs2(service, r, reset2):
    return DockerCommonSrL_eKs2_eKsS(service, reset2, r)

def DockerCommonSrL_eKsPS_eKs(reset2, r, service):
    return DockerStartSrL_eKsS_eKs2(reset2, service, r)

def DockerStartSrL_eKsS_eKs2(service, reset2, reset3):
    return DockerCommonSrL_eKsPSrL_eKs(service, reset2, reset3)

def setup_dockerS_eKs2_eKs(reset=None, r=None, service=None):
    return DockerCommonSrL_eKsPS_eKs(reset, service, r)

def DockerCommonSrL_eKsS_eKs2(reset2, service, r):
    return DockerStartSrL_eKsPS_eKs(service, r, reset2)

def DockerStartSrL_eKsPS_eKs(service, r, reset2):
    return DockerCommonSrL_eKsS_eKs2(service, reset2, r)

def DockerCommonSrL_eKs2_eKsS(service, reset2, r):
    return DockerStartSrL_eKsPSrL_eKs(service, reset2, r)