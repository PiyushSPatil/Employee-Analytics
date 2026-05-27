from backend.data_processing.loader import load_data, preview_data
from backend.data_processing.cleaner import clean_data
from backend.data_processing.feature_engineering import create_features

# Update path accordingly
file_path = "data/raw/employee_data.csv"


# Step 1: Load
df = load_data(file_path)

# Step 2: Preview
preview_data(df)

# Step 3: Clean
df = clean_data(df)

# Step 4: Feature Engineering
df = create_features(df)

# Final preview
print("\n✅ Final Data Preview:")
print(df.head())

from backend.analytics.performance_analysis import (
    skill_vs_performance,
    compare_high_low_performers,
    identify_top_performers
)

# Run analytics
correlation = skill_vs_performance(df)
comparison = compare_high_low_performers(df)
identify_top_performers(df)


from backend.llm_engine.insight_generator import generate_performance_insights

print("\n🤖 Generating AI Insights...\n")

generate_performance_insights(correlation, comparison)

from backend.analytics.attrition_analysis import (
    attrition_distribution,
    attrition_vs_factors,
    identify_high_risk_employees
)

print("\n📉 Running Attrition Analysis...\n")

attrition_dist = attrition_distribution(df)
attrition_factors = attrition_vs_factors(df)
high_risk = identify_high_risk_employees(df)


from backend.llm_engine.insight_generator import generate_attrition_insights

print("\n🤖 Generating Attrition Insights...\n")

generate_attrition_insights(attrition_dist, attrition_factors)


from backend.analytics.behavioral_analysis import (
    cluster_soft_skills,
    conflict_vs_teamwork,
    engagement_impact
)

from backend.llm_engine.insight_generator import generate_behavioral_insights

print("\n🧠 Running Behavioral Analysis...\n")

cluster_data = cluster_soft_skills(df)
conflict_data = conflict_vs_teamwork(df)
engagement_data = engagement_impact(df)

print("\n🤖 Generating Behavioral Insights...\n")

generate_behavioral_insights(cluster_data, conflict_data, engagement_data)


from backend.analytics.training_analysis import (
    training_vs_performance,
    mentor_impact_analysis,
    low_improvement_employees
)

from backend.llm_engine.insight_generator import generate_training_insights

print("\n🎓 Running Training Analysis...\n")

training_corr = training_vs_performance(df)
mentor_data = mentor_impact_analysis(df)
low_perf = low_improvement_employees(df)

print("\n🤖 Generating Training Insights...\n")

generate_training_insights(training_corr, mentor_data, low_perf)


from backend.analytics.project_analysis import (
    project_complexity_vs_performance,
    project_outcome_vs_performance,
    role_based_performance,
    success_but_low_performance
)

from backend.llm_engine.insight_generator import generate_project_insights

print("\n📁 Running Project Analysis...\n")

complexity = project_complexity_vs_performance(df)
success_corr = project_outcome_vs_performance(df)
role_data = role_based_performance(df)
contradiction = success_but_low_performance(df)

print("\n🤖 Generating Project Insights...\n")

generate_project_insights(complexity, success_corr, role_data, contradiction)


from backend.analytics.compensation_analysis import (
    salary_vs_performance,
    bonus_vs_performance,
    underpaid_high_performers,
    benefits_vs_attrition
)

from backend.llm_engine.insight_generator import generate_compensation_insights

print("\n💰 Running Compensation Analysis...\n")

salary_corr = salary_vs_performance(df)
bonus_corr = bonus_vs_performance(df)
underpaid = underpaid_high_performers(df)
benefits = benefits_vs_attrition(df)

print("\n🤖 Generating Compensation Insights...\n")

generate_compensation_insights(salary_corr, bonus_corr, underpaid, benefits)

from backend.analytics.recruitment_analysis import (
    hiring_source_analysis,
    recruitment_cost_vs_performance,
    time_to_hire_analysis,
    high_cost_low_performance,
    conversion_by_source
)

from backend.llm_engine.insight_generator import generate_recruitment_insights

print("\n📥 Running Recruitment Analysis...\n")

source_perf = hiring_source_analysis(df)
cost_corr = recruitment_cost_vs_performance(df)
time_corr = time_to_hire_analysis(df)
high_cost = high_cost_low_performance(df)
conversion = conversion_by_source(df)

print("\n🤖 Generating Recruitment Insights...\n")

generate_recruitment_insights(
    source_perf,
    cost_corr,
    time_corr,
    high_cost,
    conversion
)


from backend.analytics.advanced_performance_analysis import (
    calculate_weighted_score,
    high_perf_low_leadership,
    compare_extreme_performers,
    skill_project_mismatch,
    ideal_employee_profile
)

from backend.llm_engine.insight_generator import generate_advanced_performance_insights

print("\n🧠 Running Advanced Performance Analysis...\n")

df = calculate_weighted_score(df)

leadership = high_perf_low_leadership(df)
comparison = compare_extreme_performers(df)
mismatch = skill_project_mismatch(df)
profile = ideal_employee_profile(df)

print("\n🤖 Generating Advanced Insights...\n")

generate_advanced_performance_insights(
    df,
    comparison,
    leadership,
    mismatch,
    profile
)


from backend.analytics.training_analysis import predict_training_benefit, training_program_comparison
from backend.analytics.attrition_analysis import attrition_risk_profile
from backend.analytics.project_analysis import project_success_factors
from backend.analytics.recruitment_analysis import hiring_source_retention
from backend.llm_engine.insight_generator import generate_final_insights

print("\n🧠 Running Final Intelligence Layer...\n")

training_pred = predict_training_benefit(df)
training_prog = training_program_comparison(df)

attrition_risk = attrition_risk_profile(df)
success = project_success_factors(df)
retention = hiring_source_retention(df)

print("\n🤖 Generating Final Decision Insights...\n")

generate_final_insights(training_pred, attrition_risk, success, retention)