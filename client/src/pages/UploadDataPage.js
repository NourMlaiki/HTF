import React, { useState } from "react";

function UploadData() {
  const [inputData, setInputData] = useState("");
  const [analysisResult, setAnalysisResult] = useState("");

  const handleAnalyze = async () => {
    if (!inputData) {
      alert("Please enter some text.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:5000/analyze/data", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data: inputData }),
      });

      const data = await response.json();
      setAnalysisResult(data.summary || "No analysis received.");
    } catch (error) {
      console.error("Error:", error);
      setAnalysisResult("Failed to analyze text.");
    }
  };

  return (
    <div>
      <h2>Enter Text for AI Analysis</h2>
      <textarea
        value={inputData}
        onChange={(e) => setInputData(e.target.value)}
        placeholder="Enter data to analyze..."
      />
      <button onClick={handleAnalyze}>Analyze</button>
      {analysisResult && (
        <div>
          <h3>AI Summary:</h3>
          <p>{analysisResult}</p>
        </div>
      )}
    </div>
  );
}

export default UploadData;
