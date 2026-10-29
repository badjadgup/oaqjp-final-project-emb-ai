const RunSentimentAnalysis = async () => {
    const text = document.getElementById("textToAnalyze").value;
    const output = document.getElementById("system_response");
    output.textContent = "Analyzing...";
    try {
        const response = await fetch("/emotionDetector?textToAnalyze=" + encodeURIComponent(text));
        if (!response.ok) throw new Error("Analysis service unavailable. Try again in the course lab.");
        output.textContent = await response.text();
    } catch (error) {
        output.textContent = error.message;
    }
};
