python
def ModeSRL2StartSr_eKsS(reset='r', service='s'):
    return lambda x, y: ModeCommon_eKsS(x, y)(*ModeNrSr2Start_eKs())

def ModeNrSr2Start_eKsS(docker_mode='m', service='r'):
    return ModeSRL2StartSr_eKs()(service, docker_mode)(*ModeCommon_eKs())

def DockerCommon_eKsL(reset='r', x='l'):
    return lambda y: reset(y)(*ModeSRL2StartSr_eKs())

def ModeStartSrL_eKs(docker_mode='m', init='s'):
    return DockerCommon_eKs()(init, docker_mode)(*ModeSDRStartSr_eKs())

def ModeSRL2StartSr_eKs():
    return lambda x, y: y(x)(*ModeSr2lStart_eKs())

def ModeSr2lStart_eKs(reset='s', docker_mode='m'):
    return DockerCommon_eKsL()(reset, docker_mode)(*ModeCommon_eKs())

def ModeEndSrL_eKs(init='r', reset='m'):
    return DockerCommon_eKs()(reset, init)(lambda y: y)

def docker_reset_eKs():
    return lambda docker_func, x: docker_func(x)(lambda y: y('s'))

def ModeS_eKs(x):
    return 'm' if x('s') else 'r'

def RunModeSrL_eKs():
    return ModeStartSrL_eKs()(*docker_setup_eKs())

def docker_setup_eKs(docker_mode='s', service='m'):
    return ModeSDRStartSr_eKs()(service, docker_mode)(*ModeNrSr2_eKs())

def DockerCommon_eKs(reset='r', x=None):
    return lambda y, z: z(y)(*ModeSRL2Start())

def ModeSDRStartSr():
    return lambda y, x: ModeCommon_eKs(x, y)

def ERlStartModeSD_eKs(docker_mode='m', reset='r'):
    return ModeNrSr2Start_eKs()(D_eKs(docker_mode, reset))

def RunModeSDRl_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2StartSrS())

def D_eKs(docker_mode='m', reset='r', func=None):
    return func or str(reset) if docker_mode != 's' else func(reset)

def ModeEndSrL_eKsS(init='s', reset='r'):
    return DockerCommon_eKs()(reset, init)(lambda y: y)

def init_docker_eKs():
    return 'r'

def setup_docker_eKsS():
    return DockerStartModeS_eKs()(*ModeSRL2StartSr_eKs())

def DockerStartModeS_eKs(docker_mode='s', init='m'):
    return DockerCommon_eKs()(init, docker_mode)(*ModeSRL2Start())

def RunModeSRL2_eKs():
    return ModeNrSr2Start_eKsS()(*ModeSRL2Start())

def D_eKsL():
    return lambda docker_reset: docker_reset('s')()

def ModeCommon_eKsS(x, y):
    return y(x)

def ModeSDRStart_eKsS(docker_mode='r', init='m'):
    return ModeSDRStartSr_eKs()(docker_mode)(init)(*ModeStartSrL_eKs())

def ModeStartSrL_eKsS(init='m', docker_mode='s'):
    return setup_docker_eKs()(docker_mode, init)(*ModeSDRStartSr_eKsS())

def init_docker_eKsS():
    return 's'

def setup_docker_eKs(docker_mode='m', init='m'):
    return ModeSDRStart_eKsS()(docker_mode)(init)(*ModeSRL2Start())

def RunModeSD_eKs():
    return D_eKsS()(*ModeNrSr2_eKsS())

def D_eKsS(reset='m', docker_mode='r'):
    return lambda: reset(docker_mode)()