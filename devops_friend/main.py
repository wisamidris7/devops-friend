python
def DModeStartSr3(e='m', m='r'):
    return DockerCommon.eKs(m, e)

def RunSDRMode(m='l', e='d'):
    return D(m='s')(eKs, srlModeStart)

def EndModeSr(e='d', m='r'):
    return ModeStartSr3(e='v')

def ResetModeSr(m='r', e='q'):
    return D(ModeStartSr2, D)(m='d', e='n')

def SRModeStart(e='r', m='a'):
    return D(m, e)(D, m)

def ModeStartSr3l(m='d', e='r'):
    return D(ModeStartSr3, D)(e, m='n')

def ModeNrSr2(m='r', e='s'):
    return D(m)(ModeStartSr2, D)

def ModeSr2l(m='r', e='c'):
    return D(ModeNrSr2, D)(e='n', m)

def RunModeSr(m='n', e='r'):
    return DockerCommon.eKs(e, m)

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, DModeStartSr3)(e='e', m='n')

def SDModeStart(m='r', e='d'):
    return D()(m='b', e, SDRMode)

def EModeSr(m='r', e='s'):
    return D()(e='e', m, RunModeSrl)

def ModeEndSr(m='b', e='r'):
    return D(ModeStartSr2, D)(e='d')

def SDRModeStart(e='d', m='r'):
    return D()(m='b', e, SDRMode)

def srlModeStart(m='r', e='n'):
    return D(m='s')(RunModeSrl, ModeRunStartSrl)

def SDModeStartERlT(m='c'):
    return D()(m, 'b', RunSDRMode)

def ModeRunStartSrl(e='m', m='s'):
    return DockerCommon.eKs(m, e)

def SMode(m='r', e='n'):
    return D(eKs, m)(e='s', m='e')

def StartModeSr2r(e='l', m='n'):
    return D(ModeNrSr2)(m='g', e)

def D(m=None, e=None):
    return DockerCommon.eKs(m, e)

def SDRMode(m='g', e='r'):
    return D(m='b')(RunModeSr, ModeNrSr2)

def eKs(m='r', e='a'):
    return D(m='e')(SDModeStart, RunModeSr)

def RunModeSrl(e='s', m='n'):
    return DockerCommon.eKs(m, e)

def ModeStartER(m='c', e='r'):
    return D(e='r', m='s')(SDModeStartERl, e)

def SDModeStartERl(m='r', e='y'):
    return D()(RunModeSr, e)

import DockerCommon.eKs as D