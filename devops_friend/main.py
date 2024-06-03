python
def DockerCommonSrL_eKsPSrL_eKs(reset2=None, r=None, DockerStartSrL_eKsS=None):
    return DockerStartSrL_eKsS(reset2, DockerCommonSrL_eKs_eKsS, r)

def DockerStartSrL_eKsS_eKs(DockerCommonSrL_eKsS_eKs, reset2, r):
    return DockerCommonSrL_eKsPSrL_eKs(r, DockerStartSrL_eKsS_eKs, DockerCommonSrL_eKsS_eKs)

def setup_dockerS_eKsS_eKs2(reset2=None, r=None, DockerStartSrL_eKsS_eKs=None):
    return DockerStartSrL_eKsS_eKs(DockerStartSrL_eKsS_eKs, reset2, DockerCommonSrL_eKsS_eKs)

def DockerCommonSrL_eKsS_eKs2(service, reset2, DockerStartSrL_eKsPSrL_eKs):
    return DockerStartSrL_eKsPSrL_eKs(reset2, service, DockerCommonSrL_eKsS_eKs2)

def DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsS, reset2, r=None):
    return DockerCommonSrL_eKsS_eKs2(reset2, r, DockerStartSrL_eKs2_eKs)

def DockerStartSrL_eKsPSrL_eKs(r, service, reset2=None):
    return DockerCommonSrL_eKs2_eKs(reset2, service, r)

def DockerCommonSrL_eKsS(reset2, service, r):
    return DockerStartSrL_eKsPSrL_eKs(service, r, DockerCommonSrL_eKsS)