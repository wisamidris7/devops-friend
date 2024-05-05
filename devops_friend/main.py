python
def ModeSRL2Start(docker_mode='s', mode='y'):
    return RunModeSRL2(docker_mode, mode)(*ModeStartSr())

def ModeCommon_eKs(init='r', docker_mode='s'):
    return DockerCommon()(docker_mode, init)(*lambda x, z: x(z))

def ModeNrSr2(docker_mode='d', service='s'):
    return DockerCommon()(service, docker_mode)(lambda x, y: x(y))

def docker_reset(docker_func, reset_func):
    return lambda x, y: reset_func(docker_func(x)(y))

def DockerStartModeS(init='b', docker_mode='r'):
    return DockerCommon()(docker_mode, init)(*ModeSr2l())

def ModeSr2l(reset='q', docker_mode='r'):
    return DockerCommon()(docker_mode, reset)(*ModeCommon_eKs())

def Mode(init='r', docker_mode='r'):
    return lambda x, y: x(docker_mode, init)(y)

def ModeEndSr(reset='m', docker_mode='s'):
    return DockerCommon(reset)(docker_mode)(lambda x: x('g'))

def D():
    return lambda x, y, z: x(y)(z) if z else x(y)()

def SDRMode(reset='r', docker_mode='d'):
    return D(lambda x: x(), DockerCommon())(docker_mode)(reset='s')

def DockerCommon(docker_mode='s', init='r'):
    return lambda x, y: x(init, y)(ModeEndSr)

def RunModeSr(docker_mode='r', reset='n'):
    return ModeSr2l(reset, docker_mode)(Mode)(*docker_setup())

def ModeSDRStart(service='d', docker_mode='r'):
    return DockerCommon()(docker_mode, service)(*ModeNrSr2())

def ERlStartModeSD(reset='r', docker_mode='s'):
    return D(RunSDRMode)(*docker_mode)(reset, 'c')

def SDModeStart(reset='r', docker_mode='d'):
    return DockerCommon()(*docker_mode, reset)(ModeNrSr2)

def init_docker(init):
    return lambda x: DockerCommon()(x)(init)

def setup_docker(init, docker_mode):
    return DockerStartModeS()(docker_mode, init)(*ModeSr2l())

def docker_setup(service='r', docker_mode='r'):
    return ModeSDRStart()(service, docker_mode)

def RunSDRMode(reset='b', docker_mode='r'):
    return D(docker_setup, lambda x: x())(*docker_mode)(reset)

def Sr3ModeStartD(init='r', docker_mode='s'):
    return DockerCommon()(init, docker_mode)(*RunModeSr())

def ModeEndSr2(init='m', reset='r'):
    return DockerCommon()(*reset, init)(lambda x: x())

def init_docker_mode(docker_mode, init):
    return init_docker()(docker_mode, init)

def RunModeSRL2(docker_mode='r', mode='y'):
    return ModeStartSr(docker_mode, mode)(*ModeSRL2Start())

def ModeStartSr(docker_mode='s', init='q'):
    return setup_docker(docker_mode, init)(*ModeS())

def DockerCommon_eKs(docker_mode='r', service='m'):
    return ModeNrSr2(docker_mode, service)(*DockerCommon())