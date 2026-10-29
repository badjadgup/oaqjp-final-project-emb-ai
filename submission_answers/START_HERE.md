# Submission guide: all 16 boxes

Code answers are ready to copy from the .txt files listed below. Paste only their
contents, without Markdown fences. Terminal answers and screenshots must come
from your actual run; no invented transcripts or service scores are included.

## Publish correctly first (Q1 and Q6)

1. Sign in to GitHub and fork https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai
2. Keep the fork PUBLIC and its name exactly `oaqjp-final-project-emb-ai`.
3. Upload this folder's contents into that fork's root and commit them. Do not
   upload the enclosing folder, ZIP, or .git directory. Keep the starter LICENSE.
4. Confirm README starts with `# Final Project` and the default branch is `main`.
5. Replace YOUR_USERNAME below with your own GitHub username. Open both links to
   confirm they work while signed out. Use the actual branch if it isn't main.

Q1 (README URL):
https://github.com/YOUR_USERNAME/oaqjp-final-project-emb-ai/blob/main/README.md

Q6 (package __init__.py URL):
https://github.com/YOUR_USERNAME/oaqjp-final-project-emb-ai/blob/main/EmotionDetection/__init__.py

## Box-by-box key

| Question | What to paste or upload |
|---|---|
| 1 | Your README URL above, after publishing |
| 2 | Contents of 2a_emotion_detection.txt (initial version returns response.text) |
| 3 | Actual terminal session from the Q3 steps below |
| 4 | Contents of 3a_output_formatting.txt |
| 5 | Actual terminal command and printed dictionary from Q5 below |
| 6 | Your __init__.py URL above, after publishing |
| 7 | Exact command AND actual printed dictionary from Q7 below |
| 8 | Contents of 5a_unit_testing.txt |
| 9 | Actual command and all unit-test output from Q9 below |
| 10 | Contents of 6a_server.txt |
| 11 | Actual browser screenshot named 6b_deployment_test.png |
| 12 | Contents of 7a_error_handling_function.txt |
| 13 | Contents of 7b_error_handling_server.txt |
| 14 | Actual browser screenshot named 7c_error_handling_interface.png |
| 15 | Contents of 8a_server_modified.txt |
| 16 | Actual pylint command and score from Q16 below |

## Run in the course's Skills Network Linux lab

Clone YOUR fork into the required location. If /home/project/final_project already
exists, use it and copy/update files there instead of cloning over it.

```bash
cd /home/project
git clone https://github.com/YOUR_USERNAME/oaqjp-final-project-emb-ai.git final_project
cd /home/project/final_project
python3 -m pip install -r requirements.txt
```

### Q3: 2b_application_creation

Run these commands from the integrated terminal. Include the terminal prompt
showing `/home/project/final_project`, the Python prompts, responses, and test
summary when copying the transcript. The final version's top-level compatibility
module supports the exact import required by this question. Q2 separately shows
the earlier raw-response function; do not overwrite the final package with it.

```text
python3
from emotion_detection import emotion_detector
print(emotion_detector('I am really mad about this'))
exit()
python3 test_emotion_detection.py
```

The middle four lines are entered inside Python, not as shell commands.
Save the real session as `2b_application_creation.txt` and paste its contents.

### Q5: 3b_formatted_output_test

```bash
python3 -c "from emotion_detection import emotion_detector; print(emotion_detector('I am really mad about this'))"
```

Copy the command and result, including all five scores and dominant_emotion.
Save as `3b_formatted_output_test.txt`.

### Q7: 4b_packaging_test

Use this exact command, and include it in the answer with the actual output:

```bash
python3 -c "from EmotionDetection.emotion_detection import emotion_detector; print(emotion_detector('I am very angry'))"
```

Check the output has five scores and `'dominant_emotion': 'anger'`.
Save as `4b_packaging_test.txt`.

### Q9: 5b_unit_testing_result

```bash
python3 test_emotion_detection.py
```

Paste the real command, the five test indicators, `Ran 5 tests ...`, and `OK`.
These are live service tests. If the endpoint fails, resolve access in the lab
before submission. Do not substitute the offline verification output.

### Q11 and Q14: interface screenshots

```bash
python3 server.py
```

Open the lab's application launch/preview feature on port 5000 (or
http://localhost:5000 when running locally with service access).

For Q11, enter `I am really mad about this`, click Run Sentiment Analysis, and
wait for five scores and dominant emotion anger. Capture the BROWSER PAGE with
both the input and real result visible as `6b_deployment_test.png`.

For Q14, clear the input, click the button, and capture the BROWSER PAGE with
the empty field and `Invalid Input! Please try again.` visible as
`7c_error_handling_interface.png`. A terminal or editor screenshot is insufficient.

### Q16: 8b_static_code_analysis

In a second terminal, from /home/project/final_project:

```bash
python3 -m pylint server.py
```

Copy the actual command and full output, including its score, to
`8b_static_code_analysis.txt`. Local validation notes in this package are for
reference; they do not replace the required lab transcript.

## Why these corrections matter

The real Watson response contains `emotionPredictions[0].emotion`. Reading
`data.get('text')` as in your attempt can silently yield five zero scores and an
incorrect dominant emotion. The code here reads the actual nested response and
handles HTTP 400 by returning six None values.

The assessment explicitly requests different versions of the function at
different stages. Use the matching answer file rather than pasting the final
function into every box. No specific grade can be guaranteed.
