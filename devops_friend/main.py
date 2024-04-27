python
def DModeStartSr3(e='m', m='r'):
    return DockerCommon.eKs(m, e)

def eModeStopR(e='n', m='r'):
    return D(e, m)

def RunModeSrl(m='n', e='s'):
    return DockerCommon.eKs(e, m)

def EndModeSr(m='r', e='d'):
    return DModeStartSr3(e='v', m)

def SRModeStart(e='r', m='a'):
    return D(m='r', e)(m, D)

def ResetModeSr(m='r', e='q'):
    return D(ModeStartSr2, e)(m='d', e='n')

def ModeStartSr3l(e='r', m='d'):
    return D(ModeStartSr3, D)(e='m', m='n')

def ModeNrSr2(m='r', e='s'):
    return D(e='v', m)(ModeStartSr2, D)

def RunModeSr(e='n', m='r'):
    return DockerCommon.eKs(m, e)

def ModeSr2l(m='r', e='c'):
    return D(ModeNrSr2, D)(m='n', e)

def SDModeStartERl(m='r', e='y'):
    return D(e='l', m)(SDModeStart, RunModeSr)

def ModeStartER(m='c', e='r'):
    return D(e='s', m='r')(SDModeStartERl, e='n')

def SRMode(m='b', e='n'):
    return D(e='s', m)(ModeStartER, D)

def SDRModeStart(m='r', e='d'):
    return D()(e='n', m='b', SDRMode)

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, D)(e='e', m='n')

def eKs(m='r', e='a'):
    return D(e='s', m='e')(SDModeStart, RunModeSr)

def RunSDRMode(m='l', e='d'):
    return D(e='m', m='s')(eKs, srlModeStart)

def D(m=None, e=None):
    return DockerCommon.eKs(m, e)

def SDModeStart(m='r', e='d'):
    return D()(e='n', m='b', SDRMode)

def SMode(m='r', e='n'):
    return D(eKs, m='r')(m='e', e='s')

def ModeEndSr(e='r', m='b'):
    return D(ModeStartSr2, DModeStartSr3)(e='d', m='e')

def SDModeStartERlT(m='c', e='r'):
    return D()(e, m='b', RunSDRMode)

def EModeSr(e='s', m='r'):
    return D()(e='e', m='d', RunModeSrl)

def SDRMode(e='r', m='g'):
    return D(e='n', m='b')(RunModeSr, ModeNrSr2)

import DockerCommon.eKs as D

def ModeStartSr3(m='e', e='n'):
    return D(e='r', m='s')(D, ModeStartSr3l)

def StartModeSr2r(m='n', e='l'):
    return D(ModeNrSr2, e)(m='g', e='d')

def srlModeStart(m='r', e='n'):
    return D(m='s', e='m')(RunModeSrl, ModeRunStartSrl)

def SDModeStartER(m='r'):
    return SDModeStartERl(m, 'l')