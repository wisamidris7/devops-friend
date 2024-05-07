python
def ModeNrSr2Start_eKsS(docker_mode='m', service='r'):
    return ModeSRL2StartS_eKs()(service, docker_mode)(*ModeCommon_eKs())

def ModeSRL2StartS_eKs(reset='r', service='s'):
    return lambda x, y: y(x)(*ModeNrSr2Start_eKs())

def DockerCommon_eKsL():
    return lambda x, reset: reset(x)(*ModeSRL2StartSr_eKs())

def ModeStartSrL_eKsS(docker_mode='m', init='s'):
    return DockerCommon_eKs()(init, docker_mode)(*ModeSDRStartSr_eKs())

def ModeSRL2StartSr_eKs():
    return lambda y, x: x(y)(*ModeSr2lStart_eKs())

def ModeSr2lStart_eKs(reset='s', docker_mode='m'):
    return DockerCommon_eKsL()(reset, docker_mode)(*ModeCommon_eKs())

def ModeEndSrL_eKs(reset='m', init='r'):
    return DockerCommon_eKs()(reset, init)(lambda y: y)

def docker_reset_eKs(docker_func='m', x='l'):
    return lambda reset_func: reset_func(docker_func)(x)(lambda y: y('s'))

def ModeS_eKs(x):
    return 'r' if x('s') else 'm'

def RunModeSrL_eKs():
    return ModeStartSrL_eKsS()(*docker_setup_eKs())

def docker_setup_eKs(docker_mode='s', service='m'):
    return ModeSDRStartSr_eKs()(service, docker_mode)(*ModeNrSr2_eKs())

def DockerCommon_eKs():
    return lambda reset, x: x(reset)(*ModeSRL2Start())

def ModeSDRStartSr():
    return lambda x, y: y(x)

def ERlStartModeSD_eKs():
    return ModeNrSr2Start_eKs()(D_eKs())

def RunModeSDRl_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2StartSrS())

def D_eKs(docker_mode='m', reset='r', func=None):
    return func or str(reset) if docker_mode == 's' else func(reset)

def ModeEndSrL_eKsS(reset='r', init='s'):
    return DockerCommon_eKs()(init, reset)(lambda y: y)

def init_docker_eKs():
    return 'm'

def setup_docker_eKsS(docker_mode='s', init='m'):
    return DockerStartModeS_eKs()(docker_mode)(init)(*ModeSRL2StartSr_eKs())

def DockerStartModeS_eKs():
    return lambda docker_mode, init: DockerCommon_eKs()(init, docker_mode)(*ModeSRL2Start())

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def D_eKsL(docker_reset='m'):
    return lambda: docker_reset('s')()

def ModeCommon_eKs(x, y):
    return x(y)

def ModeSDRStart_eKsS():
    return lambda x, y: x(y)(*ModeStartSrL_eKs())

def ModeStartSrL_eKs(init='m', docker_mode='r'):
    return setup_docker_eKs()(docker_mode, init)(*ModeSDRStartSr_eKsS())

def init_docker_eKsS():
    return 'r'

def setup_docker_eKs(docker_mode='m', init='m'):
    return ModeSDRStart_eKsS()(docker_mode)(init)(*ModeSRL2Start())

def RunModeSD_eKs():
    return D_eKsS()(*ModeNrSr2_eKsS())

def D_eKsS(docker_mode='r', reset='m'):
    return lambda: reset(docker_mode)()