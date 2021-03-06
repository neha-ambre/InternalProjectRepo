from django.db import models

# Create your models here.
class AutisticData(models.Model):
    caseno=models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50,default='')
    address = models.TextField(default='')
    gender=models.CharField(max_length=20,default='other')
    refferedBy= models.CharField(max_length=50,default='')
    
    # Birth history
    birthDate=models.DateField(default='2001-01-01')
    birthWeight=models.IntegerField(default=0)
    term=models.CharField(max_length=20,default='NA')
    delivery=models.CharField(max_length=20,default='NA')
    deliveryDetails=models.CharField(max_length=1000,default='NA')
    consanguinity=models.CharField(max_length=20,default='NA')
    perninantalEvents=models.CharField(max_length=20,default='NA')
    perninantalEventsDetails=models.CharField(max_length=1000,default='NA')
    treatment=models.CharField(max_length=20,default='NA')
    requiredNICUstay=models.CharField(max_length=20,default='NA')
    
    #Concerns
    neurological_concern=models.TextField(default='NA')
    developemental_concerns=models.TextField(default='NA')
    learning_concerns=models.TextField(default='NA')
    behavioral_concerns=models.TextField(default='NA')
    
    #Developement History
    motor_development=models.CharField(max_length=20,default='normal')
    social_smile=models.IntegerField(default=0)
    neck_holding=models.IntegerField(default=0)
    roll_over=models.IntegerField(default=0)
    sitting_up=models.IntegerField(default=0)
    standing=models.IntegerField(default=0)
    walking=models.IntegerField(default=0)
    speech_developement=models.CharField(max_length=20,default='normal')
    single_words=models.IntegerField(default=0)
    full_sentences=models.IntegerField(default=0)
    response_to_calling_names=models.CharField(max_length=20,default='yes')
    response_to_instructions=models.CharField(max_length=20,default='yes')
    reapeats_spoken_words=models.CharField(max_length=20,default='no')
    communication_loops=models.CharField(max_length=20,default='no')
        
    #Past history
    past_history_significance=models.CharField(max_length=20,default='not significant')
    clinical_history_significance=models.CharField(max_length=20,default='NA')
    ho_surgery=models.CharField(max_length=20,default='absent')
    ho_hospitalization=models.CharField(max_length=20,default='absent')
    ho_previous_treatment=models.CharField(max_length=20,default='absent')
    
    #
    personal_developement=models.TextField(default='NA')
    learning_behavior=models.TextField(default='NA')
    behavior=models.TextField(default='NA')
    parenting_style=models.CharField(max_length=20,default='mixed')
    
    #academic history
    present_school_name=models.TextField(default='NA')
    school_board=models.TextField(default='state')
    school_medium=models.TextField(default='english')
    school_comments=models.TextField(default='NA')
    concerns_first_noticed_in=models.TextField(default='NA')
    attendance=models.TextField(default='average')
    liked_subjects=models.TextField(default='NA')
    unliked_subjects=models.TextField(default='NA')
    present_school_concerns=models.TextField(default='NA')
    
    
    weight=models.IntegerField(default=0)
    height=models.IntegerField(default=0)
    head_circumference=models.IntegerField(default=0)
    skull_shape=models.TextField(default='NA')
    general_neurology=models.TextField(default='NA')
    general_neurology_details=models.TextField(default='NA')
    skin_exam=models.TextField(default='NA')
    joints=models.TextField(default='NA')
    neurology=models.TextField(default='NA')
    neurology_details=models.TextField(default='NA')
    hypertrophy_of_muscles=models.TextField(default='NA')
    abnormal_tone_pattern=models.TextField(default='NA')
    muscle_tone_neurology=models.TextField(default='normal')
    muscle_neurology=models.TextField(default='NA')
    muscle_neurology_details=models.TextField(default='NA')
    muscle_power_details=models.TextField(default='NA')
    deep_tendon_reflexes=models.TextField(default='normal')
    deep_tendon_reflexes_details=models.TextField(default='NA')
    coordination=models.TextField(default='normal')
    coordination_details=models.TextField(default='NA')
    abnormal_movements=models.TextField(default='no')
    abnormal_movements_details=models.TextField(default='NA')
    motor_deficit=models.TextField(default='no')
    gait=models.TextField(default='NA')
    balance=models.TextField(default='developed for age')
    
    #evaluation
    visual_deficit=models.TextField(default='NA')
    hearing_deficit=models.TextField(default='NA')
    eye_contact=models.TextField(default='NA')
    motor_imitation_skills=models.TextField(default='NA')
    pointing_behaviors=models.TextField(default='NA')
    stereotypic_behaviors=models.TextField(default='NA')
    sensory_defensive_behaviors=models.TextField(default='NA')
    speech=models.TextField(default='NA')
    evaluationMChat=models.TextField(default='NA')
    development_screening=models.TextField(default='NA')
    gross_motor=models.TextField(default='NA')
    speech_screening=models.TextField(default='NA')
    fine_motor=models.TextField(default='NA')
    social_emotion=models.TextField(default='NA')
    learning_evaluation=models.TextField(default='NA')
    behavior_evaluation=models.TextField(default='NA')
    
    #impression
    neurology_impression=models.TextField(default='NA')
    cerebral_palsy=models.TextField(default='No')
    cognitive_disability=models.TextField(default='NA')
    mental_retardation=models.TextField(default='NA')
    developement_impression=models.TextField(default='NA')
    learning_impression=models.TextField(default='NA')
    behavior_impression=models.TextField(default='NA')
    
    #plan
    neurology_evaluation=models.TextField(default='NA')
    developement_evaluation=models.TextField(default='NA')
    learning_evaluation_plan=models.TextField(default='NA')
    special_education_intervention=models.TextField(default='NA')
    remedial_intervention=models.TextField(default='NA')
    behavioral_modification=models.TextField(default='NA')
    academic_suggestions=models.TextField(default='NA')
    followUpPlan=models.TextField(default='NA')
    
    #medical treatment
    medical_treatment_plan=models.TextField(default='NA')
    