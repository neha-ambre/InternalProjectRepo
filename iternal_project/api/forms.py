from django import forms
from .models import AutisticData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field,Div,Submit,Layout,Row,Column
from crispy_forms.bootstrap import InlineRadios,FormActions,Tab,TabHolder

class DataForm(forms.Form):
    name=forms.CharField(max_length=50)
    address=forms.CharField(max_length=1000)
    gender=forms.ChoiceField(choices=[('male','Male'),('female','Female'),('other','Other')],widget=forms.RadioSelect,initial='male')
    refferedby=forms.CharField(required=False)
    
    # Birth history
    birthDate=forms.DateField()
    birthWeight=forms.IntegerField()
    term=forms.ChoiceField(choices=[('fullterm','Fullterm'),('preterm','Preterm')],widget=forms.RadioSelect,initial='preterm')
    delivery=forms.ChoiceField(choices=[('normal','Normal'),('lscs','LSCS'),('foreceps','Foreceps')],widget=forms.RadioSelect,initial='normal')
    deliveryDetails=forms.CharField(max_length=1000)
    consanguinity=forms.ChoiceField(choices=[('present','Present'),('absesnt','Absent')],widget=forms.RadioSelect,initial='absent')
    perninantalEvents=forms.ChoiceField(choices=[('fullterm','Fullterm'),('preterm','Preterm')],widget=forms.RadioSelect,initial='preterm')
    perninantalEventsDetails=forms.CharField(max_length=1000)
    term=forms.ChoiceField(choices=[('fullterm','Fullterm'),('preterm','Preterm')],widget=forms.RadioSelect,initial='preterm')
    treatment=forms.ChoiceField(choices=[('treatment','Treatment'),('intubation','Intubation at birth'),('required oxygen support','Required oxygen support'),('ventilator','Ventilator'),('required surfactant','Required Surfactant'),('ionotropic Supprot','Ionotropic Supprot')])
    
    # class Meta:
    #     model=AutisticData
    #     fields="__all__"
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_method='post'
        self.helper.form_action='saveForm'
        # self.helper.add_input(Submit('save_customer','Submit'))
        # self.helper.add_input(Submit('cancel','Cancel',css_class='btn btn-danger'))
        
        # self.helper.layout=Layout(
        #     TabHolder(
        #     Tab('Personal Details',
        #         Div(
        #             Row(
        #         Column('name')
        #     ),
        #     Row(
        #         Column('address')
        #     ),
        #     InlineRadios('gender'),
        #     'refferedby',css_class='justify-content-center'
        #             )
        #         ,css_class='justify-content-center outer'
        #     ),
        #     Tab('Second Tab'
                
        #     )
        #     ),
        #     FormActions(
        #         Submit('save_customer','Submit'),
        #         Submit('cancel','Cancel',css_class='btn btn-danger')
        #     )
            
        # )
        