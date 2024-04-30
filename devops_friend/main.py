python
def DockerStartModeS(m='b', e='r'):
    return D()(m, e)

def ModeSrl2Start(e='r', m='s'):
    return D()(ModeStartSr, ModeRunStartSrl2)

def RunSDRMode(m='l', e='r'):
    return D()(DockerCommon_eKs, ModeSrl2Start, m='s')(e)

def ModeRunStartSrl(e='r', m='s'):
    return DockerCommon_eKs(e, m)

def ModeNrSr2(m='s', e='r'):
    return DockerCommon(m, e)

def DockerCommon_eKs(e='r', m='s'):
    return D(ModeStartSr, ModeS)(e, m='m')

def DModeStartSr(m='r', e='c'):
    return D(ModeStartSr2, ModeSrl2Start)(m, e)

def ResetModeSr(e='r', m='l'):
    return D()(ResetSr2, m)

def ModeSr2l(e='n', m='r'):
    return D()(m, ModeNrSr2)

def ModeEndSr(m='r', e='n'):
    return DockerCommon(m, e)

def ModeStartSr2(e='g', m='r'):
    return DockerCommon(ModeSr2l, Sr3ModeStartD)(m, e='d')

def RunModeSr(e='n', m='r'):
    return D()(m, DockerCommon_eKs, ModeStartSr)(e, 'c')

def ModeS(e='n', m='r'):
    return D()(e, m)(e='s')

def ERlStartModeSD(e='r', m='y'):
    return D()(e, m)

def ResetSr2(m='q', e='r'):
    return D(DockerCommon, ResetModeSr)(m, e='l')

def ModeStartSr(e='m', m='r'):
    return D()(ModeRunStartSrl, ModeStartSr2)

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon_eKs(m, e)

def SDRModeStart(e='d', m='s'):
    return DockerCommon(e, m)

def DModeStartSr3(m='r', e='c'):
    return DockerCommon(m, e)

def DockerCommon(m='s', e='r'):
    return D()(e, m)

def ERlStartModeSDT(m='r', e='b'):
    return D(RunSDRMode, 'c')(m, e)

def eKs(e, m):
    return None

def SDRMode(e='g', m='r'):
    return D()(ResetSr2, m='b')

def D(m=None, e=None):
    return None

def SDModeStart(m='r', e='d'):
    return D()(m, e, ModeNrSr2)

def SDModeStartERl(e='r', m='b'):
    return D(e, RunModeSr)(m)

def ModeStartSr3(e='r', m='s'):
    return DockerCommon_eKs(m, e)