#!/usr/bin/env python2
from model import Model

population_density = 0.5
students_to_speakers_ratio = 20
speaker_range = 2

expected_student_diplomacy = 50
expected_speaker_diplomacy = 75
expected_abs_student_ideology = 30
expected_abs_speaker_ideology = 80

student_diplomacy_std_deviation = 25
speaker_diplomacy_std_deviation = 25
student_ideology_std_deviation = 25
speaker_ideology_std_deviation = 25

test_model = Model(
	population_density,
    students_to_speakers_ratio,
    speaker_range,

    expected_student_diplomacy,
    expected_speaker_diplomacy,
    expected_abs_student_ideology,
    expected_abs_speaker_ideology,

    student_diplomacy_std_deviation,
    speaker_diplomacy_std_deviation,
    student_ideology_std_deviation,
    speaker_ideology_std_deviation)
test_model.run_model()
