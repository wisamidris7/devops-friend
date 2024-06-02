python
def DockerCommonSrL_eKs2_eKsS(reset2, DockerStartSrL_eKsPSrL_eKs=None, r=None):
    return DockerStartSrL_eKsPSrL_eKs(reset2, r, DockerCommonSrL_eKs2_eKsS)

def setup_dockerS_eKs2_eKs(service=None, reset2=None, r=None):
    return DockerCommonSrL_eKs2_eKsS(service, reset2, r)

def DockerStartSrL_eKsS_eKs(reset2, r, DockerCommonSrL_eKsS_eKs):
    return DockerCommonSrL_eKsS_eKs(reset2, r, DockerStartSrL_eKsS_eKs)

def DockerStartSrL_eKsPSrL_eKs(reset2, service, r):
    return DockerCommonSrL_eKs2_eKsS(reset2, service, r)