import re
from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .models import AutisticData


import pygsheets
  
# Create the Client
# Enter the name of the downloaded KEYS 
# file in service_account_file
client = pygsheets.authorize(service_account_file="./api/inte-355404-dc597e53e58e.json")
  
# opens a spreadsheet by its name/title
spreadsht = client.open("InternalProject autistic data records")
  
# opens a worksheet by its name/title
worksht = spreadsht.worksheet("title", "Sheet1")
  

# Create your views here.
def index(request):
    context={
        'variable':'this is sent'
    }
    return render(request,'index.html',context)

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
#     return render(request,'temp.html')

def temp(request):
    form=DataForm()
    return render(request,'temp.html',{'form':form})

def saveForm(request):
    if request.method == 'POST':
        name=request.POST.get('personName')
        address=request.POST.get('address')
        gender=request.POST.get('gender')
        refferedby=request.POST.get('refferedby')
        
        birthDate=request.POST.get('birthDate')
        birthWeight=request.POST.get('birthWeight')
        if(birthWeight==''):
            birthWeight=0
        term=request.POST.get('term')
        delivery=request.POST.get('delivery')
        if(delivery!='normal'):
            deliveryDetails=request.POST.get('deliveryDetails')
        else:
            deliveryDetails=delivery
        consanguinity=request.POST.get('consanguinity')
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
        learning_concerns=request.POST.getlist('learning_concerns')
        behavioral_concerns=request.POST.getlist('behavior_concerns')
        
        motor_development=request.POST.get('motor-developement')
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
        speech_developement=request.POST.get('speech-developement')
        if(speech_developement==''):
            speech_developement=0
        single_words=request.POST.get('single-words')
        if(single_words==''):
            single_words=0
        full_sentences=request.POST.get('full-sentences')
        if(full_sentences==''):
            full_sentences=0
        response_to_calling_names=request.POST.get('res-name-call')
        response_to_instructions=request.POST.get('res-inst-call')
        reapeats_spoken_words=request.POST.get('rep-words')
        communication_loops=request.POST.get('comm-loop')
        
        past_history_significance=request.POST.get('past-his')
        clinical_history_significance=request.POST.get('clinical-history-significance')
        ho_surgery=request.POST.get('ho-surg')
        ho_hospitalization=request.POST.get('ho-hosp')
        ho_previous_treatment=request.POST.get('ho-treatment')
        
        personal_developement=request.POST.getlist('personal_developement')
        learning_behavior=request.POST.getlist('learning_behavior')
        behavior=request.POST.getlist('behavior')
        parenting_style=request.POST.get('parenting-style')
        
        #academic history
        present_school_name=request.POST.get('schoolName')
        school_board=request.POST.get('schoolBoard')
        school_medium=request.POST.get('schoolMedium')
        school_comments=request.POST.get('schoolComments')
        concerns_first_noticed_in=request.POST.get('concerns-first-noticed-in')
        attendance=request.POST.get('attendance')
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
        coordination_details=request.POST.get('coordination_details')
        abnormal_movements=request.POST.get('abnormal_movements')
        abnormal_movements_details=request.POST.get('abnormal_movements_details')
        motor_deficit=request.POST.get('motor_deficit')
        gait=request.POST.get('Gait')
        if(gait==None):
            gait='NA'
        balance=request.POST.get('balance')
        
        #Evaluation
        visual_deficit=request.POST.getlist('visual_deficit')
        hearing_deficit=request.POST.getlist('hearing_deficit')
        eye_contact=request.POST.get('eye_contact')
        if(eye_contact==None):
            eye_contact='normal'
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
        cognitive_disability=request.POST.get('cognitive_disability')
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
        
        autData=AutisticData(firstName=name,address=address,gender=gender,refferedBy=refferedby,birthDate=birthDate,birthWeight=birthWeight,term=term,delivery=deliveryDetails,consanguinity=consanguinity,perninantalEvents=perninantalEventsDetails,treatment=treatment,requiredNICUstay=requiredNICUstayDets,
                             neurological_concern=neurological_concerns,developemental_concerns=developemental_concerns,learning_concerns=learning_concerns,behavioral_concerns=behavioral_concerns,
                             motor_development=motor_development,social_smile=social_smile,neck_holding=neck_holding,roll_over=roll_over,sitting_up=sitting_up,standing=standing,walking=walking,speech_developement=speech_developement,
                             single_words=single_words,full_sentences=full_sentences,response_to_calling_names=response_to_calling_names,response_to_instructions=response_to_instructions,reapeats_spoken_words=reapeats_spoken_words,communication_loops=communication_loops,
                             past_history_significance=past_history_significance,clinical_history_significance=clinical_history_significance,ho_surgery=ho_surgery,ho_hospitalization=ho_hospitalization,ho_previous_treatment=ho_previous_treatment,
                             personal_developement=personal_developement,learning_behavior=learning_behavior,behavior=behavior,parenting_style=parenting_style,present_school_name=present_school_name,school_board=school_board,school_medium=school_medium,school_comments=school_comments,concerns_first_noticed_in=concerns_first_noticed_in,attendance=attendance,liked_subjects=liked_subjects,unliked_subjects=unliked_subjects,present_school_concerns=present_school_concerns,
                             weight=weight,height=height,head_circumference=head_circumference,skull_shape=skull_shape,general_neurology=general_neurology,general_neurology_details=general_neurology_details,
                             skin_exam=skin_exam,joints=joints,neurology=neurology,neurology_details=neurology_details,hypertrophy_of_muscles=hypertrophy_of_muscles,abnormal_tone_pattern=abnormal_tone_pattern,muscle_tone_neurology=muscle_tone_neurology,muscle_neurology=muscle_neurology,muscle_neurology_details=muscle_neurology_details,muscle_power_details=muscle_power_details,
                             deep_tendon_reflexes=deep_tendon_reflexes,deep_tendon_reflexes_details=deep_tendon_reflexes_details,coordination=coordination,coordination_details=coordination_details,
                             abnormal_movements=abnormal_movements,abnormal_movements_details=abnormal_movements_details,motor_deficit=motor_deficit,gait=gait,balance=balance,visual_deficit=visual_deficit,
                             hearing_deficit=hearing_deficit,eye_contact=eye_contact,motor_imitation_skills=motor_imitation_skills,pointing_behaviors=pointing_behaviors,stereotypic_behaviors=stereotypic_behaviors,sensory_defensive_behaviors=sensory_defensive_behaviors,speech=speech,evaluationMChat=evaluationMChat,development_screening=development_screening,gross_motor=gross_motor,speech_screening=speech_screening,fine_motor=fine_motor,
                             social_emotion=social_emotion,learning_evaluation=learning_evaluation,behavior_evaluation=behavior_evaluation,neurology_impression=neurology_impression,cerebral_palsy=cerebral_palsy,cognitive_disability=cognitive_disability,mental_retardation=mental_retardation,developement_impression=developement_impression,
                             learning_impression=learning_impression,behavior_impression=behavior_impression,neurology_evaluation=neurology_evaluation,
                             developement_evaluation=developement_evaluation,learning_evaluation_plan=learning_evaluation_plan,special_education_intervention=special_education_intervention,remedial_intervention=remedial_intervention,
                             behavioral_modification=behavioral_modification,academic_suggestions=academic_suggestions,followUpPlan=followUpPlan,medical_treatment_plan=medical_treatment_plan)
        autData=AutisticData()
        autData.save()
        
        
        # # Now, let's add data to our worksheet
        # colNames=["Name","Address","Gender","Reffered By","Birth Date","Birth Weight","Term","Delivery Details","Consanguinity","Perninantal Events Details","Treatment","Required NICU stay","Neurological Concerns","Developement Concerns","Learning Concerns","Behavioral Concerns","Motor Developement","Social Smile","Neck Holding","Roll Over","Sitting Up","Standing","Walking","Speech Developement","Single Words","Full Sentences At","Resopnse to calling names","Response to instructions","Repeats spoken words","Communication Loops","Past History Significance","Clinical History Significance","H/O surgery","H/O Hospitalization","H/O previous treatment","Personal Developement","Learning Behavior","Parenting Style","Present School Name","School Board","School Medium","School Comments","Concerns first noticed in","Attendance","Liked Subjects","Unliked Subjects","Present School Concers","Weight","Height","Head circumference","Skull Shape","General Neurology","General Neurology Details","Skin Exam","Joints","Neurology","Neurology Details","Hypertrophy Of Muscles","Abnormal Tone Pattern","Muscle tone neurology","Muscle Neurology","Muscle Neurology Details","Muscle power Details","Deep Tendon Reflexes","Deep tendon reflexes details","Coordination","Coordination Details","Abnormal Movements","Abnormal Movements Details","Motor Deficit","Gait","Balance","Visual Deficit","Hearing Deficit","Eye Contact","Motor Imitation Skills","Pointing Behaviors","Stereotypic Behaviors","Sensory Defensive Behaviors","Speech","Evaluation on MChat","Developement Screening","Gross Motor","Speech Screening","Fine motor","Social Emotion","Learing Evaluation","Behavior Evaluation","Neurology Impression","Cerebral Palsy","Cognitive Disability","Mental Retardation","Developemental Impression","Learning Impression","Behavior Impression","Neurology Evaluation","Developement Evaluation","Learning Evaluation Plan","Special Education Intervention","Remedial Intervention","Behavioral Modification","Academic Suggestions","Follow Up Plan","Medical Treatment Plan"]
  
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
        
        row_count = len(worksht.get_all_records()) + 2
        df=worksht.get_all_records()
        # print(df,"records ")
        print(row_count)
        
        neurological_concerns="\n".join(neurological_concerns)
        developemental_concerns="\n".join(developemental_concerns)
        learning_concerns="\n".join(learning_concerns)
        behavioral_concerns="\n".join(behavioral_concerns)
        
        personal_developement="\n".join(personal_developement)
        learning_behavior="\n".join(learning_behavior)
        behavior="\n".join(behavior)
        present_school_concerns="\n".join(present_school_concerns)
        general_neurology="\n".join(general_neurology)
        neurology="\n".join(neurology)
        muscle_neurology="\n".join(muscle_neurology)
        visual_deficit="\n".join(visual_deficit)
        hearing_deficit="\n".join(hearing_deficit)
        
        speech_screening="\n".join(speech_screening)
        fine_motor="\n".join(fine_motor)
        social_emotion="\n".join(social_emotion)
        learning_evaluation="\n".join(learning_evaluation)
        behavior_evaluation="\n".join(behavior_evaluation)
        
        neurology_impression="\n".join(neurology_impression)
        developement_impression="\n".join(developement_impression)
        learning_impression="\n".join(learning_impression)
        behavior_impression="\n".join(behavior_impression)
        
        neurology_evaluation="\n".join(neurology_evaluation)
        developement_evaluation="\n".join(developement_evaluation)
        learning_evaluation_plan="\n".join(learning_evaluation_plan)
        special_education_intervention="\n".join(special_education_intervention)
        remedial_intervention="\n".join(remedial_intervention)
        behavioral_modification="\n".join(behavioral_modification)
        academic_suggestions="\n".join(academic_suggestions)
        medical_treatment_plan="\n".join(medical_treatment_plan)
        
        colValues=[name,address,gender,refferedby,birthDate,birthWeight,term,delivery,consanguinity,perninantalEvents,treatment,requiredNICUstay,neurological_concerns,developemental_concerns,learning_concerns,behavioral_concerns,
                   motor_development,social_smile,neck_holding,roll_over,sitting_up,standing,walking,speech_developement,single_words,full_sentences,response_to_calling_names,response_to_instructions,reapeats_spoken_words,communication_loops,
                   past_history_significance,clinical_history_significance,ho_surgery,ho_hospitalization,ho_previous_treatment,
                   personal_developement,learning_behavior,behavior,parenting_style,
                   present_school_name,school_board,school_medium,school_comments,concerns_first_noticed_in,attendance,liked_subjects,unliked_subjects,present_school_concerns,
                   weight,height,head_circumference,skull_shape,general_neurology,general_neurology_details,skin_exam,joints,neurology,neurology_details,hypertrophy_of_muscles,abnormal_tone_pattern,muscle_tone_neurology,muscle_neurology,muscle_neurology_details,muscle_power_details,deep_tendon_reflexes,deep_tendon_reflexes_details,coordination,coordination_details,abnormal_movements,abnormal_movements_details,motor_deficit,gait,balance,
                   visual_deficit,hearing_deficit,eye_contact,motor_imitation_skills,pointing_behaviors,stereotypic_behaviors,sensory_defensive_behaviors,speech,evaluationMChat,development_screening,gross_motor,speech_screening,fine_motor,social_emotion,learning_evaluation,behavior_evaluation,
                   neurology_impression,cerebral_palsy,cognitive_disability,mental_retardation,developement_impression,learning_impression,behavior_impression,
                   neurology_evaluation,developement_evaluation,learning_evaluation_plan,special_education_intervention,remedial_intervention,behavioral_modification,academic_suggestions,followUpPlan,
                   medical_treatment_plan]
        char='A'
        char2=chr(ord('A')-1)
        flag=0
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
        
        
        # worksht.set_dataframe(new_row,(row_count,1), copy_index = 'TRUE', copy_head = 'TRUE')
        # worksht.delete_rows(row_count , number=1)

        # worksheet = worksht.insert_rows(last_row, number=1, values= new_row)
        
        
