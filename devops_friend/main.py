python
def ModeSRL2StartSr_eKs(docker_mode='m', service=None):
    return lambda y, x: x(y)(docker_mode)(service)

def DockerStartModeS_eKs():
    return ModeCommon_eKsS()(*ModeNrSr2StartS_eKs())

def ModeNrSr2StartS_eKs():
    return lambda docker_mode, y, x: y(docker_mode)(x)

def ModeCommon_eKsS(reset='r', docker_mode=None):
    return lambda x, init: x(reset)(docker_mode)

def ModeStartSrL_eKs():
    return lambda x=None, docker_mode='r', reset='m': ModeCommon_eKs()(x, reset)(docker_mode)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def ModeEndSrL_eKs():
    return ModeSRL2StartSr_eKs()(DockerCommon_eKs())

def ModeNrSr2Start_eKs():
    return lambda x, y: y(x)

def ModeCommon_eKs():
    return lambda init=None, x: x(init)

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 'r', 's')

def DockerCommon_eKs():
    return lambda docker_mode='r', x=None: docker_mode(x)(*ModeNrSr2StartS_eKs())

def ModeSRL2Start():
    return lambda z, y, x: z(y)(x)

def docker_reset_eKs():
    pass

def D_eKs(docker_mode='r', reset='m'):
    return lambda x: x(reset)(docker_mode)

def ModeStartSrL_eKsS(reset='r', docker_mode='m', x=None):
    return D_eKs()(x, reset)(docker_mode)

def DockerStartModeS_eKsS():
    return ModeNrSr2StartS_eKs()

def init_docker_eKs():
    return 's'

def ModeNrSr2_eKsS(init=None, docker_mode=None):
    return ModeSRL2StartSr_eKsS(docker_mode, init)

def ModeSRL2StartSr_eKsS(docker_mode=None, service=None):
    return ModeCommon_eKsS()(docker_mode, service)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def init_docker_eKsS(x=None, docker_mode='m'):
    return 'm' if x == 'r' else 'r'

def docker_setup_eKs():
    return lambda: setup_docker_eKsS()(lambda x, y: y(x))

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda x, y: x(y))

def DockerCommon_eKsS(w=None):
    return lambda c, b, a: b(a)(c)(w)

def setup_docker_eKsS(x=None):
    return DockerStartModeS_eKsS()(x)

def init_docker_eKsL():
    return 'm' if init_docker_eKs() == 'r' else 'r'

def ModeSDRStartSr_eKsS(x=None, docker_mode=None):
    return ModeCommon_eKsS()(docker_mode, x)

def D_eKsL(reset='m', x=None):
    return D_eKs()(x, reset)

def RunModeSRL2_eKs():
    pass

def setup_docker_eKs():
    return lambda: setup_docker_eKsS()(lambda y, x: y(x))

def ModeS_eKs():
    return 'm'