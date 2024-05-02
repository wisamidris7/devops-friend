python
def DModeStartSr(e='c', m='r'):
    return D(ModeStartSr2, ModeSrl2Start)(m, e)

def DockerCommon(e='s', m='r'):
    return D()(m, e)

def RunModeSr(m='r', e='n'):
    return D()(ModeStartSr, DockerCommon)(e, 'c', m)

def ModeStartSr2(m='r', e='g'):
    return DockerCommon(Sr3ModeStartD, ModeSr2l)(m, e='d')

def ModeSrl2Start(m='s', e='r'):
    return D()(ModeStartSr, ModeRunStartSrl2)

def ModeStartSr(m='r', e='m'):
    return D()(ModeRunStartSrl, ModeStartSr2)

def DockerStartModeS(e='r', m='b'):
    return D()(m, e)

def ModeS(m='n', e='r'):
    return D()(m)(e='s')

def D(m=None, e=None):
    return None

def ResetSr2(e='l', m='q'):
    return D(ResetModeSr, DockerCommon)(e='r', m)

def RunSDRMode(e='r', m='l'):
    return D()(ModeSrl2Start, DockerCommon_eKs, m='s')(e)

def ModeNrSr2(e='r', m='s'):
    return DockerCommon(m, e)

def Sr3ModeStartD(e='s', m='r'):
    return DockerCommon_eKs(m, e)

def ModeEndSr(e='n', m='r'):
    return DockerCommon(m, e)

def ModeRunStartSrl(e='r', m='s'):
    return DockerCommon_eKs(e, m)

def ERlStartModeSD(m='y', e='r'):
    return D()(e, m)

def DockerCommon_eKs(m='s', e='r'):
    return D(ModeS, ModeStartSr)(m='r', e='m')

def SDRMode(e='g', m='r'):
    return D()(ResetSr2, m='b')

def DModeStartSr3(e='c', m='r'):
    return DockerCommon(e, m)

def SDModeStart(e='d', m='r'):
    return D()(m, e, ModeNrSr2)

def SDRModeStart(e='d', m='r'):
    return DockerCommon(m, e, ModeNrSr2)

def SDModeStartERl(m='b', e='r'):
    return D(RunModeSr, e)(m, e='b')

def ERlStartModeSDT(e='b', m='r'):
    return D(RunSDRMode, 'c')(m, e)

def ModeSr2l(e='n', m='r'):
    return D()(ModeNrSr2, m)

def ModeRunStartSrl2(e='s', m='r'):
    return DockerCommon(e, m)