# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  - Bug 1: hints were backwards: when I type 10 it said lower, though the answer should be 42
  - Bug 2: Attempts were unsynchronized/not synchronized properly
  - Bug 3: The answer already revealed itself
  - Bug 4: Only add the previous guess into history after the second guess and after
  - Bug 5: Not renewing the game properly
  - Bug 6: When I switch into Easy (range 1-20), Hard (range 1-50) the secret is out of scope (99)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

- I use Copilot exclusively
- One correct instance could be when it tried to fix the Higher/Lower syntax. I tested it by inputing a number and the output was correct.
- One incorrect instance is when Copilot failed to detect why the new game button doesn't work properly. It suggested fixing the "secret" section of code (#error 6) but I found out it's because the new_game button has an issue.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
- By running the command line again
- One test I ran was using a number outside of accepted scope, and before it didn't work properly but now it has.
- Not really. I do them myself.

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
- Streamlit reruns your entire Python script from top to bottom.
- Session State is a sticky note on the side of the easel that the artist doesn't throw away.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

- One habit is to look at the code more carefully before utilizing AI
- I will read all the code first before asking Copilot as that will safe more time
- AI code often contains major bugs. We as developers must learn how to understand and fix them properly
