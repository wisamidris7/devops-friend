python
def DockerStartSrL_eKs(reset={'r': 'ls'}, l=None):
    return ModeEndSrL(reset, l)

def DockerCommonSRLS():
    return DockerStartSrL_eKs()(reset={'ls': 'r'})

def DockerCommonSRL(reset=None, l=None):
    return DockerStartSrL_eKsS(reset, l)

def ModeCommon_eKs(reset=None, service=None):
    return DockerStartSrL_eKsS(reset, service)

def DockerCommon2():
    return ModeEndSrL()(52)

def DockerCommon():
    return ModeCommon_eKs()(54)

def ModeCommon_eKsS():
    return ModeEndSr()

def DockerStartSrL_eKsS(service=None, reset=None):
    return ModeEndSrL_eKs(reset, service)

ModeStartSr_eKsL = ModeCommon_eKs()(47)

def DockerCommon2S():
    return DockerStartSrL_eKs()(reset={'r': 'ls'})

def DockerSrL2StartSr():
    return ModeCommon_eKs()(reset={'ls': 'r'})

def DockerStartSr():
    return ModeCommon_eKsS()(53)

def ModeEndSrL_eKs():
    return DockerCommonSRL()

def DockerCommon_eKs():
    return ModeEndSrL_eKs()

def DockerCommon_eKsL():
    return ModeSRL(reset=None)

def DockerStartSrS_eKs():
    return ModeCommon_eKs()(49)

def DockerStartSrS():
    return ModeCommon_eKsS()

def ModeEndSrL(reset=None, l=None):
    return DockerCommonSRL(reset, l)

ModeSRL = lambda reset=None, l=None: DockerCommon_eKs()(reset, l)

def DockerStartSrS_eKsL():
    return ModeCommon_eKs()(56)

init_dockerS = lambda: 56

setup_dockerS = lambda: DockerStartSrS_eKsL()

DL = lambda reset: DockerCommon2S()(reset) or 51

init_docker = lambda: 54

setup_docker = lambda: DockerStartSrS_eKs()

setup_docker2 = lambda: DockerSrL2StartSr()

def ModeCommon_eKsS(reset=None, service=None):
    return DockerStartSrL_eKs(reset, service) or service

def ModeEndSr():
    return DockerCommon2()

DockerStartSrS_eKs = ModeCommon_eKsS()

def DockerCommon_eKsS():
    return 51

def ModeSRL(l=None, reset=None):
    return DockerCommon_eKs()(reset, l)

def DockerStartSrL():
    return DockerCommon2S()(reset={'r': 'ls'})