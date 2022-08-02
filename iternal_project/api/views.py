from django.shortcuts import redirect, render
from django.http import HttpResponse
from rest_framework.response import Response

from .serializers import AutisticDataSerializer
from django.core import serializers as sr
from django import template

from .models import AutisticData
import pandas as pd
from rest_framework.views import APIView
import pygsheets
import json


from google.oauth2 import service_account

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
  
# Create the Client
# Enter the name of the downloaded KEYS 
# file in service_account_file
client = pygsheets.authorize(service_account_file="./api/keys.json")
  
# opens a spreadsheet by its name/title
spreadsht = client.open("InternalProject autistic data records")
  
# opens a worksheet by its name/title
worksht = spreadsht.worksheet("title", "Sheet1")
  

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contactus(request):
    return render(request,'contact.html')

# def temp(request):
#     if request.method == 'POST':
#         firstName=request.POST.get('firstname')
#         address=request.POST.get('address')
#         refferedby=request.POST.get('refferedBy')
#         gender=request.POST.get('gender')
#         print(firstName,address,refferedby,gender)
#     return render(request,'FormTemp.html')


def login(request):
    return render(request,'Login.html')

def signUp(request):
    return render(request,'SignUp.html')

def temp(request):
    return render(request,'FormTemp.html')




# Task.update_state( 
#     state=0, 
#     meta={'current': "current", 'total': "total"} 
# )



