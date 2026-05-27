def build_performance_prompt(correlation, comparison):

    prompt = f"""
You are a senior HR data consultant.

STRICT RULES:
- Use ONLY the given data
- DO NOT assume anything not supported
- CHALLENGE wrong business assumptions
- If recommendation contradicts data, DO NOT give it

--- DATA ---

Correlation Matrix:
{correlation}

High vs Low Performer Comparison:
{comparison}

--- TASKS ---

1. Identify TRUE relationships (based on numbers)
2. Highlight contradictions
3. Identify flawed assumptions in current system
4. DO NOT recommend improving skills if they don’t affect performance
5. Provide BUSINESS DECISIONS (not generic suggestions)

--- OUTPUT FORMAT ---

Key Insights:
(Data-backed only)

Critical Findings:
(What is WRONG in current system)

Business Impact:
(Consequences of this issue)

Recommendations:
(ONLY data-supported decisions)
"""
    return prompt


def build_attrition_prompt(distribution, factors):

    prompt = f"""
You are a senior HR consultant.

STRICT RULES:
- Use ONLY given data
- DO NOT assume statistical significance unless tested
- Do NOT exaggerate findings
- Be precise and data-driven

--- DATA ---

Attrition Distribution:
{distribution}

Factor Analysis:
{factors}

--- TASKS ---

1. Identify actual drivers of attrition
2. Compare differences (but DO NOT assume statistical significance)
3. Identify strongest factor based on magnitude difference
4. Avoid exaggeration like "major problem" unless clearly supported
5. Give precise business recommendations

--- OUTPUT FORMAT ---

Key Insights:
(Data-based observations)

Critical Findings:
(What actually influences attrition)

Business Impact:
(Realistic interpretation)

Recommendations:
(Actionable and justified)
"""
    return prompt


def build_behavioral_prompt(cluster_data, conflict_data, engagement_data):

    prompt = f"""
You are a senior HR behavioral analyst.

STRICT RULES:
- Use ONLY the exact data provided
- DO NOT assume departments, percentages, or correlations unless explicitly given
- DO NOT calculate percentages unless numbers are provided
- If something is not present, say "data not available"

--- DATA ---

Cluster Distribution:
{cluster_data["Soft_Skill_Cluster"].value_counts()}

Conflict Cases Count:
{len(conflict_data)}

Engagement Data:
{engagement_data}

--- TASKS ---

1. Describe behavioral clusters using ONLY given counts
2. Explain conflict vs teamwork contradictions
3. Analyze engagement impact (based only on given values)
4. DO NOT invent patterns or assumptions

--- OUTPUT FORMAT ---

Key Insights:
Critical Findings:
Business Impact:
Recommendations:
"""
    return prompt


def build_training_prompt(training_corr, mentor_data, low_perf_count):

    prompt = f"""
You are a senior HR training consultant.

STRICT RULES:
- Use ONLY the given data
- Highlight the MOST important insight (do not ignore it)
- DO NOT downplay large numbers
- Avoid generic recommendations
- Focus on business decisions

--- DATA ---

Training vs Performance Correlation:
{training_corr}

Mentor Impact:
{mentor_data}

Employees with High Training but Low Performance:
{low_perf_count}

--- TASKS ---

1. Identify the strongest insight in the data
2. Evaluate if training is effective
3. Identify inefficiencies (especially large numbers)
4. Give business-level conclusions
5. Provide specific, actionable recommendations

--- OUTPUT FORMAT ---

Key Insights:
Critical Findings:
Business Impact:
Recommendations:
"""
    return prompt


def build_project_prompt(complexity_data, outcome_data, role_data, contradiction_count):

    prompt = f"""
You are a senior project performance consultant.

STRICT RULES:
- Use ONLY given data
- DO NOT claim correlation if differences are small
- Highlight strongest contradiction clearly
- Avoid generic recommendations
- Focus on decision-level insights

--- DATA ---

Project Complexity vs Performance:
{complexity_data}

Project Outcome vs Performance:
{outcome_data}

Role-Based Performance:
{role_data}

Successful Projects but Low Performance Count:
{contradiction_count}

--- TASKS ---

1. Evaluate if project complexity truly impacts performance
2. Analyze project outcome vs performance (highlight contradictions)
3. Identify role-based differences
4. Highlight strongest inconsistency in system
5. Provide strong business conclusions

--- OUTPUT FORMAT ---

Key Insights:
Critical Findings:
Business Impact:
Recommendations:
"""
    return prompt

