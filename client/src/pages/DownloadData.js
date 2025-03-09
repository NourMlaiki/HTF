import React from "react";

function DownloadData() {
  return (
    <div>
      <h2>Download Sample Data</h2>
      <button onClick={() => window.open("http://127.0.0.1:5000/download/data")}>
        Download Excel File
      </button>
      <button onClick={() => window.open("http://127.0.0.1:5000/download/image")}>
        Download Sample Image
      </button>
    </div>
  );
}

export default DownloadData;
