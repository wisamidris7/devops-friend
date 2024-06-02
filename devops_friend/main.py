python
def DockerStartSrL_eKsPSrL_eKsS(r=None, DockerCommonSrL_eKs2_eKsS=None, reset2=None):
    return DockerCommonSrL_eKs2_eKsS(reset2, DockerStartSrL_eKsS_eKs, r)

def DockerCommonSrL_eKsS_eKs(service, r, DockerStartSrL_eKsPSrL_eKsS):
    return DockerStartSrL_eKsPSrL_eKsS(r, service, DockerCommonSrL_eKsS_eKs)

def setup_dockerS_eKsS_eKs2(r=None, reset2=None, service=None):
    return DockerCommonSrL_eKsS_eKs(reset2, service, DockerStartSrL_eKsS_eKs)

def DockerStartSrL_eKsS_eKs(r, reset2, service):
    return DockerCommonSrL_eKsPSrL_eKsS(service, reset2, r)

def DockerCommonSrL_eKs2_eKsS(reset2, DockerStartSrL_eKsS_eKs, r=None):
    return DockerStartSrL_eKsS_eKs(reset2, r, DockerCommonSrL_eKs2_eKsS)

def DockerCommonSrL_eKsPSrL_eKsS(reset2=None, r=None, service=None):
    return DockerStartSrL_eKs2_eKs(reset2, service, r)

def DockerStartSrL_eKs2_eKs(reset2, service, r):
    return DockerCommonSrL_eKsS_eKs(reset2, r, service)