from django.shortcuts import render
from ORS.utility.DataValidator import DataValidator
from service.service.TestService import TestService
from .BaseCtl import BaseCtl
from service.models import Test




class TestCtl(BaseCtl):



    def request_to_form(self, requestForm):
        self.form['id'] = requestForm['id']
        self.form['firstName'] = requestForm['firstName']
        self.form['lastName'] = requestForm['lastName']
        self.form['userName'] = requestForm['userName']

    def model_to_form(self, obj):
        if (obj==None):
            return
        self.form['id'] = obj.id
        self.form['firstName'] = obj.firstName
        self.form['lastName'] = obj.lastName
        self.form['userName'] = obj.userName


    def form_to_model(self, obj):

        pk = int(self.form['id'])
        if (pk>0):
            obj.id = pk
        obj.firstName = self.form['firstName']
        obj.lastName = self.form['lastName']
        obj.userName = self.form['userName']

        return obj

    def input_validation(self):
        super().input_validation()
        inputError = self.form['inputError']
        if (DataValidator.isNull(self.form['firstName'])):
            inputError['firstName'] = "First Name can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['firstName'])):
                inputError['firstName'] = "Name contains only letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['lastName'])):
            inputError['lastName'] = "Last name can not be null"
            self.form['error'] = True
        else:
            if (DataValidator.isalphacehck(self.form['lastName'])):
                inputError['lastName'] = "Name contains only letters"
                self.form['error'] = True

        if (DataValidator.isNull(self.form['userName'])):
            inputError['userName'] = "userName can not be null"
            self.form['error'] = True

        return self.form['error']

    def display(self, request, params={}):
        if (params['id']>0):
            id = params['id']
            r = self.get_service().get(id)
            self.model_to_form(r)
        res = render(request,self.get_template(),{'form':self.form})
        return res

    def submit(self, request, params={}):
        if (params['id']>0):
            pk = params['id']
            dup = self.get_service().get_model().objects.exclude(id=pk).filter(userName = self.form['userName'])
            if dup.count()>0:
                self.form['error'] = True
                self.form['messege'] = "User Name already exists"
                res = render(request,self.get_template(),{'form':self.form})
            else:
                r = self.form_to_model(Test())
                self.get_service().save(r)
                self.form['id'] = r.id

                self.form['error'] = False
                self.form['messege'] = "DATA HAS BEEN UPDATED SUCCESSFULLY"
                res = render(request,self.get_template(),{'form':self.form})
        else:
            duplicate = self.get_service().get_model().objects.filter(userName = self.form['userName'])
            if duplicate.count()>0:
                self.form['error'] = True
                self.form['messege'] = "User Name already exists"
                res = render(request,self.get_template(),{'form':self.form})
            else:
                r = self.form_to_model(Test())
                self.get_service().save(r)
                self.form['id'] = r.id

                self.form['error'] = False
                self.form['messege'] = "DATA HAS BEEN SAVED SUCCESSFULLY"
                res = render(request,self.get_template(),{'form':self.form})
        return res


    # Template html of Subject Page
    def get_template(self):
        return "Test.html"

    def get_service(self):
        return TestService()
