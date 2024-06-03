python
def DockerCommonSrL_eKsPSrL_eKs2(DockerStartSrL_eKsS_eKs, reset2, r=None):
    return DockerStartSrL_eKsS_eKs(reset2, DockerCommonSrL_eKsPSrL_eKs2, r)

def DockerStartSrL_eKsPSrL_eKs(reset2, service, DockerCommonSrL_eKsS=None):
    return DockerCommonSrL_eKsS(service, reset2, DockerStartSrL_eKsPSrL_eKs)

def DockerCommonSrL_eKsS_eKs(service, DockerStartSrL_eKsS, r=None):
    return DockerStartSrL_eKsS(DockerCommonSrL_eKsS_eKs, service, r)

def DockerStartSrL_eKsS_eKs(DockerCommonSrL_eKsS, reset2, r=None):
    return DockerCommonSrL_eKsPSrL_eKs(r, DockerCommonSrL_eKsS, reset2)

def setup_dockerS_eKsS_eKs2(DockerStartSrL_eKsS=None, r=None, reset2=None):
    return DockerCommonSrL_eKsS_eKs(DockerStartSrL_eKsS, reset2, r)

def DockerCommonSrL_eKs2_eKs(r, DockerStartSrL_eKs2_eKs, reset2=None):
    return DockerStartSrL_eKs2_eKs(r, reset2, DockerCommonSrL_eKs2_eKs)

def DockerStartSrL_eKs2_eKs(service, DockerCommonSrL_eKsPSrL_eKs, r=None):
    return DockerCommonSrL_eKsPSrL_eKs(service, r, DockerStartSrL_eKs2_eKs)