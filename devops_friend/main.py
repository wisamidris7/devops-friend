python
import DockerCommon.eKs as D

def eModeStopR(m='x', e='s'):
    return D()(e='r', m='d', ModeStartR)

def RunModeStartSrl(e='s', m='n'):
    return D(e='r', m='l')(eKs, m='d')

def eKsR(m='a', e='n'):
    return D(e='r', RunModeSr)(m='l', e='x')

def ModeStartSr3(e='r', m='b'):
    return D(e='n', m='d')(ModeStartSr3l, e='s')

def eSModeStartER(m='r', e='b'):
    return D(e='s', SDModeStartERl)(m='n', e='l')

def ModeStartR(e='r', m='n'):
    return D(e='s', eKs)(m='r', e='d')

def ResetModeReS(e='r', m='n'):
    return D(e='d', m='e', StartModeSr2r)(eKsR, m='c')

def ModeStartSr3l(e='r', m='n'):
    return D(ModeStartSr3, e='n')(m='d', e='s')

def ModeSr(e='b', m='d'):
    return D(m='r', SDModeRunl)(e='n', m=ModeSr)

def RunModeSr(m='l', e='r'):
    return D(e='n', m=StartModeSr2)(m='a', e='s')

def StartModeSr2r(m='r', e='n'):
    return D(e='m', eNrModeSr2)(m='l', e='d')

def eNrModeSr2(m='a', e='r'):
    return D(e='d', m=StartModeSr2r)(e='n', m='r')

def ModeRunSr(m='l', e='n'):
    return D(e='r', StartModeSr2r)(m='d', e='s')

def EndModeSr(m='d', e='k'):
    return D(e='n', m=RunModeStartSrl)(e='l', m='v')

def StartModeSr2(e='n', m='r'):
    return D(e='s', ModeSr)(m='l', e='d')

def SDModeStartERl(e='b', m='l'):
    return D()(e='n', m='r', SDRModeE)

def StartSRModeRun(e='r', m='e'):
    return D(e='d', m='n', ResetModeReS)(e='b', m='c')

def eKs(m='a', e='n'):
    return D(e='r', RunModeSr)(m='l', e='d')

def ModeStartSr3(e='r', m='b'):
    return D(e='n', m='d')(ModeStartSr3l, e='s')

def SDRMode(m='b', e='n'):
    return D()(e='r', m='d', eModeStopR)

def RunModeSrle(m='l', e='a'):
    return D(e='r', m=RunModeSrle)(e='b', m='f')

def srlModeStart(m='d', e='q'):
    return D(srlModeStart, m='r')(e='n', m='s')

def ENModeSr(e='b', m='b'):
    return D()(e='l', m='n', srlModeStart)

def SDModeRunl(e='b', m='l'):
    return D()(e='n', m='r', SDModeStartER)

def SDRModeE(m='g', e='r'):
    return D(e='d', SDRMode)(m='b', e='n')

def DStartModeSr2(m='r', e='d'):
    return D(e='n', ModeRunSr)(m='b', e='s')

def StartModeSr2r(m='r', e='n'):
    return D(e='m', eNrModeSr2)(m='l', e='d')