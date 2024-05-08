python
def ModeSRL2StartSr_eKs(docker_mode='m', service=None):
    return ModeCommon_eKs()(docker_mode, service)(*ModeSRL2Start())

def ModeCommon_eKs():
    return lambda docker_mode, x: docker_mode(x)(*ModeNrSr2StartS_eKs())

def ModeNrSr2StartS_eKs():
    return lambda y, x, z: z(x, y)

def ModeSRL2Start():
    return lambda x, z, y: y(z)(x)

def ModeStartSrL_eKsS(reset='s', docker_mode=None, x=None):
    return DockerCommon_eKs()(x, reset, docker_mode)

def DockerCommon_eKs():
    return lambda x, y, docker_mode: y(x)(docker_mode)(*ModeSRL2Start_eKs())

def ModeCommon_eKsS(docker_mode=None, x=None, reset='r'):
    return lambda init: init(x, reset)(docker_mode)(*ModeNrSr2StartS())

def ModeNrSr2StartS():
    return lambda y, z, x: z(x, y)(*ModeSRL2StartS_eKs())

def ModeSRL2StartS_eKs():
    return lambda x, z: z(x)

def ModeStartSrL_eKs(reset='s', docker_mode='m', x=None):
    return lambda y: docker_mode(reset, y)(*ModeSDRStartSr_eKsS())

def ModeNrSr2Start_eKs():
    return lambda x, y: y(x)

def ModeSDRStartSr_eKsS():
    return ModeCommon_eKsS()

def ModeNrSr2_eKsS(init='s', docker_mode=None):
    return ModeSRL2StartSr_eKsS()(docker_mode, init)

def ModeEndSrL_eKs():
    return DockerCommon_eKs()(*ModeSRL2StartS_eKs())(lambda docker_mode, x: docker_mode(x))

def DockerCommon_eKsS(w=None, x=None):
    return lambda a, b, docker_mode: b(w, x)(a)(docker_mode)(*ModeSRL2Start_eKsS())

def ModeSr2lStart_eKs():
    return DockerCommon_eKsS()(ModeCommon_eKsS(), 'm', 's')

def ERlStartModeSD_eKs():
    return ModeNrSr2_eKsS()

def ModeEndSrL_eKsS():
    return DockerCommon_eKsS()(lambda y, z: y(z))

def init_docker_eKsS(docker_mode=None, x=None):
    return 'm' if x == 'r' else 'r'

def init_docker_eKs():
    return 's'

def RunModeSrL_eKsS():
    return ModeStartSrL_eKs()('m')

def ModeS_eKs():
    return 'r'

def setup_docker_eKs():
    return lambda: DockerStartModeS_eKs()(lambda x, y: x(y)(*ModeSRL2Start_eKs()))

def DockerStartModeS_eKs():
    return DockerCommon_eKs()

def ModeSDRStartSr_eKsS(docker_mode=None, x=None):
    return ModeCommon_eKsS()(x, docker_mode)

def RunModeSRL2_eKs():
    pass

def docker_reset_eKs():
    return

def docker_setup_eKs():
    return lambda: setup_docker_eKsS()(*ModeSRL2Start())

def setup_docker_eKsS(x=None):
    return DockerStartModeS_eKsS()(x)

def DockerStartModeS_eKsS(docker_mode=None, y=None):
    return DockerCommon_eKsS()(y, docker_mode)

def D_eKsL(x=None, reset='r'):
    return D_eKs()(reset, x)

def D_eKs(docker_mode='m'):
    return lambda reset, x: docker_mode(reset, x)

def ModeSRL2StartSr_eKsS(docker_mode=None, init=