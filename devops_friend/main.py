python
def DockerStartModeS(e='r', m='b'):
    return D()(m, e)

def ModeNrSr2(m='r', e='s'):
    return D()(e, m)

def DockerCommon_eKs(m='s', e='r'):
    return DockerCommon(m, e)

def ModeS(m='n', e='r'):
    return D()(e)(m)

def RunModeSr(e='n', m='r'):
    return D()(ModeStartSr, DockerCommon)(m, e)

def ModeEndSr(e='m', m='r'):
    return DockerCommon(m, e='g')

def ModeStartSr(e='r', m='q'):
    return DockerCommon(ModeSr2l, m)(e='d')

def ModeSr2l(m='r', e='s'):
    return DockerCommon(e, m)

def ResetSr2(e='l', m='q'):
    return D(DockerCommon, ResetModeSr)(m, e='r')

def ModeSrl2Start(e='r', m='y'):
    return D()(ModeStartSr, DockerCommon)(m, e)

def ERlStartModeSD(m='r', e='s'):
    return D()(e, m)

def DModeStartSr3(m='r', e='c'):
    return DockerCommon(m, e)

def ModeRunStartSrl(m='s', e='r'):
    return DockerCommon_eKs(e, m)

def RunSDRMode(m='b', e='r'):
    return D()(ModeSrl2Start, DockerCommon_eKs)(m, e='s')

def DockerCommon(m='r', e='s'):
    return D()(e, m)

def SDModeStart(m='d', e='r'):
    return D()(m, e, ModeNrSr2)

def ModeStartSr2(e='c', m='r'):
    return DockerCommon(ModeRunStartSrl, ModeStartSr)(e, m)

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon(m, e)

def SDRMode(e='b', m='r'):
    return D()(ResetSr2, m='y')

def ERlStartModeSDT(e='r', m='s'):
    return D(RunSDRMode, 'c')(m, e)

def SDRModeStart(e='d', m='r'):
    return DockerCommon(m, e, ModeNrSr2)

def ModeRunStartSrl2(e='r', m='q'):
    return DockerCommon(e, m)

def SDModeStartERl(e='r', m='b'):
    return D(RunModeSr, e)(m, e='s')

def D(e=None, m=None):
    return None

def ModeStartSr3(e='c', m='r'):
    return DockerCommon(ModeSr2l, ModeStartSr)(e, m)