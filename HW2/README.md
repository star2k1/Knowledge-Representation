# Homework: LLM Reasoning Task Experimentation

## Objective

Compare the performance of multiple LLMs, each in two categories: **standard** and **reasoning** mode, on a set of inference tasks. The goal is to identify the complexity level at which each model begins to fail and to assess how reasoning mode improves performance.

## Methodology

1.  **LLM Selection:**

    - Include the following AI chats (free tier):
      - [ChatGPT](chatgpt.com)
      - [Copilot](copilot.microsoft.com)
      - [Grok](grok.com)
      - [DeepSeek](chat.deepseek.com)
      - [Claude](claude.ai)
      - [Mistral](chat.mistral.ai)
      - [Gemini](gemini.google.com)

2.  **Experimentation:**

    - For each task, query each LLM in both standard and reasoning mode if available.
    - Record the prompts and the responses.
    - Repeat twice for confirmation.

3.  **Analysis:**
    - Analyze weaknesses, compare the models based on the results.

## Task 1

### Prompt 1

`John had three apples. Mike has two pears. Pears and apples are fruits. Mike eats two pears. Mike gives all his fruits to John. John eats one apple. How many fruits does John have?`

### Results

| Model    | Model                      | Response | Correctness |
| -------- | -------------------------- | -------- | ----------- |
| ChatGPT  | GPT-4o                     | 2        | ✅          |
| ChatGPT  | OpenAI o3-mini (Reasoning) | 2        | ✅          |
| Copilot  | GPT-4                      | 2        | ✅          |
| Copilot  | OpenAI o1 (Reasoning)      | 2        | ✅          |
| Grok     | Grok 3                     | 2        | ✅          |
| Grok     | Grok 3 (Reasoning)         | 2        | ✅          |
| DeepSeek | V3                         | 2        | ✅          |
| DeepSeek | R1 (Reasoning)             | 2        | ✅          |
| Claude   | Sonnet 3.7                 | 2        | ✅          |
| Claude   | Sonnet 3.7 (Reasoning)     | N/A      | N/A         |
| Mistral  | Mistral Large              | 2        | ✅          |
| Mistral  | Mistral Large (Reasoning)  | N/A      | N/A         |
| Gemini   | 2.0 Flash                  | 2        | ✅          |
| Gemini   | 2.0 Flash (Reasoning)      | 2        | ✅          |

### Prompt 2

## Task 2 (Artificial language)

### Prompt 1

```
Here are some words translated from an artificial language. kingibing means cake decoration; tolobing means cake topping; kingiohoo means christmas decoration. Which word could mean “christmas tree”?

a) kingitringo
b) gringobing
c) ohookingo
d) zuzuohoo
```

### Results

| Model    | Model                      | Response    | Correctness |
| -------- | -------------------------- | ----------- | ----------- |
| ChatGPT  | GPT-4o                     | ohookingo   | ❌          |
| ChatGPT  | OpenAI o3-mini (Reasoning) | kingitringo | ❌          |
| Copilot  | GPT-4                      | ohookingo   | ❌          |
| Copilot  | OpenAI o1 (Reasoning)      | zuzuohoo    | ✅          |
| Grok     | Grok 3                     | ohookingo   | ❌          |
| Grok     | Grok 3 (Reasoning)         | ohookingo   | ❌          |
| DeepSeek | V3                         | zuzuohoo    | ✅          |
| DeepSeek | R1 (Reasoning)             | zuzuohoo    | ✅          |
| Claude   | Sonnet 3.7                 | zuzuohoo    | ✅          |
| Claude   | Sonnet 3.7 (Reasoning)     | N/A         | N/A         |
| Mistral  | Mistral Large              | ohookingo   | ❌          |
| Mistral  | Mistral Large (Reasoning)  | N/A         | N/A         |
| Gemini   | 2.0 Flash                  | ohookingo   | ❌          |
| Gemini   | 2.0 Flash (Reasoning)      | ohookingo   | ❌          |

### Prompt 2 (Simplified by matching order of words)

```
Here are some words translated from an artificial language. bingkingi means cake decoration; bingtolo means cake topping; ohookingi means christmas decoration. Which word could mean “christmas tree”?

a) tringokingi
b) binggringo
c) kingoohoo
d) ohoozuzu
```

### Results

