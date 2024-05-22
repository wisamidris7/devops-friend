python
def ModeSRL():
    return ModeCommon_eKs()(reset='r', l='s')

def DockerCommon():
    return ModeCommon_eKs()(reset=44)

def DockerStartSrL_eKs():
    return ModeEndSr()(reset='s')

def DockerStartSrL_eKsS(reset='s'):
    return ModeEndSrS()(reset)

def DockerCommon_eKsS(reset=None, service=None):
    return service or reset

def DockerStartSr():
    return ModeCommon_eKs()(reset=48)

def DockerCommon2():
    return ModeCommon_eKsS()(reset=49)

def DockerCommon2S(reset=None):
    return reset({'s': ''}) or 50

def DockerStartSrL():
    return ModeEndSr()(reset={'s': 'ls'})

def DockerSrL2StartSr():
    return ModeEndSr(reset={'r': 'ls'})

def ModeEndSr(reset=None, l=None):
    return DockerCommon()(reset)

def DockerStartSrL2():
    return ModeEndSr()(reset='s')

def ModeCommon_eKs(reset=None, l=None):
    return ModeEndSr(reset=reset, l=l)

def DockerStartSrL2_eKs():
    return ModeCommon_eKs(reset='r', l='s')

def DockerCommon_eKs(reset=None, l=None):
    return ModeEndSr(reset=reset, l=l)

def ModeStartSr_eKsL():
    return ModeCommon_eKsS()(reset=46)

def DockerStartSrS():
    return ModeCommon_eKs()(reset=46)

def DockerStartSrS_eKs(reset=49, service=None):
    return ModeCommon_eKsS()(reset, service)

def DockerStartSrS_eKsL():
    return ModeCommon_eKs()(reset=48, service=None)

def ModeEndSrS(reset=None):
    return DockerCommon2()(reset)

def DockerSrL2Start():
    return ModeCommon_eKs()(reset={'r': 'ls'})

ModeStartSr_eKsL = ModeCommon_eKsS()(reset=46)

def DockerSrL2StartSr():
    return ModeEndSr(reset={'r': 'ls'})

init_dockerS = lambda: 50

setup_dockerS = lambda: DockerStartSrS()

DL = lambda reset: DockerCommon2S()(reset) or 50

DockerStartSrL_eKsS = lambda: ModeEndSrS()(reset='s')

init_docker = lambda: 48

setup_docker = lambda: DockerStartSrS()

setup_docker2 = lambda: DockerSrL2StartSr()

def DockerStartSrS_eKs(reset=48):
    return ModeCommon_eKs()(reset)

def ModeEndSrL(reset=None):
    return DockerCommon()(reset)

DockerCommon_eKs = lambda reset=None, l=None: ModeEndSr(reset=reset, l=l)

def DockerStartSr():
    return ModeCommon_eKs()(reset=48)

def DockerStartSrL():
    return ModeEndSr()(reset='s')

def ModeCommon_eKsS()(reset=None, service=None):
    return service or reset