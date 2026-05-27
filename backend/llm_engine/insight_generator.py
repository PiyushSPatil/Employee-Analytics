from backend.llm_engine.groq_client import get_llm_response
from backend.llm_engine.prompt_builder import build_performance_prompt

def generate_performance_insights(correlation, comparison):
    """
    Generate AI insights using LLM
    """

    prompt = build_performance_prompt(correlation, comparison)

    response = get_llm_response(prompt)

    print("\n🤖 AI Generated Insights:\n")
    print(response)

    return response


def generate_attrition_insights(distribution, factors):

    from backend.llm_engine.prompt_builder import build_attrition_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_attrition_prompt(distribution, factors)

    response = get_llm_response(prompt)

    print("\n🤖 Attrition AI Insights:\n")
    print(response)

    return response


def generate_behavioral_insights(cluster_data, conflict_data, engagement_data):

    from backend.llm_engine.prompt_builder import build_behavioral_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_behavioral_prompt(cluster_data, conflict_data, engagement_data)

    response = get_llm_response(prompt)

    print("\n🤖 Behavioral AI Insights:\n")
    print(response)

    return response

def generate_training_insights(training_corr, mentor_data, low_perf):

    from backend.llm_engine.prompt_builder import build_training_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_training_prompt(training_corr, mentor_data, len(low_perf))

    response = get_llm_response(prompt)

    print("\n🤖 Training AI Insights:\n")
    print(response)

    return response

def generate_project_insights(complexity, success_corr, role_data, contradiction):

    from backend.llm_engine.prompt_builder import build_project_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_project_prompt(
        complexity,
        success_corr,
        role_data,
        len(contradiction)
    )

    response = get_llm_response(prompt)

    print("\n🤖 Project AI Insights:\n")
    print(response)

    return response

def generate_compensation_insights(salary_corr, bonus_corr, underpaid, benefits):

    from backend.llm_engine.prompt_builder import build_compensation_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_compensation_prompt(
        salary_corr,
        bonus_corr,
        len(underpaid),
        benefits
    )

    response = get_llm_response(prompt)

    print("\n🤖 Compensation AI Insights:\n")
    print(response)

    return response

def generate_recruitment_insights(source_perf, cost_corr, time_corr, high_cost, conversion):

    from backend.llm_engine.prompt_builder import build_recruitment_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_recruitment_prompt(
        source_perf,
        cost_corr,
        time_corr,
        len(high_cost),
        conversion
    )

    response = get_llm_response(prompt)

    print("\n🤖 Recruitment AI Insights:\n")
    print(response)

    return response

def generate_advanced_performance_insights(df, comparison, leadership, mismatch, profile):

    from backend.llm_engine.prompt_builder import build_advanced_performance_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_advanced_performance_prompt(
        "Weighted model applied",
        len(leadership),
        comparison,
        len(mismatch),
        profile
    )

    response = get_llm_response(prompt)

    print("\n🤖 Advanced Performance Insights:\n")
    print(response)

    return response


def generate_final_insights(training_pred, attrition_risk, success, retention):

    from backend.llm_engine.prompt_builder import build_final_intelligence_prompt
    from backend.llm_engine.groq_client import get_llm_response

    prompt = build_final_intelligence_prompt(
        len(training_pred),
        len(attrition_risk),
        success,
        retention
    )

    response = get_llm_response(prompt)

    print("\n🤖 Final Decision Intelligence:\n")
    print(response)

    return response