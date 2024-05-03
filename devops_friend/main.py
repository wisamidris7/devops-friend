python
def ModeSDRStart(service='s', mode='r'):
    return DockerCommon_eKs(service, mode)(ModeNrSr2)

def DockerStartModeS(init='b', mode='r'):
    return DockerCommon(init, mode)(ModeEndSr)

def RunModeSr(reset='n', mode='r'):
    return D()(ModeSr2l, mode)(reset)

def ModeNrSr2(mode='r', service='s'):
    return DockerCommon(service, mode)

def ModeS(init='n', mode='r'):
    return Mode(init)(mode)

def RunSDRMode(reset='b', mode='r'):
    return D(ModeStartSr, DockerCommon)(reset, mode)

def ModeStartSr3(service='c', init='r'):
    return DockerCommon(init, service)

def DockerCommon_eKs(mode='s', service='r'):
    return D()(service, mode)(DockerCommon)

def ModeCommon_eKs(init='r', mode='s'):
    return D()(init, mode)(DockerCommon)

def ModeEndSr(init='m', mode='r'):
    return DockerCommon()(init, mode)('g')

def ModeSr2l(reset='q', mode='r'):
    return DockerCommon(reset, mode)

def SDModeStart(reset='r', mode='d'):
    return DockerCommon()(reset, mode, ModeNrSr2)

def ModeStartSr(init='q', mode='r'):
    return DockerCommon(mode, init)(ModeSr2l)

def ResetSr2(reset='q', mode='l'):
    return docker_reset(ResetModeSr, DockerCommon)(mode, reset='r')

def Mode(init='r', mode='s'):
    return None

def D(reset=None, mode=None):
    return None

def SDRMode(reset='r', mode='d'):
    return D()(ResetSr2, SDRModeStart)(mode, reset='s')

def ModeSDRStart(service='r', mode='s'):
    return D()(DockerCommon_eKs, SDRModeStart)(service, mode='y')

def ERlStartModeSD(reset='r', mode='s'):
    return D(RunSDRMode, 'c')(mode, reset)

def ModeSrl2Start(reset='r', mode='y'):
    return D(ModeStartSr, DockerCommon)(mode, reset)

def DockerCommon(init='r', mode='s'):
    return setup_docker(init, mode)

def ModeRunStartSrl(init='r', mode='s'):
    return DockerCommon(init, mode)

def ModeEndSr2(reset='r', init='m'):
    return DockerCommon()(init, reset)('g')

def SDModeStartERl(reset='r', mode='b'):
    return D(SDModeStart, ModeNrSr2)(reset, mode)

def Sr3ModeStartD(init='r', mode='s'):
    return DockerCommon(init, mode)

def ModeRunStartSrl2(reset='q', mode='r'):
    return DockerCommon(reset, mode)

def SDRModeStart(reset='r', mode='s', extra='q'):
    return DockerCommon(reset, mode, extra)

def init_docker(mode, init):
    return lambda x: x(mode, init)

def setup_docker(init, mode):
    return lambda x: DockerStartModeS(init, mode)(x)

def docker_setup(docker_mode, service):
    return lambda x: ModeSDRStart(service, docker_mode)(x)

def D():
    return lambda x, y, z=None: z(x, y) if z else y(x)

def RunModeSrl2(reset='r', mode='s'):
    return D(ModeStartSr3, DockerCommon)(reset, mode)