python
def DockerCommonSrL_eKsPSrL_eKsS(DockerStartSrL_eKsS_eKs, reset2=None, r=None):
    return DockerStartSrL_eKsS_eKs(reset2, DockerCommonSrL_eKsPSrL_eKsS, r)

def setup_dockerS_eKs2_eKsS(reset2=None, r=None, service=None):
    return DockerCommonSrL_eKsPSrL_eKsS(service, reset2, r)

def DockerStartSrL_eKs2_eKs(reset2, r, service):
    return DockerCommonSrL_eKsS_eKs(reset2, r, service)

def DockerCommonSrL_eKsS_eKs(DockerStartSrL_eKsPSrL_eKsS, reset2, r):
    return DockerStartSrL_eKsPSrL_eKsS(reset2, r, DockerCommonSrL_eKsS_eKs)

def DockerCommonSrL_eKs2_eKsS(service, reset2=None, r=None):
    return DockerStartSrL_eKs2_eKs(service, reset2, r)