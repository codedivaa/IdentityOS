import re


TECHNOLOGIES = [
    "Python",
    "React",
    "FastAPI",
    "Docker",
    "Git",
    "SQL",
    "JavaScript",
    "TypeScript",
    "Machine Learning",
    "AI",
    "TensorFlow",
    "PyTorch",
    "OpenCV",
    "MediaPipe",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "Flask",
    "Django",
    "AWS",
    "Azure",
    "MongoDB",
    "PostgreSQL",
]


def analyze(text):

    lower = text.lower()

    technologies = []

    for tech in TECHNOLOGIES:
        if tech.lower() in lower:
            technologies.append(tech)

    technologies = sorted(set(technologies))

    project_words = [
        "built",
        "developed",
        "created",
        "implemented",
        "designed",
    ]

    achievement_words = [
        "won",
        "award",
        "hackathon",
        "rank",
        "leaderboard",
        "achievement",
    ]

    leadership_words = [
        "lead",
        "led",
        "mentor",
        "managed",
        "organized",
    ]

    communication_words = [
        "team",
        "presentation",
        "presented",
        "collaborated",
        "communication",
    ]

    projects = sum(lower.count(word) for word in project_words)
    achievements = sum(lower.count(word) for word in achievement_words)
    leadership = sum(lower.count(word) for word in leadership_words)
    communication_hits = sum(lower.count(word) for word in communication_words)

    execution = min(100, 40 + projects * 10)

    learning = min(100, 40 + len(technologies) * 4)

    communication = min(100, 40 + communication_hits * 10)

    creativity = min(
        100,
        50
        + lower.count("design") * 8
        + lower.count("ui") * 5
        + lower.count("ux") * 5,
    )

    score = int(
        (
            execution
            + learning
            + communication
            + creativity
        )
        / 4
    )

    # -------- Archetype --------

    if {"Python", "React", "FastAPI"}.issubset(technologies):
        archetype = "Full Stack AI Engineer"

    elif "AI" in technologies or "Machine Learning" in technologies:
        archetype = "AI Builder"

    elif "React" in technologies:
        archetype = "Creative Engineer"

    elif "FastAPI" in technologies or "Flask" in technologies:
        archetype = "Backend Architect"

    else:
        archetype = "Software Builder"

    # -------- Alias --------

    if archetype == "Full Stack AI Engineer":
        alias = "AI Product Builder"

    elif archetype == "AI Builder":
        alias = "Neural Architect"

    elif archetype == "Creative Engineer":
        alias = "Pixel Engineer"

    elif archetype == "Backend Architect":
        alias = "System Architect"

    else:
        alias = "Digital Builder"

    # -------- Reputation --------

    if projects >= 4:
        reputation = "Known for shipping practical software."

    elif achievements >= 2:
        reputation = "Turns ambitious ideas into working products."

    elif communication_hits >= 2:
        reputation = "Strong technical communicator."

    else:
        reputation = "Consistently building and learning."

    # -------- Recommendations --------

    recommendations = []

    if "AWS" not in technologies:
        recommendations.append("Learn AWS")

    if "Docker" not in technologies:
        recommendations.append("Learn Docker")

    if "Testing" not in lower:
        recommendations.append("Write automated tests")

    if "Open Source" not in lower and "opensource" not in lower:
        recommendations.append("Contribute to Open Source")

    if not recommendations:
        recommendations.append("Keep shipping projects")

    return {
        "alias": alias,
        "archetype": archetype,
        "reputation": reputation,
        "skills": technologies,
        "execution": execution,
        "creativity": creativity,
        "learning": learning,
        "communication": communication,
        "score": score,
        "recommendations": recommendations,
        "projects": projects,
        "achievements": achievements,
    }