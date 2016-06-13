# -*- coding:utf-8 -*-
import util
import Upgrade_Group

class UpgradeGroupBuffer:
    """
    這個類別用來存一群 group buffer
    """
    def __init__(self):
        self.buffer = {}

    def append(self, UG):
        """
        Append an upgrade group into the buffer
        :param UG: the appended upgrade group
        :return: None
        """
        s = UG.getSubspace()
        id = util.getSubspaceUniqueID_numpy(s)
        if self.buffer.has_key(id):
            self.buffer[id].append(UG)
        else:
            tmpb = []
            tmpb.append(UG)
            self.buffer[id].append(tmpb)

