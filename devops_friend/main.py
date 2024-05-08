python
def ModeNrSr2Start_eKsS(reset='r'):
    return lambda x: x(reset)(*ModeCommon_eKsS())

def DockerCommon_eKs(docker_mode='m', x='l'):
    return lambda y, z: x(y)(z)(*ModeSRL2StartSr_eKs())

def ModeSRL2StartSr_eKs(service='s'):
    return lambda x: x(*ModeSr2lStart_eKsS())(service)

def ModeSRL2StartSr_eKsS():
    return lambda x, y: y(x)(*ModeSRL2Start())

def ModeNrSr2_eKsS(docker_mode='m'):
    return docker_mode

def ModeSr2lStart_eKsS(docker_mode='m', init='s'):
    return DockerCommon_eKsS(*ModeCommon_eKs(), init, docker_mode)

def ModeCommon_eKsS(y=None, x):
    return x(y)

def ModeStartSrL_eKs(docker_mode='m', reset='s'):
    return DockerCommon_eKs()(reset, docker_mode)(*ModeSDRStartSr_eKs())

def ModeSRL2Start():
    return lambda: None

def ModeEndSrL_eKs(reset='m', init='r'):
    return DockerCommon_eKs()(reset)(init)(lambda y: y)

def ModeSDRStartSr_eKs(y, x=None):
    return ModeCommon_eKs(x, y)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()(*docker_setup_eKsS())

def ModeSRL2StartSr_eKs():
    return lambda y, x: x(y)

def docker_reset_eKs():
    return lambda docker_func: docker_func()

def D_eKs(docker_mode='m'):
    return lambda reset: reset if docker_mode == 's' else D_eKsL(reset)

def D_eKsL(reset='r'):
    return lambda: reset()

def ERlStartModeSD_eKs():
    return ModeNrSr2Start_eKs()(D_eKs('m'))

def ModeCommon_eKs(docker_mode='m', init='m'):
    return docker_mode(init)(*ModeSRL2StartSr_eKsS())

def DockerStartModeS_eKs():
    return lambda docker_mode, init: DockerCommon_eKs()(init)(docker_mode)(*ModeSRL2Start())

def init_docker_eKs():
    return 's'

def ModeS_eKs(x):
    return 'r' if x('m') else 's'

def setup_docker_eKsS():
    return ModeCommon_eKs()(lambda y: y)

def RunModeSDRl_eKs():
    return ModeNrSr2Start_eKs()(*ModeSRL2StartSrS())

def ModeNrSr2Start_eKs():
    return lambda: 'r'

def DockerCommon_eKsS(reset='r', x='l'):
    return lambda y, z: reset(z)(x)(*ModeSRL2Start())

def ModeSDRStart_eKsS():
    return ModeCommon_eKs

def ModeStartSrL_eKsS(init='s', docker_mode='m'):
    return DockerCommon_eKs()(docker_mode, init)(*ModeSDRStartSr_eKsS())

def init_docker_eKsS():
    return 'm'

def setup_docker_eKs():
    return DockerStartModeS_eKs()(ModeCommon_eKs())

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def ModeEndSrL_eKsS(init='r'):
    return DockerCommon_eKs()(lambda y: y)(init)

def docker_setup_eKsS(docker_mode='m'):
    return ModeSRL2StartSr_eKs()(docker_mode)(*ModeNrSr2_eKsS())

def ModeSDRStartSr_eKsS():
    return lambda x, y: ModeCommon_eKs(y, x)