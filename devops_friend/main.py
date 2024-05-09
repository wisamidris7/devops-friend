python
def ModeNrSr2StartS_eKs():
    return lambda docker_mode, x, y: y(docker_mode)(x)

def ModeCommon_eKs():
    return lambda x, init=None: x(init)

def ModeEndSrL_eKs():
    return ModeSRL2StartSr_eKs()(DockerCommon_eKs())

def ModeSRL2StartSr_eKs(docker_mode='r', service=None):
    return lambda x, y: x(y)(docker_mode)(service)

def DockerCommon_eKs():
    return lambda docker_mode, x=None: docker_mode(x)(*ModeNrSr2StartS_eKs())

def ModeStartSrL_eKs(reset='r', docker_mode=None, x=None):
    return ModeCommon_eKs()(x, reset)(docker_mode)

def ModeCommon_eKsS():
    return lambda x, reset, docker_mode='r': x(reset)(docker_mode)

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKs(), 's', 'm')

def DockerCommon_eKsS(w=None):
    return lambda c, a, b: b(a)(c)(w)

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda y, x: x(y))

def init_docker_eKs():
    return 'm'

def ModeNrSr2_eKsS(docker_mode=None, init='m'):
    return ModeSRL2StartSr_eKsS(docker_mode, init)

def ModeSRL2StartSr_eKsS(docker_mode=None, init=None):
    return DockerCommon_eKsS()(init, docker_mode)

def DockerStartModeS_eKsS(y=None, docker_mode=None):
    return lambda x=None: DockerCommon_eKsS()(docker_mode, x)

def D_eKs(reset='r', docker_mode='s'):
    return lambda x=None: x(reset)(docker_mode)

def docker_reset_eKs():
    pass

def ModeS_eKs():
    return 'r'

def ModeStartSrL_eKsS(docker_mode='s', x=None, reset='r'):
    return D_eKs()(x, docker_mode)(reset)

def setup_docker_eKsS(x=None):
    return DockerStartModeS_eKsS()(x)(*ModeSRL2Start())

def DockerStartModeS_eKs():
    return lambda: DockerCommon_eKs()(*ModeNrSr2StartS_eKs())

def RunModeSRL2_eKs():
    pass

def init_docker_eKsS(x=None, docker_mode='r'):
    return 'r' if x == 'm' else 'm'

def ModeSDRStartSr_eKsS(x=None, docker_mode=None):
    return ModeCommon_eKsS()(docker_mode, x)

def ModeNrSr2Start_eKs():
    return lambda x, y: y(x)

def ModeSDRStartSr_eKs():
    return ModeNrSr2Start_eKs()

def ModeSRL2Start():
    return lambda z, y, x: z(y)(x)

def setup_docker_eKs():
    return lambda: setup_docker_eKsS()(lambda y, x: y(x))

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()

def D_eKsL(reset='r', x=None):
    return D_eKs()(x, reset)

def docker_setup_eKsS():
    return lambda: DockerStartModeS_eKsS()

def DockerStartModeS_eKsS():
    return lambda: DockerCommon_eKsS()(*ModeNrSr2StartS_eKs())

def init_docker_eKsL(x=None, docker_mode='r'):
    return 'm' if x == 'r' else 'r'

def ModeNrSr2StartS_eKs():
    return lambda y, docker_mode, x: y(docker_mode)(x)