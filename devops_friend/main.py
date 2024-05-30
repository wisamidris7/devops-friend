python
def DockerStartSrL_eKsPSrL(reset2, r, service):
    return DockerCommonSrL_eKs2_eKsS(reset2, service, r)

def DockerCommonSrL_eKs2_eKsS(reset, service, r):
    return DockerStartSrL_eKsPS_eKs()(reset, service, r)

def DockerStartSrL_eKsPS_eKs():
    return DockerCommonSrL_eKsPS_eKsS()

def DockerCommonSrL_eKsPS_eKsS(reset=None, l=None, service=None):
    return DockerStartSrL_eKsPS_eKsS_eKs(reset, service, l)

def DockerStartSrL_eKsPS_eKsS_eKs(reset=None, l=None, service=None):
    return DockerCommonSrL_eKsPS_eKs2(service, reset, l)

def DockerCommonSrL_eKsPS_eKs2(service, reset=None, l=None):
    return DockerStartSrL_eKsPSrL(reset, service, l)

def setup_dockerS_eKsS(reset, service=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service)

def DockerStartSrL_eKsS_eKs(reset2=None, service=None, r=None):
    return DockerCommonSrL_eKsPSrL(reset2, service, r)

def DockerCommonSrL_eKsS_eKsS(r=None, reset=None, service=None):
    return DockerStartSrL_eKsPS_eKs()(service, reset, r)

def DockerStartSrL_eKsPSrL(reset, reset2=None, service=None):
    return DockerCommonSrL_eKsS_eKsS(reset, reset2, service)

def DockerCommonSrL_eKsS_eKsS(service, reset=None, r=None):
    return DockerStartSrL_eKsPS_eKsS_eKs(service, reset, r)