def saveForm(request):
    if request.method == 'POST':
        name=request.POST.get('personName')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        if(gender==None):
            gender=''
        refferedby=request.POST.get('refferedby')
        referredBy_phone=request.POST.get('referredBy_phone')
        
        birthDate=request.POST.get('birthDate')
        birthWeight=request.POST.get('birthWeight')
        if(birthWeight==''):
            birthWeight=0
        term=request.POST.get('term')
        if(term==None):
            term=''
        preterm_weeks=request.POST.get('preterm_weeks')
        delivery=request.POST.get('delivery')
        if(delivery==None):
            delivery=''
        deliveryDetails=request.POST.get('deliveryDetails')
        if(deliveryDetails==''):
            deliveryDetails=delivery
        consanguinity=request.POST.get('consanguinity')
        if(consanguinity==None):
            consanguinity=''
        
        perninantalEvents=request.POST.get('perninantalEvents')
        if(perninantalEvents=='present'):
            perninantalEventsDetails=request.POST.get('perninantalEventsDetails')
        else:
            perninantalEventsDetails='absent'
        treatment=request.POST.get('treatment')
        requiredNICUstay=request.POST.get('requiredNICUstay')
        if(requiredNICUstay=='present'):
            requiredNICUstayDets=request.POST.get('requiredNICUstayDets')
        else:
            requiredNICUstayDets='absent'
            
        neurological_concerns=request.POST.getlist('neurology_concerns')
        developemental_concerns=request.POST.getlist('developement_concerns')
        delayed_motor_developement=request.POST.getlist('delayed_motor_developement')
        delayed_sensory_dev=request.POST.getlist('delayed_sensory_dev')
        delayed_speech_developement=request.POST.getlist('delayed_speech_developement')
        learning_concerns=request.POST.getlist('learning_concerns')
        behavioral_concerns=request.POST.getlist('behavior_concerns')
        
        motor_development=request.POST.get('motor-developement')
        if(motor_development==None):
            motor_development=''
        social_smile=request.POST.get('social-smile')
        if(social_smile==''):
            social_smile=0
        neck_holding=request.POST.get('neck-holding')
        if(neck_holding==''):
            neck_holding=0
        roll_over=request.POST.get('roll-over')
        if(roll_over==''):
            roll_over=0
        sitting_up=request.POST.get('sitting-up')
        if(sitting_up==''):
            sitting_up=0
        standing=request.POST.get('standing')
        if(standing==''):
            standing=0
        walking=request.POST.get('walking')
        if(walking==''):
            walking=0
        climbing_staircase=request.POST.get('climbing_staircase')
        if(climbing_staircase==''):
            climbing_staircase=0
        speech_developement=request.POST.get('speech-developement')
        if(speech_developement==None):
            speech_developement=''
        single_words=request.POST.get('single-words')
        if(single_words==''):
            single_words=0
        full_sentences=request.POST.get('full-sentences')
        if(full_sentences==''):
            full_sentences=0
        response_to_calling_names=request.POST.get('res-name-call')
        if(response_to_calling_names==None):
            response_to_calling_names=''
        response_to_instructions=request.POST.get('res-inst-call')
        if(response_to_instructions==None):
            response_to_instructions=''
        reapeats_spoken_words=request.POST.get('rep-words')
        if(reapeats_spoken_words==None):
            reapeats_spoken_words=''
        communication_loops=request.POST.get('comm-loop')
        if(communication_loops==None):
            communication_loops=''
        motorDevDetails=request.POST.get('motorDevDetails')
        speechDevDetails=request.POST.get('speechDevDetails')
        PastHistoryDetails=request.POST.get('PastHistoryDetails')
        BehavioralAndPersonalDetails=request.POST.get('BehavioralAndPersonalDetails')
        
        clinical_history_significance=request.POST.get('clinical-history-significance')
        ho_surgery=request.POST.get('ho-surg')
        if(ho_surgery==None):
            ho_surgery=''
        ho_hospitalization=request.POST.get('ho-hosp')
        if(ho_hospitalization==None):
            ho_hospitalization=''
        ho_previous_treatment=request.POST.get('ho-treatment')
        if(ho_previous_treatment==None):
            ho_previous_treatment=''
        personal_developement=request.POST.getlist('personal_developement')
        learning_behavior=request.POST.getlist('learning_behavior')
        behavior=request.POST.getlist('behavior')
        parenting_style=request.POST.get('parenting-style')
        if(parenting_style==None):
            parenting_style=''
        tv_view_hrs=request.POST.get('tv_view_hrs')
        if(tv_view_hrs==''):
            tv_view_hrs=0
        UnhealthyDietryHabits=request.POST.get('UnhealthyDietryHabits')
        UnhealthySleepHabits=request.POST.get('UnhealthySleepHabits')
        
        #academic history
        present_school_name=request.POST.get('schoolName')
        school_board=request.POST.get('schoolBoard')
        if(school_board=='Board'):
            school_board=''
        school_medium=request.POST.get('schoolMedium')
        if(school_medium=='Medium'):
            school_medium=''
        school_comments=request.POST.get('schoolComments')
        concerns_first_noticed_in=request.POST.get('concerns-first-noticed-in')
        attendance=request.POST.get('attendance')
        if(attendance==None):
            attendance=''
        liked_subjects=request.POST.get('liked subjects')
        unliked_subjects=request.POST.get('unliked subjects')
        present_school_concerns=request.POST.getlist('school concerns')
        
        #Examination
        weight=request.POST.get('weight')
        if(weight==''):
            weight=0
        height=request.POST.get('height')
        if(height==''):
            height=0
        head_circumference=request.POST.get('head-circumference')
        if(head_circumference==''):
            head_circumference=0
        skull_shape=request.POST.get('skull-shape-details')
        general_neurology=request.POST.getlist('general_neurology')
        general_neurology_details=request.POST.get('general_neurology_details')
        skin_exam=request.POST.get('skin-exam-text')
        joints=request.POST.get('joints-text')
        neurology=request.POST.getlist('neurology')
        neurology_details=request.POST.get('neurology_details')
        hypertrophy_of_muscles=request.POST.get('hypertrophy-of-muscles')
        abnormal_tone_pattern=request.POST.get('muscle_tone_neurology')
        muscle_tone_neurology=request.POST.get('muscle_tone_neurology')
        muscle_neurology=request.POST.getlist('muscle_neurology')
        muscle_neurology_details=request.POST.get('muscle_neurology_details')
        muscle_power_details=request.POST.get('muscle_power_details')
        deep_tendon_reflexes=request.POST.get('deep-tendon-reflexes')
        deep_tendon_reflexes_details=request.POST.get('deep-tendon-reflexes-details')
        coordination=request.POST.get('coordination')
        if(coordination==None):
            coordination=''
        coordination_details=request.POST.get('coordination_details')
        abnormal_movements=request.POST.get('abnormal_movements')
        if(abnormal_movements==None):
            abnormal_movements=''
        abnormal_movements_details=request.POST.get('abnormal_movements_details')
        motor_deficit=request.POST.get('motor_deficit')
        gait=request.POST.get('Gait')
        if(gait==None):
            gait=''
        balance=request.POST.get('balance')
        if(balance==None):
            balance=''        
        #Evaluation
        visual_deficit=request.POST.getlist('visual_deficit')
        hearing_deficit=request.POST.getlist('hearing_deficit')
        eye_contact=request.POST.get('eye_contact')
        if(eye_contact==None):
            eye_contact=''
        motor_imitation_skills=request.POST.get('motor_imitation_skills')
        pointing_behaviors=request.POST.get('pointing_behaviors')
        stereotypic_behaviors=request.POST.get('stereotypic_behaviors')
        sensory_defensive_behaviors=request.POST.get('sensory_defensive_behaviors')
        speech=request.POST.get('speech')
        evaluationMChat=request.POST.get('evaluationMChat')
        development_screening=request.POST.get('development_screening')
        gross_motor=request.POST.getlist('gross_motor')
        speech_screening=request.POST.getlist('speech_screening')
        fine_motor=request.POST.getlist('fine_motor')
        social_emotion=request.POST.getlist('social_emotion')
        learning_evaluation=request.POST.getlist('learning_evaluation')
        behavior_evaluation=request.POST.getlist('behavior_evaluation')
        
        #impression
        neurology_impression=request.POST.getlist('neurology_impression')
        cerebral_palsy=request.POST.get('cerebral_palsy')
        if(cerebral_palsy==None):
            cerebral_palsy=''
        cognitive_disability=request.POST.get('cognitive_disability')
        if(cognitive_disability==None):
            cognitive_disability=''
        mental_retardation=request.POST.get('mental_retardation')
        developement_impression=request.POST.getlist('developement_impression')
        learning_impression=request.POST.getlist('learning_impression')
        behavior_impression=request.POST.getlist('behavior_impression')
        
        #plan
        neurology_evaluation=request.POST.getlist('neurology_evaluation')
        developement_evaluation=request.POST.getlist('developement_evaluation')
        learning_evaluation_plan=request.POST.getlist('learning_evaluation_plan')
        special_education_intervention=request.POST.getlist('special_education_intervention')
        remedial_intervention=request.POST.getlist('remedial_intervention')
        behavioral_modification=request.POST.getlist('behavioral_modification')
        academic_suggestions=request.POST.getlist('academic_suggestions')
        followUpPlan=request.POST.get('followUpPlan')
        
        #medical treatment
        medical_treatment_plan=request.POST.getlist('medical_treatment_plan')
        
        # data=(name,address,gender,refferedby,birthDate,birthWeight,term,delivery,consanguinity,perninantalEvents,treatment,requiredNICUstay,str1)
        # sheet.append(data)
        # wb.save("https://docs.google.com/spreadsheets/d/1w4wO_ZomtF8nt3E9czaIJZEZXDh4IUTblhnvwag1998/edit?usp=sharing")
        
        
                
        neurological_concerns=" , ".join(neurological_concerns)
        developemental_concerns=" , ".join(developemental_concerns)
        delayed_motor_developement=" , ".join(delayed_motor_developement)
        delayed_sensory_dev=" , ".join(delayed_sensory_dev)
        delayed_speech_developement=" , ".join(delayed_speech_developement)
        learning_concerns=" , ".join(learning_concerns)
        behavioral_concerns=" , ".join(behavioral_concerns)
        
        personal_developement=" , ".join(personal_developement)
        learning_behavior=" , ".join(learning_behavior)
        behavior=" , ".join(behavior)
        present_school_concerns=" , ".join(present_school_concerns)
        general_neurology=" , ".join(general_neurology)
        neurology=" , ".join(neurology)
        muscle_neurology=" , ".join(muscle_neurology)
        visual_deficit=" , ".join(visual_deficit)
        hearing_deficit=" , ".join(hearing_deficit)
        
        speech_screening=" , ".join(speech_screening)
        gross_motor=" , ".join(gross_motor)
        fine_motor=" , ".join(fine_motor)
        social_emotion=" , ".join(social_emotion)
        learning_evaluation=" , ".join(learning_evaluation)
        behavior_evaluation=" , ".join(behavior_evaluation)
        
        neurology_impression=" , ".join(neurology_impression)
        developement_impression=" , ".join(developement_impression)
        learning_impression=" , ".join(learning_impression)
        behavior_impression=" , ".join(behavior_impression)
        
        neurology_evaluation=" , ".join(neurology_evaluation)
        developement_evaluation=" , ".join(developement_evaluation)
        learning_evaluation_plan=" , ".join(learning_evaluation_plan)
        special_education_intervention=" , ".join(special_education_intervention)
        remedial_intervention=" , ".join(remedial_intervention)
        behavioral_modification=" , ".join(behavioral_modification)
        academic_suggestions=" , ".join(academic_suggestions)
        medical_treatment_plan=" , ".join(medical_treatment_plan)
        
        autData=AutisticData(firstName=name,address=address,gender=gender,reffered_By=refferedby,referred_By_phone_no=referredBy_phone,birth_Date=birthDate,birth_Weight=birthWeight,term=term,preterm_weeks=preterm_weeks,delivery=delivery,delivery_Details=deliveryDetails,consanguinity=consanguinity,perninantal_Events=perninantalEvents,perninantal_Events_Details=perninantalEventsDetails,treatment=treatment,required_NICU_stay=requiredNICUstayDets,
                             neurological_concern=neurological_concerns,developemental_concerns=developemental_concerns,delayed_motor_developement=delayed_motor_developement,delayed_sensory_dev=delayed_sensory_dev,delayed_speech_developement=delayed_speech_developement,learning_concerns=learning_concerns,behavioral_concerns=behavioral_concerns,
                             motor_development=motor_development,social_smile=social_smile,neck_holding=neck_holding,roll_over=roll_over,sitting_up=sitting_up,standing=standing,walking=walking,climbing_staircase=climbing_staircase,motor_devlopement_details=motorDevDetails,speech_developement=speech_developement,
                             single_words=single_words,full_sentences=full_sentences,response_to_calling_names=response_to_calling_names,response_to_instructions=response_to_instructions,reapeats_spoken_words=reapeats_spoken_words,communication_loops=communication_loops,speech_devlopement_details=speechDevDetails,
                             clinical_history_significance=clinical_history_significance,ho_surgery=ho_surgery,ho_hospitalization=ho_hospitalization,ho_previous_treatment=ho_previous_treatment,Past_History_Details=PastHistoryDetails,
                             personal_developement=personal_developement,learning_behavior=learning_behavior,behavior=behavior,tv_view_hrs=tv_view_hrs,Unhealthy_Dietry_Habits=UnhealthyDietryHabits,Unhealthy_Sleep_Habits=UnhealthySleepHabits,parenting_style=parenting_style,Behavioral_And_Personal_Details=BehavioralAndPersonalDetails,
                             present_school_name=present_school_name,school_board=school_board,school_medium=school_medium,school_comments=school_comments,concerns_first_noticed_in=concerns_first_noticed_in,attendance=attendance,liked_subjects=liked_subjects,unliked_subjects=unliked_subjects,present_school_concerns=present_school_concerns,
                             weight=weight,height=height,head_circumference=head_circumference,skull_shape=skull_shape,general_neurology=general_neurology,general_neurology_details=general_neurology_details,
                             skin_exam=skin_exam,joints=joints,neurology=neurology,neurology_details=neurology_details,hypertrophy_of_muscles=hypertrophy_of_muscles,abnormal_tone_pattern=abnormal_tone_pattern,muscle_tone_neurology=muscle_tone_neurology,muscle_neurology=muscle_neurology,muscle_neurology_details=muscle_neurology_details,muscle_power_details=muscle_power_details,
                             deep_tendon_reflexes=deep_tendon_reflexes,deep_tendon_reflexes_details=deep_tendon_reflexes_details,coordination=coordination,coordination_details=coordination_details,
                             abnormal_movements=abnormal_movements,abnormal_movements_details=abnormal_movements_details,motor_deficit=motor_deficit,gait=gait,balance=balance,visual_deficit=visual_deficit,
                             hearing_deficit=hearing_deficit,eye_contact=eye_contact,motor_imitation_skills=motor_imitation_skills,pointing_behaviors=pointing_behaviors,stereotypic_behaviors=stereotypic_behaviors,sensory_defensive_behaviors=sensory_defensive_behaviors,speech=speech,evaluationMChat=evaluationMChat,development_screening=development_screening,gross_motor=gross_motor,speech_screening=speech_screening,fine_motor=fine_motor,
                             social_emotion=social_emotion,learning_evaluation=learning_evaluation,behavior_evaluation=behavior_evaluation,neurology_impression=neurology_impression,cerebral_palsy=cerebral_palsy,cognitive_disability=cognitive_disability,mental_retardation=mental_retardation,developement_impression=developement_impression,
                             learning_impression=learning_impression,behavior_impression=behavior_impression,neurology_evaluation=neurology_evaluation,
                             developement_evaluation=developement_evaluation,learning_evaluation_plan=learning_evaluation_plan,special_education_intervention=special_education_intervention,remedial_intervention=remedial_intervention,
                             behavioral_modification=behavioral_modification,academic_suggestions=academic_suggestions,follow_Up_Plan=followUpPlan,medical_treatment_plan=medical_treatment_plan)
        # autData=AutisticData()
        autData.save()
        
        p_k=autData.case_no
         
        # # Now, let's add data to our worksheet
        colNames=["Case No" , "Name" , "Address" , "Gender" , "Reffered By" , "Phone no" , "Birth Date" , "Birth Weight" , "Term" , "Term Weeks" , "Delivery" , "Delivery Details" , "Consanguinity" , "Perninantal Events" , "Perninantal Events Details" , "Treatment" , "Required NICU stay" , "Neurological Concerns" , "Developement Concerns" , "Delayed Motor Developement" , "Delayed Sensory Developement" , "Delayed Speech Developement" , "Learning Concerns" , "Behavioral Concerns" , "Motor Developement" , "Social Smile" , "Neck Holding" , "Roll Over" , "Sitting Up" , "Standing" , "Climbing Staircase" , "Walking" , "Speech Developement" , "Single Words" , "Full Sentences At" , "Resopnse to calling names" , "Response to instructions" , "Repeats spoken words" , "Communication Loops" , "Motor Developement Details" , "Speech Developement Details" , "Clinical History Significance" , "H/O surgery" , "H/O Hospitalization" , "H/O previous treatment" , "Past History Details" , "Personal Developement" , "Learning Behavior" , "Behavior" , "Parenting Style" , "Behavioral and Personal Details" , "Present School Name" , "School Board" , "School Medium" , "School Comments" , "Concerns first noticed in" , "Attendance" , "Liked Subjects" , "Unliked Subjects" , "Present School Concers" , "TV viewing hours" , "Unhealthy Dietry Habits" , "Unhealthy Sleep Habits" , "Weight" , "Height" , "Head circumference" , "Skull Shape" , "General Neurology" , "General Neurology Details" , "Skin Exam" , "Joints" , "Neurology" , "Neurology Details" , "Hypertrophy Of Muscles" , "Abnormal Tone Pattern" , "Muscle tone neurology" , "Muscle Neurology" , "Muscle Neurology Details" , "Muscle power Details" , "Deep Tendon Reflexes" , "Deep tendon reflexes details" , "Coordination" , "Coordination Details" , "Abnormal Movements" , "Abnormal Movements Details" , "Motor Deficit" , "Gait" , "Balance" , "Visual Deficit" , "Hearing Deficit" , "Eye Contact" , "Motor Imitation Skills" , "Pointing Behaviors" , "Stereotypic Behaviors" , "Sensory Defensive Behaviors" , "Speech" , "Evaluation on MChat" , "Developement Screening" , "Gross Motor" , "Speech Screening" , "Fine motor" , "Social Emotion" , "Learing Evaluation" , "Behavior Evaluation" , "Neurology Impression" , "Cerebral Palsy" , "Cognitive Disability" , "Mental Retardation" , "Developemental Impression" , "Learning Impression" , "Behavior Impression" , "Neurology Evaluation" , "Developement Evaluation" , "Learning Evaluation Plan" , "Special Education Intervention" , "Remedial Intervention" , "Behavioral Modification" , "Academic Suggestions" , "Follow Up Plan" , "Medical Treatment Plan"]
  
        # # # Creating the first column
        # char='A'
        # char2=chr(ord('A')-1)
        # flag=0
        # for name in colNames:
        #     if char<='Z' and flag==0:
        #         worksht.cell("{char}1".format(char=char)).set_text_format("bold", True).value = name
        #     else:
        #         flag=1
        #         if(char>'Z'):
        #             char='A'
        #             char2=chr(ord(char2)+1)
        #         worksht.cell("{char2}{char}1".format(char2=char2,char=char)).set_text_format("bold", True).value = name
        #     char=chr(ord(char)+1)
        
        df=worksht.get_all_records()

        
        colValues=[name,address,gender,refferedby,referredBy_phone,birthDate,birthWeight,term,preterm_weeks,delivery,consanguinity,perninantalEvents,treatment,requiredNICUstay,neurological_concerns,developemental_concerns,delayed_motor_developement,delayed_sensory_dev,delayed_speech_developement,learning_concerns,behavioral_concerns,
                   motor_development,social_smile,neck_holding,roll_over,sitting_up,standing,walking,climbing_staircase,motorDevDetails,speech_developement,single_words,full_sentences,response_to_calling_names,response_to_instructions,reapeats_spoken_words,communication_loops,speechDevDetails,
                   clinical_history_significance,ho_surgery,ho_hospitalization,ho_previous_treatment,PastHistoryDetails,
                   personal_developement,learning_behavior,tv_view_hrs,UnhealthyDietryHabits,UnhealthySleepHabits,parenting_style,BehavioralAndPersonalDetails,
                   present_school_name,school_board,school_medium,school_comments,concerns_first_noticed_in,attendance,liked_subjects,unliked_subjects,present_school_concerns,
                   weight,height,head_circumference,skull_shape,general_neurology,general_neurology_details,skin_exam,joints,neurology,neurology_details,hypertrophy_of_muscles,abnormal_tone_pattern,muscle_tone_neurology,muscle_neurology,muscle_neurology_details,muscle_power_details,deep_tendon_reflexes,deep_tendon_reflexes_details,coordination,coordination_details,abnormal_movements,abnormal_movements_details,motor_deficit,gait,balance,
                   visual_deficit,hearing_deficit,eye_contact,motor_imitation_skills,pointing_behaviors,stereotypic_behaviors,sensory_defensive_behaviors,speech,evaluationMChat,development_screening,gross_motor,speech_screening,fine_motor,social_emotion,learning_evaluation,behavior_evaluation,
                   neurology_impression,cerebral_palsy,cognitive_disability,mental_retardation,developement_impression,learning_impression,behavior_impression,
                   neurology_evaluation,developement_evaluation,learning_evaluation_plan,special_education_intervention,remedial_intervention,behavioral_modification,academic_suggestions,followUpPlan,
                   medical_treatment_plan]
        
        
        json_serialized = sr.serialize("json", [AutisticData.objects.get(pk=p_k)])
        # print(json_serialized,"done")
        
        data=AutisticData.objects.filter(case_no=p_k)
        serializer= AutisticDataSerializer(data,many=True)
        df = pd.DataFrame(serializer.data)
        # print(serializer.data)
        # arr = df.to_numpy()


        # If modifying these scopes, delete the file token.json.
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        # The ID and range of a sample spreadsheet.
        SERVICE_ACCOUNT_FILE = './api/keys.json'

        credentials = None
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE,scopes=SCOPES)

        SAMPLE_SPREADSHEET_ID ='1w4wO_ZomtF8nt3E9czaIJZEZXDh4IUTblhnvwag1998'

        try:
            service = build('sheets', 'v4', credentials=credentials)

            # Call the Sheets API
            sheet = service.spreadsheets()
            # result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,
            #                                 range=SAMPLE_RANGE_NAME).execute()
            # values = result.get('values', [])
            
            row_count = len(worksht.get_all_records()) + 2
            
            df=df.to_json(orient='values')
            arr=json.loads(df)
            # arr[0].insert(0,'{pk}'.format(pk=p_k))
            print(arr)
            # print(arr,"done")
            
            myBody = {u'range': u'Sheet1!A{a}'.format(a=row_count), u'values': arr, u'majorDimension': u'ROWS'}

            if arr is not None:
                requestVal=sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Sheet1!A{a}".format(a=row_count),valueInputOption="USER_ENTERED",body=myBody).execute()
        except HttpError as err:
            print(err)

        # fill_gsheet(colValues,row_count)
        
        
        # worksht.set_dataframe(new_row,(row_count,1), copy_index = 'TRUE', copy_head = 'TRUE')
        # worksht.delete_rows(row_count , number=1)

        # worksheet = worksht.insert_rows(last_row, number=1, values= new_row)
        
   
    data=json.loads(json_serialized)
    print(arr)
    
    data=data[0]["fields"]
    temp={"case_no":'{pk}'.format(pk=p_k)}
    temp.update(data)
    data=temp
    data.pop('user')
    data=list(data.values())
    data=zip(colNames,data)
    
    data=dict(data)
    
    i=[x for x in range(0,120)]
    
    request.session["data"] = data
    
    return redirect('formSubmitted')