# # if updating multiple values, the data
# # should be in a matrix format
# worksht.update_values("A2:A6", [["Pencil"], ["Eraser"], 
#                                 ["Sharpener"], ["Ruler"], 
#                                 ["Pen"]])  # Adding row values
  
# # Similarly, creating the second column
# worksht.cell("B1").set_text_format("bold", True).value = "Price"
# worksht.update_values("B2:B6", [[5], [3], [5], [15], [10]])
  
# # Creating a basic bar chart
# worksht.add_chart(("A2", "A6"), [("B2", "B6")], "Shop")


    return HttpResponse('ok')

# ,motor_development,social_smile,neck_holding,roll_over,sitting_up,standing,walking,speech_developement,single_words,full_sentences,response_to_calling_names,response_to_instructions,reapeats_spoken_words,communication_loops,past_history_significance,clinical_history_significance,ho_surgery,ho_hospitalization,ho_previous_treatment,personal_developement,learning_behavior,behavior,parenting_style,present_school_name,school_board,school_medium,school_comments,concerns_first_noticed_in,attendance,liked_subjects,unliked_subjects,present_school_concerns,weight,height,head_circumference,skull_shape,general_neurology,general_neurology_details,skin_exam,joints,neurology,neurology_details,hypertrophy_of_muscles,abnormal_tone_pattern,muscle_tone_neurology,muscle_neurology,muscle_neurology_details,muscle_power_details,deep_tendon_reflexes,deep_tendon_reflexes_details,coordination,coordination_details,abnormal_movements,abnormal_movements_details,motor_deficit,gait,balance,visual_deficit,hearing_deficit,eye_contact,motor_imitation_skills,pointing_behaviors,stereotypic_behaviors,sensory_defensive_behaviors,speech,evaluationMChat,development_screening,gross_motor,speech_screening,fine_motor,social_emotion,learning_evaluation,behavior_evaluation,neurology_impression,cerebral_palsy,cognitive_disability,mental_retardation,developement_impression,learning_impression,behavior_impression,neurology_evaluation,developement_evaluation,learning_evaluation_plan,special_education_intervention,remedial_intervention,behavioral_modification,academic_suggestions,followUpPlan,medical_treatment_plan