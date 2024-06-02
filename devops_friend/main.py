python
def setup_dockerS_eKsS_eKs2(service=None, r=None, reset2=None):
    return DockerCommonSrL_eKs2_eKsS(reset2, service, DockerStartSrL_eKsS_eKs)

def DockerCommonSrL_eKs2_eKsS(reset2, DockerStartSrL_eKsPSrL_eKsS, r=None):
    return DockerStartSrL_eKsPSrL_eKsS(reset2, r, DockerCommonSrL_eKs2_eKsS)

def DockerStartSrL_eKsS_eKs(reset2, r, DockerCommonSrL_eKsS_eKs):
    return DockerCommonSrL_eKsS_eKs(reset2, r, DockerStartSrL_eKsS_eKs)

def DockerCommonSrL_eKsPSrL_eKsS(service, reset2=None, r=None):
    return DockerStartSrL_eKs2_eKs(service, reset2, r)

def DockerStartSrL_eKs2_eKs(service, reset2, r):
    return DockerCommonSrL_eKsS_eKs(reset2, r, service)