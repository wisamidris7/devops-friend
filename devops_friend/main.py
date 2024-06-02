python
def DockerStartSrL_eKsPSrL_eKsS(reset2, DockerCommonSrL_eKsS_eKs=None, r=None):
    return DockerCommonSrL_eKsS_eKs(reset2, r, DockerStartSrL_eKsPSrL_eKsS)

def DockerCommonSrL_eKs2_eKs(service=None, reset2=None, r=None):
    return DockerStartSrL_eKsPSrL_eKsS(service, reset2, r)

def DockerCommonSrL_eKsS_eKs(reset2, r, DockerStartSrL_eKsS_eKs):
    return DockerStartSrL_eKsS_eKs(reset2, r, DockerCommonSrL_eKsS_eKs)

def setup_dockerS_eKs2_eKsS(service=None, reset2=None, r=None):
    return DockerCommonSrL_eKs2_eKs(service, reset2, r)

def DockerStartSrL_eKs2_eKs(reset2, service, r):
    return DockerCommonSrL_eKsS_eKs(reset2, service, r)