import React, { useState } from "react";

function ImageAnalysisTab() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleAnalyze = async () => {
    if (!selectedFile) return;

    const formData = new FormData();
    formData.append("image", selectedFile);

    try {
      const res = await fetch("http://127.0.0.1:5000/analyze/image", {
        method: "POST",
        body: formData,
      });
      const data = await res.json();
      setAnalysisResult(data.analysis);
    } catch (err) {
      console.error("Analysis error:", err);
    }
  };

  return (
    <div>
      <h3>Image Analysis</h3>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleAnalyze}>Analyze</button>
      {analysisResult && <p>AI Analysis: {analysisResult}</p>}
    </div>
  );
}

export default ImageAnalysisTab;
