def calculate_aggregate_score(scores, weights):
    """
    Calculate the aggregate score for each project based on the individual scores and the weights for each category.

    :param scores: A dictionary of scores for each project. Each key is the project name and the value is a list of scores.
    :param weights: A list of weights for each category in the same order as the scores.
    :return: A dictionary with the project names and their aggregate scores.
    """
    aggregate_scores = {}
    for project, project_scores in scores.items():
        # Calculate the weighted score
        weighted_score = sum(score * weight for score, weight in zip(project_scores, weights)) / sum(weights)
        aggregate_scores[project] = round(weighted_score, 2)
    return aggregate_scores

# Scores for each project in the order: Career Aspects, Technical Viability, Data Availability, Publishing/Impact
project_scores = {
    "Machine Learning Arbitrage Discovery in Financial Markets with Graph Neural Networks": [9, 9, 7, 9],
    "Reinsurance Markets & Climate Change": [7, 8, 8, 9],
    "Deflation Prediction in Generative AI": [9, 9, 7, 8],
    "Generative AI - Mini Economies": [10, 10, 9, 10]
}

# Example weights for each category: Career Aspects, Technical Viability, Data Availability, Publishing/Impact
weights = [1.5, 1, 1, 1.1]  # Default weights (equal importance)

# Calculate the aggregate scores with the default weights
aggregate_scores = calculate_aggregate_score(project_scores, weights)
print(aggregate_scores)