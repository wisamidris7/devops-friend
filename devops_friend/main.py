python
def ModeSRL2StartSr_eKsS(service='s'):
    return lambda x, y: y(x)(*ModeSRL2Start())

def ModeNrSr2Start_eKs(reset='r'):
    return lambda x: x(*ModeCommon_eKsS(), reset)

def ModeCommon_eKs(init='m', docker_mode=None):
    return docker_mode(init)(*ModeSRL2StartSr_eKsS())

def ModeSRL2StartSr_eKs():
    return lambda y, x: x(y)(*ModeSRL2Start())

def ModeStartSrL_eKs(reset='s', docker_mode='m'):
    return DockerCommon_eKs()(docker_mode, reset)(*ModeSDRStartSr_eKs())

def ModeNrSr2_eKsS(docker_mode='m'):
    return ModeNrSr2Start_eKs()(docker_mode)

def ModeSRL2Start():
    return lambda: None

def ModeEndSrL_eKs():
    return DockerCommon_eKs()(lambda y: y)

def ModeSDRStartSr_eKs(x=None, y=None):
    return ModeCommon_eKs(x, y)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()(docker_setup_eKsS())

def ModeCommon_eKsS(reset='r', x=None):
    return lambda y: x(reset)(y)

def DockerCommon_eKs():
    return lambda x, y, z: y(x)(z)(*ModeSRL2StartSr_eKs())

def ERlStartModeSD_eKs():
    return ModeNrSr2Start_eKs()(D_eKs('m'))

def D_eKsL(reset='r'):
    return lambda: reset

def ModeSr2lStart_eKsS(init='s', docker_mode='m'):
    return DockerCommon_eKsS(ModeCommon_eKs(), init, docker_mode)

def ModeS_eKs(x):
    return 'r' if x('m') else 's'

def ModeEndSrL_eKsS(init='r', docker_mode='m'):
    return DockerCommon_eKs()(docker_mode)(init)(lambda y: y)

def docker_reset_eKs():
    return lambda docker_func: docker_func()

def D_eKs(docker_mode='m', reset=None):
    return reset if docker_mode == 's' else D_eKsL(reset)

def ModeNrSr2Start_eKs():
    return lambda: 'r'

def DockerStartModeS_eKs():
    return lambda docker_mode, init: DockerCommon_eKs()(init)(docker_mode)(*ModeSRL2Start())

def init_docker_eKs():
    return 's'

def docker_setup_eKsS(docker_mode='m', reset=None):
    return ModeSRL2StartSr_eKs()(docker_mode)(*ModeNrSr2_eKsS(reset))

def RunModeSDRl_eKs():
    return ModeNrSr2Start_eKs()(*ModeSRL2StartSrS())

def ModeStartSrL_eKsS(docker_mode='m', init='s', reset=None):
    return DockerCommon_eKs()(reset, docker_mode, init)(*ModeSDRStartSr_eKsS())

def setup_docker_eKsS():
    return ModeCommon_eKs()(lambda y: y)

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def init_docker_eKsS():
    return 'm'

def ModeSDRStartSr_eKsS(y=None, x=None):
    return ModeCommon_eKsS(x, y)

def setup_docker_eKs():
    return DockerStartModeS_eKs()(ModeCommon_eKs())

def DockerCommon_eKsS(x='l', reset='r', docker_mode=None):
    return lambda y, z: reset(z)(x)(*ModeSRL2Start())

def ModeSr2lStart_eKs():
    return DockerCommon_eKs()(*ModeCommon_eKs(), 's')

def ModeSRL2StartSrS():
    return