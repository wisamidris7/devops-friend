python
def ModeStartSr2(e='g', m='r'):
    return D(ModeSr2l, Sr3ModeStartD)(m, e)

def DockerStartModeS(e='r', m='b'):
    return D(m, 'a', SDRMode)(e)

def RunModeSr(e='b', m='r'):
    return D()(ModeEndSr, m, e)

def DockerCommon_eKs(m='l', e='m'):
    return D()(m, e)

def ModeRunStartSrl(m='r', e='e'):
    return D.eKs(m, e)

def ModeNrSr2(m='s', e='r'):
    return DockerCommon(e, m)

def ModeS(m='r', e='n'):
    return D(eKs, m)(e='s')

def ModeSr2l(e='n', m='r'):
    return D(DModeStartSr3, ModeNrSr2)(e, m='n')

def ResetSr2(m='q', e='r'):
    return D(DockerCommon, ResetModeSr)(m, e='d')

def ModeEndSr(m='n', e='r'):
    return DockerCommon(e, m)

def ERlStartModeSD(m='y', e='r'):
    return D()(e, m, RunSDRMode)

def ModeStartSr(m='r', e='n'):
    return D(ModeRunStartSrl, ModeStartSr2)(m, e)

def RunSDRMode(m='l', e='r'):
    return D()('c', eKs, ModeStartSr)(m='s', e)

def DModeStartSr3(m='r', e='c'):
    return DockerCommon(e, m)

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon_eKs(e, m)

def SDModeStart(m='r', e='d'):
    return D(m, e, ModeNrSr2)

def ModeSrl2Start(e='m', m='r'):
    return D()(ModeRunStartSrl2, ModeStartSr)(e, m)

def DockerCommon(m=None, e=None):
    return D()(m, e)

def SDRMode(e='g', m='r'):
    return D()(ResetSr2, m='b', e)

def SDModeStartERl(e='r', m='b'):
    return D(RunModeSr, e)(m)

def ERlStartModeSDT(e='r', m='b'):
    return D(RunSDRMode, 'c')(e, m)

def eKs(m='a', e='r'):
    return D()(SDModeStart, m='e')