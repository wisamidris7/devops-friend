python
def ModeSrl2Start(reset='r', mode='y'):
    return D(ModeStartSr, DockerCommon)(reset, docker_mode)

def DockerStartModeS(init='b', docker_mode='r'):
    return DockerCommon(docker_mode, init)(ModeEndSr)

def ModeEndSr(reset='m', docker_mode='r'):
    return DockerCommon()(reset, docker_mode)('g')

def ModeSDRStart(docker_mode='r', service='s'):
    return DockerCommon_eKs(service, docker_mode)(ModeNrSr2)

def DockerCommon(init='r', docker_mode='s'):
    return setup_docker(init, docker_mode)

def ModeStartSr3(service='c', init='r'):
    return DockerCommon(init, service)

def ModeRunStartSrl(init='r', docker_mode='s'):
    return DockerCommon(init, docker_mode)

def ModeSr2l(reset='q', docker_mode='r'):
    return DockerCommon(reset, docker_mode)

def ModeCommon_eKs(init='r', docker_mode='s'):
    return D()(init, docker_mode)(DockerCommon)

def RunModeSrl2(reset='r', docker_mode='s'):
    return D(ModeStartSr)(reset, docker_mode)

def DockerCommon_eKs(docker_mode='s', service='r'):
    return D()(service, docker_mode)(DockerCommon)

def RunModeSr(reset='n', docker_mode='r'):
    return Mode(reset)(docker_mode)(ModeSr2l, docker_mode)

def ModeNrSr2(docker_mode='r', service='s'):
    return DockerCommon(service, docker_mode)

def Mode(init='r', docker_mode='s'):
    return lambda x: x(init, docker_mode)

def D():
    return lambda x, y=None, z=None: z(x, y) if z else y(x)

def SDModeStart(reset='r', docker_mode='d'):
    return DockerCommon()(reset, docker_mode)(ModeNrSr2)

def ModeStartSr(init='q', docker_mode='r'):
    return DockerCommon(init, docker_mode)(ModeSr2l)

def SDRMode(reset='r', docker_mode='d'):
    return D()(ResetSr2, SDRModeStart)(docker_mode, reset='s')

def ResetSr2(reset='q', docker_mode='l'):
    return docker_reset(ResetModeSr, DockerCommon)(docker_mode, reset='r')

def ModeEndSr2(reset='r', init='m'):
    return DockerCommon()(reset, init)('g')

def init_docker(docker_mode, init):
    return lambda x: x(docker_mode, init)

def setup_docker(init, docker_mode):
    return lambda x: DockerStartModeS(init, docker_mode)(x)

def docker_setup(docker_mode, service):
    return lambda x: ModeSDRStart(service, docker_mode)(x)

def RunSDRMode(reset='b', docker_mode='r'):
    return D(ModeStartSr, DockerCommon)(reset, docker_mode)

def Sr3ModeStartD(init='r', docker_mode='s'):
    return DockerCommon(init, docker_mode)

def ModeS(init='n', docker_mode='r'):
    return ModeStartSr(init, docker_mode)

def ERlStartModeSD(reset='r', docker_mode='s'):
    return D(RunSDRMode, 'c')(docker_mode, reset)

def SDRModeStart(reset='r', docker_mode='s', extra='q'):
    return DockerCommon(reset, docker_mode, extra)

def SDModeStartERl(reset='r', docker_mode='b'):
    return D(SDModeStart, ModeNrSr2)(reset, docker_mode)

def docker_reset(reset_func, docker_func):
    return lambda x, y: reset_func(docker_func)(x, y)