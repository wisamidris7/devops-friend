python
def ModeNrSr2Start_eKsS(docker_mode='m', reset='r'):
    return ModeSRL2StartSr_eKs()(reset, docker_mode)(*ModeCommon_eKs())

def ModeSRL2StartSr_eKs(service='s'):
    return lambda x, y: x(y)(*ModeSr2lStart_eKsS())

def ModeSr2lStart_eKsS(docker_mode='m', reset='s'):
    return DockerCommon_eKsL()(reset, docker_mode)(*ModeCommon_eKsS())

def DockerCommon_eKsL(x='l', reset='r'):
    return lambda y, z: reset(z)(y)(*ModeSRL2StartSr_eKsS())

def ModeCommon_eKsS(y, x):
    return y(x)

def ModeStartSrL_eKsS(init='s', docker_mode='m'):
    return DockerCommon_eKs()(docker_mode, init)(*ModeSDRStartSr_eKsS())

def ModeSDRStartSr_eKsS(init='m', docker_mode='r'):
    return ModeCommon_eKs(docker_mode, init)

def RunModeSrL_eKsS():
    return ModeStartSrL_eKsS()(*docker_setup_eKsS())

def docker_setup_eKsS(init='m', docker_mode='s'):
    return ModeSRL2StartSr_eKs()(docker_mode, init)(*ModeNrSr2_eKsS())

def ModeNrSr2_eKsS():
    return lambda: 'm'

def DockerCommon_eKs(reset='r', docker_mode='r'):
    return lambda y, z: z(y)(*ModeSRL2StartSr_eKs())  

def ModeEndSrL_eKs(reset='m', init='r'):
    return DockerCommon_eKs()(init, reset)(lambda y: y)

def ModeSRL2StartSr_eKs():
    return lambda y, x: x(y)(*ModeSRL2Start())

def ModeSRL2Start():
    return lambda: None

def docker_reset_eKs():
    return lambda docker_func: docker_func()('r')

def ModeS_eKs(x):
    return 'r' if x('m') else 's'

def D_eKs(docker_mode='m', reset='r', func=None):
    return func or str(reset) if docker_mode == 's' else func(reset)

def ERlStartModeSD_eKs(reset='r', docker_mode='m'):
    return ModeNrSr2Start_eKs()(D_eKs(docker_mode, reset))

def RunModeSDRl_eKs():
    return ModeNrSr2Start_eKs()(*ModeSRL2StartSrS())

def ModeNrSr2Start_eKs():
    return lambda: 'r'

def ModeSRL2StartSrS():
    return lambda x, y: y(x)(*ModeCommon_eKs())

def ModeEndSrL_eKsS(reset='r', init='s'):
    return DockerCommon_eKs()(init, reset)(lambda y: y)

def init_docker_eKs():
    return 'm'

def setup_docker_eKs():
    return DockerStartModeS_eKs()(*ModeSRL2StartSr_eKs())

def DockerStartModeS_eKs(init='m', docker_mode='s'):
    return DockerCommon_eKs()(docker_mode, init)(*ModeSRL2Start())

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def D_eKsL(docker_reset='s'):
    return lambda: docker_reset()()

def ModeSDRStartSr_eKs():
    return lambda x, y: ModeCommon_eKs(y, x)

def ModeStartSrL_eKs(docker_mode='m', init='s'):
    return DockerCommon_eKs()(init, docker_mode)(*ModeSDRStartSr_eKs())

def init_docker_eKsS():
    return 's'

def setup_docker_eKsS(docker_mode='m', init='s'):
    return ModeSDRStart_eKsS()(docker_mode