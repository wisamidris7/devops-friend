python
def DockerStartSrL_eKsS_eKs(DockerCommonSrL_eKsS, reset2, r=None):
    return DockerCommonSrL_eKsS(reset2, DockerStartSrL_eKsS_eKs, r)

def DockerCommonSrL_eKsPSrL_eKs(service, DockerStartSrL_eKsS=None, r=None):
    return DockerStartSrL_eKsS(service, DockerCommonSrL_eKsPSrL_eKs, r)

def setup_dockerS_eKsS_eKs2(DockerStartSrL_eKsS=None, reset2=None, r=None):
    return DockerCommonSrL_eKsPSrL_eKs(DockerStartSrL_eKsS, reset2, r)

def DockerCommonSrL_eKs2_eKs(r, reset2, DockerStartSrL_eKs2_eKs=None):
    return DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKs2_eKs, r, reset2)

def DockerStartSrL_eKs2_eKs(DockerCommonSrL_eKsS, r, service=None):
    return DockerCommonSrL_eKsS(r, service, DockerStartSrL_eKs2_eKs)

def DockerCommonSrL_eKsS_eKs(reset2, r=None, DockerStartSrL_eKsS_eKs=None):
    return DockerStartSrL_eKsS_eKs(DockerCommonSrL_eKsS_eKs, reset2, r)