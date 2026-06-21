# Planning

## Community Overview

r/TrueFilm is a dedicated community for in-depth, analytical, and text-based discourse on cinema, prioritizing artistic intent, film theory, and formal mechanics over casual entertainment value.

## Labels

### Formal and Thematic Exegesis

Posts that structurally dissect a film's technical craftsmanship (such as blocking, framing, and cinematography) or its deeper philosophical, literary, and allegorical underpinnings.

- Cure (Kiyoshi Kurosawa, 1997) scene composition — Breaks down specific camera movements, static framing, and how character blocking communicates hypnotism within the frame.

- Barry Lyndon, The Sublime and Leo Tolstoy — Interrogates Kubrick's visual framing by connecting it directly to Tolstoy's literature and the Romantic movement's exploration of the sublime.

- Uncertain Case: Just watched Belladonna of sadness — The author attempts to grapple with the discomfort of gender dynamics and thematic framing, but the post remains largely a raw, subjective emotional reaction rather than a fully realized formal analysis.

### Narrative and Cultural Reception Commentary

Posts that focus primarily on the literal mechanics of plot logic, personal review scores, or meta-discourse regarding how audiences and critics are reacting to a film.

- Does the plot of Bladerunner make sense? — Focuses strictly on literal narrative continuity, questioning character motivations, identifying tracking methods, and pointing out apparent plot holes.

- Does anyone watch obsession actually thinking Bear is an innocent victim? — Discusses the online meta-discourse, audience "hot takes," and basic character morality surrounding a recent release rather than analyzing the film's structural form.

- Uncertain Case: Right now people are saying movies dying, I actually think audience IQ is growing. — While it tackles media literacy and audience reception trends, it acts as a macro-critique of the entire film industry and studio outputs rather than focusing on the narrative text or reception of an individual movie.

## Data Collection Plan

* Source Data: Public posts from the front page, top weekly feeds, and archival entries of [r/TrueFilm](https://www.reddit.com/r/TrueFilm/).
* Target Sample Size: 200 total examples, aiming for an approximate 50/50 split (~100 posts per label).
* I will explicitly search the subreddit for keywords associated with formal mechanics to selectively sample analytical posts and restore class balance.

## Evaluation Metrics

Accuracy, Per-Class Precision, Per-Class Recall, and F1-Score.

While **Accuracy** provides a general overview of model health, it doesn't reveal structural confusion. Because `reception_commentary` posts are often shorter and more conversational, a model might over-rely on vocabulary cues. Tracking **Precision** ensures the model isn't misclassifying casual reviews as deep exegesis, while **Recall** guarantees the model is actually identifying high-level formal analyses instead of filtering them out. The **F1-Score** will serve as our primary comparative baseline metric.

## Definition of Success

An overall macro F1-score of **$\ge 0.75$** for the fine-tuned model, and a minimum **10% absolute accuracy improvement** over the zero-shot Llama-3.3 baseline.

To be genuinely useful as a moderation assistant or content filter for a community like r/TrueFilm, the model must accurately separate structural film theory from conversational plot reviews without silencing borderline deep discussions.

## AI Tool Plan

* **Label Stress-Testing:** I will prompt an LLM with these two specific definitions and ask it to generate 5 highly ambiguous hypothetical posts sitting on the boundary line. I will use those generations to stress-test my explicit decision rule before annotating the final CSV.
* **Annotation Assistance:** I will use a zero-shot prompt to pre-label a subset of 50 posts to check initial alignment. However, I will manually read, audit, and finalize all 200 labels in the final dataset to prevent training on algorithmic bias.
* **Failure Analysis:** Post-evaluation, I will feed the misclassified text strings into an LLM to look for linguistic patterns (e.g., length penalties, presence of sarcasm, or hidden entities) that explain why the fine-tuned model misread the text.



🎯 Baseline accuracy: 0.976  (evaluated on 41/41 parseable responses)

Per-class metrics (baseline):
                      precision    recall  f1-score   support

     formal_exegesis       0.95      1.00      0.98        21
reception_commentary       1.00      0.95      0.97        20

            accuracy                           0.98        41
           macro avg       0.98      0.97      0.98        41
        weighted avg       0.98      0.98      0.98        41
