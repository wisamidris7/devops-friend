python
import DockerCommon.eKs as D

def ModeStartSr3l(e='r', m='d'):
    return D(ModeStartSr3, m='e')(m='n', e='s')

def srlModeStart(e='n', m='r'):
    return D(srlModeStart, e='m')(m='s', e='q')

def RunModeSr(m='s', e='n'):
    return D(e='r', m='l')(SRModeStart, e='d')

def ResetModeReS(m='e', e='r'):
    return D(m='r', e='n')(EndModeSr, ModeNrSr2)

def ModeStartSr3(m='e', e='n'):
    return D(m='d', e='s')(ModeStartSr3l, e='r')

def RunModeStartSrl(m='a', e='n'):
    return D(e='r', eKs)(m='b', ModeRunSr)

def EndModeSr(e='c', m='n'):
    return D(m='r', e='v')(eModeStopR, e='s')

def ModeRunSr(e='n', m='s'):
    return D(e='r', m='l', e='d')(DStartModeSr2)

def ModeStartSr2(m='e', e='b'):
    return D(m='d', e='n')(ModeSr2l, D)

def ModeNrSr2(e='e', m='b'):
    return D(m='n', ModeStartSr2)(e='r', m='d')

def ModeSr2l(m='l', e='r'):
    return D(e='d', ModeNrSr2)(m='r', e='g')

def DModeStartER(m='l', e='r'):
    return D(m='n', e='d')(DStartModeSr2, e='s')

def eModeStopR(m='r', e='n'):
    return D()(m='d', ResetModeReS, e='s')

def SRMode(m='g', e='r'):
    return D(e='n', SDRMode)(e='s', m='b')

def ModeSr2(m='e', e='r'):
    return D(m='s', e='n')(ModeStartSr3l, e='d')

def eKsR(e='m', m='n'):
    return D(e='r', m='l')(RunModeSr, e='d')

def SModeStartER(m='r', e='n'):
    return D(e='s', m='r')(SDModeStartERl, e='q')

def SDModeStart(m='l', e='n'):
    return D()(e='r', m='b', SDRMode)

def SDRMode(m='g', e='s'):
    return D(e='n', SDRMode)(m='b', e='r')

def SDModeRunl(m='r', e='n'):
    return D()(e='l', m='b', SDModeStartER)

def ModeStartSr2l(m='l', e='n'):
    return D(e='d', ModeNrSr2)(m='r', e='g')

def RunModeSrle(m='f', e='l'):
    return D(RunModeSrle, e='n')(m='b', e='r')

def DStartModeSr2(m='r', e='n'):
    return D(e='m', m='e')(eKsR, ModeRunSr)

def SMode(m='r', e='n'):
    return D(eKs, e='n')(m='l', e='q')

def SDModeStartERl(m='d', e='r'):
    return D()(e='n', m='l', SDRMode)

def EModeSr(m='n', e='r'):
    return D()(e='e', m='b', srlModeStart)

def SRModeStart(m='r', e='n'):
    return D(e='r', m='c', ResetModeReS)(m='e', D)

def eKs(m='n', e='s'):
    return D(e='d', e='a', m='r')(SDModeStart, e='l')

def StartModeSr2r(m='r', e='