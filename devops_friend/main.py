python
def setup_dockerS_eKs2_eKs(reset=None, r=None, service=None):
    return DockerCommonSrL_eKsPS_eKs(reset, service, r)

def DockerStartSrL_eKsPS_eKs(reset2=None, service=None, l=None):
    return DockerCommonSrL_eKsS_eKs2(service, reset2, l)

def DockerCommonSrL_eKsPS_eKs(reset2=None, r=None, service=None):
    return DockerStartSrL_eKsS_eKs2(reset2, service, r)

def DockerStartSrL_eKsS_eKs2(reset2=None, service=None, reset3=None):
    return DockerCommonSrL_eKsPSrL_eKs(service, reset2, reset3)

def DockerCommonSrL_eKsS_eKs2(service=None, reset2=None, r=None):
    return DockerStartSrL_eKsPS_eKs(service, reset2, r)

def DockerStartSrL_eKsPSrL_eKs(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKs2_eKsS(service, reset2, r)

def DockerCommonSrL_eKs2_eKsS(service=None, r=None, reset2=None):
    return DockerStartSrL_eKsPSrL_eKs2(service, r, reset2)