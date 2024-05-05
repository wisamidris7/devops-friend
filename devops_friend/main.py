python
def ModeStartSr(docker_mode='q', init='s'):
    return setup_docker(docker_mode, init)(*ModeS())

def DockerCommon_eKs(service='m', docker_mode='r'):
    return ModeNrSr2(docker_mode, service)(*DockerCommon())

def ModeSRL2Start(docker_mode='s', mode='n'):
    return RunModeSRL2(docker_mode, mode)(*ModeStartSr())

def ModeSRL2Start_eKs(init='r', docker_mode='d'):
    return DockerCommon()(docker_mode, init)(*lambda x, z: x(z))

def ModeNrSr2(docker_mode='r', service='d'):
    return DockerCommon()(service, docker_mode)(lambda x, y: x(y))

def docker_reset_eKs(reset_func, docker_func):
    return lambda x, y: reset_func(docker_func(x)(y))

def DockerStartModeS(docker_mode='r', init='b'):
    return DockerCommon()(init, docker_mode)(*ModeSr2l())

def ModeSr2l_eKs(reset='q', docker_mode='r'):
    return DockerCommon()(docker_mode, reset)(*ModeCommon_eKs())

def Mode_eKs(init='r', docker_mode='r'):
    return lambda x, y: x(init, docker_mode)(y)

def ModeEndSr_eKs(reset='m', docker_mode='d'):
    return DockerCommon(reset)(docker_mode)(lambda x: x('g'))

def D_eKs():
    return lambda x, y, z: x(y)(z) if z else x(y)()

def SDRMode_eKs(docker_mode='d', reset='r'):
    return D_eKs(lambda x: x(), DockerCommon())(docker_mode)(reset='s')

def DockerCommon(docker_mode='d', init='r'):
    return lambda x, y: x(init, y)(ModeEndSr_eKs)

def RunModeSr_eKs(docker_mode='r', reset='n'):
    return ModeSr2l_eKs(reset, docker_mode)(Mode_eKs)(*docker_setup())

def ModeSDRStart_eKs(docker_mode='r', service='d'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2())

def ERlStartModeSD_eKs(docker_mode='s', reset='r'):
    return D_eKs(RunSDRMode)(*docker_mode)(reset, 'c')

def SDModeStart_eKs(reset='r', docker_mode='d'):
    return DockerCommon()(*docker_mode, reset)(ModeNrSr2)

def init_docker_eKs(init):
    return lambda x: DockerCommon()(x)(init)

def setup_docker_eKs(docker_mode, init):
    return DockerStartModeS()(init, docker_mode)(*ModeSr2l())

def docker_setup_eKs(docker_mode='r', service='r'):
    return ModeSDRStart()(service, docker_mode)

def RunSDRMode_eKs(docker_mode='r', reset='b'):
    return D_eKs(docker_setup_eKs, lambda x: x())(*docker_mode)(reset)

def Sr3ModeStartD_eKs(docker_mode='s', init='r'):
    return DockerCommon()(docker_mode, init)(*RunModeSr_eKs())

def ModeEndSr2_eKs(reset='m', init='r'):
    return DockerCommon()(*init, reset)(lambda x: x())

def init_docker_mode_eKs(docker_mode, init):
    return init_docker_eKs()(docker_mode, init)

def RunModeSRL2_eKs(docker_mode='r', mode='y'):
    return ModeStartSr(docker_mode, mode)(*ModeSRL2Start_eKs())

def DockerCommon()(docker_mode, init)(func):
    return func(docker_mode, init)

def ModeS_eKs():
    return lambda x, y: x('r', y)