def formSubmitted(request):
    return render(request,'../templates/afterSubmit.html');

register = template.Library()
@register.filter
def remove_substr(string, char):
    return string.replace(char, '')

def fill_gsheet(colValues,row_count):
    # progress_recorder= ProgressRecorder(self)
    char='A'
    char2=chr(ord('A')-1)
    flag=0
    i=0
    for name in colValues:
        if char<='Z' and flag==0:
            worksht.cell("{char}{row_count}".format(char=char,row_count=row_count)).value = name
        else:
            flag=1
            if(char>'Z'):
                char='A'
                char2=chr(ord(char2)+1)
            worksht.cell("{char2}{char}{row_count}".format(char2=char2,char=char,row_count=row_count)).value = name
        char=chr(ord(char)+1)
        i+=1
        # progress_observer.set_progress(i, total_work_to_do)
        # progress_recorder.set_progress(i+1,len(colValues),f'On {i}')
           
           

    # users=UserCred.objects.all()
    # user_list=list(users)
    
    # print(username,emailID,contactNo,password)
    # flag=False
    # for user in user_list:
    #     if(username==user.username):
    #         flag=True
    #         break
    # if flag==True:
    #     return HttpResponse('User loged in')
    # else:
    #     return HttpResponse('Wrong Credentials')
    return HttpResponse('User loged in')