| Model    | Model                      | Response  | Correctness |
| -------- | -------------------------- | --------- | ----------- |
| ChatGPT  | GPT-4o                     | kingoohoo | ❌          |
| ChatGPT  | OpenAI o3-mini (Reasoning) | ohoozuzu  | ✅          |
| Copilot  | GPT-4                      | kingoohoo | ❌          |
| Copilot  | OpenAI o1 (Reasoning)      | ohoozuzu  | ✅          |
| Grok     | Grok 3                     | ohoozuzu  | ✅          |
| Grok     | Grok 3 (Reasoning)         | ohoozuzu  | ✅          |
| DeepSeek | V3                         | ohoozuzu  | ✅          |
| DeepSeek | R1 (Reasoning)             | ohoozuzu  | ✅          |
| Claude   | Sonnet 3.7                 | ohoozuzu  | ✅          |
| Claude   | Sonnet 3.7 (Reasoning)     | N/A       | N/A         |
| Mistral  | Mistral Large              | ohoozuzu  | ✅          |
| Mistral  | Mistral Large (Reasoning)  | N/A       | N/A         |
| Gemini   | 2.0 Flash                  | ohoozuzu  | ✅          |
| Gemini   | 2.0 Flash (Reasoning)      | ohoozuzu  | ✅          |

## Task 3 ([Theme detection](https://www.examveda.com/the-attainment-of-individual-and-organisational-goals-is-mutually-interdependent-and-linked-by-a-common-denominator-employee-work-motivation-organisational-members-are-motivated-to-satisfy-their-personal-goals-and-20094/))

### Prompt 1

```
The attainment of individual and organisational goals is mutually interdependent and linked by a common denominator - employee work motivation. Organisational members are motivated to satisfy their personal goals, and they contribute their efforts to the attainment of organisational objectives as means of achieving these personal goals.

The passage best supports the statement that motivation:

A) encourages an individual to give priority to personal goals over organisational goals.

B) is crucial for the survival of an individual and organisation.

C) is the product of an individual.

D) is the external force which induces an individual to contribute his efforts.

E) makes organisation and society inseparable.
```

### Results

| Model    | Model                      | Response | Correctness |
| -------- | -------------------------- | -------- | ----------- |
| ChatGPT  | GPT-4o                     | B        | ❌          |
| ChatGPT  | OpenAI o3-mini (Reasoning) | D        | ❌          |
| Copilot  | GPT-4                      | D        | ❌          |
| Copilot  | OpenAI o1 (Reasoning)      | D        | ❌          |
| Grok     | Grok 3                     | B        | ❌          |
| Grok     | Grok 3 (Reasoning)         | B        | ❌          |
| DeepSeek | V3                         | D        | ❌          |
| DeepSeek | R1 (Reasoning)             | D        | ❌          |
| Claude   | Sonnet 3.7                 | B        | ❌          |
| Claude   | Sonnet 3.7 (Reasoning)     | N/A      | N/A         |
| Mistral  | Mistral Large              | B        | ❌          |
| Mistral  | Mistral Large (Reasoning)  | N/A      | N/A         |
| Gemini   | 2.0 Flash                  | B        | ❌          |
| Gemini   | 2.0 Flash (Reasoning)      | A/C      | ❌          |

## Analysis Summary

### Failure Points

- **Claude** and **Mistral** struggled with tasks requiring deeper inference, especially in the absence of reasoning mode.
- **Gemini** and **Mistral** showed incorrect results for medium-complexity tasks like counting letters in "senselessness."
- Artificial language tasks revealed weaknesses in **ChatGPT** and **Grok** in standard mode, while **Copilot** showed improvement with reasoning mode.

- **On the theme detection** (reading comprehension/inference) task, **all models failed** to select the correct answer, regardless of reasoning mode, indicating a shared limitation in nuanced inference from text.

### Strongest and Weakest Models

- **Strongest Models:** **DeepSeek** and **Copilot** (with reasoning) performed consistently well, showing high accuracy across all tasks except the theme detection/inference task. **Grok** also performed well but with longer processing times.
- **Weakest Models:** **Claude** and **Mistral** were the weakest, lacking reasoning mode and struggling with complex or nuanced tasks.

### Impact of Reasoning

Reasoning mode significantly improved results for models like **ChatGPT**, **Grok**, **Copilot**, and **Gemini** on structured or pattern-based tasks (e.g., artificial language, counting letters). However, reasoning mode did not help any model solve the theme detection/inference task, showing its current limitations.

### Reasoning Time

Reasoning mode introduced noticeable latency:

- **ChatGPT:** ~3–211 seconds depending on task complexity
- **Copilot:** ~3–20 seconds, showing efficient reasoning times
- **Grok:** ~46–138 seconds, with longer delays for complex tasks
- **DeepSeek:** ~19–137 seconds, balancing accuracy and speed
- **Gemini:** Fast reasoning with mixed accuracy

### Conclusion

Reasoning mode improves accuracy for structured and pattern-based tasks but does not enable LLMs to solve more abstract or nuanced inference tasks such as theme detection from text. Currently, LLMs are strong at direct pattern recognition and compositional reasoning, but struggle with deeper, context-dependent inference and reading comprehension that requires subtle understanding or synthesis.
