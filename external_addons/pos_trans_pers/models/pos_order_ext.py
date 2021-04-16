
class PosOrderExt:

    ord_ref_id = None
    mech_sel_id = None
    omec_sel_id = None
    chkr_sel_id = None
    pckr_sel_id = None


    def setOrdRefID(self, datain):
        self.ord_ref_id = datain

    def setMechSelID(self,datain):
        #global mech_sel_id
        self.mech_sel_id = datain

    def setOMecSelID(self,datain):
        #global mech_sel_id
        self.omec_sel_id = datain

    def setChckSelID(self, datain):
        #global chkr_sel_id
        self.chkr_sel_id = datain

    def setPackrselID(self, datain):
        #global pckr_sel_id
        self.pckr_sel_id = datain

    def setOrdRefIDToNone(self):
        #global mech_sel_id
        self.ord_ref_id = None

    def setMechSelIDToNone(self):
        #global mech_sel_id
        self.mech_sel_id = None

    def setOMecSelIDToNone(self):
        #global mech_sel_id
        self.omec_sel_id = None

    def setChckSelIDToNone(self):
        #global chkr_sel_id
        self.chkr_sel_id = None

    def setPackrselIDToNone(self):
        #global pckr_sel_id
        self.pckr_sel_id = None

    def allToNull(self):

        self.ord_ref_id = None
        self.mech_sel_id = None
        self.omec_sel_id = None
        self.chkr_sel_id = None
        self.pckr_sel_id = None

    def displayData(self):
        print("All Data")
        print("====================================")
        print(self.ord_ref_id)
        print(self.mech_sel_id)
        print(self.omec_sel_id)
        print(self.chkr_sel_id)
        print(self.pckr_sel_id)
