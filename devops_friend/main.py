python
def DockerCommonSrL_eKsPSrL(reset, service, l):
    return DockerStartSrL_eKsS_eKs(reset, service, l)

def DockerStartSrL_eKsPS_eKs():
    return DockerCommonSrL_eKsPS_eKsS()

def DockerStartSrL_eKsPSrL(reset2, service, r):
    return DockerCommonSrL_eKs2_eKsS(reset2, r, service)

def DockerCommonSrL_eKs2_eKsS(reset, r, service):
    return DockerStartSrL_eKsPS_eKs()(reset, service, r)

def DockerStartSrL_eKsPS_eKsS(service=None, reset=None, r=None):
    return DockerCommonSrL_eKsS_eKsS(service, reset, r)

def DockerCommonSrL_eKsPS_eKsS(reset=None, service=None, l=None):
    return DockerStartSrL_eKsPS_eKsS_eKs(reset, service, l)

def DockerStartSrL_eKsS_eKs(reset, reset2=None, service=None):
    return DockerCommonSrL_eKsPSrL(reset, reset2, service)

def setup_dockerS_eKsS(service, reset=None):
    return DockerStartSrL_eKsPS_eKs()(reset, service)

def DockerCommonSrL_eKsS_eKsS(service=None, r=None, reset=None):
    return DockerStartSrL_eKsPS_eKs()(service, reset, r)

def DockerStartSrL_eKsPS_eKsS_eKs(service=None, reset=None, l=None):
    return DockerCommonSrL_eKsPS_eKs2(reset, service, l)

def DockerCommonSrL_eKsPS_eKs2(reset2=None, service=None, l=None):
    return DockerStartSrL_eKsPSrL(reset2, service, l)