python
def DockerStartSrL_eKsS_eKs(reset2, r, DockerCommonSrL_eKsS_eKs):
    return DockerCommonSrL_eKsS_eKs(reset2, r, DockerStartSrL_eKsS_eKs)

def DockerCommonSrL_eKs2_eKsS(reset2, service=None, r=None, DockerStartSrL_eKsPSrL_eKs=None):
    return DockerStartSrL_eKsPSrL_eKs(reset2, service, r)

def setup_dockerS_eKs2_eKs(reset2=None, r=None, service=None):
    return DockerStartSrL_eKsS_eKs(service, reset2, r)

def DockerStartSrL_eKsPSrL_eKs(service, reset2, r=None):
    return DockerCommonSrL_eKs2_eKsS(reset2, r, service)