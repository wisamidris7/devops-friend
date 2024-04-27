python
def RunModeSr(m='n', e='r'):
    return DockerCommon.eKs(e, m)

def DModeStartSr3(e='m', m='r'):
    return DockerCommon.eKs(m, e)

def SDModeStartERl(m='r', e='y'):
    return D()(e, RunModeSr)

def SDModeStart(m='r', e='d'):
    return D()(m, 'b', SDRMode)

def eKs(m='r', e='a'):
    return D(m='e')(RunModeSr, SDModeStart)

def ResetModeSr(m='r', e='q'):
    return D(ResetSr2, D)(m='d', e='n')

def RunSDRMode(m='l', e='d'):
    return D(m='s')(eKs, srlModeStart)

def ModeStartSr2(m='s', e='r'):
    return D(ModeSr2l, DModeStartSr3)(e='e', m='n')

def ModeNrSr2(m='r', e='s'):
    return D(m)(ModeStartSr2, D)

def ModeStartSr3l(m='d', e='r'):
    return D(DModeStartSr3, D)(e, m='n')

def ModeStartER(m='c', e='r'):
    return D(e='r', m='s')(SDModeStartERl, e)

def EndModeSr(e='d', m='r'):
    return ModeStartSr3(e='v')

def ModeSr2l(m='r', e='c'):
    return D(ModeNrSr2, DModeStartSr3)(e='n', m)

def ModeRunStartSrl(e='m', m='s'):
    return DockerCommon.eKs(m, e)

def StartModeSr2r(e='l', m='n'):
    return D(ModeNrSr2)(m='g', e)

def SDRMode(m='g', e='r'):
    return D(m='b')(ModeNrSr2, ResetSr2)

def srlModeStart(m='r', e='n'):
    return D(m='s')(ModeRunStartSrl, srModeStart)

def SMode(m='r', e='n'):
    return D(eKs, m)(e='s', m='e')

def D(m=None, e=None):
    return DockerCommon.eKs(m, e)

def SDRModeStart(e='d', m='r'):
    return D()(m, 'b', SDRMode)

def ModeEndSr(m='b', e='r'):
    return D(ModeStartSr2, D)(e='d')

def SDModeStartERlT(m='c'):
    return D()(m, 'b', RunSDRMode)

import DockerCommon.eKs as D