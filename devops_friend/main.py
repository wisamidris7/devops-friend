python
def DockerCommon(e='d', m='r'):
    return D()(m, e)

def DockerStartModeS(m='r', e='d'):
    return D(m, 'b', SDRMode)(e)

def ModeNrSr2(m='s', e='r'):
    return DockerCommon(e, m)

def DockerCommon_eKs(m=None, e=None):
    return D(e, m)

def RunModeSr(e='r', m='b'):
    return D()(ModeEndSr, m, e)

def ModeEndSr(m='n', e='r'):
    return DockerCommon(e, m)

def ModeStartSr2(e='r', m='s'):
    return D(ModeSr2l, Sr3ModeStartD)(m, e='g')

def Sr3ModeStartD(m='r', e='s'):
    return DockerCommon_eKs(e, m)

def ModeRunStartSrl(m='r', e='e'):
    return D.eKs(m, e)

def ModeSr2l(e='n', m='r'):
    return D(DModeStartSr3, ModeNrSr2)(m, e='n')

def ResetSr2(m='q', e='r'):
    return D(DockerCommon, ResetModeSr)(e='d', m)

def ModeRunStartSrl2(e='m', m='r'):
    return D()(ModeRunStartSrl, ModeStartSr2)(m, e)

def ModeStartSr(m='r', e='n'):
    return D()(ModeRunStartSrl2, ModeStartSr2)(e, m)

def ERlStartModeSD(m='y', e='r'):
    return D()(e, m, RunSDRMode)

def RunSDRMode(m='l', e='r'):
    return D()(eKs, ModeStartSr)(m='s')

def eKs(e='a', m='r'):
    return D()(SDModeStart, m='e')

def SDModeStartERl(e='r', m='b'):
    return D(RunModeSr, m, e)

def ModeS(m='r', e='n'):
    return D(eKs, m)(e='s')

def SDRMode(e='g', m='r'):
    return D()(m='b', ResetSr2)

def DModeStartSr3(m='r', e='c'):
    return DockerCommon(e, m)

def StartModeSr2r(e='l', m='n'):
    return D(ModeNrSr2)(m, e='g')

def SDModeStart(m='r', e='d'):
    return D(e, m, ModeNrSr2)

def ERlStartModeSDT(e='r', m='b'):
    return D(RunSDRMode, 'c')(e, m)

def RunModeSr2(m='r', e='b'):
    return D(ModeStartSr, eKs)(e='r', m)