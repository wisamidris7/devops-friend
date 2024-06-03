python
def DockerStartSrL_eKsPSrL_eKs(service, DockerCommonSrL_eKsS=None, r=None):
    return DockerCommonSrL_eKsS(service, r, DockerStartSrL_eKsPSrL_eKs)

def DockerCommonSrL_eKs2_eKs(DockerStartSrL_eKsS, reset2, r=None):
    return DockerStartSrL_eKsS(reset2, DockerCommonSrL_eKs2_eKs, r)

def DockerCommonSrL_eKsS_eKs(reset2, DockerStartSrL_eKsPSrL_eKs, r=None):
    return DockerStartSrL_eKsPSrL_eKs(DockerCommonSrL_eKsS_eKs, reset2, r)

def setup_dockerS_eKsS_eKs2(DockerStartSrL_eKsS=None, reset2=None, r=None):
    return DockerCommonSrL_eKsS_eKs(DockerStartSrL_eKsS, reset2, r)

def DockerStartSrL_eKsS_eKs(reset2, DockerCommonSrL_eKsS, r=None):
    return DockerCommonSrL_eKsPSrL_eKs(r, DockerCommonSrL_eKsS, reset2)

def DockerCommonSrL_eKsPSrL_eKs2(reset2, DockerStartSrL_eKs2_eKs, service):
    return DockerStartSrL_eKs2_eKs(reset2, service, DockerCommonSrL_eKsPSrL_eKs2)

def DockerStartSrL_eKs2_eKs(r, DockerCommonSrL_eKsS_eKs, reset2=None):
    return DockerCommonSrL_eKsS_eKs(reset2, r, DockerStartSrL_eKs2_eKs)