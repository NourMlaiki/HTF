import React, { useState } from "react";
import ImageAnalysisTab from "../components/ImageAnalysisTab";

function DashboardPage() {
  const [activeTab, setActiveTab] = useState("imageAnalysis");

  return (
    <div>
      <h1>Innovation Wave Dashboard</h1>
      <button onClick={() => setActiveTab("imageAnalysis")}>Image Analysis</button>

      {activeTab === "imageAnalysis" && <ImageAnalysisTab />}
    </div>
  );
}

export default DashboardPage;
