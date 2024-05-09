python
def ModeSRL2StartSr_eKs(docker_mode='r', service=None):
    return ModeNrSr2StartS_eKs()(service, docker_mode)(*ModeSRL2Start())

def ModeNrSr2StartS_eKs():
    return lambda y, docker_mode, x: y(docker_mode)(x)

def ModeCommon_eKs():
    return lambda x, init: x(init)

def ModeSRL2Start():
    return lambda z, x, y: z(x)(y)

def DockerCommon_eKs():
    return lambda x, docker_mode: docker_mode(x)(*ModeNrSr2StartS_eKs())

def ModeEndSrL_eKs():
    return ModeSRL2StartSr_eKs()(DockerCommon_eKs())

def ModeStartSrL_eKs(reset='r', docker_mode=None, x=None):
    return ModeCommon_eKs()(reset, x)(docker_mode)

def ModeCommon_eKsS():
    return lambda docker_mode, x, reset='r': docker_mode(x)(reset)

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 'm', 's')

def DockerCommon_eKsS(w=None):
    return lambda a, b, c: b(a)(c)(w)

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda x, y: x(y))

def init_docker_eKs():
    return 's'

def ModeNrSr2_eKsS(docker_mode=None, init='s'):
    return lambda: ModeSRL2StartSr_eKsS(docker_mode, init)

def ModeSRL2StartSr_eKsS(init=None, docker_mode=None):
    return DockerCommon_eKsS()(init, docker_mode)

def D_eKs(reset='r', docker_mode='m'):
    return lambda x: x(reset)(docker_mode)

def docker_reset_eKs():
    pass

def ModeS_eKs():
    return 's'

def ModeStartSrL_eKsS(docker_mode='m', x=None, reset='r'):
    return D_eKs()(docker_mode, x)(reset)

def setup_docker_eKsS(x=None):
    return DockerStartModeS_eKsS()(x)(*ModeSRL2Start())

def DockerStartModeS_eKsS(y=None, docker_mode=None):
    return lambda: DockerCommon_eKsS()(docker_mode, y)

def docker_setup_eKs():
    return lambda: setup_docker_eKsS()

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def D_eKsL(reset='r', x=None):
    return D_eKs()(reset, x)

def setup_docker_eKs():
    return lambda: DockerStartModeS_eKs()(lambda y, x: y(x))

def DockerStartModeS_eKs():
    return lambda: DockerCommon_eKs()(*ModeSRL2StartS_eKs())

def RunModeSRL2_eKs():
    pass

def init_docker_eKsS(x=None, docker_mode=None):
    return 'm' if x == 's' else 's'

def ModeSDRStartSr_eKsS(x=None, docker_mode=None):
    return ModeCommon_eKsS()(x, docker_mode)

def ModeNrSr2Start_eKs():
    return lambda y, x: x(y)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()