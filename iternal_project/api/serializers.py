from rest_framework import serializers

from .models import AutisticData

class AutisticDataSerializer(serializers.ModelSerializer):
    # firstName = serializers.CharField(max_length=50,default='')
    # address = serializers.CharField(max_length=5000,default='')
    # gender=serializers.CharField(max_length=20,default='other')
    # refferedBy= serializers.CharField(max_length=50,default='')
    # referredBy_phone = serializers.CharField(max_length=50,default='')
    
    # # Birth history
    # birthDate=serializers.CharField(max_length=20,default='')
    # birthWeight=serializers.CharField(max_length=20,default='NA')
    # term=serializers.CharField(max_length=20,default='NA')
    # preterm_weeks=serializers.CharField(max_length=20,default='0')
    # delivery=serializers.CharField(max_length=20,default='NA')
    # deliveryDetails=serializers.CharField(max_length=1000,default='NA')
    # consanguinity=serializers.CharField(max_length=20,default='NA')
    # perninantalEvents=serializers.CharField(max_length=20,default='NA')
    # perninantalEventsDetails=serializers.CharField(max_length=1000,default='NA')
    # treatment=serializers.CharField(max_length=20,default='NA')
    # requiredNICUstay=serializers.CharField(max_length=20,default='NA')
    
    # #Concerns
    # neurological_concern=serializers.CharField(max_length=5000,default='NA')
    # developemental_concerns=serializers.CharField(max_length=5000,default='NA')
    # delayed_motor_developement=serializers.CharField(max_length=5000,default='NA')
    # delayed_sensory_dev=serializers.CharField(max_length=5000,default='NA')
    # delayed_speech_developement=serializers.CharField(max_length=5000,default='NA')
    # learning_concerns=serializers.CharField(max_length=5000,default='NA')
    # behavioral_concerns=serializers.CharField(max_length=5000,default='NA')
    
    # #Developement History
    # motor_development=serializers.CharField(max_length=20,default='normal')
    # social_smile=serializers.IntegerField(default=0)
    # neck_holding=serializers.IntegerField(default=0)
    # roll_over=serializers.IntegerField(default=0)
    # sitting_up=serializers.IntegerField(default=0)
    # standing=serializers.IntegerField(default=0)
    # climbing_staircase=serializers.IntegerField(default=0)
    # walking=serializers.IntegerField(default=0)
    # speech_developement=serializers.CharField(max_length=20,default='normal')
    # single_words=serializers.IntegerField(default=0)
    # full_sentences=serializers.IntegerField(default=0)
    # response_to_calling_names=serializers.CharField(max_length=20,default='yes')
    # response_to_instructions=serializers.CharField(max_length=20,default='yes')
    # reapeats_spoken_words=serializers.CharField(max_length=20,default='no')
    # communication_loops=serializers.CharField(max_length=20,default='no')
    # motorDevDetails=serializers.CharField(max_length=5000,default='NA')
    # speechDevDetails=serializers.CharField(max_length=5000,default='NA')
    
    # #Past history
    # clinical_history_significance=serializers.CharField(max_length=20,default='NA')
    # ho_surgery=serializers.CharField(max_length=20,default='absent')
    # ho_hospitalization=serializers.CharField(max_length=20,default='absent')
    # ho_previous_treatment=serializers.CharField(max_length=20,default='absent')
    # PastHistoryDetails=serializers.CharField(max_length=5000,default='NA')
    
    # #
    # personal_developement=serializers.CharField(max_length=5000,default='NA')
    # learning_behavior=serializers.CharField(max_length=5000,default='NA')
    # behavior=serializers.CharField(max_length=5000,default='NA')
    # parenting_style=serializers.CharField(max_length=20,default='mixed')
    # BehavioralAndPersonalDetails=serializers.CharField(max_length=5000,default='NA')
    
    # #academic history
    # present_school_name=serializers.CharField(max_length=5000,default='NA')
    # school_board=serializers.CharField(max_length=5000,default='state')
    # school_medium=serializers.CharField(max_length=5000,default='english')
    # school_comments=serializers.CharField(max_length=5000,default='NA')
    # concerns_first_noticed_in=serializers.CharField(max_length=5000,default='NA')
    # attendance=serializers.CharField(max_length=5000,default='average')
    # liked_subjects=serializers.CharField(max_length=5000,default='NA')
    # unliked_subjects=serializers.CharField(max_length=5000,default='NA')
    # present_school_concerns=serializers.CharField(max_length=5000,default='NA')
    # tv_view_hrs=serializers.CharField(max_length=20,default='NA')
    # UnhealthyDietryHabits=serializers.CharField(max_length=5000,default='NA')
    # UnhealthySleepHabits=serializers.CharField(max_length=5000,default='NA')
    
    # weight=serializers.IntegerField(default=0)
    # height=serializers.IntegerField(default=0)
    # head_circumference=serializers.IntegerField(default=0)
    # skull_shape=serializers.CharField(max_length=5000,default='NA')
    # general_neurology=serializers.CharField(max_length=5000,default='NA')
    # general_neurology_details=serializers.CharField(max_length=5000,default='NA')
    # skin_exam=serializers.CharField(max_length=5000,default='NA')
    # joints=serializers.CharField(max_length=5000,default='NA')
    # neurology=serializers.CharField(max_length=5000,default='NA')
    # neurology_details=serializers.CharField(max_length=5000,default='NA')
    # hypertrophy_of_muscles=serializers.CharField(max_length=5000,default='NA')
    # abnormal_tone_pattern=serializers.CharField(max_length=5000,default='NA')
    # muscle_tone_neurology=serializers.CharField(max_length=5000,default='normal')
    # muscle_neurology=serializers.CharField(max_length=5000,default='NA')
    # muscle_neurology_details=serializers.CharField(max_length=5000,default='NA')
    # muscle_power_details=serializers.CharField(max_length=5000,default='NA')
    # deep_tendon_reflexes=serializers.CharField(max_length=5000,default='normal')
    # deep_tendon_reflexes_details=serializers.CharField(max_length=5000,default='NA')
    # coordination=serializers.CharField(max_length=5000,default='normal')
    # coordination_details=serializers.CharField(max_length=5000,default='NA')
    # abnormal_movements=serializers.CharField(max_length=5000,default='no')
    # abnormal_movements_details=serializers.CharField(max_length=5000,default='NA')
    # motor_deficit=serializers.CharField(max_length=5000,default='no')
    # gait=serializers.CharField(max_length=5000,default='NA')
    # balance=serializers.CharField(max_length=5000,default='developed for age')
    
    # #evaluation
    # visual_deficit=serializers.CharField(max_length=5000,default='NA')
    # hearing_deficit=serializers.CharField(max_length=5000,default='NA')
    # eye_contact=serializers.CharField(max_length=5000,default='NA')
    # motor_imitation_skills=serializers.CharField(max_length=5000,default='NA')
    # pointing_behaviors=serializers.CharField(max_length=5000,default='NA')
    # stereotypic_behaviors=serializers.CharField(max_length=5000,default='NA')
    # sensory_defensive_behaviors=serializers.CharField(max_length=5000,default='NA')
    # speech=serializers.CharField(max_length=5000,default='NA')
    # evaluationMChat=serializers.CharField(max_length=5000,default='NA')
    # development_screening=serializers.CharField(max_length=5000,default='NA')
    # gross_motor=serializers.CharField(max_length=5000,default='NA')
    # speech_screening=serializers.CharField(max_length=5000,default='NA')
    # fine_motor=serializers.CharField(max_length=5000,default='NA')
    # social_emotion=serializers.CharField(max_length=5000,default='NA')
    # learning_evaluation=serializers.CharField(max_length=5000,default='NA')
    # behavior_evaluation=serializers.CharField(max_length=5000,default='NA')
    
    # #impression
    # neurology_impression=serializers.CharField(max_length=5000,default='NA')
    # cerebral_palsy=serializers.CharField(max_length=5000,default='No')
    # cognitive_disability=serializers.CharField(max_length=5000,default='NA')
    # mental_retardation=serializers.CharField(max_length=5000,default='NA')
    # developement_impression=serializers.CharField(max_length=5000,default='NA')
    # learning_impression=serializers.CharField(max_length=5000,default='NA')
    # behavior_impression=serializers.CharField(max_length=5000,default='NA')
    
    # #plan
    # neurology_evaluation=serializers.CharField(max_length=5000,default='NA')
    # developement_evaluation=serializers.CharField(max_length=5000,default='NA')
    # learning_evaluation_plan=serializers.CharField(max_length=5000,default='NA')
    # special_education_intervention=serializers.CharField(max_length=5000,default='NA')
    # remedial_intervention=serializers.CharField(max_length=5000,default='NA')
    # behavioral_modification=serializers.CharField(max_length=5000,default='NA')
    # academic_suggestions=serializers.CharField(max_length=5000,default='NA')
    # followUpPlan=serializers.CharField(max_length=5000,default='NA')
    
    # #medical treatment
    # medical_treatment_plan=serializers.CharField(max_length=5000,default='NA')
    
    class Meta:
        model = AutisticData
        fields = '__all__'