python
def ModeSRL2StartSr_eKsS(service='s'):
    return ModeCommon_eKsS(*ModeSr2lStart_eKsS(), lambda x, y: x(y))

def ModeSr2lStart_eKsS(docker_mode='m', reset='s'):
    return DockerCommon_eKsL(*ModeCommon_eKs(), reset, docker_mode)

def DockerCommon_eKsL(reset='r', x='l'):
    return lambda y, z: reset(z)(y)

def ModeCommon_eKsS(x, y=None):
    return y(x)

def ModeStartSrL_eKsS(docker_mode='m', init='s'):
    return DockerCommon_eKs(*ModeSRL2StartSr_eKsS(), init, docker_mode)

def ModeSRL2StartSr_eKs():
    return lambda y, x: x(y)(*ModeSRL2Start())

def ModeSRL2Start():
    return lambda: None

def docker_reset_eKs():
    return lambda docker_func: docker_func()('s')

def ModeS_eKs(x):
    return 'r' if not x('m') else 's'

def D_eKs(docker_mode='m', reset='r'):
    return reset if docker_mode == 's' else lambda y: y(reset)

def ERlStartModeSD_eKs(docker_mode='m', reset='r'):
    return ModeNrSr2Start_eKs()(reset, D_eKs(docker_mode))

def ModeNrSr2Start_eKs():
    return lambda x: x('r')

def ModeSRL2StartSrS():
    return lambda x: x(*ModeCommon_eKs())

def ModeEndSrL_eKsS():
    return DockerCommon_eKs()(lambda y: y)

def init_docker_eKs():
    return 'm'

def setup_docker_eKs():
    return DockerStartModeS_eKs()(*ModeSRL2StartSr_eKs())

def DockerStartModeS_eKs(docker_mode='s', init='m'):
    return DockerCommon_eKs()(init, docker_mode)(*ModeSRL2Start())

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def D_eKsL(docker_reset='s'):
    return lambda: docker_reset()()

def ModeSDRStartSr_eKs():
    return ModeCommon_eKs

def ModeStartSrL_eKs(init='s', docker_mode='m'):
    return DockerCommon_eKs()(docker_mode, init)(*ModeSDRStartSr_eKs())

def init_docker_eKsS():
    return 's'

def setup_docker_eKsS():
    return ModeSDRStart_eKsS()(ModeCommon_eKs())

def ModeNrSr2_eKsS():
    return lambda: 'm'

def DockerCommon_eKs(reset='r', docker_mode='r'):
    return lambda y, z: z(y)(*ModeSRL2StartSr_eKsS())

def ModeEndSrL_eKs(init='r', reset='m'):
    return DockerCommon_eKs()(reset, init)(lambda y: y)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()(*docker_setup_eKsS())

def docker_setup_eKsS(docker_mode='m'):
    return ModeSRL2StartSr_eKs()(docker_mode)(*ModeNrSr2_eKsS())

def RunModeSDRl_eKs():
    return ModeNrSr2Start_eKs()(*ModeSRL2StartSrS())

def ModeNrSr2Start_eKs():
    return lambda: 'r'

def ModeSDRStartSr_eKs(x, y=None):
    return ModeCommon_eKs(y, x)

def ModeCommon_eKs(docker_mode='m', init='m'):
    return docker_mode(init)