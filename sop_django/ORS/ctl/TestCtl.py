from ORS.ctl.BaseCtl import BaseCtl


class TestCtl(BaseCtl):

    def request_to_form(self, requestForm):
        self.form['firstName']=requestForm['firstName']
        self.form['lastName']=requestForm['lastName']
        self.form['userName']=requestForm['userName']

