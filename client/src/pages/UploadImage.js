import React, { useState } from "react";

function UploadImage() {
  const [selectedFile, setSelectedFile] = useState(null);
  const [analysisResult, setAnalysisResult] = useState("");

  const handleFileChange = (e) => {
    setSelectedFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!selectedFile) {
      alert("Please select an image first.");
      return;
    }

    const formData = new FormData();
    formData.append("image", selectedFile);

    try {
      const response = await fetch("http://127.0.0.1:5000/analyze/image", {
        method: "POST",
        body: formData,
      });

      const data = await response.json();
      setAnalysisResult(data.analysis || "No analysis received.");
    } catch (error) {
      console.error("Error:", error);
      setAnalysisResult("Failed to analyze image.");
    }
  };

  return (
    <div>
      <h2>Upload Image for AI Analysis</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Analyze</button>
      {analysisResult && (
        <div>
          <h3>Analysis Result:</h3>
          <p>{analysisResult}</p>
        </div>
      )}
    </div>
  );
}

export default UploadImage;
