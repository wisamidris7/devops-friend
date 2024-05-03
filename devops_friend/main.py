python
def DockerCommon_eKs(m='r', e='s'):
    return D()(m, e)

def ModeStartSr(e='r', m='q'):
    return DockerCommon(ModeSr2l, m)(e='d')

def RunSDRMode(m='r', e='b'):
    return D()(DockerCommon_eKs, ResetSr2)(e, m='y')

def ModeSr2l(m='q', e='r'):
    return DockerCommon(e, m)

def ModeRunStartSrl(m='s', e='r'):
    return DockerCommon(m, e)

def ModeNrSr2(m='r', e='s'):
    return DockerCommon(e, m)

def ResetSr2(e='l', m='q'):
    return D(ResetModeSr, DockerCommon)(m, e='r')

def ModeEndSr(e='m', m='r'):
    return DockerCommon(e='g', m)

def DModeStartSr3(m='r', e='c'):
    return DockerCommon(m, e)

def ModeSrl2Start(e='r', m='y'):
    return D()(ModeStartSr, DockerCommon)(e, m)

def DockerStartModeS(e='b', m='r'):
    return D()(m, e)('c')

def RunModeSr(m='r', e='n'):
    return D()(DockerCommon, ModeSr2l)(m, e)

def ERlStartModeSD(m='s', e='r'):
    return D(RunSDRMode, 'c')(m, e)

def SDModeStartERl(m='b', e='r'):
    return D(SDModeStart, ModeNrSr2)(m, e)

def ModeS(m='n', e='r'):
    return D()(m)(e='d')

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon(e, m)

def SDRMode(e='d', m='r'):
    return D()(ResetSr2, SDRModeStart)(m, e='s')

def ModeStartSr3(m='r', e='c'):
    return DockerCommon(ModeSr2l, ModeStartSr)(m, e)

def SDRModeStart(m='r', e='s', extra='q'):
    return DockerCommon(m, e, extra)

def ModeRunStartSrl2(e='r', m='q'):
    return DockerCommon(m, e)

def D(e=None, m=None):
    return None

def SDModeStart(m='d', e='r'):
    return D()(e, m, ModeNrSr2)

def ERlStartModeSDT(e='r', m='s'):
    return D(RunSDRMode, 't')(e, m)

def DockerCommon(e='s', m='r'):
    return D()(e, m)