# ,motor_development,social_smile,neck_holding,roll_over,sitting_up,standing,walking,speech_developement,single_words,full_sentences,response_to_calling_names,response_to_instructions,reapeats_spoken_words,communication_loops,past_history_significance,clinical_history_significance,ho_surgery,ho_hospitalization,ho_previous_treatment,personal_developement,learning_behavior,behavior,parenting_style,present_school_name,school_board,school_medium,school_comments,concerns_first_noticed_in,attendance,liked_subjects,unliked_subjects,present_school_concerns,weight,height,head_circumference,skull_shape,general_neurology,general_neurology_details,skin_exam,joints,neurology,neurology_details,hypertrophy_of_muscles,abnormal_tone_pattern,muscle_tone_neurology,muscle_neurology,muscle_neurology_details,muscle_power_details,deep_tendon_reflexes,deep_tendon_reflexes_details,coordination,coordination_details,abnormal_movements,abnormal_movements_details,motor_deficit,gait,balance,visual_deficit,hearing_deficit,eye_contact,motor_imitation_skills,pointing_behaviors,stereotypic_behaviors,sensory_defensive_behaviors,speech,evaluationMChat,development_screening,gross_motor,speech_screening,fine_motor,social_emotion,learning_evaluation,behavior_evaluation,neurology_impression,cerebral_palsy,cognitive_disability,mental_retardation,developement_impression,learning_impression,behavior_impression,neurology_evaluation,developement_evaluation,learning_evaluation_plan,special_education_intervention,remedial_intervention,behavioral_modification,academic_suggestions,followUpPlan,medical_treatment_plan


# def get_progress(self, request, task_id): 
#     result = AsyncResult(task_id) 
#     response_data = { 
#         'state': result.state, 
#         'details': self.result.info,
#     } 
#     return HttpResponse(
#         json.dumps(response_data), 
#         content_type='application/json'
#     )


class ExportImportExcel(APIView):
    def get(self,request):
        data=AutisticData.objects.all()
        serializer= AutisticDataSerializer(data,many=True)
        df = pd.DataFrame(serializer.data)
        arr = df.to_numpy()
        # arr = np.transpose(arr)

        # df.to_csv(f"worksht.csv")
        # print(arr)
        return Response({'status':200})