def build_compensation_prompt(salary_corr, bonus_corr, underpaid_count, benefits_data):

    prompt = f"""
You are a senior HR compensation strategist.

STRICT RULES:
- Use ONLY the given data
- Highlight the MOST critical inefficiency
- DO NOT interpret underpayment as cost saving
- Avoid generic statements
- Focus on risk and business impact

--- DATA ---

Salary vs Performance Correlation:
{salary_corr}

Bonus vs Performance Correlation:
{bonus_corr}

Underpaid High Performers:
{underpaid_count}

Benefits vs Attrition:
{benefits_data}

--- TASKS ---

1. Evaluate if compensation aligns with performance
2. Identify the biggest compensation problem
3. Assess retention risk
4. Highlight strongest inefficiency
5. Provide strategic recommendations

--- OUTPUT FORMAT ---

Key Insights:
Critical Findings:
Business Impact:
Recommendations:
"""
    return prompt

def build_recruitment_prompt(source_perf, cost_corr, time_corr, high_cost_count, conversion_data):

    prompt = f"""
You are a senior hiring strategy consultant.

STRICT RULES:
- Use ONLY the given data
- DO NOT claim differences if values are very close
- Highlight the biggest inefficiency clearly
- Avoid recommending budget increase without strong evidence
- Focus on cost inefficiency and hiring quality
- DO NOT claim superiority if values are close

--- DATA ---

Hiring Source vs Performance:
{source_perf}

Recruitment Cost vs Performance:
{cost_corr}

Time to Hire vs Performance:
{time_corr}

High Cost Low Performance Hires:
{high_cost_count}

Conversion Rate by Source:
{conversion_data}

--- TASKS ---

1. Evaluate if hiring source really matters
2. Analyze cost effectiveness of hiring
3. Identify biggest inefficiency
4. Avoid misleading comparisons
5. Provide strong hiring strategy

--- OUTPUT FORMAT ---

Key Insights:
Critical Findings:
Business Impact:
Recommendations:
"""
    return prompt

def build_advanced_performance_prompt(weighted_info, leadership_count, comparison, mismatch_count, profile):

    prompt = f"""
You are a senior HR analytics expert.

STRICT RULES:
- Use ONLY given data
- Focus on reasoning, not correlation
- Identify contradictions and patterns

--- DATA ---

Weighted Score Model: {weighted_info}

High Performance but Low Leadership Count:
{leadership_count}

Rating 10 vs 5 Comparison:
{comparison}

High Skill but Failed Projects:
{mismatch_count}

Ideal Employee Profile:
{profile}

--- TASKS ---

1. Explain what drives high performance
2. Identify leadership gaps
3. Compare extreme performers
4. Explain skill-performance contradictions
5. Define ideal employee characteristics

--- OUTPUT FORMAT ---

Key Insights:
Critical Findings:
Business Impact:
Recommendations:
"""
    return prompt


def build_final_intelligence_prompt(training_pred, attrition_risk, success_factors, retention):

    prompt = f"""
You are a senior HR decision strategist.

STRICT RULES:
- Use ONLY given data
- Focus on prediction and decision making
- Highlight risks and opportunities

--- DATA ---

Training Beneficiaries:
{training_pred}

Attrition Risk:
{attrition_risk}

Project Success Factors:
{success_factors}

Hiring Source Retention:
{retention}

--- TASKS ---

1. Predict which employees should be trained
2. Identify high-risk employees
3. Define success factors for projects
4. Evaluate hiring impact on retention
5. Provide decision-level recommendations

--- OUTPUT FORMAT ---

Key Insights:
Critical Findings:
Business Impact:
Recommendations:
"""
    return prompt